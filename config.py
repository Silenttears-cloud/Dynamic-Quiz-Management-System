"""Configuration constants for the Quiz Management System."""

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

QUESTIONS_FILE = os.path.join(DATA_DIR, "questions.json")
LEADERBOARD_FILE = os.path.join(DATA_DIR, "leaderboard.json")
USERS_FILE = os.path.join(DATA_DIR, "users.json")
ACHIEVEMENTS_FILE = os.path.join(DATA_DIR, "achievements.json")
DAILY_CHALLENGE_FILE = os.path.join(DATA_DIR, "daily_challenge.json")
EXPORTS_DIR = os.path.join(BASE_DIR, "exports")

ADMIN_PASSWORD = "Aayushi@2006"
MAX_LEADERBOARD_ENTRIES = 10
NUM_OPTIONS = 4

DIFFICULTY_LEVELS = {
    "easy": {"time_limit": 30, "multiplier": 1.0},
    "medium": {"time_limit": 20, "multiplier": 1.5},
    "hard": {"time_limit": 10, "multiplier": 2.0},
}

CATEGORIES = ["General", "Science", "Math", "History", "Technology", "Sports", "Entertainment"]

MAX_LIFELINES = {
    "fifty_fifty": 1,
    "skip": 1,
    "hint": 1,
}

ACHIEVEMENT_DEFS = {
    "first_quiz": {"name": "🎓 First Quiz", "desc": "Complete your first quiz"},
    "perfect_score": {"name": "💯 Perfect Score", "desc": "Get 100% on a quiz"},
    "speed_demon": {"name": "⚡ Speed Demon", "desc": "Answer 5 questions under 5 seconds each"},
    "quiz_master": {"name": "🏆 Quiz Master", "desc": "Complete 10 quizzes"},
    "streak_5": {"name": "🔥 On Fire", "desc": "Get 5 correct answers in a row"},
    "streak_10": {"name": "💎 Unstoppable", "desc": "Get 10 correct answers in a row"},
    "all_categories": {"name": "🌍 Well Rounded", "desc": "Play quizzes in all categories"},
    "multiplayer_win": {"name": "⚔️ Champion", "desc": "Win a multiplayer match"},
    "daily_complete": {"name": "📅 Daily Player", "desc": "Complete a daily challenge"},
}

DAILY_CHALLENGE_COUNT = 5
