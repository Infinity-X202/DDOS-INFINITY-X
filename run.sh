#!/usr/bin/env bash
# DDOS INFINITY X — launcher (always uses venv)
cd "$(dirname "$0")"

if [ ! -d "venv" ]; then
  echo "[!] Virtual environment not found."
  echo "    Run first:  chmod +x install.sh && ./install.sh"
  exit 1
fi

# shellcheck disable=SC1091
source venv/bin/activate
exec python start.py "$@"
