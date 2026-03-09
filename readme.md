
```
 ____                              _        ___        _
|  _ \ _   _ _ __   __ _ _ __ ___ (_) ___  / _ \ _   _(_)____
| | | | | | | '_ \ / _` | '_ ` _ \| |/ __|| | | | | | | |_  /
| |_| | |_| | | | | (_| | | | | | | | (__ | |_| | |_| | |/ /
|____/ \__, |_| |_|\__,_|_| |_| |_|_|\___| \__\_\\__,_|_/___|
       |___/
 __  __                                                   _
|  \/  | __ _ _ __   __ _  __ _  ___ _ __ ___   ___ _ __ | |_
| |\/| |/ _` | '_ \ / _` |/ _` |/ _ \ '_ ` _ \ / _ \ '_ \| __|
| |  | | (_| | | | | (_| | (_| |  __/ | | | | |  __/ | | | |_
|_|  |_|\__,_|_| |_|\__,_|\__, |\___|_| |_| |_|\___|_| |_|\__|
                           |___/
 ____            _
/ ___| _   _ ___| |_ ___ _ __ ___
\___ \| | | / __| __/ _ \ '_ ` _ \
 ___) | |_| \__ \ ||  __/ | | | | |
|____/ \__, |___/\__\___|_| |_| |_|
       |___/
```

<div align="center">

# 🎮 Dynamic Quiz Management System

### ✨ Full Featured Edition ✨

A feature-packed, colorful, terminal-based quiz game built with Python.
Challenge yourself, compete with friends, unlock achievements, and climb the leaderboard!

---

```
╔═══════════════════════════════════════════════════╗
║                                                   ║
║   📝 Quizzes  ⚔️ Multiplayer  📅 Daily Challenge  ║
║   🏆 Leaderboard  🏅 Achievements  📤 Export      ║
║   👤 User Profiles  🔧 Admin Panel                ║
║                                                   ║
╚═══════════════════════════════════════════════════╝
```

</div>

---

## 📖 Introduction

**Dynamic Quiz Management System** is a fully-featured terminal quiz application written in Python. It's designed to be fun, educational, and competitive. Whether you're playing solo, challenging a friend in multiplayer mode, or tackling the daily challenge — there's always something exciting to do!

The system includes an **admin panel** to manage questions, a **user registration & login system** to track your progress, and an **achievement engine** with 9 unlockable badges. All data is saved locally using JSON files, so your progress is never lost.

---

## 🚀 How to Run (Step-by-Step for Beginners)

> ⚠️ **Prerequisite:** You need **Python 3.7 or higher** installed on your computer.
> Don't have Python? Download it from [python.org](https://www.python.org/downloads/)

### Step 1 — Download the Project

Download or clone this project to your computer.

```bash
git clone <your-repo-url>
```

Or simply download as ZIP and extract it.

### Step 2 — Open Terminal / Command Prompt

| Operating System | How to Open |
|---|---|
| 🪟 **Windows** | Press `Win + R`, type `cmd`, press Enter |
| 🍎 **Mac** | Press `Cmd + Space`, type `Terminal`, press Enter |
| 🐧 **Linux** | Press `Ctrl + Alt + T` |

### Step 3 — Navigate to the Project Folder

```bash
cd python-quiz
```

> 💡 **Tip:** If you don't know where the folder is, drag and drop the folder into the terminal — it will auto-fill the path!

### Step 4 — Install Dependencies

```bash
pip install -r requirements.txt
```

> If `pip` doesn't work, try `pip3 install -r requirements.txt`

### Step 5 — Run the Game! 🎉

```bash
python main.py
```

> If `python` doesn't work, try `python3 main.py`

You should see something like this:

```
╔═════════════════════════════════════════════╗
║      DYNAMIC QUIZ MANAGEMENT SYSTEM        ║
╚═════════════════════════════════════════════╝
    ✨ Full Featured Edition ✨

  1.  📝 Take Quiz
  2.  ⚔️  Multiplayer
  3.  📅 Daily Challenge
  4.  🏆 Leaderboard
  5.  👤 Login / Register
  6.  📊 My Profile
  7.  🏅 Achievements
  8.  📤 Export Results
  9.  🔧 Admin Panel
  0.  🚪 Exit

  Select:
```

**That's it! You're ready to play! 🎮**

---

## 🎯 Game Features

### 📝 Take Quiz
- Choose a **category** (Science, Math, History, Technology, Sports, Entertainment, or All)
- Choose a **difficulty** (Easy, Medium, or Hard)
- Answer questions within a **time limit**
- Use **lifelines** when you're stuck
- Build **streaks** for consecutive correct answers

### ⚔️ Multiplayer Mode
- **2 players** compete head-to-head on the same computer
- Both players answer the same questions
- Scores are tracked round by round
- Winner is crowned at the end! 🏆

### 📅 Daily Challenge
- A fixed set of **5 questions** that changes every day
- Everyone gets the **same questions** on the same day
- Can only be attempted **once per day**
- Come back tomorrow for a new challenge!

### 🏆 Leaderboard
- View the **Top 10** highest scores
- Shows player name, score, percentage, category, and difficulty
- Gold 🥇, Silver 🥈, Bronze 🥉 highlighting for top 3

### 👤 User Profiles & Login
- **Register** with a username, password, and display name
- **Login** to track all your stats
- View your quiz history, average score, best streak, and categories played
- Passwords are securely hashed (SHA-256)

### 🏅 Achievements (9 Badges to Unlock!)

```
╔══════════════════════════════════════════════════════════════╗
║  Badge              ║  How to Unlock                        ║
╠══════════════════════════════════════════════════════════════╣
║  🎓 First Quiz      ║  Complete your first quiz             ║
║  💯 Perfect Score    ║  Get 100% on any quiz                 ║
║  ⚡ Speed Demon      ║  Answer 5 questions in under 5s each  ║
║  🏆 Quiz Master     ║  Complete 10 quizzes                  ║
║  🔥 On Fire         ║  Get 5 correct answers in a row       ║
║  💎 Unstoppable     ║  Get 10 correct answers in a row      ║
║  🌍 Well Rounded    ║  Play all categories                  ║
║  ⚔️ Champion        ║  Win a multiplayer match              ║
║  📅 Daily Player    ║  Complete a daily challenge            ║
╚══════════════════════════════════════════════════════════════╝
```

### 📤 Export Results
- Export leaderboard as a **Text File** (.txt)
- Export leaderboard as a **PDF** (.pdf)
- Files are saved in the `exports/` folder

### 🔧 Admin Panel
- **Add** new questions with category, difficulty, and hints
- **Edit** existing questions
- **Delete** questions
- **Filter** questions by category or difficulty
- Default password: `Astreon@4547`

---

## 🕹️ How to Play — Quick Guide

### Taking a Quiz

1. Select **"1. Take Quiz"** from the main menu
2. Pick a **category** (or choose "All")
3. Pick a **difficulty level**:
   - 🟢 **Easy** — 30 seconds per question, 1x points
   - 🟡 **Medium** — 20 seconds per question, 1.5x points
   - 🔴 **Hard** — 10 seconds per question, 2x points
4. Read the question and type your answer number (1-4)
5. Watch the timer! ⏰ If time runs out, you lose the question

### Using Lifelines

During a quiz, you get **3 lifelines** (one use each):

| Key | Lifeline | What it Does |
|-----|----------|-------------|
| `5` | 🎯 **50:50** | Removes 2 wrong answers |
| `6` | ⏭️ **Skip** | Skips the question (no points) |
| `7` | 💡 **Hint** | Shows a hint (if available) |

### Streaks 🔥

- Get **3+ correct in a row** to start a streak
- Streaks are displayed during the quiz
- Your best streak is saved to your profile

---

## 📁 Project Structure

```
python-quiz/
│
├── 🚀 main.py                 ← Start here! Entry point
├── ⚙️ config.py               ← All settings & constants
├── 📦 requirements.txt        ← Dependencies
│
├── 🧠 quiz/
│   ├── quiz_engine.py         ← Main quiz logic
│   ├── multiplayer.py         ← 2-player mode
│   └── daily_challenge.py     ← Daily challenge mode
│
├── 👤 users/
│   └── profiles.py            ← Registration, login, stats
│
├── 🏅 achievements/
│   └── badges.py              ← Achievement system
│
├── 🏆 leaderboard/
│   └── leaderboard.py         ← Leaderboard display
│
├── 📤 exports/
│   └── export_results.py      ← Text & PDF export
│
├── 🎨 utils/
│   ├── colors.py              ← Colorful terminal output
│   ├── file_handler.py        ← JSON read/write
│   ├── sound.py               ← Sound effects
│   └── timer.py               ← Question timer
│
└── 💾 data/                   ← Auto-generated data files
    ├── questions.json
    ├── users.json
    ├── leaderboard.json
    ├── achievements.json
    └── daily_challenge.json
```

---

## 🛠️ Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `colorama` | 0.4.6 | Colorful terminal text |
| `fpdf2` | 2.8.1 | PDF export |

---

## 💡 Tips for New Players

- 🔐 **Register first** (option 5) so your progress is saved
- 🎯 Start with **Easy** difficulty to learn the ropes
- 📅 Don't forget the **Daily Challenge** — it changes every day!
- 🏅 Check your **Achievements** to see what badges you can unlock
- 📤 **Export** your results to share with friends

---

## ❓ Troubleshooting

| Problem | Solution |
|---------|----------|
| `python` command not found | Try `python3` instead |
| `pip` command not found | Try `pip3` instead |
| No questions available | Use Admin Panel (option 9) to add questions first! |
| Colors look weird | Make sure your terminal supports ANSI colors |
| Sound not working | Sound uses system beep — may not work on all systems |

---

<div align="center">

```
╔═══════════════════════════════════════════╗
║                                           ║
║        Made with ❤️ and Python            ║
║                                           ║
║     Happy Quizzing! 🎮✨                  ║
║                                           ║
╚═══════════════════════════════════════════╝
```

**⭐ Star this repo if you enjoyed it! ⭐**

</div>





