# Sprint 0.1 – Architecture Review & Foundation Refactoring

**Datum**: 2026-06-28  
**Sprint**: 0.1 (Post-Sprint 0 Review)  
**Dauer**: Foundation Refactoring  
**Status**: 🔄 In Progress

---

## 🎯 Sprint Goal

Überprüfe die gesamte Projektbasis (Sprint 0) hinsichtlich Architektur, Wartbarkeit und Konsistenz. Führe notwendige Verbesserungen durch, ohne bestehende, funktionierende Lösungen zu ersetzen.

---

## 📊 Analyse des bisherigen Sprint 0

### ✅ Stärken

#### Architektur
- ✅ **Flask Application Factory Pattern** – Saubere Implementierung
- ✅ **Blueprint System** – Modulare Route-Organisation
- ✅ **Service Layer** – Email-Service separiert
- ✅ **Environment Configuration** – Dev/Prod/Test Configs vorhanden

#### Frontend Structure
- ✅ **Base Template Inheritance** – base.html korrekt implementiert
- ✅ **Component-based Templates** – navbar, footer, hero, etc. modulare Komponenten
- ✅ **CSS Load Order** – Korrekt definiert (variables → style → typography → layout → sections)
- ✅ **Design System** – Comprehensive variables.css mit modernen Naming-Konventionen

#### Dokumentation
- ✅ **DesignSystem.md** – Detaillierte Design-Token Dokumentation
- ✅ **Architecture.md** – System-Architektur dokumentiert
- ✅ **ProjectStatus.md** – Projekt-Status aktuell
- ✅ **Referenzanalyse** – Umfassende Analyse durchgeführt

---

## ⚠️ Identifizierte Probleme

### 1. CSS Variable Konsistenz (KRITISCH)

**Problem**: CSS-Dateien verwenden alte Variable-Namen, die nicht in variables.css definiert sind.

**Betroffene Dateien**:
- contact.css
- footer.css
- hero.css
- services.css

**Alte vs. Neue Variablen**:
| Alt | Neu | Wert |
|-----|-----|------|
| `--primary-color` | `--color-primary` | #0f172a |
| `--accent-color` | `--color-secondary` | #d97706 |
| `--light-text` | `--color-text-light` | #ffffff |
| `--light-bg` | `--color-bg-secondary` | #f8fafc |
| `--spacing-lg` | `--space-6` oder `--space-8` | 24px / 32px |
| `--spacing-md` | `--space-4` | 16px |
| `--spacing-sm` | `--space-2` | 8px |
| `--spacing-xl` | `--space-12` | 48px |
| `--border-radius` | `--radius-base` | 4px |
| `--transition` | `--duration-base` | 200ms |

**Impact**: Diese Variablen existieren nicht in variables.css, daher fallen Styles aus oder verursachen Rendering-Fehler.

**Aktion**: Alle alten Variablen durch neue ersetzen.

---

### 2. Hardcoded Farben (KRITISCH)

**Problem**: Einige CSS-Dateien enthalten hardcoded Hex-Farben statt Variablen.

**Betroffene Werte**:
- `#7f8c8d` (contact.css, services.css) → sollte `--color-text-muted` oder `--slate-500` sein
- `#ecf0f1` (footer.css, hero.css) → sollte `--slate-100` oder `--color-bg-secondary` sein
- `#bdc3c7` (footer.css) → sollte `--color-border` oder `--slate-400` sein

**Aktion**: Alle Hardcodes durch CSS-Variablen ersetzen.

---

### 3. Hardcoded Pixel-Werte

**Problem**: Einige Pixel-Werte sind hardcoded statt über Variables definiert.

**Beispiele**:
- `100px`, `50px`, `500px` Padding/Heights → sollten `--space-*` verwenden
- `rgba(0, 0, 0, 0.1)` Shadow-Farben → teilweise OK (shadows sind Variablen)

**Aktion**: Pixel-Werte mit Spacing-Variablen standardisieren.

---

### 4. CSS Variable Definitions Mismatch

**Problem**: variables.css definiert moderne Namen, aber alte CSS-Dateien verwenden andere Namen.

**Status**:
- ✅ variables.css ist modern und vollständig
- ⚠️ style.css, typography.css, layout.css: Gut, verwenden korrekte Variablen
- ❌ contact.css, footer.css, hero.css, services.css: Verwenden alte/falsche Variablen

---

## 🔧 Durchgeführte Änderungen

### Phase 1: CSS-Variablen Konsistenz (IN PROGRESS)

#### contact.css – Fixes:
- [ ] `--spacing-xl` → `--space-12`
- [ ] `--spacing-md` → `--space-6`
- [ ] `#7f8c8d` → `--color-text-muted`
- [ ] `--light-bg` → `--color-bg-secondary`
- [ ] `--spacing-lg` → `--space-8`
- [ ] `--border-radius` → `--radius-md`

#### footer.css – Fixes:
- [ ] `--primary-color` → `--color-primary`
- [ ] `--light-text` → `--color-text-light`
- [ ] `--spacing-xl` → `--space-12`
- [ ] `--spacing-lg` → `--space-8`
- [ ] `--secondary-color` → `--color-secondary`
- [ ] `--spacing-md` → `--space-6`
- [ ] `--spacing-sm` → `--space-2`
- [ ] `#ecf0f1` → `--slate-100`
- [ ] `#bdc3c7` → `--color-border`
- [ ] `--transition` → `all var(--duration-base)`

#### hero.css – Fixes:
- [ ] `--primary-color` → `--color-primary`
- [ ] `--accent-color` → `--color-secondary`
- [ ] `--light-text` → `--color-text-light`
- [ ] `#ecf0f1` → `--slate-100`
- [ ] `--spacing-lg` → `--space-8`
- [ ] `--spacing-md` → `--space-6`
- [ ] `--spacing-xl` → `--space-12`
- [ ] `--font-size-3xl` ✅ (OK)
- [ ] `--font-size-xl` ✅ (OK)
- [ ] `--font-size-lg` ✅ (OK)
- [ ] Hardcoded `100px`, `50px`, `500px`, `400px` → `--space-*`

#### services.css – Fixes:
- [ ] `--light-bg` → `--color-bg-secondary`
- [ ] `--spacing-xl` → `--space-12`
- [ ] `--spacing-lg` → `--space-8`
- [ ] `--spacing-md` → `--space-4`
- [ ] `--light-text` → `--color-text-light`
- [ ] `--border-radius` → `--radius-md`
- [ ] `--primary-color` → `--color-primary`
- [ ] `#7f8c8d` → `--color-text-muted`
- [ ] `--font-size-sm` ✅ (OK)
- [ ] Hardcoded `0 4px 6px rgba(0, 0, 0, 0.1)` → `--shadow-md`

---

## ✅ Architektur Review – Ergebnisse

### 1. Projektstruktur ✅

```
qualityprintweb/
├── app.py                          ✅ OK
├── config.py                       ✅ OK
├── models.py                       ✅ OK
├── requirements.txt                ✅ OK
├── .env                            ✅ OK
├── .env.example                    ✅ OK
├── routes/
│   ├── __init__.py                ✅ OK
│   ├── home.py                    ✅ OK
│   ├── kontakt.py                 ✅ OK
├── services/
│   ├── __init__.py                ✅ OK
│   ├── mail.py                    ✅ OK
├── static/
│   ├── css/                       ⚠️ CSS-Variablen inkonsistent
│   ├── js/
│   │   ├── menu.js                ✅ OK
│   ├── images/                    ✅ OK
│   ├── icons/                     ✅ OK
├── templates/
│   ├── base.html                  ✅ OK
│   ├── home.html                  ✅ OK
│   ├── kontakt.html               ✅ OK
│   ├── impressum.html             ✅ OK
│   ├── datenschutz.html           ✅ OK
│   ├── components/
│   │   ├── navbar.html            ✅ OK
│   │   ├── footer.html            ✅ OK
│   │   ├── hero.html              ✅ OK
│   │   ├── services.html          ✅ OK
│   │   ├── cta.html               ✅ OK
│   │   ├── contact_form.html      ✅ OK
│   ├── emails/
│   │   ├── kontakt_email.html     ✅ OK
├── docs/
│   ├── DesignSystem.md            ✅ OK
│   ├── Architecture.md            ✅ OK
│   ├── ProjectStatus.md           ✅ OK
│   ├── Changelog.md               ✅ OK
│   ├── Roadmap.md                 ✅ OK
│   ├── Sprint-00-*.md             ✅ OK
│   ├── CSS-Architecture.md        ✅ OK
│   ├── SETUP.md                   ✅ OK
│   ├── Referenzanalyse-*.md       ✅ OK
```

**Bewertung**: ✅ **EXCELLENT** – Struktur ist konsistent und modular.

---

### 2. Flask Template Architektur ✅

- ✅ base.html existiert und wird als Template-Basis verwendet
- ✅ Alle Seiten erweitern base.html
- ✅ Komponenten sind modular in templates/components/
- ✅ Navbar und Footer als Komponenten mit {% include %}
- ✅ Main-Content-Block ist flexibel

**Bewertung**: ✅ **EXCELLENT** – Modular und wartbar.

---

### 3. CSS Architektur ⚠️

**CSS Load Order**: ✅ **CORRECT**
1. variables.css ✅
2. style.css ✅
3. typography.css ✅
4. layout.css ✅
5. Section CSS (navbar, hero, services, contact, footer) ⚠️
6. utilities.css ✅

**CSS File Structure**:
- ✅ variables.css – Moderne CSS-Variablen mit korrekten Namen
- ✅ style.css – Global Styles, korrekt implementiert
- ✅ typography.css – Text Utilities, korrekt
- ✅ layout.css – Grid & Spacing, korrekt
- ❌ contact.css – Alte Variablen, Hardcodes
- ❌ footer.css – Alte Variablen, Hardcodes
- ❌ hero.css – Alte Variablen, Hardcodes
- ❌ services.css – Alte Variablen, Hardcodes
- ✅ utilities.css – Helper Classes, korrekt

**Bewertung**: ⚠️ **NEEDS REFACTORING** – Inkonsistente Variable-Namen und Hardcodes.

---

### 4. Komponentenarchitektur ✅

**HTML-Komponenten**:
- ✅ navbar.html – Saubere Struktur
- ✅ footer.html – Modular
- ✅ hero.html – Wiederverwendbar
- ✅ services.html – Flexibel
- ✅ cta.html – CTA-Komponente
- ✅ contact_form.html – Form-Komponente

**Bewertung**: ✅ **EXCELLENT** – Klare Verantwortlichkeiten, wiederverwendbar.

---

### 5. Designsystem ✅

**Farbpalette**:
- ✅ Slate 900 (Primary)
- ✅ Amber 600 (Secondary)
- ✅ Emerald 600 (Tertiary) – Neu hinzugefügt
- ✅ Semantic Colors (Success, Error, Warning, Info)
- ✅ Proper Aliases (--color-primary, --color-secondary, etc.)

**Typografie**:
- ✅ Font Scale (1.125 Ratio)
- ✅ Font Weights (300-800)
- ✅ Line Heights
- ✅ Letter Spacing

**Spacing**:
- ✅ 8px Grid System
- ✅ 20+ Spacing Values
- ✅ Consistent Naming (--space-1 to --space-32)

**Schatten & Transitions**:
- ✅ 7 Shadow Levels
- ✅ Transition Durations
- ✅ Easing Functions

**Bewertung**: ✅ **EXCELLENT** – Vollständig und modern.

---

### 6. HTML Qualität ✅

- ✅ Semantisches HTML5
- ✅ Korrekte Heading-Hierarchie (H1 → H6)
- ✅ ARIA Labels teilweise vorhanden
- ✅ Meta-Tags vorhanden
- ✅ Sinnvolle Container

**Bewertung**: ✅ **GOOD** – Semantic HTML wird korrekt verwendet.

---

### 7. CSS Qualität ⚠️

**Modularität**: ✅ **GOOD** – Separate CSS-Dateien für Sections.

**Lesbarkeit**: ✅ **GOOD** – Kommentare und Struktur klar.

**Wiederverwendbarkeit**: ⚠️ **NEEDS WORK** – Alte Variable-Namen, Hardcodes.

**Performance**: ✅ **GOOD** – Keine unnötigen Styles.

**Responsive**: ⚠️ **PARTIAL** – Mobile-First ist definiert, aber Implementierung inkonsistent.

**Bewertung**: ⚠️ **NEEDS REFACTORING** – CSS-Variablen müssen konsistent sein.

---

## 📝 Entwicklungsregeln (DOKUMENTIERT)

### Verbindliche Projektregeln:

1. **Template Hierarchy**
   - ✅ base.html ist obligatorisch
   - ✅ Alle Seiten erweitern base.html
   - ✅ {% extends 'base.html' %} in jeder Seite

2. **Komponenten**
   - ✅ Komponenten befinden sich ausschließlich unter templates/components/
   - ✅ Komponenten werden mit {% include 'components/name.html' %} eingebunden
   - ✅ Gemeinsame Bereiche werden niemals dupliziert
   - ✅ max. 3 Ebenen Verschachtelung

3. **CSS-Variablen (KRITISCH)**
   - ✅ ALLE Designwerte stammen ausschließlich aus variables.css
   - ✅ Keine Hardcoded Farben (#xxx)
   - ✅ Keine Hardcoded Abstände (px, em, rem)
   - ✅ Keine Hardcoded Schriftgrößen
   - ✅ Keine Hardcoded Border-Radius
   - ✅ Keine Hardcoded Schatten
   - ✅ Keine Hardcoded Übergänge

4. **CSS-Struktur**
   - ✅ Komponenten besitzen eigene CSS-Dateien
   - ✅ Keine Inline Styles in HTML
   - ✅ BEM-Naming-Konvention
   - ✅ Low Specificity (0,0,1 oder 0,0,2)
   - ✅ Mobile-First Media Queries

5. **HTML**
   - ✅ Semantisches HTML ist verpflichtend
   - ✅ Sinnvolle Container (main, section, article, etc.)
   - ✅ Korrekte Heading-Hierarchie
   - ✅ ARIA-Labels wo notwendig
   - ✅ Keine leeren Divs ohne Zweck

6. **Benennungskonventionen**
   - ✅ CSS-Variablen: `--category-name` (z.B. `--color-primary`, `--space-4`)
   - ✅ CSS-Klassen: BEM-Pattern (z.B. `.button--primary`, `.card__header`)
   - ✅ HTML-Klassen: kebab-case (z.B. `class="hero-section"`)
   - ✅ Template-Dateien: kebab-case.html (z.B. `contact_form.html`)

---

## 🏗️ Architekturverbesserungen

### Farbpalette
✅ **Modern und eigenständig**
- Slate 900 (statt klassisches Grau)
- Amber 600 (statt Rot)
- Emerald 600 (für Nachhaltigkeit)
- Bessere Kontraste für Accessibility

### CSS-Struktur
✅ **Modulare Architektur**
- 10 CSS-Dateien in richtigem Load-Order
- Design-Tokens zentral in variables.css
- Keine Code-Duplikation

### Template-Struktur
✅ **Saubere Inheritance**
- base.html als Single Source of Truth
- Komponenten-basiert
- Jinja2 {% extends %} und {% include %} korrekt verwendet

### Komponenten
✅ **Modular und wiederverwendbar**
- navbar.html
- footer.html
- hero.html
- services.html
- cta.html
- contact_form.html

---

## 📋 Aktualisierte Projektregeln

### CSS Variable Rules (PRIORITY)

```css
/* ✅ KORREKT */
color: var(--color-primary);
padding: var(--space-4) var(--space-6);
border-radius: var(--radius-md);
box-shadow: var(--shadow-md);
transition: all var(--duration-base);
font-size: var(--font-size-lg);

/* ❌ FALSCH */
color: #0f172a;
padding: 16px 24px;
border-radius: 8px;
box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
transition: all 200ms;
font-size: 18px;
```

### Template Rules

```html
<!-- ✅ KORREKT -->
{% extends 'base.html' %}
{% include 'components/navbar.html' %}

<!-- ❌ FALSCH -->
<!-- Direktes HTML statt base.html -->
<!-- Duplizierter Code statt Components -->
```

### Component Rules

```
templates/components/
├── navbar.html ✅
├── footer.html ✅
├── hero.html ✅
├── services.html ✅
├── cta.html ✅
├── contact_form.html ✅
```

---

## 🔄 Sprint 1 Vorbereitung

Basierend auf Sprint 0.1 sind folgende Features für Sprint 1 empfohlen:

1. **Accent-Sections mit Hintergrundfarbe**
   - `.section-accent` CSS-Klasse
   - Hintergrund: --color-bg-accent oder --emerald-50

2. **Headline Underlines**
   - `.headline--accent` CSS-Klasse
   - 4px Amber Underline

3. **Team-Member Cards**
   - Neue Komponente: team-cards.html
   - Grid-Layout: 3-4 Spalten

4. **Link Animations**
   - Bottom Border Animation
   - CSS: `transform: scaleX(0→1)`

5. **Responsive Refinement**
   - Testen auf echten Geräten
   - Breakpoint-Optimierung

---

## 📊 Offene Punkte

### Sofort (Sprint 0.1)
- [ ] CSS-Variablen Konsistenz beheben (contact.css, footer.css, hero.css, services.css)
- [ ] Hardcoded Farben durch Variablen ersetzen
- [ ] Hardcoded Pixel-Werte standardisieren
- [ ] Dokumentation aktualisieren

### Sprint 1
- [ ] Accent-Sections implementieren
- [ ] Headline Underlines hinzufügen
- [ ] Team-Member Cards Komponente
- [ ] Link Animations refinieren
- [ ] Mobile Optimization

### Sprint 2+
- [ ] Performance Optimization
- [ ] SEO Enhancement
- [ ] Analytics Integration
- [ ] Advanced Features

---

## ✅ Empfehlungen für Sprint 1

### Direkt umsetzen
1. Accent-Sections mit Hintergrund-Variablen
2. Headline Underlines mit Amber
3. Team-Member Cards Komponente
4. Link Animation Refinement

### Testen & Validieren
1. Responsive Design auf Geräten
2. Lighthouse Audit durchführen
3. Accessibility Check (WCAG AA)
4. Cross-Browser Testing

### Performance
1. Bilder optimieren (WebP)
2. Lazy Loading implementieren
3. CSS Minification
4. Critical CSS extraction

---

## 📈 Zusammenfassung

| Aspekt | Status | Bewertung | Aktion |
|--------|--------|-----------|--------|
| **Architektur** | ✅ | Excellent | Beibehalten |
| **Template System** | ✅ | Excellent | Beibehalten |
| **Design System** | ✅ | Excellent | Beibehalten |
| **CSS Konsistenz** | ⚠️ | Needs Fix | Variablen vereinheitlichen |
| **HTML Qualität** | ✅ | Good | Beibehalten |
| **Dokumentation** | ✅ | Excellent | Beibehalten |

---

## 🚀 Definition of Done

Sprint 0.1 ist abgeschlossen wenn:

- ✅ Projektstruktur überprüft wurde
- ✅ Architektur überprüft wurde
- ✅ CSS-Struktur überprüft wurde
- ✅ Komponenten überprüft wurden
- ✅ Designsystem überprüft wurde
- ✅ CSS-Variablen konsistent sind
- ✅ Dokumentation aktualisiert wurde
- ✅ Sprint-00.1-Architecture-Review.md erstellt wurde
- ✅ ProjectStatus.md aktualisiert wurde
- ✅ Changelog.md aktualisiert wurde

---

**Status**: 🔄 In Progress
**Next**: Sprint 1 – CSS Implementation & Component Development
**Commit Message**: `refactor(project): architecture review and foundation improvements`
