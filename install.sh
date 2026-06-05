#!/usr/bin/env bash
# DDOS INFINITY X — install script (Linux / Kali / Debian / Ubuntu)
set -e
cd "$(dirname "$0")"

echo "=============================================="
echo "  DDOS INFINITY X — Install"
echo "  by adil fayyaz"
echo "=============================================="

if ! command -v python3 >/dev/null 2>&1; then
  echo "[!] python3 not found. Install: sudo apt install python3 python3-venv python3-pip git"
  exit 1
fi

if ! command -v git >/dev/null 2>&1; then
  echo "[!] git not found (required for PyRoxy). Install: sudo apt install git"
  exit 1
fi

echo "[*] Creating virtual environment..."
python3 -m venv venv

echo "[*] Installing dependencies (may take a few minutes)..."
# shellcheck disable=SC1091
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

mkdir -p files/proxies
touch files/proxies/http.txt

chmod +x run.sh 2>/dev/null || true

echo ""
echo "[+] Install complete!"
echo ""
echo "  Start interactive menu:"
echo "    ./run.sh"
echo ""
echo "  Or:"
echo "    source venv/bin/activate"
echo "    python start.py"
echo ""
