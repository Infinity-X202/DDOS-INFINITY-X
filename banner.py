#!/usr/bin/env python3
"""DDOS INFINITY X - startup banner and branding."""

__brand__ = "DDOS INFINITY X"
__author__ = "adil fayyaz"
__version__ = "1.0 INFINITY"
__repo__ = "https://github.com/adilf/DDOS-INFINITY-X"
__disclaimer__ = (
    "For educational purposes only. "
    "Use only on systems you own or have explicit written permission to test."
)

_Y = "\033[93m"
_M = "\033[95m"
_C = "\033[96m"
_W = "\033[97m"
_D = "\033[90m"
_R = "\033[0m"
_B = "\033[1m"

_LOGO = r"""
  _____  _____   ___   _____     ___ _   _ _   _ _   _ _____ _   _ _____ ____  
 |  __ \|  __ \ / _ \ / ____|   |_ _| \ | | | | | \ | |_   _| | | |  ___/ ___| 
 | |  | | |  | | | | | (___      | ||  \| | | | |  \| | | | | | | | |_  \___ \ 
 | |  | | |  | | | | |\___ \     | || |\  | |_| | |\  | | | | |_| |  _| |___) |
 |_____/|_____/ \___/ |____/    |___|_| \_|\___/|_| \_| |_|  \___/|_|   |____/ 

  ___ _   _ _   _ _   _ _____ _   _ _____ ____  __  __  __  __
 |_ _| \ | | | | | \ | |_   _| | | |  ___/ ___| \ \/ / \ \/ /
  | ||  \| | | | |  \| | | | | | | | |_  \___ \  \  /   \  / 
  | || |\  | |_| | |\  | | | | |_| |  _| |___) | /  \   /  \ 
 |___|_| \_|\___/|_| \_| |_|  \___/|_|   |____/ /_/\_\ /_/\_\

       _  __  __
      / \/ / \ \
      \  /\  / /
       \/  \/ /
"""

_SEP = f"{_M}{'=' * 72}{_R}"


def _gradient_print(text: str) -> None:
    lines = text.strip("\n").split("\n")
    n = max(len(lines) - 1, 1)
    for i, line in enumerate(lines):
        r = i / n
        if r < 0.4:
            c = _Y
        elif r < 0.7:
            c = _M
        else:
            c = _C
        print(f"{c}{_B}{line}{_R}")


def show_banner(*, clear: bool = False) -> None:
    if clear:
        print("\033c", end="")
    _gradient_print(_LOGO)
    print()
    print(f"{_M}  </> {_W}Author: {_B}{__author__}{_R}{_M}  |  {_W}Build: {_C}{__version__}{_R}")
    print(f"{_D}  >> {__disclaimer__}{_R}")
    print()
    print(_SEP)
    print(
        f"{_M}  {_B}{__brand__}{_R}{_M}  |  "
        f"Layer4 / Layer7 / Tools  |  python start.py HELP{_R}"
    )
    print(f"{_D}  {_C}{__repo__}{_R}")
    print(_SEP)
    print()


def show_attack_banner(method: str, target: str, threads: int, duration: int) -> None:
    print(f"\n{_M}{_SEP}{_R}")
    print(f"{_Y}{_B}  [*] ENGAGE{_R}  {_W}{method}{_R}  {_D} -> {_R}  {_C}{target}{_R}")
    print(
        f"{_D}      threads: {_W}{threads}{_R}  |  "
        f"duration: {_W}{duration}s{_R}  |  {_M}{__brand__}{_R}"
    )
    print(f"{_M}{_SEP}{_R}\n")


if __name__ == "__main__":
    show_banner()
