"""Simple sound effects using system beep."""

import sys


def beep():
    try:
        if sys.platform == "win32":
            import winsound
            winsound.Beep(1000, 200)
        else:
            sys.stdout.write("\a")
            sys.stdout.flush()
    except Exception:
        pass

def correct_sound():
    try:
        if sys.platform == "win32":
            import winsound
            winsound.Beep(1200, 150)
            winsound.Beep(1500, 150)
        else:
            sys.stdout.write("\a")
            sys.stdout.flush()
    except Exception:
        pass

def wrong_sound():
    try:
        if sys.platform == "win32":
            import winsound
            winsound.Beep(400, 300)
        else:
            sys.stdout.write("\a")
            sys.stdout.flush()
    except Exception:
        pass

def achievement_sound():
    try:
        if sys.platform == "win32":
            import winsound
            for freq in [800, 1000, 1200, 1500]:
                winsound.Beep(freq, 100)
        else:
            sys.stdout.write("\a\a")
            sys.stdout.flush()
    except Exception:
        pass
