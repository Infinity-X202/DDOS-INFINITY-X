#!/usr/bin/env python3
"""DDOS INFINITY X — UI, banner, and optional menu."""

from __future__ import annotations

import subprocess
import sys
from typing import Iterable, List, Sequence

__brand__ = "DDOS INFINITY X"
__author__ = "adil fayyaz"
__version__ = "1.0 INFINITY"
__repo__ = "https://github.com/Infinity-X202/DDOS-INFINITY-X"
__disclaimer__ = (
    "For educational purposes only. "
    "Use only on systems you own or have explicit written permission to test."
)
# Back-compat (prevents NameError on old copies)
__disclaimer = __disclaimer__

_Y, _M, _C, _W, _D, _R, _B = (
    "\033[93m", "\033[95m", "\033[96m", "\033[97m", "\033[90m", "\033[0m", "\033[1m"
)
_G, _RED = "\033[92m", "\033[91m"
_WBOX = 72
_SEP = f"{_M}{'═' * _WBOX}{_R}"


def _out(text: str) -> None:
    try:
        print(text)
    except UnicodeEncodeError:
        print(text.encode("ascii", "replace").decode("ascii"))


def _supports_unicode_box() -> bool:
    try:
        "\u2554\u2550\u2557".encode(sys.stdout.encoding or "utf-8")
        return True
    except (UnicodeEncodeError, LookupError, AttributeError):
        return False


def _print_logo() -> None:
    """Clean DDOS + INFINITY X banner for Kali / Linux terminals."""
    u = _supports_unicode_box()
    if u:
        top, side, mid, bot = "\u2554", "\u2551", "\u256a", "\u255a"
        hbar, vbar = "\u2550", "\u2557"
    else:
        top, side, mid, bot, hbar, vbar = "+", "|", "+", "+", "=", "+"

    ddos = [
        f"{_Y}{_B}██████╗ ██████╗  ██████╗ ███████╗{_R}",
        f"{_Y}{_B}██╔══██╗██╔══██╗██╔═══██╗██╔════╝{_R}",
        f"{_M}{_B}██║  ██║██║  ██║██║   ██║███████╗{_R}",
        f"{_M}{_B}██║  ██║██║  ██║██║▄▄ ██║╚════██║{_R}",
        f"{_C}{_B}██████╔╝██████╔╝╚██████╔╝███████║{_R}",
        f"{_C}{_B}╚═════╝ ╚═════╝  ╚══▀▀═╝ ╚══════╝{_R}",
    ]
    infx = [
        f"{_M}{_B}██╗███╗   ██╗███████╗██╗███╗   ██╗██╗████████╗██╗  ██╗   ██╗{_R}",
        f"{_C}{_B}██║████╗  ██║██╔════╝██║████╗  ██║██║╚══██╔══╝╚██╗██╔╝   ██║{_R}",
        f"{_C}{_B}██║██╔██╗ ██║█████╗  ██║██╔██╗ ██║██║   ██║   ╚███╔╝    ██║{_R}",
        f"{_Y}{_B}██║██║╚██╗██║██╔══╝  ██║██║╚██╗██║██║   ██║   ██╔██╗    ██║{_R}",
        f"{_Y}{_B}██║██║ ╚████║██║     ██║██║ ╚████║██║   ██║   ██╔╝ ██╗   ██║{_R}",
        f"{_M}{_B}╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝   ╚═╝{_R}",
    ]

    _out("")
    _out(f"{_M}{top}{hbar * _WBOX}{vbar}{_R}")
    for line in ddos:
        _out(f"{_M}{side}{_R} {line}")
    _out(f"{_M}{mid}{hbar * _WBOX}{vbar}{_R}")
    title = f"  ★  {__brand__}  ★  "
    _out(f"{_M}{side}{_R}{_C}{_B}{title.center(_WBOX + 8)}{_R}")
    sub = f"  by {__author__}  ·  {__version__}  "
    _out(f"{_M}{side}{_R}{_D}{sub.center(_WBOX + 4)}{_R}")
    _out(f"{_M}{mid}{hbar * _WBOX}{vbar}{_R}")
    for line in infx:
        _out(f"{_M}{side}{_R} {line}")
    _out(f"{_M}{bot}{hbar * _WBOX}{vbar}{_R}\n")


def _print_quick_commands() -> None:
    _out(f"  {_G}{_B}Quick commands:{_R}")
    _out(f"  {_W}python3 start.py HELP{_R}  {_D}|{_R}  {_W}python3 start.py tools{_R}")
    _out(
        f"  {_W}python3 start.py GET http://target 0 1000 http.txt 10 60{_R}"
    )
    _out(
        f"  {_W}python3 start.py TCP ip:port 500 60{_R}  "
        f"{_D}|  Full list: github.com/Infinity-X202/DDOS-INFINITY-X/blob/main/COMMANDS.md{_R}\n"
    )


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


def show_banner(*, clear: bool = False, show_commands: bool = True) -> None:
    if clear:
        print("\033c", end="")
    _print_logo()
    _out(f"  {_D}>> {_R}{__disclaimer__}")
    _out(f"  {_C}{__repo__}{_R}")
    if show_commands:
        _print_quick_commands()


def show_main_menu(
    *,
    l7: Iterable[str],
    l4: Iterable[str],
    tools: Iterable[str],
    script: str = "start.py",
) -> None:
    show_banner(show_commands=False)
    _out(_SEP)
    _out(f"  {_Y}{_B}  MAIN MENU  —  DDOS INFINITY X{_R}\n")
    opts = [
        ("1", "Layer 7 attack", "GET POST CFB BYPASS …"),
        ("2", "Layer 4 attack", "TCP UDP SYN …"),
        ("3", "Tools console", "PING CHECK DSTAT"),
        ("4", "List all methods", ""),
        ("5", "Full HELP / syntax", ""),
        ("6", "Exit", ""),
    ]
    for num, title, desc in opts:
        _out(f"  {_G}[{num}]{_R} {_W}{title:<22}{_R} {_D}{desc}{_R}")
    _out(f"\n{_SEP}\n")


def show_attack_banner(method: str, target: str, threads: int, duration: int) -> None:
    _out(f"\n{_M}{_SEP}{_R}")
    _out(f"  {_Y}{_B}[ ENGAGE ]{_R}  {_C}{__brand__}{_R}")
    _out(f"  {_W}Method:{_R} {_M}{method}{_R}   {_W}Target:{_R} {_C}{target}{_R}")
    _out(f"  {_W}Threads:{_R} {threads}   {_W}Duration:{_R} {duration}s")
    _out(f"{_M}{_SEP}{_R}\n")


def _prompt(label: str, default: str = "") -> str:
    hint = f" [{default}]" if default else ""
    return input(f"  {_C}{label}{_R}{hint}: ").strip() or default


def _run_script(args: List[str], script: str) -> None:
    cmd = [sys.executable, script, *args]
    _out(f"\n  {_D}>> {' '.join(cmd)}{_R}\n")
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        _out(f"\n  {_Y}Stopped.{_R}")


def run_interactive_menu(
    script: str,
    l7: Sequence[str],
    l4: Sequence[str],
    tools: Sequence[str],
    usage_cb=None,
) -> None:
    l7_set = {m.upper() for m in l7}
    l4_set = {m.upper() for m in l4}

    while True:
        show_main_menu(l7=l7, l4=l4, tools=tools, script=script)
        choice = _prompt("Choice", "5").upper()

        if choice in {"6", "Q", "EXIT", "E"}:
            _out(f"  {_Y}Goodbye.{_R}\n")
            return
        if choice == "4":
            _print_methods(l7, "LAYER 7", _M)
            _print_methods(l4, "LAYER 4", _C)
            _out(f"\n  {_D}Tools:{_R} {', '.join(sorted(tools))}")
            input(f"\n  {_D}Press Enter...{_R}")
            continue
        if choice == "5":
            if usage_cb:
                usage_cb()
            input(f"\n  {_D}Press Enter...{_R}")
            continue
        if choice == "3":
            _run_script(["tools"], script)
            continue
        if choice == "1":
            method = _prompt("L7 Method", "GET").upper()
            if method not in l7_set:
                _out(f"  {_RED}Unknown method.{_R}")
                continue
            _run_script([
                method,
                _prompt("URL", "http://"),
                _prompt("Socks", "0"),
                _prompt("Threads", "1000"),
                _prompt("Proxy file", "http.txt"),
                _prompt("RPC", "10"),
                _prompt("Seconds", "60"),
            ], script)
            continue
        if choice == "2":
            method = _prompt("L4 Method", "TCP").upper()
            if method not in l4_set:
                _out(f"  {_RED}Unknown method.{_R}")
                continue
            _run_script([
                method,
                _prompt("ip:port", "127.0.0.1:80"),
                _prompt("Threads", "500"),
                _prompt("Seconds", "60"),
            ], script)
            continue
        _out(f"  {_RED}Invalid. Use 1-6.{_R}")
