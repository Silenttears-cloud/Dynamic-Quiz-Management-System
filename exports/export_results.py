"""Export quiz results as text or PDF."""

import os
from datetime import datetime
from config import LEADERBOARD_FILE, EXPORTS_DIR
from utils.file_handler import load_json
from utils.colors import success, error, info, warning, banner


def export_as_text():
    leaderboard = load_json(LEADERBOARD_FILE, [])
    if not leaderboard:
        print(error("  No data to export."))
        return
    os.makedirs(EXPORTS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(EXPORTS_DIR, f"results_{timestamp}.txt")
    with open(filepath, "w") as f:
        f.write("=" * 60 + "\n")
        f.write("  QUIZ MANAGEMENT SYSTEM — LEADERBOARD EXPORT\n")
        f.write(f"  Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        f.write("=" * 60 + "\n\n")
        f.write(f"  {'Rank':<6}{'Name':<15}{'Score':<10}{'%':<8}{'Category':<12}{'Difficulty'}\n")
        f.write("  " + "-" * 55 + "\n")
        for i, entry in enumerate(leaderboard, 1):
            score_str = f"{entry['score']}/{entry['total']}"
            cat = entry.get("category", "All")
            diff = entry.get("difficulty", "medium").capitalize()
            f.write(f"  {i:<6}{entry['name']:<15}{score_str:<10}{entry['percentage']:.1f}%   {cat:<12}{diff}\n")
    print(success(f"  ✓ Exported to: {filepath}\n"))


def export_as_pdf():
    try:
        from fpdf import FPDF
    except ImportError:
        print(error("  fpdf2 not installed. Run: pip install fpdf2"))
        return
    leaderboard = load_json(LEADERBOARD_FILE, [])
    if not leaderboard:
        print(error("  No data to export."))
        return
    os.makedirs(EXPORTS_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filepath = os.path.join(EXPORTS_DIR, f"results_{timestamp}.pdf")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 16)
    pdf.cell(0, 10, "Quiz Management System — Leaderboard", ln=True, align="C")
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 8, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
    pdf.ln(10)
    pdf.set_font("Helvetica", "B", 10)
    headers = ["Rank", "Name", "Score", "%", "Category", "Difficulty"]
    widths = [15, 40, 25, 20, 40, 30]
    for h, w in zip(headers, widths):
        pdf.cell(w, 8, h, border=1, align="C")
    pdf.ln()
    pdf.set_font("Helvetica", "", 10)
    for i, entry in enumerate(leaderboard, 1):
        score_str = f"{entry['score']}/{entry['total']}"
        row = [str(i), entry["name"], score_str, f"{entry['percentage']:.1f}%",
               entry.get("category", "All"), entry.get("difficulty", "medium").capitalize()]
        for val, w in zip(row, widths):
            pdf.cell(w, 8, val, border=1, align="C")
        pdf.ln()
    pdf.output(filepath)
    print(success(f"  ✓ PDF exported to: {filepath}\n"))


def export_menu():
    banner("EXPORT RESULTS")
    print(info("  1. Export as Text File"))
    print(info("  2. Export as PDF"))
    print(info("  3. Back"))
    choice = input(warning("  Select: ")).strip()
    if choice == "1":
        export_as_text()
    elif choice == "2":
        export_as_pdf()
    elif choice == "3":
        return
    else:
        print(error("  Invalid choice."))
