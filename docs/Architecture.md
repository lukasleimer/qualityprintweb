# Project Architecture – Quality Print Web

## 🏗️ System Architektur

```
qualityprintweb/
│
├── 📋 Configuration & Core
│   ├── app.py                    # Flask Application Factory
│   ├── config.py                 # Environment-based Configuration
│   ├── models.py                 # SQLAlchemy ORM Models
│   ├── requirements.txt          # Python Dependencies
│   └── .env                      # Secrets & API Keys
│
├── 📁 Backend (routes/)
│   ├── __init__.py
│   ├── home.py                   # Home & Legal Routes (Blueprint)
│   └── kontakt.py                # Contact Form Routes (Blueprint)
│
├── ⚙️ Services (services/)
│   ├── __init__.py
│   ├── mail.py                   # Email Service (SMTP)
│   └── [future: payment, storage, etc]
│
├── 🎨 Frontend (static/)
│   ├── css/
│   │   ├── variables.css         # Design Tokens & CSS Variables
│   │   ├── reset.css             # Browser Reset
│   │   ├── typography.css        # Font Definitions
│   │   ├── layout.css            # Grid & Spacing
│   │   ├── components/
│   │   │   ├── buttons.css
│   │   │   ├── forms.css
│   │   │   ├── cards.css
│   │   │   └── ...
│   │   ├── sections/
│   │   │   ├── navbar.css
│   │   │   ├── hero.css
│   │   │   ├── footer.css
│   │   │   └── ...
│   │   ├── utilities.css         # Helper Classes
│   │   └── responsive.css        # Media Queries
│   │
│   ├── js/
│   │   ├── main.js               # Main JS Bundle
│   │   ├── components/
│   │   │   ├── menu.js           # Mobile Menu Toggle
│   │   │   ├── form-handler.js   # Form Submissions
│   │   │   └── ...
│   │   └── utils/
│   │       └── helpers.js        # Utility Functions
│   │
│   ├── images/                   # Optimized Images (WebP, JPEG)
│   ├── icons/                    # SVG Icons
│   └── fonts/                    # Web Fonts (WOFF2)
│
├── 📄 Templates (templates/)
│   ├── base.html                 # Base Template (extends)
│   ├── home.html
│   ├── kontakt.html
│   ├── impressum.html
│   ├── datenschutz.html
│   ├── components/               # Reusable Components
│   │   ├── navbar.html
│   │   ├── footer.html
│   │   ├── hero.html
│   │   ├── services.html
│   │   ├── cta.html
│   │   ├── contact_form.html
│   │   └── ...
│   └── emails/                   # Email Templates
│       └── kontakt_email.html
│
├── 📚 Dokumentation (docs/)
│   ├── DesignSystem.md           # Design Tokens & System
│   ├── Architecture.md           # This File
│   ├── ProjectStatus.md          # Current Status
│   ├── Roadmap.md                # Feature Roadmap
│   ├── Changelog.md              # Version History
│   └── Sprint-00-*.md            # Sprint Reports
│
├── 🗄️ Database
│   └── instance/
│       └── messages.db           # SQLite (gitignored)
│
└── 📦 Deployment
    ├── Dockerfile                # Container Image
    ├── docker-compose.yml        # Services
    └── gunicorn.conf.py          # Production Server
```

---

## 🔄 Data Flow

### Request/Response Cycle

```
User Request
    ↓
Browser (HTML5, CSS3, JS)
    ↓
Flask Router (routes/)
    ↓
View Function / Blueprint
    ↓
Service Layer (services/)
    ↓
Database Layer (models.py, SQLAlchemy)
    ↓
Response (JSON / HTML)
    ↓
Browser Render
    ↓
User sees Page
```

### Contact Form Flow

```
1. User fills form (HTML5 Validation)
   ↓
2. JavaScript submits via AJAX/Fetch
   ↓
3. kontakt.py@send_message() receives POST
   ↓
4. Validate data
   ↓
5. Save to Database (Message Model)
   ↓
6. Send Email via services/mail.py
   ↓
7. Return JSON Response
   ↓
8. JavaScript shows success/error message
```

---

## 🏛️ Design Patterns

### 1. Application Factory Pattern

**Ziel**: Mehrere App-Instanzen mit verschiedenen Konfigurationen

```python
# app.py
def create_app(config_name='development'):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    db.init_app(app)
    register_blueprints(app)
    return app
```

**Vorteil**: 
- Testbar (separate Test-App)
- Produktionsreif (verschiedene Configs)
- Flexible Initialization

### 2. Blueprint Pattern

**Ziel**: Modulare Route-Verwaltung

```python
# routes/home.py
home_bp = Blueprint('home', __name__)

@home_bp.route('/')
def index(): ...

# app.py
app.register_blueprint(home_bp)
```

**Vorteil**:
- Separation of Concerns
- Einfach neue Routes hinzufügen
- Namespace-Management

### 3. Service Layer Pattern

**Ziel**: Business Logic von Routes trennen

```python
# services/mail.py
def send_contact_email(data): ...

# routes/kontakt.py
from services.mail import send_contact_email
result = send_contact_email(data)
```

**Vorteil**:
- DRY (Don't Repeat Yourself)
- Leicht testbar
- Wiederverwendbar

### 4. Template Inheritance

**Ziel**: Layout-Konsistenz, Redundanz vermeiden

```html
<!-- base.html -->
<html>
    <head>{% block head %}{% endblock %}</head>
    <body>
        {% include 'components/navbar.html' %}
        {% block content %}{% endblock %}
        {% include 'components/footer.html' %}
    </body>
</html>

<!-- home.html -->
{% extends "base.html" %}
{% block content %}...{% endblock %}
```

**Vorteil**:
- Konsistente Header/Footer
- Einfache Template-Updates
- DRY Prinzip

### 5. CSS Architecture (Consolidated – Sprint 2)

**Ziel**: Wartbare, skalierbare CSS mit zentralem Import-Management

**CSS Load Order** (in `style.css`):

```css
/* 1. RESETS (Normalize Browser Defaults) */
@import url('./reset.css');              /* HTML5 element resets, box-sizing */

/* 2. TYPOGRAPHY (Base Text Styles) */
@import url('./typography.css');         /* Font styles, display classes */

/* 3. LAYOUT (Grid & Container System) */
@import url('./layout.css');             /* Containers, grids, flex, spacing */

/* 4. UTILITIES (Helper Classes) */
@import url('./utilities.css');          /* Text, colors, borders, shadows */

/* 5. SECTION-SPECIFIC (Component Styles) */
@import url('./navbar.css');
@import url('./hero.css');
@import url('./about.css');
@import url('./services.css');
@import url('./quality.css');
@import url('./references.css');
@import url('./sustainability.css');
@import url('./contact-preview.css');
@import url('./contact.css');
@import url('./footer.css');
```

**Cascade Explanation**:

| Priority | Layer | Purpose | Specificity |
|----------|-------|---------|-------------|
| 1 | Reset | Browser defaults removed | Low |
| 2 | Typography | Font families, sizes, weights | Low |
| 3 | Layout | Containers, grids, flex | Medium |
| 4 | Utilities | Helper classes (.text-center, etc) | Medium-High |
| 5 | Components | Section/component styles | High |

**Benefits**:
- Single import point (`style.css`)
- Clear cascade hierarchy
- Easy to debug (trace through imports)
- Future-ready for CSS bundling
- Reduced HTTP requests (11 → 2)

---

## 🎨 CSS System (Sprint 2 Foundation)

### Container System

Three ways to constrain content width:

```html
<!-- Standard (1280px max) - for most content -->
<section class="section">
    <div class="container">Content</div>
</section>

<!-- Wide (1440px max) - for complex layouts -->
<section class="section">
    <div class="container container--wide">Content</div>
</section>

<!-- Narrow (960px max) - for text-heavy content -->
<section class="section">
    <div class="container container--narrow">Content</div>
</section>

<!-- Full Width - for hero/backgrounds -->
<section class="section container--full">Content</section>
```

### Grid System

```html
<!-- 3-column grid (responsive) -->
<div class="grid grid-cols-3 gap-8">
    <div>Column 1</div>
    <div>Column 2</div>
    <div>Column 3</div>
</div>

<!-- Auto-responsive grid (cards) -->
<div class="grid grid-cols-auto">
    <div class="card">Card 1</div>
    <div class="card">Card 2</div>
    <div class="card">Card 3</div>
</div>

<!-- Equal height cards -->
<div class="grid grid-cols-3 grid-cards">
    <article>
        <img src="..." alt="...">
        <h3>Title</h3>
        <p>Content</p>
        <button>Action</button>  <!-- Pushed to bottom -->
    </article>
</div>
```

### Spacing System

```html
<!-- Standard section spacing (64px mobile → 48px on small) -->
<section class="section">Content</section>

<!-- Variants -->
<section class="section--sm">Compact (48px)</section>
<section class="section--lg">Large (80px)</section>
<section class="section--xl">Extra Large (112px)</section>
```

### Responsive Breakpoints

| Breakpoint | Width | Usage |
|-----------|-------|-------|
| Mobile | 320px-639px | Base styles (no prefix) |
| Tablet | 640px-767px | `.sm:*` classes |
| Tablet/Desktop | 768px-1023px | `.md:*` classes |
| Desktop | 1024px-1279px | `.lg:*` classes |
| Large Desktop | 1280px-1535px | `.xl:*` classes |
| Extra Large | 1536px+ | `.2xl:*` classes |

Example responsive grid:

```html
<!-- Mobile: 1 column, Tablet: 2 columns, Desktop: 3 columns -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3">
    <!-- Responsive layout -->
</div>
```

---

## 🔗 Dependencies & Versions

### Backend
- **Flask 3.0.0** – Web Framework
- **Flask-SQLAlchemy 3.1.1** – ORM
- **python-dotenv 1.0.0** – Environment Variables
- **gunicorn 21.2.0** – Production Server
- **email-validator 2.1.0** – Email Validation

### Frontend
- **Vanilla HTML5** – No Framework
- **CSS3** – No Bootstrap/Tailwind
- **Vanilla JavaScript** – ES6+, No jQuery

### Database
- **SQLite** – Development/Simple Production
- **PostgreSQL** – Future (Production-Ready)

---

## 🚀 Deployment Architecture

### Development

```
Local Machine
    ↓
Flask Development Server (port 5000)
    ↓
SQLite Database
```

### Production

```
nginx (Reverse Proxy, Static Files)
    ↓
gunicorn (4 Workers)
    ↓
Flask Application
    ↓
PostgreSQL Database
```

### Docker

```
docker-compose up
    ↓
- nginx container
- app container (gunicorn)
- postgres container
```

---

## 📋 Configuration Management

### Environment-based Config

```python
# config.py
class Config:
    DEBUG = False
    TESTING = False
    
class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
    
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
```

### Environment Variables

```env
# .env (never commit!)
FLASK_ENV=development
SECRET_KEY=xyz...
MAIL_USERNAME=user@gmail.com
MAIL_PASSWORD=app-password
DATABASE_URL=postgresql://...
```

---

## 🔐 Security Considerations

### Implemented

- ✅ Secret Key Management (.env)
- ✅ CSRF Protection (Flask-WTF ready)
- ✅ SQL Injection Prevention (SQLAlchemy)
- ✅ XSS Prevention (Jinja2 auto-escape)
- ✅ Email Validation (email-validator)

### TODO

- [ ] Rate Limiting
- [ ] Content Security Policy (CSP)
- [ ] HTTPS/SSL
- [ ] CORS Protection
- [ ] Form Rate Limiting
- [ ] File Upload Security

---

## 📊 Scalability Strategy

### Phase 1: MVP (Current)
- Single server
- SQLite
- Static file serving

### Phase 2: Growth
- Nginx + Gunicorn
- PostgreSQL
- Redis Caching
- CDN for Static Files

### Phase 3: Enterprise
- Load Balancer
- Multiple App Servers
- Database Replication
- Message Queue (Celery)
- Docker Kubernetes

---

## 🧪 Testing Architecture

### Unit Tests
```
tests/
├── test_routes.py         # Route Tests
├── test_services.py       # Service Tests
├── test_models.py         # Model Tests
└── test_forms.py          # Form Validation
```

### Integration Tests
```python
# tests/integration/test_contact_flow.py
def test_contact_form_submission():
    # 1. Submit form
    # 2. Check database
    # 3. Verify email sent
    # 4. Check response
```

### E2E Tests (Future)
```
Selenium/Playwright Tests
- Full User Workflows
- Browser Testing
- Visual Regression
```

---

## 📈 Performance Strategy

### Frontend Optimization
- ✅ CSS Variablen (kein SASS nötig)
- ✅ Minimal JavaScript
- ✅ Image Optimization
- ✅ Critical CSS
- ⏳ Lazy Loading
- ⏳ Caching Strategy

### Backend Optimization
- ✅ Database Indexing
- ⏳ Query Optimization
- ⏳ Caching Layer (Redis)
- ⏳ Async Tasks (Celery)

### Monitoring
- ⏳ Error Tracking (Sentry)
- ⏳ Performance Monitoring (New Relic)
- ⏳ Uptime Monitoring

---

## 🔄 Development Workflow

### Version Control

```bash
# Main branches
main            # Production
develop         # Development

# Feature branches
feature/feature-name
bugfix/bug-name
docs/documentation-name
```

### Commit Convention

```
<type>(<scope>): <subject>

feat(design): add new button component
fix(navbar): mobile menu toggle bug
docs(setup): add installation guide
refactor(css): optimize grid system
style(navbar): formatting changes
test(contact): add form validation tests
chore(deps): update Flask to 3.0
```

### Release Process

```
1. Feature Branch → Pull Request
2. Code Review
3. Merge to develop
4. Version Bump (0.1.0)
5. Merge develop → main
6. Tag Release
7. Deploy to Production
```

---

## 📚 Documentation Structure

| File | Purpose |
|------|---------|
| **DesignSystem.md** | Design Tokens, Color, Typography |
| **Architecture.md** | System Structure, Patterns |
| **ProjectStatus.md** | Current Status, Completed Features |
| **Roadmap.md** | Planned Features, Timelines |
| **Changelog.md** | Version History, Changes |
| **Sprint-*.md** | Sprint-specific Reports |

---

## 🎯 Key Principles

1. **Simplicity** – Einfach, wartbar, nicht overengineered
2. **Performance** – Schnell laden, responsive
3. **Accessibility** – WCAG 2.1 AA Standard
4. **Security** – Best Practices implementiert
5. **Scalability** – Ausbaufähig, flexibel
6. **Modularity** – Loose Coupling, High Cohesion
7. **Documentation** – Alles dokumentiert
8. **Testing** – Unit-, Integration-, E2E Tests

---

## 🔗 Related Documents

- [Design System](./DesignSystem.md)
- [Project Status](./ProjectStatus.md)
- [Roadmap](./Roadmap.md)
- [Changelog](./Changelog.md)
