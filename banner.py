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


def _default_l7_method(l7: Sequence[str]) -> str:
    order = ("GET", "POST", "CFB", "BYPASS", "HEAD")
    for m in order:
        if m in {x.upper() for x in l7}:
            return m
    return sorted(l7)[0].upper() if l7 else "GET"


def _default_l4_method(l4: Sequence[str]) -> str:
    order = ("TCP", "UDP", "SYN")
    for m in order:
        if m in {x.upper() for x in l4}:
            return m
    return sorted(l4)[0].upper() if l4 else "TCP"


def show_main_menu(
    *,
    l7: Iterable[str],
    l4: Iterable[str],
    tools: Iterable[str],
    script: str = "start.py",
) -> None:
    show_banner(show_commands=False)
    m7 = _default_l7_method(tuple(l7))
    m4 = _default_l4_method(tuple(l4))
    _out(_SEP)
    _out(f"  {_Y}{_B}  MENU  —  scegli 1 2 3 4{_R}\n")
    opts = [
        ("1", f"Attacco L7 ({m7})", "solo URL → parte subito"),
        ("2", f"Attacco L4 ({m4})", "solo ip:port → parte subito"),
        ("3", "Tools", "PING CHECK DSTAT …"),
        ("4", "Lista metodi + HELP", ""),
        ("0", "Esci", ""),
    ]
    for num, title, desc in opts:
        _out(f"  {_G}[{num}]{_R} {_W}{title:<28}{_R} {_D}{desc}{_R}")
    _out(f"\n  {_D}Invio = opzione 1  ·  anche: python3 {script} 1 <url>{_R}")
    _out(f"\n{_SEP}\n")


def run_quick_l7(
    script: str,
    *,
    url: str | None = None,
    method: str | None = None,
    l7: Sequence[str] | None = None,
) -> None:
    """Option 1 — first L7 attack (GET) with defaults."""
    l7_set = {m.upper() for m in (l7 or ())}
    method = (method or _default_l7_method(l7 or ("GET",))).upper()
    if l7_set and method not in l7_set:
        method = _default_l7_method(l7 or ())
    if not url:
        url = _prompt("URL target", "http://")
    if not url.startswith(("http://", "https://")):
        url = "http://" + url.lstrip("/")
    show_attack_banner(method, url, 1000, 60)
    _run_script(
        [method, url, "0", "1000", "http.txt", "10", "60"],
        script,
    )


def run_quick_l4(
    script: str,
    *,
    target: str | None = None,
    method: str | None = None,
    l4: Sequence[str] | None = None,
) -> None:
    """Option 2 — first L4 attack (TCP) with defaults."""
    l4_set = {m.upper() for m in (l4 or ())}
    method = (method or _default_l4_method(l4 or ("TCP",))).upper()
    if l4_set and method not in l4_set:
        method = _default_l4_method(l4 or ())
    if not target:
        target = _prompt("ip:port", "127.0.0.1:80")
    show_attack_banner(method, target, 500, 60)
    _run_script([method, target, "500", "60"], script)


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
    while True:
        show_main_menu(l7=l7, l4=l4, tools=tools, script=script)
        choice = _prompt("Scelta (1-4, 0 esci)", "1").upper()

        if choice in {"0", "6", "Q", "EXIT", "E"}:
            _out(f"  {_Y}Uscita.{_R}\n")
            return
        if choice in {"1", ""}:
            run_quick_l7(script, l7=l7)
            continue
        if choice == "2":
            run_quick_l4(script, l4=l4)
            continue
        if choice == "3":
            _run_script(["tools"], script)
            continue
        if choice == "4":
            _print_methods(l7, "LAYER 7", _M)
            _print_methods(l4, "LAYER 4", _C)
            _out(f"\n  {_D}Tools:{_R} {', '.join(sorted(tools))}")
            if usage_cb:
                usage_cb()
            input(f"\n  {_D}Invio per tornare al menu...{_R}")
            continue
        _out(f"  {_RED}Non valido. Usa 1, 2, 3, 4 o 0.{_R}")
