"""Admin panel for managing quiz questions with categories and difficulty."""

from config import QUESTIONS_FILE, NUM_OPTIONS, CATEGORIES, DIFFICULTY_LEVELS
from utils.file_handler import load_json, save_json
from utils.colors import success, error, info, warning, highlight, banner, dim


def _get_questions():
    return load_json(QUESTIONS_FILE, [])

def _save(questions):
    save_json(QUESTIONS_FILE, questions)


def add_question():
    banner("ADD NEW QUESTION")
    text = input(info("  Question: ")).strip()
    if not text:
        print(error("  Question cannot be empty."))
        return

    print(highlight("\n  Categories:"))
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"    {i}. {cat}")
    while True:
        try:
            cat_idx = int(input(warning(f"  Select category (1-{len(CATEGORIES)}): "))) - 1
            if 0 <= cat_idx < len(CATEGORIES):
                category = CATEGORIES[cat_idx]
                break
            print(error(f"  Enter 1-{len(CATEGORIES)}."))
        except ValueError:
            print(error("  Invalid input."))

    diff_keys = list(DIFFICULTY_LEVELS.keys())
    print(highlight("\n  Difficulty:"))
    for i, d in enumerate(diff_keys, 1):
        mult = DIFFICULTY_LEVELS[d]["multiplier"]
        time_l = DIFFICULTY_LEVELS[d]["time_limit"]
        print(f"    {i}. {d.capitalize()} (x{mult} points, {time_l}s)")
    while True:
        try:
            d_idx = int(input(warning("  Select difficulty (1-3): "))) - 1
            if 0 <= d_idx < len(diff_keys):
                difficulty = diff_keys[d_idx]
                break
            print(error("  Enter 1-3."))
        except ValueError:
            print(error("  Invalid input."))

    options = []
    for i in range(NUM_OPTIONS):
        opt = input(info(f"  Option {i + 1}: ")).strip()
        if not opt:
            print(error("  Option cannot be empty. Aborting."))
            return
        options.append(opt)

    while True:
        try:
            correct = int(input(warning(f"  Correct option (1-{NUM_OPTIONS}): ")))
            if 1 <= correct <= NUM_OPTIONS:
                break
            print(error(f"  Enter 1-{NUM_OPTIONS}."))
        except ValueError:
            print(error("  Invalid input."))

    hint = input(info("  Hint (optional): ")).strip() or None

    questions = _get_questions()
    questions.append({
        "question": text, "options": options, "answer": correct,
        "category": category, "difficulty": difficulty, "hint": hint,
    })
    _save(questions)
    print(success("\n  ✓ Question added successfully!\n"))


def view_questions(filter_cat=None, filter_diff=None):
    questions = _get_questions()
    if not questions:
        print(error("\n  No questions available.\n"))
        return
    filtered = questions
    if filter_cat:
        filtered = [q for q in filtered if q.get("category") == filter_cat]
    if filter_diff:
        filtered = [q for q in filtered if q.get("difficulty") == filter_diff]
    if not filtered:
        print(warning(f"\n  No questions match the filter.\n"))
        return
    banner(f"QUESTIONS ({len(filtered)})")
    for i, q in enumerate(filtered, 1):
        cat = q.get("category", "General")
        diff = q.get("difficulty", "medium").capitalize()
        print(highlight(f"\n  Q{i}: {q['question']}"))
        print(dim(f"       [{cat} | {diff}]"))
        for j, opt in enumerate(q["options"], 1):
            marker = success(" ✓") if j == q["answer"] else ""
            print(f"       {j}. {opt}{marker}")
        if q.get("hint"):
            print(dim(f"       💡 Hint: {q['hint']}"))
    print()


def edit_question():
    questions = _get_questions()
    view_questions()
    if not questions:
        return
    try:
        idx = int(input(warning("  Question number to edit: "))) - 1
        if not (0 <= idx < len(questions)):
            print(error("  Invalid number."))
            return
    except ValueError:
        print(error("  Invalid input."))
        return
    q = questions[idx]
    print(info(f"\n  Editing: {q['question']}"))
    print(dim("  (Press Enter to keep current value)\n"))
    new_text = input(info(f"  Question [{q['question']}]: ")).strip()
    if new_text:
        q["question"] = new_text
    for i in range(NUM_OPTIONS):
        new_opt = input(info(f"  Option {i+1} [{q['options'][i]}]: ")).strip()
        if new_opt:
            q["options"][i] = new_opt
    new_ans = input(info(f"  Correct answer [{q['answer']}]: ")).strip()
    if new_ans:
        try:
            ans = int(new_ans)
            if 1 <= ans <= NUM_OPTIONS:
                q["answer"] = ans
        except ValueError:
            pass
    new_hint = input(info(f"  Hint [{q.get('hint', 'None')}]: ")).strip()
    if new_hint:
        q["hint"] = new_hint
    _save(questions)
    print(success("  ✓ Question updated!\n"))


def delete_question():
    questions = _get_questions()
    view_questions()
    if not questions:
        return
    try:
        idx = int(input(warning("  Question number to delete: "))) - 1
        if 0 <= idx < len(questions):
            removed = questions.pop(idx)
            _save(questions)
            print(success(f"  ✓ Deleted: {removed['question']}\n"))
        else:
            print(error("  Invalid number.\n"))
    except ValueError:
        print(error("  Invalid input.\n"))


def admin_menu():
    while True:
        banner("ADMIN PANEL")
        print(info("  1. Add Question"))
        print(info("  2. View All Questions"))
        print(info("  3. Edit Question"))
        print(info("  4. Delete Question"))
        print(info("  5. Filter by Category"))
        print(info("  6. Filter by Difficulty"))
        print(info("  7. Back to Main Menu"))
        choice = input(warning("\n  Select: ")).strip()
        if choice == "1":
            add_question()
        elif choice == "2":
            view_questions()
        elif choice == "3":
            edit_question()
        elif choice == "4":
            delete_question()
        elif choice == "5":
            print(highlight("\n  Categories:"))
            for i, cat in enumerate(CATEGORIES, 1):
                print(f"    {i}. {cat}")
            try:
                ci = int(input(warning("  Select: "))) - 1
                if 0 <= ci < len(CATEGORIES):
                    view_questions(filter_cat=CATEGORIES[ci])
            except ValueError:
                print(error("  Invalid."))
        elif choice == "6":
            for i, d in enumerate(["easy", "medium", "hard"], 1):
                print(f"    {i}. {d.capitalize()}")
            try:
                di = int(input(warning("  Select: "))) - 1
                diffs = ["easy", "medium", "hard"]
                if 0 <= di < 3:
                    view_questions(filter_diff=diffs[di])
            except ValueError:
                print(error("  Invalid."))
        elif choice == "7":
            break
        else:
            print(error("  Invalid choice.\n"))
