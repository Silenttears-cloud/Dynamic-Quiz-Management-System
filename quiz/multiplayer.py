"""Multiplayer head-to-head quiz mode."""

import random
from config import QUESTIONS_FILE, NUM_OPTIONS
from utils.file_handler import load_json
from utils.colors import success, error, info, warning, highlight, banner, gold
from utils.sound import correct_sound, wrong_sound


def multiplayer_quiz():
    questions = load_json(QUESTIONS_FILE, [])
    if len(questions) < 3:
        print(error("\n  Need at least 3 questions for multiplayer.\n"))
        return

    banner("MULTIPLAYER MODE")
    p1 = input(info("  Player 1 name: ")).strip() or "Player 1"
    p2 = input(info("  Player 2 name: ")).strip() or "Player 2"

    max_q = min(len(questions), 10)
    while True:
        try:
            num = int(input(warning(f"  Number of questions (1-{max_q}): ")))
            if 1 <= num <= max_q:
                break
            print(error(f"  Enter 1-{max_q}."))
        except ValueError:
            print(error("  Invalid input."))

    selected = random.sample(questions, num)
    scores = {p1: 0, p2: 0}

    for i, q in enumerate(selected, 1):
        banner(f"ROUND {i}/{num}")
        print(highlight(f"  {q['question']}\n"))
        for j, opt in enumerate(q["options"], 1):
            print(f"    {j}. {opt}")

        for player in [p1, p2]:
            while True:
                try:
                    ans = int(input(gold(f"\n  {player}'s answer (1-{NUM_OPTIONS}): ")))
                    if 1 <= ans <= NUM_OPTIONS:
                        if ans == q["answer"]:
                            scores[player] += 1
                            correct_sound()
                            print(success(f"  ✓ {player} got it right!"))
                        else:
                            wrong_sound()
                            print(error(f"  ✗ {player} got it wrong."))
                        break
                    print(error(f"  Enter 1-{NUM_OPTIONS}."))
                except ValueError:
                    print(error("  Invalid input."))

        print(info(f"\n  Scoreboard: {p1}: {scores[p1]} | {p2}: {scores[p2]}"))

    banner("FINAL RESULTS")
    print(info(f"  {p1}: {scores[p1]}/{num}"))
    print(info(f"  {p2}: {scores[p2]}/{num}"))
    if scores[p1] > scores[p2]:
        print(gold(f"\n  🏆 {p1} WINS! 🏆\n"))
    elif scores[p2] > scores[p1]:
        print(gold(f"\n  🏆 {p2} WINS! 🏆\n"))
    else:
        print(warning(f"\n  🤝 It's a TIE!\n"))





