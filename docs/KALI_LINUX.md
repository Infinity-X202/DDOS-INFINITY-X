# DDOS INFINITY X — Guida Kali Linux

**Repository:** https://github.com/Infinity-X202/DDOS-INFINITY-X  
**Author:** adil fayyaz  
**For educational purposes only** — use only on systems you own or have written permission to test.

---

## Installazione (metodo consigliato)

```bash
git clone https://github.com/Infinity-X202/DDOS-INFINITY-X.git
cd DDOS-INFINITY-X
chmod +x install.sh run.sh check.sh
./install.sh
./check.sh
./run.sh
```

> **Non usare** `pip install -r requirements.txt` direttamente su Kali.  
> Otterrai: `error: externally-managed-environment`  
> Usa sempre `./install.sh` (crea un ambiente virtuale `venv`).

---

## Aggiornare da GitHub

```bash
cd ~/DDOS-INFINITY-X
git pull
chmod +x install.sh run.sh check.sh
sed -i 's/\r$//' install.sh run.sh check.sh
./install.sh
./run.sh
```

---

## Avvio

| Azione | Comando |
|--------|---------|
| Menu interattivo | `./run.sh` |
| Aiuto completo | `./run.sh HELP` |
| Strumenti (PING, DSTAT…) | `./run.sh tools` |
| Ferma attacchi Python | `./run.sh STOP` |

Dopo l’installazione usa **sempre** `./run.sh` (attiva il venv automaticamente).

---

## Esempi comandi (copia così)

Sostituisci solo il bersaglio con un host **tuo** o **autorizzato**.

### Layer 7 (HTTP/HTTPS)

```bash
./run.sh GET http://TUO-SITO 0 100 http.txt 10 60
```

| Parametro | Significato |
|-----------|-------------|
| `GET` | Metodo (GET, POST, CFB, BYPASS, …) |
| `http://TUO-SITO` | URL target |
| `0` | Proxy: 0=config, 1=HTTP, 4=SOCKS4, 5=SOCKS5, 6=random |
| `100` | Thread |
| `http.txt` | File in `files/proxies/` (può essere vuoto) |
| `10` | RPC |
| `60` | Durata (secondi) |

### Layer 4 (TCP / UDP)

```bash
./run.sh TCP 192.168.1.10:80 50 30
```

| Parametro | Significato |
|-----------|-------------|
| `TCP` | Metodo (TCP, UDP, SYN, MINECRAFT, …) |
| `192.168.1.10:80` | IP:porta |
| `50` | Thread |
| `30` | Durata (secondi) |

### Layer 4 con proxy

```bash
./run.sh TCP 192.168.1.10:80 50 30 5 http.txt
```

---

## Menu interattivo

Senza argomenti si apre il menu:

```
[1] Launch Layer 7 attack
[2] Launch Layer 4 attack
[3] Open Tools console
[4] List all methods
[5] Command syntax / HELP
[6] Exit
```

---

## Errori comuni su Kali

| Errore | Soluzione |
|--------|-----------|
| `externally-managed-environment` | `./install.sh` — non `pip` globale |
| `No module named 'PyRoxy'` | `./install.sh` poi `./run.sh` |
| `bad interpreter` / `$'\r'` | `sed -i 's/\r$//' *.sh` e `chmod +x *.sh` |
| `syntax error near '<'` | Non usare `<METHOD>` — usa `GET`, `TCP` |
| `Cannot Create Raw Socket` | Per SYN/ICMP: `sudo ./run.sh ...` |
| `docker: command not found` | Usa `install.sh` + `run.sh`, non Docker |
| impacket install fallisce | `sudo apt install -y python3-dev build-essential libffi-dev libssl-dev git` poi `./install.sh` |
| Cartella duplicata `DDOS-INFINITY-X/DDOS-INFINITY-X` | `cd` nella cartella che contiene `install.sh` |

---

## Reinstallazione pulita

```bash
cd ~/DDOS-INFINITY-X
rm -rf venv
./install.sh
./check.sh
```

`check.sh` mostra quali moduli Python mancano.

---

## Pacchetti di sistema (se install.sh fallisce)

```bash
sudo apt update
sudo apt install -y python3 python3-venv python3-pip python3-dev \
  git build-essential libffi-dev libssl-dev pkg-config
./install.sh
```

**Mai** eseguire: `sudo pip install ...`

---

## Requisiti

- Python 3.10+
- Git (per PyRoxy da GitHub)
- Connessione Internet per `pip` e proxy list

---

## Link

- Repo: https://github.com/Infinity-X202/DDOS-INFINITY-X  
- Issues: https://github.com/Infinity-X202/DDOS-INFINITY-X/issues  
