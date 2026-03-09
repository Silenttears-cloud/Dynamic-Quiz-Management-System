"""Leaderboard display module."""

from config import LEADERBOARD_FILE, MAX_LEADERBOARD_ENTRIES
from utils.file_handler import load_json
from utils.colors import info, highlight, banner, gold, dim


def view_leaderboard():
    leaderboard = load_json(LEADERBOARD_FILE, [])
    if not leaderboard:
        print(info("\n  Leaderboard is empty. Take a quiz first!\n"))
        return

    banner("LEADERBOARD")
    print(info(f"  {'Rank':<6}{'Name':<15}{'Score':<10}{'%':<8}{'Cat':<12}{'Diff':<8}"))
    print(info("  " + "─" * 55))

    for i, entry in enumerate(leaderboard[:MAX_LEADERBOARD_ENTRIES], 1):
        score_str = f"{entry['score']}/{entry['total']}"
        cat = entry.get('category', 'All')[:10]
        diff = entry.get('difficulty', 'med')[:6].capitalize()
        if i == 1:
            line = gold(f"  {i:<6}{entry['name']:<15}{score_str:<10}{entry['percentage']:.1f}%   {cat:<12}{diff}")
        elif i <= 3:
            line = highlight(f"  {i:<6}{entry['name']:<15}{score_str:<10}{entry['percentage']:.1f}%   {cat:<12}{diff}")
        else:
            line = f"  {i:<6}{entry['name']:<15}{score_str:<10}{entry['percentage']:.1f}%   {cat:<12}{diff}"
        print(line)
    print()
