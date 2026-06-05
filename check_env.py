#!/usr/bin/env python3
"""Verify DDOS INFINITY X dependencies."""
import sys

MODULES = [
    ("PyRoxy", "pip install git+https://github.com/MatrixTM/PyRoxy.git"),
    ("cloudscraper", "pip install cloudscraper"),
    ("certifi", "pip install certifi"),
    ("dns", "pip install dnspython"),
    ("requests", "pip install requests"),
    ("impacket", "pip install impacket"),
    ("psutil", "pip install psutil"),
    ("icmplib", "pip install icmplib"),
    ("yarl", "pip install yarl"),
]

ok = True
for mod, fix in MODULES:
    try:
        __import__(mod)
        print(f"  OK   {mod}")
    except ImportError as e:
        print(f"  FAIL {mod} — {e}")
        print(f"       Fix: {fix}")
        ok = False

if ok:
    print("\nAll dependencies OK.")
    sys.exit(0)
print("\nRun: ./install.sh  (inside project folder, with venv)")
sys.exit(1)
