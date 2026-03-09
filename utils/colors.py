"""Colorful terminal output utilities using colorama."""

from colorama import Fore, Back, Style, init
import sys

if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

init(autoreset=True)


def success(text):
    return f"{Fore.GREEN}{Style.BRIGHT}{text}{Style.RESET_ALL}"

def error(text):
    return f"{Fore.RED}{Style.BRIGHT}{text}{Style.RESET_ALL}"

def warning(text):
    return f"{Fore.YELLOW}{text}{Style.RESET_ALL}"

def info(text):
    return f"{Fore.CYAN}{text}{Style.RESET_ALL}"

def highlight(text):
    return f"{Fore.MAGENTA}{Style.BRIGHT}{text}{Style.RESET_ALL}"

def header(text):
    return f"{Fore.WHITE}{Back.BLUE}{Style.BRIGHT} {text} {Style.RESET_ALL}"

def gold(text):
    return f"{Fore.YELLOW}{Style.BRIGHT}{text}{Style.RESET_ALL}"

def dim(text):
    return f"{Style.DIM}{text}{Style.RESET_ALL}"

def banner(text, color=Fore.CYAN):
    width = 45
    border = "═" * width
    padding = text.center(width)
    print(f"{color}╔{border}╗")
    print(f"║{padding}║")
    print(f"╚{border}╝{Style.RESET_ALL}")





