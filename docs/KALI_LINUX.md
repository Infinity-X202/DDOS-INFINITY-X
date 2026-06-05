# DDOS INFINITY X — Kali Linux (copy & paste)

**Repository:** https://github.com/Infinity-X202/DDOS-INFINITY-X  
**Author:** adil fayyaz

---

## Install & run (recommended)

Copy and paste **all lines** in your Kali terminal:

```bash
cd ~
rm -rf DDOS-INFINITY-X
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
python3 start.py HELP
```

After install, every time you open a new terminal:

```bash
cd ~/DDOS-INFINITY-X
source venv/bin/activate
python3 start.py HELP
```

---

## Commands

```bash
python3 start.py HELP
python3 start.py tools
python3 start.py GET http://example.com 0 1000 http.txt 10 100
python3 start.py TCP 1.1.1.1:80 500 60
python3 start.py STOP
```

Full list: [COMMANDS.md](../COMMANDS.md)

---

## Update project

```bash
cd ~/DDOS-INFINITY-X
git pull
source venv/bin/activate
python3 start.py HELP
```

---

## If pip fails

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip python3-dev git build-essential
```

Then run the install block again from the top.

---

For educational purposes only.
