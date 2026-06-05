<h1 align="center">DDOS INFINITY X</h1>
<p align="center"><strong>Stress-testing framework — 57+ methods (Layer 4 & Layer 7)</strong></p>
<p align="center"><em>Created by <strong>adil fayyaz</strong> · v1.0 INFINITY</em></p>

<p align="center">
  <a href="https://github.com/Infinity-X202/DDOS-INFINITY-X"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-DDOS--INFINITY--X-181717?style=for-the-badge&logo=github"></a>
</p>

<p align="center">
  <strong>For educational purposes only.</strong><br>
  Use only on systems you own or with explicit written permission.<br>
  Unauthorized use is illegal.
</p>

---

## Install (recommended — avoids errors)

### Linux / Kali / Debian / Ubuntu

```bash
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
chmod +x install.sh run.sh
./install.sh
./run.sh
```

> **Do not** run `pip install -r requirements.txt` directly on Kali — you will get `externally-managed-environment`. Use `./install.sh` (creates a `venv`).

### Windows

```cmd
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
install.bat
run.bat
```

### Requirements

- Python **3.10+**
- **Git** (needed to install PyRoxy from GitHub)
- Linux: `python3-venv` → `sudo apt install python3 python3-venv python3-pip git`

---

## How to run

| Action | Command |
|--------|---------|
| **Interactive menu** (easiest) | `./run.sh` or `python start.py` |
| Full help + syntax | `./run.sh HELP` |
| Tools (PING, DSTAT, CHECK…) | `./run.sh tools` |
| Stop Python floods | `./run.sh STOP` |

After install, always use **`./run.sh`** (Linux) or **`run.bat`** (Windows) so the virtual environment is active.

---

## Command examples (copy as-is)

Replace only `YOUR-TARGET` with a host you **own** or are **authorized** to test.

### Layer 7 (HTTP/HTTPS)

```bash
./run.sh GET http://YOUR-TARGET 0 100 http.txt 10 60
```

| Argument | Meaning |
|----------|---------|
| `GET` | Method (GET, POST, CFB, BYPASS, …) |
| `http://YOUR-TARGET` | Target URL |
| `0` | Proxy type: 0=config, 1=HTTP, 4=SOCKS4, 5=SOCKS5, 6=random |
| `100` | Threads |
| `http.txt` | Proxy list in `files/proxies/` (can be empty) |
| `10` | RPC (requests per connection) |
| `60` | Duration in seconds |

### Layer 4 (TCP / UDP / …)

```bash
./run.sh TCP YOUR-IP:80 50 30
```

| Argument | Meaning |
|----------|---------|
| `TCP` | Method (TCP, UDP, SYN, MINECRAFT, …) |
| `YOUR-IP:80` | Target IP and port |
| `50` | Threads |
| `30` | Duration (seconds) |

### Layer 4 with proxies

```bash
./run.sh TCP 192.168.1.10:80 50 30 5 http.txt
```

---

## Kali — still errors?

```bash
cd DDOS-INFINITY-X
git pull
chmod +x install.sh run.sh check.sh
./install.sh
./check.sh
./run.sh
```

If install fails: `sudo apt install -y python3-dev build-essential libffi-dev libssl-dev git`

**Never** use `sudo pip install` on Kali.

## Common errors

| Error | Fix |
|-------|-----|
| `externally-managed-environment` | Use `./install.sh`, not system `pip` |
| `No module named 'PyRoxy'` | `./install.sh` then `./run.sh` |
| `bad interpreter` / `$'\r'` | `sed -i 's/\r$//' *.sh` then `chmod +x *.sh` |
| `syntax error near '<'` | Use `GET`, `TCP` — not `<METHOD>` |
| `Cannot Create Raw Socket` | Use `sudo ./run.sh` for SYN/ICMP |
| `docker: command not found` | Use `install.sh` + `run.sh` |
| `Cannot resolve hostname` | Check URL/IP and network |
| Proxy file missing | `touch files/proxies/http.txt` |

---

## Interactive menu

Running without arguments opens the menu:

```
[1] Launch Layer 7 attack
[2] Launch Layer 4 attack
[3] Open Tools console
[4] List all methods
[5] Command syntax / HELP
[6] Exit
```

---

## Methods overview

**Layer 7:** GET, POST, OVH, CFB, CFBUAM, BYPASS, SLOW, STRESS, DGB, BOT, XMLRPC, TOR, …

**Layer 4:** TCP, UDP, SYN, ICMP, MINECRAFT, FIVEM, TS3, VSE, CPS, CONNECTION, …

**Tools:** PING, CHECK, DSTAT, DNS, TSSRV, INFO

---

## Docker (optional)

```bash
sudo apt install docker.io docker-compose-v2
docker compose build
docker compose run -it --entrypoint /bin/bash infinityx
```

Inside container: `python start.py` or `python start.py HELP`

---

## Configuration

- `config.json` — proxy providers, Minecraft settings  
- `files/useragent.txt`, `files/referers.txt`, `files/proxies/http.txt`

---

## Links

- **Repository:** https://github.com/Infinity-X202/DDOS-INFINITY-X  
- **Issues:** https://github.com/Infinity-X202/DDOS-INFINITY-X/issues  
- **Author:** adil fayyaz  

## Credits

Fork/customization based on [MHDDoS](https://github.com/MatrixTM/MHDDoS) (MIT).  
**DDOS INFINITY X** © adil fayyaz.

## License

MIT — see [LICENSE](LICENSE).
