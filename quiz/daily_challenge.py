"""Daily challenge mode — same questions for everyone each day."""

import random
import hashlib
from datetime import date

from config import QUESTIONS_FILE, DAILY_CHALLENGE_FILE, DAILY_CHALLENGE_COUNT, NUM_OPTIONS
from utils.file_handler import load_json, save_json
from utils.colors import success, error, info, warning, highlight, banner, gold
from utils.sound import correct_sound, wrong_sound
from achievements.badges import unlock


def _get_daily_seed():
    today = date.today().isoformat()
    return int(hashlib.md5(today.encode()).hexdigest(), 16)


def _get_daily_questions():
    questions = load_json(QUESTIONS_FILE, [])
    if len(questions) < DAILY_CHALLENGE_COUNT:
        return questions
    rng = random.Random(_get_daily_seed())
    return rng.sample(questions, DAILY_CHALLENGE_COUNT)


def daily_challenge(username=None):
    questions = _get_daily_questions()
    if not questions:
        print(error("\n  No questions available for daily challenge.\n"))
        return

    daily_data = load_json(DAILY_CHALLENGE_FILE, {})
    today = date.today().isoformat()
    if username and daily_data.get(username) == today:
        print(warning("\n  You've already completed today's challenge! Come back tomorrow.\n"))
        return

    name = username or input(info("\n  Your name: ")).strip() or "Guest"

    banner(f"DAILY CHALLENGE — {today}")
    print(info(f"  {len(questions)} questions | Same for everyone today!\n"))

    score = 0
    for i, q in enumerate(questions, 1):
        print(highlight(f"  Q{i}: {q['question']}"))
        for j, opt in enumerate(q["options"], 1):
            print(f"    {j}. {opt}")
        while True:
            try:
                ans = int(input(warning(f"  Answer (1-{NUM_OPTIONS}): ")))
                if 1 <= ans <= NUM_OPTIONS:
                    if ans == q["answer"]:
                        score += 1
                        correct_sound()
                        print(success("  ✓ Correct!\n"))
                    else:
                        wrong_sound()
                        correct_text = q["options"][q["answer"] - 1]
                        print(error(f"  ✗ Wrong! Answer: {correct_text}\n"))
                    break
                print(error(f"  Enter 1-{NUM_OPTIONS}."))
            except ValueError:
                print(error("  Invalid input."))

    percentage = (score / len(questions)) * 100
    banner("DAILY RESULTS")
    print(info(f"  Score: {score}/{len(questions)} ({percentage:.1f}%)"))
    if score == len(questions):
        print(gold("  🌟 PERFECT DAILY CHALLENGE! 🌟"))
    if username:
        daily_data[username] = today
        save_json(DAILY_CHALLENGE_FILE, daily_data)
        unlock(username, "daily_complete")
    print()
