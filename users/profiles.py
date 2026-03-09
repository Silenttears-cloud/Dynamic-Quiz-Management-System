"""User profile management with login system."""

import hashlib
from config import USERS_FILE
from utils.file_handler import load_json, save_json
from utils.colors import success, error, info, warning, banner, highlight


def _hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def _get_users():
    return load_json(USERS_FILE, {})

def _save_users(users):
    save_json(USERS_FILE, users)


def register():
    banner("REGISTER")
    users = _get_users()
    username = input(info("  Choose a username: ")).strip().lower()
    if not username:
        print(error("  Username cannot be empty."))
        return None
    if username in users:
        print(error(f"  Username '{username}' already taken."))
        return None

    password = input(info("  Choose a password: ")).strip()
    if len(password) < 4:
        print(error("  Password must be at least 4 characters."))
        return None

    display_name = input(info("  Display name (optional): ")).strip() or username

    users[username] = {
        "password": _hash_password(password),
        "display_name": display_name,
        "quizzes_taken": 0,
        "total_score": 0,
        "total_questions": 0,
        "best_streak": 0,
        "categories_played": [],
        "history": [],
    }
    _save_users(users)
    print(success(f"\n  ✓ Welcome, {display_name}! Account created.\n"))
    return username


def login():
    banner("LOGIN")
    users = _get_users()
    username = input(info("  Username: ")).strip().lower()
    if username not in users:
        print(error("  User not found. Please register first."))
        return None

    password = input(info("  Password: ")).strip()
    if users[username]["password"] != _hash_password(password):
        print(error("  Incorrect password."))
        return None

    print(success(f"\n  ✓ Welcome back, {users[username]['display_name']}!\n"))
    return username


def get_profile(username):
    users = _get_users()
    return users.get(username)


def update_profile(username, data):
    users = _get_users()
    if username in users:
        users[username].update(data)
        _save_users(users)


def add_quiz_result(username, score, total, category, streak):
    users = _get_users()
    if username not in users:
        return
    user = users[username]
    user["quizzes_taken"] += 1
    user["total_score"] += score
    user["total_questions"] += total
    if streak > user["best_streak"]:
        user["best_streak"] = streak
    if category and category not in user["categories_played"]:
        user["categories_played"].append(category)
    user["history"].append({
        "score": score, "total": total, "category": category,
        "percentage": round((score / total) * 100, 1) if total > 0 else 0,
    })
    _save_users(users)


def view_profile(username):
    profile = get_profile(username)
    if not profile:
        print(error("  Profile not found."))
        return
    banner(f"PROFILE: {profile['display_name']}")
    avg = (profile["total_score"] / profile["total_questions"] * 100) if profile["total_questions"] > 0 else 0
    print(info(f"  📊 Quizzes Taken:    {profile['quizzes_taken']}"))
    print(info(f"  🎯 Total Score:      {profile['total_score']}/{profile['total_questions']}"))
    print(info(f"  📈 Average:          {avg:.1f}%"))
    print(info(f"  🔥 Best Streak:      {profile['best_streak']}"))
    print(info(f"  🌍 Categories:       {', '.join(profile['categories_played']) or 'None'}"))
    if profile["history"]:
        print(highlight("\n  Recent Results:"))
        for h in profile["history"][-5:]:
            cat = f" [{h['category']}]" if h.get("category") else ""
            print(f"    {h['score']}/{h['total']} ({h['percentage']}%){cat}")
    print()


def auth_menu():
    while True:
        print(info("\n  1. Login"))
        print(info("  2. Register"))
        print(info("  3. Play as Guest"))
        print(info("  4. Back"))
        choice = input(warning("\n  Select: ")).strip()
        if choice == "1":
            user = login()
            if user:
                return user
        elif choice == "2":
            user = register()
            if user:
                return user
        elif choice == "3":
            return None
        elif choice == "4":
            return "__back__"
        else:
            print(error("  Invalid choice."))





