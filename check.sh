#!/usr/bin/env bash
cd "$(dirname "$0")"
echo "=== DDOS INFINITY X — Diagnostics ==="
echo "OS: $(uname -a)"
echo "Python: $(python3 --version 2>&1)"
echo "Git: $(git --version 2>&1)"
echo ""
if [ ! -d venv ]; then
  echo "[!] venv missing — run: ./install.sh"
  exit 1
fi
source venv/bin/activate
echo "venv Python: $(python --version)"
echo ""
python check_env.py
echo ""
echo "Test banner:"
python -c "from banner import show_banner; show_banner()" 2>&1 | head -20
