#!/usr/bin/env bash
# DDOS INFINITY X — install (Kali / Debian / Ubuntu)
set -euo pipefail
cd "$(dirname "$0")"

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m'

echo -e "${CYAN}=============================================="
echo "  DDOS INFINITY X — Install"
echo "  by adil fayyaz"
echo -e "==============================================${NC}"

# --- System packages (Kali PEP 668) ---
MISSING_APT=()
for pkg in python3 python3-venv python3-pip git; do
  dpkg -s "$pkg" >/dev/null 2>&1 || MISSING_APT+=("$pkg")
done

if [ ${#MISSING_APT[@]} -gt 0 ]; then
  echo -e "${YELLOW}[*] Installing system packages (sudo)...${NC}"
  echo "    sudo apt update"
  echo "    sudo apt install -y python3 python3-venv python3-pip python3-dev git build-essential libffi-dev libssl-dev"
  if command -v sudo >/dev/null 2>&1; then
    sudo apt update
    sudo apt install -y python3 python3-venv python3-pip python3-dev git \
      build-essential libffi-dev libssl-dev pkg-config
  else
    echo -e "${RED}[!] Run as root or install: ${MISSING_APT[*]}${NC}"
    exit 1
  fi
fi

if ! command -v python3 >/dev/null 2>&1; then
  echo -e "${RED}[!] python3 not found.${NC}"
  exit 1
fi

PYVER=$(python3 -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')
echo -e "${GREEN}[+] Python ${PYVER}${NC}"

# --- venv ---
if [ -d "venv" ]; then
  echo -e "${YELLOW}[*] Removing old venv...${NC}"
  rm -rf venv
fi

echo -e "${CYAN}[*] Creating virtual environment...${NC}"
python3 -m venv venv
# shellcheck disable=SC1091
source venv/bin/activate

echo -e "${CYAN}[*] Upgrading pip...${NC}"
pip install --upgrade pip wheel setuptools

echo -e "${CYAN}[*] Installing dependencies (2-5 min)...${NC}"

# Install in stages so one failure does not hide the cause
pip install cloudscraper==1.2.71 certifi dnspython==2.6.1 requests psutil icmplib pyasn1 yarl || {
  echo -e "${RED}[!] Base packages failed.${NC}"
  exit 1
}

echo -e "${CYAN}[*] Installing impacket...${NC}"
pip install "impacket>=0.11.0" || pip install impacket==0.10.0 || {
  echo -e "${RED}[!] impacket failed. Try: sudo apt install -y python3-impacket${NC}"
  echo "    Then re-run ./install.sh"
  exit 1
}

echo -e "${CYAN}[*] Installing PyRoxy (from GitHub, needs git)...${NC}"
pip install "git+https://github.com/MatrixTM/PyRoxy.git" || {
  echo -e "${RED}[!] PyRoxy install failed.${NC}"
  echo "    Check: git --version"
  echo "    Manual: pip install git+https://github.com/MatrixTM/PyRoxy.git"
  exit 1
}

mkdir -p files/proxies
touch files/proxies/http.txt
chmod +x run.sh check.sh 2>/dev/null || true

echo -e "${CYAN}[*] Verifying installation...${NC}"
if ! python check_env.py; then
  echo -e "${RED}[!] Verification failed. Run: ./check.sh${NC}"
  exit 1
fi

echo ""
echo -e "${GREEN}[+] Install OK!${NC}"
echo ""
echo "  ./run.sh              → interactive menu"
echo "  ./run.sh HELP         → full help"
echo "  ./run.sh tools        → tools console"
echo ""
