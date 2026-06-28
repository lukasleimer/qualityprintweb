# Quality Print Web Project

Dies ist die Dokumentation für das Quality Print Projekt.

## Projektstruktur

- **app.py**: Flask-Einstiegspunkt
- **config.py**: Konfigurationsdatei
- **templates/**: HTML-Templates
- **static/**: CSS, JS, Bilder, Fonts
- **routes/**: Flask Blueprints für Routen
- **services/**: Geschäftslogik (Mail, etc.)
- **instance/**: Lokale Datenbankdatei

## Installation

1. Python Virtual Environment erstellen:
   ```bash
   python -m venv venv
   ```

2. Virtual Environment aktivieren:
   - Windows: `venv\Scripts\activate`
   - Unix: `source venv/bin/activate`

3. Dependencies installieren:
   ```bash
   pip install -r requirements.txt
   ```

4. .env Datei konfigurieren (SMTP-Einstellungen)

5. Flask-App starten:
   ```bash
   flask run
   ```

## Konfiguration

Die Anwendung nutzt die `.env` Datei für sensible Konfigurationen (SMTP, API Keys, etc.).

**Wichtig**: `.env` nicht in Git committen!

## Seiten

- `/` - Startseite
- `/kontakt` - Kontaktformular
- `/impressum` - Impressum
- `/datenschutz` - Datenschutz
