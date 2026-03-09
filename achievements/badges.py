"""Achievement / badge system."""

from config import ACHIEVEMENTS_FILE, ACHIEVEMENT_DEFS
from utils.file_handler import load_json, save_json
from utils.colors import gold, success, highlight, banner, info
from utils.sound import achievement_sound


def _get_achievements():
    return load_json(ACHIEVEMENTS_FILE, {})

def _save_achievements(data):
    save_json(ACHIEVEMENTS_FILE, data)


def unlock(username, achievement_id):
    if not username or achievement_id not in ACHIEVEMENT_DEFS:
        return False
    data = _get_achievements()
    if username not in data:
        data[username] = []
    if achievement_id in data[username]:
        return False
    data[username].append(achievement_id)
    _save_achievements(data)
    badge = ACHIEVEMENT_DEFS[achievement_id]
    achievement_sound()
    print(gold("\n  ╔══════════════════════════════════════╗"))
    print(gold(f"  ║  🏅 ACHIEVEMENT UNLOCKED!             ║"))
    print(gold(f"  ║  {badge['name']:<37}║"))
    print(gold(f"  ║  {badge['desc']:<37}║"))
    print(gold("  ╚══════════════════════════════════════╝\n"))
    return True


def get_user_achievements(username):
    data = _get_achievements()
    return data.get(username, [])


def view_achievements(username):
    if not username:
        print(info("  Login to track achievements!\n"))
        return
    banner("ACHIEVEMENTS")
    unlocked = get_user_achievements(username)
    for aid, badge in ACHIEVEMENT_DEFS.items():
        status = success("✓ UNLOCKED") if aid in unlocked else "  Locked  "
        print(f"  {status}  {badge['name']} — {badge['desc']}")
    count = len(unlocked)
    total = len(ACHIEVEMENT_DEFS)
    print(highlight(f"\n  Progress: {count}/{total} ({count/total*100:.0f}%)\n"))


def check_achievements(username, profile, score, total, streak, category, is_multiplayer_win=False, is_daily=False, fast_answers=0):
    if not username:
        return
    if profile["quizzes_taken"] >= 1:
        unlock(username, "first_quiz")
    if total > 0 and score == total:
        unlock(username, "perfect_score")
    if fast_answers >= 5:
        unlock(username, "speed_demon")
    if profile["quizzes_taken"] >= 10:
        unlock(username, "quiz_master")
    if streak >= 5:
        unlock(username, "streak_5")
    if streak >= 10:
        unlock(username, "streak_10")
    from config import CATEGORIES
    if set(CATEGORIES).issubset(set(profile.get("categories_played", []))):
        unlock(username, "all_categories")
    if is_multiplayer_win:
        unlock(username, "multiplayer_win")
    if is_daily:
        unlock(username, "daily_complete")
