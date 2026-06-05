<h1 align="center">DDOS INFINITY X</h1>
<p align="center"><strong>Stress-testing framework — 57+ methods (Layer 4 & Layer 7)</strong></p>
<p align="center"><em>Created by <strong>adil fayyaz</strong> · Python 3</em></p>

<p align="center">
  <a href="https://github.com/Infinity-X202/DDOS-INFINITY-X"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-DDOS--INFINITY--X-181717?style=for-the-badge&logo=github"></a>
  <a href="https://github.com/Infinity-X202/DDOS-INFINITY-X/blob/main/LICENSE"><img alt="License" src="https://img.shields.io/github/license/Infinity-X202/DDOS-INFINITY-X?color=orange&style=for-the-badge"></a>
  <a href="https://github.com/Infinity-X202/DDOS-INFINITY-X/issues"><img alt="Issues" src="https://img.shields.io/github/issues/Infinity-X202/DDOS-INFINITY-X?color=purple&style=for-the-badge"></a>
</p>

<p align="center">
  <strong>For educational purposes only.</strong><br>
  Use only on systems you own or have explicit written permission to test.<br>
  Unauthorized use against third-party services is illegal.
</p>

---

## About

**DDOS INFINITY X** is a customized stress-testing CLI built on proven flood and bypass techniques. It includes a branded terminal UI, proxy tooling, diagnostic utilities, and Docker support.

| Author | Version | Repository |
|--------|---------|------------|
| **adil fayyaz** | 1.0 INFINITY | https://github.com/Infinity-X202/DDOS-INFINITY-X |

---

## Features

### Layer 7 (HTTP/HTTPS)

GET, POST, OVH, RHEX, STOMP, STRESS, DYN, DOWNLOADER, SLOW, HEAD, NULL, COOKIE, PPS, EVEN, GSB, DGB, AVB, BOT, APACHE, XMLRPC, CFB, CFBUAM, BYPASS, BOMB, KILLER, TOR — and more.

### Layer 4 (Network / protocols)

TCP, UDP, SYN, OVH-UDP, CPS, CONNECTION, ICMP, VSE, TS3, FIVEM, FIVEM-TOKEN, MINECRAFT, MCPE, MCBOT — plus amplification methods (MEM, NTP, DNS, ARD, CLDAP, CHAR, RDP).

### Tools

```bash
python start.py tools
```

CFIP, DNS, TSSRV, PING, CHECK, DSTAT — plus HELP, STOP, CLEAR.

---

## Quick start

**Requirements:** Python 3.10+, Git (for PyRoxy dependency)

```bash
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
pip install -r requirements.txt
python start.py HELP
```

### Usage

```bash
# Help & banner
python start.py
python start.py HELP

# Layer 7
python start.py <METHOD> <url> <socks_type> <threads> <proxylist> <rpc> <duration>

# Layer 4
python start.py <METHOD> <ip:port> <threads> <duration>

# Tools console
python start.py tools
```

**Proxy types:** `0` = all from config · `1` = HTTP · `4` = SOCKS4 · `5` = SOCKS5 · `6` = random

---

## Docker

```bash
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
docker compose build
docker compose run -it --entrypoint /bin/bash infinityx
```

Image (after CI): `ghcr.io/Infinity-X202/DDOS-INFINITY-X:latest`

---

## Configuration

Edit `config.json` for Minecraft bot prefix, protocol version, and public proxy provider URLs.

Data files: `files/useragent.txt`, `files/referers.txt`, `files/proxies/`

---

## Dependencies

- [PyRoxy](https://github.com/MatrixTM/PyRoxy) — proxy handling (external library)
- cloudscraper, requests, impacket, dnspython, icmplib, psutil, yarl

See `requirements.txt` for pinned versions.

---

## Credits

This project is a fork/customization inspired by the open-source [MHDDoS](https://github.com/MatrixTM/MHDDoS) project (MIT).  
**DDOS INFINITY X** branding, banner, and documentation © **adil fayyaz**.

---

## License

MIT — see [LICENSE](LICENSE).

## Links

- **Repository:** https://github.com/Infinity-X202/DDOS-INFINITY-X  
- **Issues:** https://github.com/Infinity-X202/DDOS-INFINITY-X/issues  
- **Author:** adil fayyaz
