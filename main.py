"""
Dynamic Quiz Management System — Full Featured Edition
Entry point for the application.
"""

from colorama import Fore, Style

from config import ADMIN_PASSWORD
from admin.admin_panel import admin_menu
from quiz.quiz_engine import take_quiz
from quiz.multiplayer import multiplayer_quiz
from quiz.daily_challenge import daily_challenge
from leaderboard.leaderboard import view_leaderboard
from users.profiles import auth_menu, view_profile, get_profile
from achievements.badges import view_achievements
from exports.export_results import export_menu
from utils.colors import info, warning, error, success, highlight, banner, gold


def main():
    banner("DYNAMIC QUIZ MANAGEMENT SYSTEM")
    print(gold("    ✨ Full Featured Edition ✨\n"))

    current_user = None

    while True:
        if current_user:
            profile = get_profile(current_user)
            name = profile["display_name"] if profile else current_user
            print(success(f"  Logged in as: {name}"))

        print(info("\n  1.  📝 Take Quiz"))
        print(info("  2.  ⚔️  Multiplayer"))
        print(info("  3.  📅 Daily Challenge"))
        print(info("  4.  🏆 Leaderboard"))
        print(info("  5.  👤 Login / Register"))
        print(info("  6.  📊 My Profile"))
        print(info("  7.  🏅 Achievements"))
        print(info("  8.  📤 Export Results"))
        print(info("  9.  🔧 Admin Panel"))
        print(info("  0.  🚪 Exit"))
        choice = input(warning("\n  Select: ")).strip()

        if choice == "1":
            take_quiz(username=current_user)
        elif choice == "2":
            multiplayer_quiz()
        elif choice == "3":
            daily_challenge(username=current_user)
        elif choice == "4":
            view_leaderboard()
        elif choice == "5":
            result = auth_menu()
            if result and result != "__back__":
                current_user = result
        elif choice == "6":
            if current_user:
                view_profile(current_user)
            else:
                print(warning("  Please login first."))
        elif choice == "7":
            view_achievements(current_user)
        elif choice == "8":
            export_menu()
        elif choice == "9":
            password = input(warning("  Admin password: ")).strip()
            if password == ADMIN_PASSWORD:
                admin_menu()
            else:
                print(error("  Incorrect password.\n"))
        elif choice == "0":
            print(gold("\n  Goodbye! 👋\n"))
            break
        else:
            print(error("  Invalid choice."))


if __name__ == "__main__":
    main()
