# Quality Print Web Application

Eine professionelle Flask-basierte Website für Quality Print Druckdienstleistungen.

## Features

- ✅ Responsive Design
- ✅ Kontaktformular mit E-Mail-Versand
- ✅ Datenbankintegration (SQLite)
- ✅ Modular strukturiert (Blueprints, Services)
- ✅ Professionelle CSS-Struktur mit Variablen
- ✅ Mobile-optimiert

## Projektstruktur

```
qualityprintweb/
├── app.py                      # Flask Application Factory
├── config.py                   # Konfiguration (Dev, Prod, Test)
├── models.py                   # SQLAlchemy Models
├── requirements.txt            # Python Dependencies
├── .env                        # Umgebungsvariablen (NICHT in Git!)
├── .gitignore                  # Git Ignore Regeln
├── README.md                   # Diese Datei
│
├── templates/
│   ├── base.html              # Basis-Template
│   ├── home.html              # Startseite
│   ├── kontakt.html           # Kontaktseite
│   ├── impressum.html         # Impressum
│   ├── datenschutz.html       # Datenschutz
│   ├── components/
│   │   ├── navbar.html        # Navigation
│   │   ├── footer.html        # Footer
│   │   ├── hero.html          # Hero Section
│   │   ├── services.html      # Services/Leistungen
│   │   ├── cta.html           # Call-to-Action
│   │   └── contact_form.html  # Kontaktformular
│   └── emails/
│       └── kontakt_email.html # Email Template
│
├── static/
│   ├── css/
│   │   ├── variables.css      # CSS Variablen
│   │   ├── style.css          # Globale Styles
│   │   ├── navbar.css         # Navigation Styles
│   │   ├── hero.css           # Hero Styles
│   │   ├── services.css       # Services Styles
│   │   ├── contact.css        # Contact & CTA Styles
│   │   └── footer.css         # Footer Styles
│   ├── js/
│   │   └── menu.js            # Mobile Menu Toggle
│   ├── images/                # Bilder
│   ├── icons/                 # Icons
│   └── fonts/                 # Fonts
│
├── routes/
│   ├── __init__.py
│   ├── home.py                # Home & Legal Routes
│   └── kontakt.py             # Contact Routes
│
├── services/
│   ├── __init__.py
│   └── mail.py                # Email Service
│
└── instance/                   # Runtime Daten
    └── messages.db            # SQLite Database
```

## Installation

### 1. Virtuelle Umgebung erstellen und aktivieren

```bash
# Virtual Environment erstellen
python -m venv venv

# Aktivieren (Windows)
venv\Scripts\activate

# Oder auf Linux/Mac
source venv/bin/activate
```

### 2. Dependencies installieren

```bash
pip install -r requirements.txt
```

### 3. Umgebungsvariablen konfigurieren

Erstelle eine `.env` Datei im Projektroot und konfiguriere:

```env
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=your-secret-key-change-this

# Gmail SMTP Einstellungen
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=deine-email@gmail.com
MAIL_PASSWORD=dein-app-password

# Kontakt Email
CONTACT_MAIL=info@qualityprint.de
```

**Hinweis**: Für Gmail benötigst du ein [App Password](https://support.google.com/accounts/answer/185833)

### 4. Flask App starten

```bash
python app.py
```

Die App läuft dann unter: http://localhost:5000

## Verwendete Technologien

- **Backend**: Flask 3.0
- **ORM**: SQLAlchemy
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Database**: SQLite
- **Server**: Gunicorn (Production)

## Konfiguration nach Environment

### Development
```bash
FLASK_ENV=development python app.py
```

### Production
```bash
FLASK_ENV=production gunicorn -w 4 app:app
```

### Testing
```bash
FLASK_ENV=testing pytest
```

## Routen

| Route | Methode | Beschreibung |
|-------|---------|-------------|
| `/` | GET | Startseite |
| `/kontakt` | GET | Kontaktseite |
| `/kontakt/send` | POST | Kontaktformular absenden |
| `/impressum` | GET | Impressum |
| `/datenschutz` | GET | Datenschutzerklärung |

## API Endpoints

### Kontaktformular absenden
```
POST /kontakt/send
Content-Type: application/json

{
  "name": "Max Mustermann",
  "email": "max@example.com",
  "subject": "Anfrage",
  "message": "Nachrichtentext"
}

Response:
{
  "success": true,
  "message": "Nachricht erfolgreich versendet"
}
```

## Entwicklung

### Neue Route hinzufügen

1. Erstelle eine neue Datei in `routes/`:
```python
# routes/beispiel.py
from flask import Blueprint

beispiel_bp = Blueprint('beispiel', __name__, url_prefix='/beispiel')

@beispiel_bp.route('/')
def index():
    return render_template('beispiel.html')
```

2. Registriere die Route in `app.py`:
```python
from routes.beispiel import beispiel_bp
app.register_blueprint(beispiel_bp)
```

### Neues Template erstellen

Templates erben von `base.html`:
```html
{% extends "base.html" %}

{% block title %}Seitentitel{% endblock %}

{% block content %}
    <!-- Seiteninhalte -->
{% endblock %}
```

### CSS hinzufügen

Neue CSS-Datei in `static/css/` erstellen und in `base.html` verlinken:
```html
<link rel="stylesheet" href="{{ url_for('static', filename='css/deinfile.css') }}">
```

## Häufige Fehler

### Email wird nicht versendet
- Überprüfe `.env` Konfiguration
- Verwende Gmail App Password (nicht Passwort!)
- Überprüfe Firewall/Proxy Einstellungen

### Database-Fehler
- `instance/` Ordner muss existieren
- Lösche `instance/messages.db` bei Schema-Änderungen
- Starte Flask neu

### Static Files nicht geladen
- Überprüfe `url_for()` Pfade
- Browser-Cache löschen (Ctrl+F5)
- Flask Debug Mode aktivieren

## Lizenz

Alle Rechte vorbehalten © 2024 Quality Print

## Support

Für Fragen oder Issues: info@qualityprint.de
