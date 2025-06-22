# 📊 Checksite Log Analyzer

Sistema di analisi centralizzato per i log del progetto `checksite`, con stack leggero basato su:

- MariaDB
- Python
- Grafana

---

## 🚀 Avvio rapido

Assicurati di avere Docker e Docker Compose installati, poi esegui:

```bash
docker compose up -d
```

---

## 📂 Struttura

```
checksite-log-analyzer/
├── config/                 # Configurazione DB
│   └── db_config.py
├── dashboard/              # Dashboard Grafana JSON
│   └── grafana_dashboard.json
├── logs/                   # Inserisci qui i log da elaborare
├── main.py                 # Script principale per analizzare i log
├── load_all_logs.py        # Script per caricare tutti i log da una cartella
├── requirements.txt        # Dipendenze Python
├── .env                    # Credenziali sicure
└── docker-compose.yml      # Stack con MariaDB e Grafana
```

---

## 🔐 Configurazione sicura

Nel file `.env` puoi specificare le credenziali di accesso al database e a Grafana:

```dotenv
DB_HOST=mariadb
DB_NAME=checksite_logs
DB_USER=checksite
DB_PASSWORD=checksitepass

GRAFANA_USER=admin
GRAFANA_PASSWORD=admin
```

---

## 📥 Caricamento log

Puoi caricare un singolo file di log così:

```bash
python main.py logs/impr01c01-2025-06-13.log
```

Oppure tutti i log nella cartella `logs/`:

```bash
python load_all_logs.py logs/
```

⚠️ I file devono essere nominati con il pattern `hostname-data.log`, es:
```
impr01c01-2025-06-13.log
```

---

## 📊 Dashboard Grafana

- Accesso: [http://localhost:3000](http://localhost:3000)
- Login: usa le credenziali in `.env`
- Importa `dashboard/grafana_dashboard.json`
- Puoi filtrare per `hostname` in alto

---

## 🧩 Modulare

Puoi estendere facilmente:

- Nuovi tipi di errori → modifica `parse_error_line()` in `main.py`
- Altri status code → modifica `parse_status_line()`
- Nuove fonti log → modifica `load_all_logs.py`

---

## ✅ Esempi supportati

Esempi di log validi:

```log
[2025-06-13T17:35:12.000000] ✅ https://example.com - Status: 200
[2025-06-13T17:35:13.000000] ❌ https://example.com/errore - Errore: Page.goto: Timeout 60000ms exceeded.
```

---

## 📦 Installazione dipendenze Python (solo se non usi Docker)

```bash
pip install -r requirements.txt
```

---

## ✨ Contribuzioni

Per aggiungere nuovi tipi di errore o metriche, lavora su `main.py` e aggiorna le query Grafana nel file `grafana_dashboard.json`.

---
