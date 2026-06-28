# Quality Print Web Project

Professionelle Website für Quality Print GmbH mit vollständiger Backend-Integration und Production-Ready Setup.

## 🚀 Features

- **Responsive Design System** - 100% CSS-Variablen, mobile-first
- **Contact Form** - Flask-WTF mit vollständiger Validierung und CSRF-Schutz
- **Email Integration** - SMTP-basierter Versand mit Error Handling
- **Security** - Security Headers, CSRF-Schutz, Input Validation
- **SEO Optimiert** - Robots.txt, Sitemap.xml, Open Graph, Twitter Cards
- **Logging** - Umfassendes Error- und Activity-Logging
- **Production-Ready** - Konfiguriert für Deployment mit Gunicorn

## 📁 Projektstruktur

```
qualityprintweb/
├── app.py              # Flask Application Factory
├── wsgi.py             # WSGI Entry Point für Production
├── config.py           # Konfiguration (Development/Production)
├── forms.py            # WTForms Definitionen
├── models.py           # SQLAlchemy Models
├── requirements.txt    # Python Dependencies
├── .env.example        # Umgebungsvariablen Template
├── routes/
│   ├── home.py        # Home/Impressum/Datenschutz Routes
│   └── kontakt.py     # Contact Form Routes
├── services/
│   └── mail.py        # SMTP Mail Service
├── utils/
│   ├── logging_config.py  # Logging Setup
│   └── security.py        # Security Utilities
├── templates/
│   ├── base.html       # Base Template mit SEO
│   ├── home.html       # Home Page
│   ├── kontakt.html    # Contact Page
│   ├── impressum.html  # Legal Page
│   ├── datenschutz.html # Privacy Page
│   ├── errors/         # Error Templates (404, 500)
│   └── components/     # Reusable Components
├── static/
│   ├── css/           # Stylesheets
│   ├── js/            # JavaScript
│   ├── robots.txt     # SEO
│   └── sitemap.xml    # SEO
├── logs/              # Application Logs
└── instance/          # SQLite Database (development)
```

## 🔧 Installation

### 1. Python Virtual Environment erstellen

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 2. Dependencies installieren

```bash
pip install -r requirements.txt
```

### 3. Umgebungsvariablen konfigurieren

```bash
# Copy template
cp .env.example .env

# Bearbeiten Sie .env mit Ihren Einstellungen:
# - SECRET_KEY (generieren Sie einen sicheren Key)
# - MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
# - FLASK_ENV und FLASK_DEBUG
# - DATABASE_URL (für Production)
```

### 4. Flask starten

```bash
# Development
flask run

# Mit Watch-Mode
flask run --reload
```

Die Website ist dann erreichbar unter `http://localhost:5000`

## 📧 Email-Konfiguration

### Gmail Setup

1. 2-Faktor-Authentifizierung aktivieren
2. App-spezifisches Passwort generieren: https://myaccount.google.com/apppasswords
3. In `.env` eintragen:
   ```
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-app-password
   ```

### Andere SMTP Provider

Anpassen Sie in `.env`:
```
MAIL_SERVER=your-smtp-server.com
MAIL_PORT=587
MAIL_USERNAME=your-username
MAIL_PASSWORD=your-password
```

## 🔒 Sicherheit

Die Anwendung implementiert mehrere Sicherheitsmaßnahmen:

- ✅ **CSRF Protection** - Flask-WTF Token auf allen Forms
- ✅ **Security Headers** - CSP, X-Frame-Options, X-Content-Type-Options, etc.
- ✅ **Input Validation** - WTForms Validators + Custom Checks
- ✅ **SQL Injection Protection** - SQLAlchemy ORM
- ✅ **XSS Protection** - Template Auto-Escaping
- ✅ **Secure Session Cookies** - HTTPOnly, Secure, SameSite Flags
- ✅ **Password Security** - Environment Variables (keine Hardcodes)

## 🌐 Deployment

### Development

```bash
flask run
```

### Production mit Gunicorn

```bash
# Mit 4 Worker Processes
gunicorn -w 4 -b 0.0.0.0:5000 wsgi:app

# Mit bestimmtem Port
gunicorn -w 4 -b 127.0.0.1:8000 wsgi:app

# Mit Socket (für Nginx)
gunicorn -w 4 --bind unix:/tmp/qualityprint.sock wsgi:app
```

### Nginx Configuration (Proxy)

```nginx
server {
    listen 80;
    server_name qualityprint.at www.qualityprint.at;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static {
        alias /path/to/qualityprintweb/static;
    }
}
```

### Systemd Service (Linux)

Datei: `/etc/systemd/system/qualityprint.service`

```ini
[Unit]
Description=Quality Print Web Application
After=network.target

[Service]
Type=notify
User=www-data
WorkingDirectory=/path/to/qualityprintweb
ExecStart=/path/to/qualityprintweb/venv/bin/gunicorn \
    -w 4 \
    -b 127.0.0.1:8000 \
    wsgi:app
Restart=always
RestartSec=10

Environment="FLASK_ENV=production"
EnvironmentFile=/path/to/qualityprintweb/.env

[Install]
WantedBy=multi-user.target
```

Starten:
```bash
sudo systemctl start qualityprint
sudo systemctl enable qualityprint
```

## 📊 Logging

Logs werden in `/logs` Verzeichnis gespeichert:

- `app.log` - Alle Log-Einträge (rotierend, max 10 MB)
- `errors.log` - Nur Fehler und kritische Meldungen

Logs enthalten Informationen über:
- Formularvalidierungsfehler
- Email-Versanderrors
- Unerwartete Fehler
- Request-Details

## 🧪 Testing

```bash
# pytest ausführen (wenn installiert)
pytest

# Mit Coverage
pytest --cov=.
```

## 📄 Seiten & Routes

| Route | Beschreibung | Methode |
|-------|-------------|---------|
| `/` | Startseite | GET |
| `/kontakt` | Kontaktformular | GET |
| `/kontakt/send` | Form Submission | POST |
| `/impressum` | Rechtliche Informationen | GET |
| `/datenschutz` | Datenschutzerklärung | GET |
| `/robots.txt` | SEO Crawler Regeln | GET |
| `/sitemap.xml` | XML Sitemap | GET |
| `/404` | Seite nicht gefunden | - |
| `/500` | Serverfehler | - |

## 🔍 SEO

Die Website ist SEO-optimiert:

- ✅ Dynamische Title und Meta-Descriptions
- ✅ Canonical URLs
- ✅ Open Graph Tags (für Social Media)
- ✅ Twitter Card Tags
- ✅ Sitemap.xml
- ✅ Robots.txt
- ✅ Semantic HTML5
- ✅ Mobile-optimiert

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'flask_wtf'"

```bash
pip install -r requirements.txt
```

### "SSL: CERTIFICATE_VERIFY_FAILED" beim Email-Versand

In Config hinzufügen:
```python
MAIL_USE_TLS = True  # statt SSL
```

### Database ist locked

Bei SQLite: Beenden Sie alle Flask-Instanzen und löschen Sie `instance/messages.db`

### 500 Fehler beim Form Submit

Überprüfen Sie `/logs/errors.log` für Details

## 📚 Dokumentation

Weitere Dokumentation:
- [Sprint-13-Production-Release.md](docs/Sprint-13-Production-Release.md)
- [ProjectStatus.md](docs/ProjectStatus.md)
- [Changelog.md](docs/Changelog.md)

## 📝 License & Contributing

Dieses Projekt ist proprietär für Quality Print GmbH.

## 👤 Support

Bei Fragen oder Problemen:
- 📧 Email: office@qualityprint.at
- 📞 Telefon: +43 512 123456

