#!/usr/bin/env python3
"""DDOS INFINITY X — UI, banner, and interactive menu."""

from __future__ import annotations

import subprocess
import sys
from typing import Iterable, List, Optional, Sequence

__brand__ = "DDOS INFINITY X"
__author__ = "adil fayyaz"
__version__ = "1.0 INFINITY"
__repo__ = "https://github.com/Infinity-X202/DDOS-INFINITY-X"
__disclaimer__ = (
    "For educational purposes only. "
    "Use only on systems you own or have explicit written permission to test."
)

# ANSI
_Y, _M, _C, _W, _D, _R, _B = (
    "\033[93m", "\033[95m", "\033[96m", "\033[97m", "\033[90m", "\033[0m", "\033[1m"
)
_G = "\033[92m"
_RED = "\033[91m"

_WBOX = 70
_SEP = f"{_M}{'═' * _WBOX}{_R}"


def _out(text: str) -> None:
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode("ascii", "replace").decode("ascii"))


def _box_line(text: str, *, color: str = _W, pipe: str = "║") -> str:
    inner = _WBOX - 2
    t = text[:inner].center(inner)
    return f"{_M}{pipe}{color}{t}{_M}{pipe}{_R}"


def _print_logo() -> None:
    """DDOS INFINITY X logo — Unicode on Kali/Linux, ASCII fallback elsewhere."""
    art = [
        f"{_Y}{_B}██████╗ ██████╗  ██████╗ ███████╗    ██╗███╗   ██╗███████╗██╗███╗   ██╗██╗████████╗██╗  ██╗{_R}",
        f"{_M}██╔══██╗██╔══██╗██╔═══██╗██╔════╝    ██║████╗  ██║██╔════╝██║████╗  ██║██║╚══██╔══╝╚██╗██╔╝{_R}",
        f"{_M}██║  ██║██║  ██║██║   ██║███████╗    ██║██╔██╗ ██║█████╗  ██║██╔██╗ ██║██║   ██║   ╚███╔╝ {_R}",
        f"{_C}██║  ██║██║  ██║██║   ██║╚════██║    ██║██║╚██╗██║██╔══╝  ██║██║╚██╗██║██║   ██║   ██╔██╗ {_R}",
        f"{_C}██████╔╝██████╔╝╚██████╔╝███████║    ██║██║ ╚████║██║     ██║██║ ╚████║██║   ██║   ██╔╝ ██╗{_R}",
        f"{_C}╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝    ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝{_R}",
    ]
    ascii_art = [
        f"{_Y}{_B}  ____  ____  ___  ____     ___ _  _  _   _  _ _____ ___  ____  __  __{_R}",
        f"{_M} |  _ \\|  _ \\/ _ \\/ ___|   |_ _| || || | | || |  __ ) _ \\|  _ \\ \\/ /{_R}",
        f"{_C} | | | | | | | | | \\___ \\    | || || || |_| || | |_ | (_) | | | \\  /{_R}",
        f"{_C} |____/|____/ \\___/|____/   |___|_||_||\\___/|_||____/ \\___/|_| |_|\\_\\{_R}",
    ]
    try:
        "\u2554".encode(sys.stdout.encoding or "utf-8")
        use_unicode = True
    except (UnicodeEncodeError, LookupError, AttributeError):
        use_unicode = False

    pipe = "\u2551" if use_unicode else "|"
    top = f"{_M}\u2554{'\u2550' * _WBOX}\u2557{_R}" if use_unicode else f"{_M}+{'=' * _WBOX}+{_R}"
    mid = f"{_M}\u256a{'\u2550' * _WBOX}\u2569{_R}" if use_unicode else f"{_M}+{'-' * _WBOX}+{_R}"
    bot = f"{_M}\u255a{'\u2550' * _WBOX}\u255d{_R}" if use_unicode else f"{_M}+{'=' * _WBOX}+{_R}"

    _out("")
    _out(top)
    for line in (art if use_unicode else ascii_art):
        _out(f"{_M}{pipe}{_R} {line}")
    _out(mid)
    _out(_box_line(__brand__, color=f"{_C}{_B}", pipe=pipe))
    _out(_box_line(f"by {__author__}  |  v{__version__}", color=_D, pipe=pipe))
    _out(f"{bot}\n")


def _print_methods(columns: Sequence[str], title: str, color: str) -> None:
    _out(f"\n  {color}{_B}[ {title} ]{_R}  ({len(columns)} methods)")
    _out(f"  {_D}{'-' * 66}{_R}")
    row: List[str] = []
    for i, m in enumerate(sorted(columns), 1):
        row.append(f"{_W}{m:12}{_R}")
        if i % 5 == 0:
            _out("  " + "  ".join(row))
            row = []
    if row:
        _out("  " + "  ".join(row))


def show_banner(*, clear: bool = False) -> None:
    if clear:
        print("\033c", end="")
    _print_logo()
    _out(f"  {_D}>> {_R}{__disclaimer}")
    _out(f"  {_C}{__repo__}{_R}\n")


def show_main_menu(
    *,
    l7: Iterable[str],
    l4: Iterable[str],
    tools: Iterable[str],
    script: str = "start.py",
) -> None:
    show_banner()
    _out(_SEP)
    _out(f"  {_Y}{_B}  MAIN MENU  —  select an option{_R}\n")
    opts = [
        ("1", "Launch Layer 7 attack", "HTTP/HTTPS flood & bypass"),
        ("2", "Launch Layer 4 attack", "TCP / UDP / game protocols"),
        ("3", "Open Tools console", "PING · CHECK · DSTAT · DNS …"),
        ("4", "List all methods", "Show L4 + L7 method names"),
        ("5", "Command syntax / HELP", "Full usage examples"),
        ("6", "Exit", ""),
    ]
    for num, title, desc in opts:
        _out(f"  {_G}[{num}]{_R} {_W}{title:<28}{_R} {_D}{desc}{_R}")
    _out(f"\n{_SEP}\n")


def show_attack_banner(method: str, target: str, threads: int, duration: int) -> None:
    _out(f"\n{_M}{_SEP}{_R}")
    _out(f"  {_Y}{_B}[ ENGAGE ]{_R}  {_C}{__brand__}{_R}")
    _out(f"  {_W}Method:{_R} {_M}{method}{_R}   {_W}Target:{_R} {_C}{target}{_R}")
    _out(f"  {_W}Threads:{_R} {threads}   {_W}Duration:{_R} {duration}s")
    _out(f"{_M}{_SEP}{_R}\n")


def _prompt(label: str, default: str = "") -> str:
    hint = f" [{default}]" if default else ""
    val = input(f"  {_C}{label}{_R}{hint}: ").strip()
    return val or default


def _run_script(args: List[str], script: str) -> None:
    cmd = [sys.executable, script, *args]
    print(f"\n  {_D}>> {' '.join(cmd)}{_R}\n")
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print(f"\n  {_Y}Stopped.{_R}")


def run_interactive_menu(
    script: str,
    l7: Sequence[str],
    l4: Sequence[str],
    tools: Sequence[str],
    usage_cb=None,
) -> None:
    l7_set = set(m.upper() for m in l7)
    l4_set = set(m.upper() for m in l4)

    while True:
        show_main_menu(l7=l7, l4=l4, tools=tools, script=script)
        choice = _prompt("Choice", "1").upper()

        if choice in {"6", "Q", "EXIT", "E"}:
            print(f"  {_Y}Goodbye.{_R}\n")
            return

        if choice == "4":
            _print_methods(l7, "LAYER 7", _M)
            _print_methods(l4, "LAYER 4", _C)
            print(f"\n  {_D}Tools:{_R} {', '.join(sorted(tools))}")
            input(f"\n  {_D}Press Enter to continue...{_R}")
            continue

        if choice == "5":
            if usage_cb:
                usage_cb()
            input(f"\n  {_D}Press Enter to continue...{_R}")
            continue

        if choice == "3":
            _run_script(["tools"], script)
            continue

        if choice == "1":
            print(f"\n  {_M}{_B}── Layer 7 setup ──{_R}")
            print(f"  {_D}Methods: {', '.join(sorted(l7_set)[:12])}...{_R}\n")
            method = _prompt("Method (e.g. GET, CFB, BYPASS)").upper()
            if method not in l7_set:
                print(f"  {_RED}Unknown L7 method.{_R}")
                continue
            url = _prompt("Target URL", "http://")
            socks = _prompt("Proxy type (0=all,1=http,4=socks4,5=socks5)", "0")
            threads = _prompt("Threads", "100")
            proxy_file = _prompt("Proxy list file", "http.txt")
            rpc = _prompt("RPC", "10")
            duration = _prompt("Duration (seconds)", "60")
            _run_script(
                [method, url, socks, threads, proxy_file, rpc, duration],
                script,
            )
            continue

        if choice == "2":
            print(f"\n  {_C}{_B}── Layer 4 setup ──{_R}")
            print(f"  {_D}Methods: {', '.join(sorted(l4_set)[:12])}...{_R}\n")
            method = _prompt("Method (e.g. TCP, UDP, SYN)").upper()
            if method not in l4_set:
                print(f"  {_RED}Unknown L4 method.{_R}")
                continue
            target = _prompt("Target ip:port", "127.0.0.1:80")
            threads = _prompt("Threads", "50")
            duration = _prompt("Duration (seconds)", "30")
            _run_script([method, target, threads, duration], script)
            continue

        print(f"  {_RED}Invalid choice. Use 1-6.{_R}")


if __name__ == "__main__":
    show_banner()
    print("Run: python start.py")
