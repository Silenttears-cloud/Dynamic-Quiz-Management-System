"""Quiz engine with difficulty, timer, categories, lifelines, and streaks."""

import random
import time

from config import (
    QUESTIONS_FILE, LEADERBOARD_FILE, NUM_OPTIONS,
    DIFFICULTY_LEVELS, CATEGORIES, MAX_LIFELINES,
)
from utils.file_handler import load_json, save_json
from utils.colors import success, error, info, warning, highlight, banner, gold, dim
from utils.sound import correct_sound, wrong_sound
from utils.timer import QuestionTimer
from users.profiles import add_quiz_result, get_profile
from achievements.badges import check_achievements


def _select_category():
    print(highlight("\n  Select Category:"))
    print(info("  0. All Categories"))
    for i, cat in enumerate(CATEGORIES, 1):
        print(info(f"  {i}. {cat}"))
    while True:
        try:
            choice = int(input(warning("  Select: ")))
            if choice == 0:
                return None
            if 1 <= choice <= len(CATEGORIES):
                return CATEGORIES[choice - 1]
            print(error(f"  Enter 0-{len(CATEGORIES)}."))
        except ValueError:
            print(error("  Invalid input."))


def _select_difficulty():
    print(highlight("\n  Select Difficulty:"))
    diffs = list(DIFFICULTY_LEVELS.keys())
    for i, d in enumerate(diffs, 1):
        settings = DIFFICULTY_LEVELS[d]
        print(info(f"  {i}. {d.capitalize()} (x{settings['multiplier']} pts, {settings['time_limit']}s)"))
    while True:
        try:
            choice = int(input(warning("  Select: ")))
            if 1 <= choice <= len(diffs):
                return diffs[choice - 1]
            print(error(f"  Enter 1-{len(diffs)}."))
        except ValueError:
            print(error("  Invalid input."))


def _use_fifty_fifty(options, answer):
    wrong_indices = [i for i in range(len(options)) if i + 1 != answer]
    remove = random.sample(wrong_indices, 2)
    new_options = []
    for i, opt in enumerate(options):
        if i in remove:
            new_options.append("──────")
        else:
            new_options.append(opt)
    return new_options


def take_quiz(username=None):
    questions = load_json(QUESTIONS_FILE, [])
    if not questions:
        print(error("\n  No questions available. Ask an admin to add some!\n"))
        return

    category = _select_category()
    difficulty = _select_difficulty()

    filtered = questions.copy()
    if category:
        filtered = [q for q in filtered if q.get("category") == category]
    if difficulty:
        filtered = [q for q in filtered if q.get("difficulty", "medium") == difficulty]
    if not filtered:
        print(error("\n  No questions match your selection.\n"))
        return

    random.shuffle(filtered)
    settings = DIFFICULTY_LEVELS[difficulty]
    lifelines = {k: v for k, v in MAX_LIFELINES.items()}

    name = username or input(info("\n  Your name: ")).strip() or "Guest"

    banner(f"QUIZ: {category or 'All'} | {difficulty.upper()}")
    print(info(f"  {len(filtered)} questions | x{settings['multiplier']} multiplier | {settings['time_limit']}s per question"))
    print(info(f"  Lifelines: 50:50({lifelines['fifty_fifty']}) | Skip({lifelines['skip']}) | Hint({lifelines['hint']})\n"))

    score = 0
    streak = 0
    max_streak = 0
    fast_answers = 0

    for i, q in enumerate(filtered, 1):
        current_options = q["options"].copy()
        print(highlight(f"  Q{i}/{len(filtered)}: {q['question']}"))
        print(dim(f"  [{q.get('category', 'General')} | {q.get('difficulty', 'medium').capitalize()}]"))

        ll_text = []
        if lifelines["fifty_fifty"] > 0:
            ll_text.append("5=50:50")
        if lifelines["skip"] > 0:
            ll_text.append("6=Skip")
        if lifelines["hint"] > 0:
            ll_text.append("7=Hint")
        if ll_text:
            print(gold(f"  Lifelines: {' | '.join(ll_text)}"))
        if streak >= 3:
            print(gold(f"  🔥 Streak: {streak}"))

        for j, opt in enumerate(current_options, 1):
            print(f"    {j}. {opt}")

        timer = QuestionTimer(settings["time_limit"])
        timer.start()

        while True:
            remaining = timer.remaining()
            try:
                ans_input = input(warning(f"  Answer (1-{NUM_OPTIONS}) [{remaining:.0f}s]: ")).strip()
            except EOFError:
                ans_input = ""

            if timer.is_expired():
                timer.stop()
                print(error("  ⏰ Time's up!\n"))
                wrong_sound()
                streak = 0
                break

            if ans_input == "5" and lifelines["fifty_fifty"] > 0:
                lifelines["fifty_fifty"] -= 1
                current_options = _use_fifty_fifty(current_options, q["answer"])
                print(info("  🎯 50:50 used!"))
                for j, opt in enumerate(current_options, 1):
                    print(f"    {j}. {opt}")
                continue
            elif ans_input == "6" and lifelines["skip"] > 0:
                lifelines["skip"] -= 1
                timer.stop()
                print(warning("  ⏭️  Question skipped.\n"))
                streak = 0
                break
            elif ans_input == "7" and lifelines["hint"] > 0 and q.get("hint"):
                lifelines["hint"] -= 1
                print(info(f"  💡 Hint: {q['hint']}"))
                continue

            try:
                ans = int(ans_input)
                if 1 <= ans <= NUM_OPTIONS:
                    elapsed = timer.stop()
                    if ans == q["answer"]:
                        points = int(settings["multiplier"] * 1)
                        score += points
                        streak += 1
                        if streak > max_streak:
                            max_streak = streak
                        if elapsed < 5:
                            fast_answers += 1
                        correct_sound()
                        time_str = f" ({elapsed:.1f}s)" if elapsed else ""
                        print(success(f"  ✓ Correct! +{points} pts{time_str}\n"))
                    else:
                        correct_text = q["options"][q["answer"] - 1]
                        wrong_sound()
                        print(error(f"  ✗ Wrong! Answer: {q['answer']}. {correct_text}\n"))
                        streak = 0
                    break
                print(error(f"  Enter 1-{NUM_OPTIONS}."))
            except ValueError:
                print(error("  Invalid input."))

    total = len(filtered)
    percentage = (score / (total * settings["multiplier"])) * 100 if total > 0 else 0

    banner("RESULTS")
    print(info(f"  Player:      {name}"))
    print(info(f"  Score:       {score} pts"))
    print(info(f"  Correct:     {score}/{total}"))
    print(info(f"  Percentage:  {percentage:.1f}%"))
    print(info(f"  Best Streak: {max_streak}"))
    print(info(f"  Fast Answers: {fast_answers}\n"))

    leaderboard = load_json(LEADERBOARD_FILE, [])
    leaderboard.append({
        "name": name, "score": score, "total": total,
        "percentage": round(percentage, 1),
        "category": category or "All", "difficulty": difficulty,
    })
    leaderboard.sort(key=lambda x: x["percentage"], reverse=True)
    save_json(LEADERBOARD_FILE, leaderboard)

    if username:
        add_quiz_result(username, score, total, category or "All", max_streak)
        profile = get_profile(username)
        if profile:
            check_achievements(username, profile, score, total, max_streak, category, fast_answers=fast_answers)
