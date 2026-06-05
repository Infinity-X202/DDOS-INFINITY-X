# Kali Linux — DDOS INFINITY X

Same commands as GitHub README. Only install differs (venv).

```bash
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Run

```bash
source venv/bin/activate
python3 start.py HELP
python3 start.py GET http://example.com 0 1000 http.txt 10 60
python3 start.py tools
```

## Errors

| Error | Fix |
|-------|-----|
| externally-managed-environment | Use `venv` + `source venv/bin/activate` |
| No module named PyRoxy | `pip3 install -r requirements.txt` inside venv |
| Need git | `sudo apt install git` |

Optional helper: `./install.sh` (creates venv automatically).
