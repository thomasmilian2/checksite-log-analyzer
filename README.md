# checksite-log-analyzer
# 📊 Checksite Log Analyzer

Sistema modulare e leggero per analizzare e visualizzare i log del progetto `checksite` da più nodi (`impr01c01`, `impr02c01`, `impr03c01`) usando:

- **MariaDB** per lo storage dei log
- **Python** per il parsing e l'inserimento
- **Grafana** per la visualizzazione

---

## 🚀 Avvio rapido

1. **Clona o scarica il progetto**

2. **Avvia i container**
```bash
docker compose up -d
```

3. **Importa lo schema SQL**
```bash
docker exec -i mariadb-checksite mysql -uchecksite -pchecksitepass checksite_logs < sql/schema.sql
```

4. **Installa le dipendenze Python**
```bash
pip install -r requirements.txt
```

5. **Esegui l'import di un file log**
```bash
# Esempio con hostname nel nome file
python main.py /root/Automation/checksite/logs/impr01c01-2025-06-13.log
```

---

## 🗃️ Struttura

```
checksite-log-analyzer/
├── config/                  # Configurazione DB
├── parser/                  # Parser dei log
├── sql/                     # Schema MariaDB
├── dashboard/               # Dashboard JSON per Grafana
├── utils/                   # Utility comuni
├── main.py                  # Script principale
├── requirements.txt         # Dipendenze Python
└── docker-compose.yml       # Stack Grafana + MariaDB
```

---

## 🧠 Come funziona

- `main.py` identifica automaticamente il nodo (`hostname`) in base al nome file
- Se il file termina in `.json.log`, viene considerato un log di status HTTP
- Altrimenti, viene analizzato come log di errori testuali (es. `timeout`, `proxy_failed`...)

---

## 🧪 Esempio output in Grafana

- Andamento degli `HTTP 200` nel tempo
- Conteggio degli errori totali per giorno/ora
- URL più frequentemente in errore
- Classificazione per tipo di errore

Login:
- **URL**: http://localhost:3000
- **User**: `admin` / `admin`

Importa la dashboard da: `dashboard/grafana_dashboard.json`

---

## ⚙️ Variabili modificabili

- `config/db_config.py`: accesso DB
- `parser/error_parser.py`: nuove firme di errore in `classify_error()`
- `parser/status_parser.py`: parsing log JSON

---

## 🔄 Naming file log

Per identificare correttamente il nodo, il nome file deve essere nel formato:

```
impr01c01-2025-06-13.log
impr02c01-2025-06-13.json.log
```

---

## 🛠️ To-do futuri

- Supporto a parametri CLI tipo `--host`
- Analisi automatica directory log
- Scheduler o crontab
- API REST per invio log da remoto

---

## 👨‍💻 Autore

Massimiliano Bendotti – progetto `checksite` su 3 nodi Debian 12
