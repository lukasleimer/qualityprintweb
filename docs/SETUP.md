# Setup & Installation Guide

**Version**: 1.0.0  
**Last Updated**: 2026-06-28

---

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for version control)

### Step 1: Clone or Download Project

```bash
# If using Git
git clone <repository-url>
cd qualityprintweb

# Or extract the ZIP file
unzip qualityprintweb.zip
cd qualityprintweb
```

### Step 2: Create Virtual Environment

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

You should see `(venv)` in your terminal prompt.

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Configure Environment Variables

```bash
# Copy the example file
cp .env.example .env  # Linux/Mac
# or
copy .env.example .env  # Windows

# Edit .env with your settings
# Important: Configure SMTP settings for email to work
```

**Edit `.env` file**:
```env
FLASK_ENV=development
SECRET_KEY=your-super-secret-key
MAIL_SERVER=smtp.gmail.com
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
CONTACT_MAIL=info@yourdomain.com
```

### Step 5: Run the Application

```bash
python app.py
```

The application will start at `http://localhost:5000`

---

## 📋 Detailed Setup

### Setting Up Gmail SMTP

Gmail requires an "App Password" for security:

1. Go to [myaccount.google.com/security](https://myaccount.google.com/security)
2. Enable 2-Factor Authentication (if not already enabled)
3. Go to "App Passwords" section
4. Select "Mail" and "Windows Computer" (or your device)
5. Copy the generated 16-character password
6. Paste it into `.env` as `MAIL_PASSWORD`

### Alternative Email Services

**Outlook/Office 365**:
```env
MAIL_SERVER=smtp.office365.com
MAIL_PORT=587
MAIL_USERNAME=your-email@outlook.com
MAIL_PASSWORD=your-password
```

**SendGrid**:
```env
MAIL_SERVER=smtp.sendgrid.net
MAIL_PORT=587
MAIL_USERNAME=apikey
MAIL_PASSWORD=SG.xxxxxxxxxxxx
```

---

## 🗂️ Project Structure Overview

```
qualityprintweb/
├── app.py                  # Flask application
├── config.py              # Configuration
├── models.py              # Database models
├── requirements.txt       # Dependencies
├── .env                   # Environment variables (gitignored)
├── .env.example           # Template for .env
│
├── templates/             # Jinja2 templates
│   ├── base.html
│   ├── home.html
│   ├── kontakt.html
│   ├── components/
│   └── emails/
│
├── static/                # Static files
│   ├── css/              # Stylesheets
│   ├── js/               # JavaScript
│   ├── images/
│   ├── icons/
│   └── fonts/
│
├── routes/                # Flask blueprints
│   ├── home.py
│   └── kontakt.py
│
├── services/              # Business logic
│   └── mail.py
│
├── instance/              # Runtime data
│   └── messages.db       # SQLite database
│
└── docs/                  # Documentation
    ├── DesignSystem.md
    ├── Architecture.md
    ├── Roadmap.md
    └── ...
```

---

## 🔧 Development Workflow

### Start Development Server

```bash
# Make sure venv is activated
python app.py

# Or use Flask development server directly
flask run
```

### Making Changes

1. **Edit HTML templates** in `templates/`
2. **Edit CSS** in `static/css/`
3. **Edit JavaScript** in `static/js/`
4. **Add routes** in `routes/`

Changes are automatically reflected when Flask debug mode is on.

### Database

The SQLite database is created automatically on first run at `instance/messages.db`

To reset the database:
```bash
# Delete the database file
rm instance/messages.db  # Linux/Mac
del instance\messages.db  # Windows

# Run Flask to recreate it
python app.py
```

---

## 🧪 Testing the Application

### Test the Home Page

Navigate to: `http://localhost:5000/`

### Test the Contact Form

1. Go to: `http://localhost:5000/kontakt`
2. Fill out the form
3. Submit
4. Check if email is received (make sure email settings are correct)

### Test Email Sending

If emails aren't being sent, check:
1. `.env` SMTP configuration is correct
2. Gmail: Using "App Password" not regular password
3. Firewall: Port 587 is open
4. Check Flask logs for error messages

---

## 📦 Upgrading Dependencies

To update packages to latest versions:

```bash
pip install --upgrade -r requirements.txt
```

To see what packages are outdated:

```bash
pip list --outdated
```

---

## 🐛 Troubleshooting

### Error: "ModuleNotFoundError: No module named 'flask'"

**Solution**: Make sure virtual environment is activated:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### Error: "Address already in use"

Flask is already running on port 5000. Either:
- Stop the other process
- Run on different port: `flask run --port 5001`

### Error: "Email not sending"

Check:
1. `.env` file has correct SMTP settings
2. Gmail: Using "App Password" (16-character), not normal password
3. Port 587 is not blocked by firewall
4. Check Flask debug logs for error details

### Error: "Database locked"

Multiple Flask processes are running. Kill them:
```bash
# Windows - find and kill process on port 5000
netstat -ano | findstr :5000

# Linux/Mac
lsof -i :5000
kill -9 <PID>
```

---

## 📊 Environment Configurations

### Development

```bash
FLASK_ENV=development
FLASK_DEBUG=True
DATABASE_URL=sqlite:///instance/messages.db
```

### Production

```bash
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=<super-secret-key>
DATABASE_URL=postgresql://user:pass@host/db
```

### Testing

```bash
FLASK_ENV=testing
DATABASE_URL=sqlite:///:memory:
```

---

## 🚀 Deployment

### Using Gunicorn (Production)

```bash
# Install gunicorn
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### Using Docker

```bash
# Build image
docker build -t qualityprint .

# Run container
docker run -p 5000:5000 -e FLASK_ENV=production qualityprint
```

### Environment Variables in Production

Set environment variables via:
- `.env` file (not recommended for production secrets)
- Environment variables (recommended)
- Docker secrets
- Production secrets manager (AWS Secrets Manager, etc)

---

## 📚 Additional Resources

- [Flask Documentation](https://flask.palletsprojects.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Design System Guide](./DesignSystem.md)
- [Architecture Overview](./Architecture.md)
- [CSS Architecture](./CSS-Architecture.md)

---

## ✅ Checklist

Before deploying:

- [ ] `.env` file created and configured
- [ ] Virtual environment activated
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] Flask app runs without errors
- [ ] Contact form works
- [ ] Emails are being sent
- [ ] All static files load (CSS, JS, Images)
- [ ] Mobile responsiveness tested
- [ ] Security settings checked
- [ ] Documentation reviewed

---

## 🆘 Getting Help

If you encounter issues:

1. **Check the logs** - Flask shows detailed error messages
2. **Review documentation** - Read the relevant `.md` file in `/docs`
3. **Check `.env`** - Make sure all settings are configured
4. **Browser console** - Check for JavaScript errors (F12)
5. **Email logs** - Check if SMTP settings are correct

---

## 📞 Support

For questions or issues:
- Email: info@qualityprint.de
- GitHub Issues: [link to issues]
- Documentation: `/docs` folder

---

**Last Updated**: 2026-06-28  
**Version**: 1.0.0  
**Maintainer**: Lukas
