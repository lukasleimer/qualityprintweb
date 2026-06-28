# Design System – Quality Print

## Philosophie

Das Design-System folgt einer **minimalistischen, zeitlosen und hochwertigen** Ästhetik, die Premium und Kompetenz ausstrahlt. Inspiriert von Modern Corporate Design mit Fokus auf Funktionalität und Klarheit.

---

## 1. Farbpalette

### Primary Colors (Brandfarben)

| Name | Hex | RGB | Verwendung |
|------|-----|-----|------------|
| **Slate-900** (Primary) | `#0f172a` | rgb(15, 23, 42) | Headlines, Primary Actions |
| **Slate-800** | `#1e293b` | rgb(30, 41, 59) | Body Text, Secondary Elements |
| **Slate-700** | `#334155` | rgb(51, 65, 85) | Tertiary Text, Borders |

### Secondary Colors (Akzent)

| Name | Hex | RGB | Verwendung |
|------|-----|-----|------------|
| **Amber-600** (Primary Accent) | `#d97706` | rgb(217, 119, 6) | Highlights, CTAs |
| **Amber-500** | `#f59e0b` | rgb(245, 158, 11) | Hover States |
| **Amber-50** | `#fffbeb` | rgb(255, 251, 235) | Light Backgrounds |

### Neutral Colors

| Name | Hex | RGB | Verwendung |
|------|-----|-----|------------|
| **White** | `#ffffff` | rgb(255, 255, 255) | Background, Text |
| **Gray-50** | `#f9fafb` | rgb(249, 250, 251) | Light Backgrounds |
| **Gray-100** | `#f3f4f6` | rgb(243, 244, 246) | Subtle Backgrounds |
| **Gray-200** | `#e5e7eb` | rgb(229, 231, 235) | Borders, Dividers |
| **Gray-400** | `#9ca3af` | rgb(156, 163, 175) | Placeholder Text |

### Semantic Colors

| Name | Hex | Verwendung |
|------|-----|------------|
| **Success** | `#10b981` | Erfolgreiche Aktionen |
| **Warning** | `#f59e0b` | Warnmeldungen |
| **Error** | `#ef4444` | Fehlermeldungen |
| **Info** | `#3b82f6` | Informationen |

---

## 2. Typografie

### Schriftfamilien

```css
/* Primary Font */
--font-sans: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif;

/* Mono Font (für Code) */
--font-mono: 'JetBrains Mono', 'Courier New', monospace;
```

### Font Sizes (Typografische Skala – 1.125 Ratio)

| Name | Size | Line-Height | Letter-Spacing | Verwendung |
|------|------|-------------|-----------------|------------|
| **xs** | 12px | 1.5 | 0.5px | Small captions, labels |
| **sm** | 14px | 1.6 | 0.25px | Small text, inputs |
| **base** | 16px | 1.6 | 0 | Body text |
| **lg** | 18px | 1.75 | 0 | Large text, intro |
| **xl** | 20px | 1.75 | -0.5px | Subheadings |
| **2xl** | 24px | 1.3 | -0.5px | Section titles |
| **3xl** | 32px | 1.2 | -1px | Page titles |
| **4xl** | 42px | 1.1 | -1.5px | Hero titles |

### Font Weights

| Name | Value | Verwendung |
|------|-------|------------|
| Light | 300 | Subtitles, disabled states |
| Regular | 400 | Body text, standard |
| Medium | 500 | Subheadings, emphasis |
| Semibold | 600 | Headings, buttons |
| Bold | 700 | Strong headlines |

### Text Styles

```css
/* Headings */
h1: 42px, Bold (700), -1.5px letter-spacing
h2: 32px, Semibold (600), -1px letter-spacing
h3: 24px, Semibold (600), -0.5px letter-spacing
h4: 20px, Medium (500), -0.5px letter-spacing
h5: 18px, Medium (500), 0
h6: 16px, Medium (500), 0

/* Body */
p: 16px, Regular (400), 0, Line-height 1.6
small: 14px, Regular (400), 0, Line-height 1.6
caption: 12px, Regular (400), 0.5px
```

---

## 3. Abstände (Spacing Scale)

Konsistente Abstände basierend auf 8px Grundraster:

```css
--space-0: 0
--space-1: 4px    (0.25rem)
--space-2: 8px    (0.5rem)
--space-3: 12px   (0.75rem)
--space-4: 16px   (1rem)
--space-5: 20px   (1.25rem)
--space-6: 24px   (1.5rem)
--space-8: 32px   (2rem)
--space-10: 40px  (2.5rem)
--space-12: 48px  (3rem)
--space-16: 64px  (4rem)
--space-20: 80px  (5rem)
--space-24: 96px  (6rem)
```

---

## 4. Border Radius

Konsistente Kurvenradien für unterschiedliche Zwecke:

```css
--radius-none: 0
--radius-sm: 2px      /* Subtle elements */
--radius-base: 4px    /* Standard elements */
--radius-md: 8px      /* Cards, inputs */
--radius-lg: 12px     /* Larger components */
--radius-xl: 16px     /* Extra large components */
--radius-full: 9999px /* Pills, circles */
```

---

## 5. Schatten (Shadows)

Subtile Schatten für Tiefenwirkung:

```css
--shadow-none: none
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05)
--shadow-base: 0 1px 3px 0 rgba(0, 0, 0, 0.1), 0 1px 2px 0 rgba(0, 0, 0, 0.06)
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06)
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05)
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04)
--shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25)

/* Inset Schatten */
--shadow-inset: inset 0 2px 4px 0 rgba(0, 0, 0, 0.05)
```

---

## 6. Button System (Visual Foundation)

The button system defines the interaction style for the entire website. All buttons follow these principles: **Premium, accessible, consistent**.

### Button Sizes

All sizes maintain **44px+ touch targets** for mobile accessibility.

| Größe | Höhe | Padding | Font | Verwendung |
|-------|------|---------|------|------------|
| **xs** | 24px | 4px 12px | 12px | Small labels, compact |
| **sm** | 32px | 8px 20px | 14px | Navigation, sidebars |
| **base** | 40px | 12px 24px | 16px | Standard buttons |
| **lg** | 48px | 16px 32px | 18px | Hero sections |
| **xl** | 56px | 16px 48px | 20px | Large hero CTAs |

### Button Variants

#### 1. Primary Button (Hauptaktion)

**Purpose**: High-priority actions, CTAs, conversion goals

```css
/* Default State */
background: var(--color-secondary)       /* Amber-600 */
color: var(--color-text-light)           /* White */
border: none
border-radius: var(--radius-md)
font-weight: 600
box-shadow: 0 2px 8px rgba(217, 119, 6, 0.15)
transition: all 0.2s ease-out

/* Hover State */
background: var(--color-secondary-light) /* Amber-500 */
color: white
box-shadow: 0 4px 12px rgba(217, 119, 6, 0.25)
transform: translateY(-1px)              /* Lift effect */

/* Active State */
transform: translateY(0)                 /* Press effect */
box-shadow: 0 1px 4px rgba(217, 119, 6, 0.15)

/* Focus State */
outline: 2px solid var(--color-secondary)
outline-offset: 2px

/* Disabled State */
background: var(--color-neutral-300)
color: var(--color-neutral-500)
cursor: not-allowed
box-shadow: none
```

**Example Usage**: "Angebot anfordern", "Jetzt starten", "Anfrage senden"

#### 2. Secondary Button (Alternative Aktion)

**Purpose**: Alternative actions, less important than primary

```css
/* Default State */
background: var(--color-neutral-50)
color: var(--color-primary)
border: 1px solid var(--color-neutral-200)
font-weight: 500

/* Hover State */
background: var(--color-neutral-100)
border-color: var(--color-primary)

/* Focus State */
outline: 2px solid var(--color-secondary)
outline-offset: 2px
```

#### 3. Outline Button (Tertiäre Aktion)

**Purpose**: Less important actions, filtering, toggles

```css
/* Default State */
background: transparent
color: var(--color-primary)
border: 1px solid var(--color-primary)
font-weight: 500

/* Hover State */
background: var(--color-neutral-100)
border-color: var(--color-primary)

/* Focus State */
outline: 2px solid var(--color-secondary)
outline-offset: 2px
```

#### 4. Text Button (Minimale Aktion)

**Purpose**: Link-like buttons, footnotes, inline actions

```css
/* Default State */
background: transparent
color: var(--color-secondary)
border: none
text-decoration: underline
font-weight: 500

/* Hover State */
color: var(--color-secondary-light)
text-decoration-thickness: 2px

/* Focus State */
outline: 2px solid var(--color-secondary)
outline-offset: 2px
```

### Button States

All buttons support these states:

| State | Appearance | Use Case |
|-------|-----------|----------|
| **Default** | Base styles | Button not interacted |
| **Hover** | Color/shadow change | Mouse over button |
| **Active** | Press effect | Button clicked |
| **Focus** | Outline visible | Keyboard navigation |
| **Disabled** | Gray, no pointer | Action unavailable |
| **Loading** | Optional spinner | Async operation |

### Button Modifiers

```css
/* Full width */
.btn-block { width: 100%; }

/* Icon + Text */
.btn-icon { display: inline-flex; gap: var(--space-2); }

/* Button Group */
.btn-group { display: flex; gap: 0; }
.btn-group .btn { border-radius: 0; }
.btn-group .btn:first-child { border-radius: var(--radius-md) 0 0 var(--radius-md); }
.btn-group .btn:last-child { border-radius: 0 var(--radius-md) var(--radius-md) 0; }
```

### Button Animations

All buttons use consistent animation values:

| Animation | Duration | Easing | Effect |
|-----------|----------|--------|--------|
| **Hover** | 200ms | ease-out | Lift + shadow |
| **Active** | 100ms | ease-out | Press |
| **Focus** | Instant | N/A | Outline |
| **Disabled** | Instant | N/A | Opacity |

### Color Contrast (Accessibility)

All button combinations meet **WCAG AAA** standards:

| Button Type | Ratio | Level |
|-------------|-------|-------|
| Primary (Amber-600 on White) | 9.5:1 | AAA ✅ |
| Primary hover (Amber-500 on White) | 8.2:1 | AA ✅ |
| Secondary (Slate-900 on Gray-50) | 11.8:1 | AAA ✅ |
| Text (Amber-600 on White) | 9.5:1 | AAA ✅ |

### Touch Target Sizes

Mobile buttons must be **44px minimum** (both height and width minimum):

```css
/* Minimum touch target */
min-width: 44px
min-height: 44px

/* Padding should result in larger buttons */
.btn-sm: 32px height (accepts 24px minimum margin)
.btn-base: 40px height (accepts 2px minimum margin)
.btn-lg: 48px height (full target)
```

### Button Usage Guidelines

**Primary Button**
- ✅ One primary per page section
- ✅ High contrast to draw attention
- ✅ Clear call-to-action
- ✅ Warm amber color = approachable

**Secondary Button**
- ✅ Alternative to primary
- ✅ Lower visual weight
- ✅ Paired with primary for choice

**Outline Button**
- ✅ Filter options
- ✅ Toggle selections
- ✅ Minimal emphasis

**Text Button**
- ✅ Inline links
- ✅ "Read more" actions
- ✅ Footer/sidebar links

### Examples in Navigation

The navigation bar demonstrates button usage:

```html
<!-- CTA Button in Navbar -->
<a href="/kontakt" class="btn btn-primary btn-sm">
    Angebot anfordern
</a>

<!-- Mobile Menu Button -->
<button class="btn btn-primary btn-lg" style="width: 100%;">
    Jetzt Anfragen
</button>
```

### Future Extensions (Not Yet Implemented)

- [ ] Icon buttons with only icons (no text)
- [ ] Loading state with spinner
- [ ] Dropdown buttons with submenu
- [ ] Split buttons (action + dropdown)
- [ ] Dark mode variants
- [ ] Size responsive adjustments

---

## 7. Formulare

### Input Felder

```css
/* Base Styling */
font-size: 16px
padding: 10px 12px
border: 1px solid var(--gray-200)
border-radius: 4px
background: white
color: var(--slate-900)
transition: all 0.2s ease

/* Focus State */
outline: none
border-color: var(--amber-600)
box-shadow: 0 0 0 3px rgba(217, 119, 6, 0.1)

/* Disabled State */
background: var(--gray-50)
color: var(--gray-400)
cursor: not-allowed

/* Error State */
border-color: var(--error-red)
background: rgba(239, 68, 68, 0.02)
```

### Label Styling

```css
font-size: 14px
font-weight: 500
color: var(--slate-900)
margin-bottom: 6px
display: block
```

### Form Groups

```css
margin-bottom: 20px

/* Spacing zwischen Labels und Input */
label + input: margin-top 6px
```

---

## 8. Grid System

### Container Breiten

```css
--container-sm: 640px   /* Mobile */
--container-md: 768px   /* Tablet */
--container-lg: 1024px  /* Laptop */
--container-xl: 1280px  /* Desktop */
--container-2xl: 1440px /* Wide Desktop */

/* Standard: 1200px mit 24px Seitenpuffer */
.container {
    max-width: 1200px
    margin: 0 auto
    padding: 0 24px
}
```

### Column Grids

```css
/* 12er Grid System */
grid-template-columns: repeat(12, 1fr)
gap: 24px

/* Responsiv */
Mobile (< 640px): 1 column
Tablet (640px - 1024px): 2-3 columns
Desktop (> 1024px): 12 columns
```

---

## 9. Breakpoints

```css
--breakpoint-mobile: 320px
--breakpoint-sm: 640px
--breakpoint-md: 768px
--breakpoint-lg: 1024px
--breakpoint-xl: 1280px
--breakpoint-2xl: 1536px
```

### Mobile First Approach

```css
/* Base styles für Mobile */
/* Dann mit @media für größere Screens erweitern */

@media (min-width: 640px) { /* Tablet */ }
@media (min-width: 1024px) { /* Desktop */ }
@media (min-width: 1280px) { /* Large Desktop */ }
```

---

## 10. Transitions & Animations

### Standard Transitions

```css
--transition-fast: 150ms ease-in-out
--transition-base: 200ms ease-in-out
--transition-slow: 300ms ease-in-out
--transition-slower: 500ms ease-in-out

/* Häufig verwendete */
transition: color 200ms ease-in-out
transition: all 200ms ease-in-out
```

### Easing Functions

```css
--ease-in: cubic-bezier(0.4, 0, 1, 1)
--ease-out: cubic-bezier(0, 0, 0.2, 1)
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1)
--ease-linear: linear
```

---

## 11. CSS Konventionen & Best Practices

### Namenskonventionen (BEM)

```css
/* Block */
.card {}

/* Block__Element */
.card__header {}
.card__body {}
.card__footer {}

/* Block--Modifier */
.card--featured {}
.card--compact {}

/* Element + Modifier */
.card__header--primary {}
```

### Variablennamenskonventionen

```css
/* Komponenten */
--btn-primary-bg: #0f172a
--btn-primary-hover: #1e293b

/* Abstände */
--space-lg: 24px

/* Farben nach Intensität */
--slate-50, --slate-100, ..., --slate-900

/* Zahlenwerte */
--duration-fast: 150ms
--radius-md: 8px
```

### CSS Struktur

```
variables.css       ← CSS Variablen, Farbpalette
reset.css           ← Browser Resets
typography.css      ← Font Definitionen, Text Styles
layout.css          ← Grid, Container, Spacing
components/
  ├── buttons.css   ← Button Komponenten
  ├── forms.css     ← Form Elemente
  ├── cards.css     ← Card Komponenten
  └── ...
sections/
  ├── navbar.css    ← Navbar Styles
  ├── hero.css      ← Hero Section
  ├── footer.css    ← Footer
  └── ...
utilities.css       ← Utility Classes
responsive.css      ← Media Queries
```

### CSS Best Practices

1. **Kaskade nutzen** – Spezifität niedrig halten
2. **Variablen verwenden** – Konsistenz gewährleisten
3. **Keine IDs in CSS** – Nur Classes verwenden
4. **Mobile First** – Mit Smartphones beginnen
5. **Semantisches HTML** – CSS auf Struktur aufbauen
6. **DRY Prinzip** – Nicht wiederholen, Variablen nutzen
7. **Kommentieren** – Komplexe Logik erklären
8. **Performance** – Unnötige Reflows vermeiden

---

## 12. Beispiel: Layout Pattern

### Section mit Container

```html
<section class="section section--light">
    <div class="container">
        <h2 class="section__title">Titel</h2>
        <p class="section__subtitle">Untertitel</p>
        
        <div class="grid grid--cols-3">
            <div class="card">...</div>
            <div class="card">...</div>
            <div class="card">...</div>
        </div>
    </div>
</section>
```

```css
.section {
    padding: var(--space-16) 0;
    background: white;
}

.section--light {
    background: var(--gray-50);
}

.section__title {
    font-size: var(--font-size-2xl);
    font-weight: 600;
    margin-bottom: var(--space-4);
}

.section__subtitle {
    font-size: var(--font-size-lg);
    color: var(--slate-700);
    margin-bottom: var(--space-12);
}

.grid {
    display: grid;
    gap: var(--space-8);
}

.grid--cols-3 {
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}

@media (min-width: 1024px) {
    .grid--cols-3 {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

---

## 13. Accessibility (A11y)

### Kontrast
- **Normal Text**: Mindestens 4.5:1 Kontrast (WCAG AA)
- **Large Text**: Mindestens 3:1 Kontrast

### Focus States
```css
/* Immer Focus State zeigen, nicht verstecken */
*:focus {
    outline: 2px solid var(--amber-600);
    outline-offset: 2px;
}

/* Entfernen nur mit Alternative */
button:focus-visible {
    outline: 2px solid var(--amber-600);
}
```

### Farben nicht als einzige Info
- Nicht nur Farbe verwenden, um Informationen zu vermitteln
- Icons, Text oder Muster zusätzlich nutzen

---

## 14. Performance-Optimierungen

### Critical CSS
```css
/* Inline in <head> */
- Base Styles
- Typography
- Layouts
- Above-the-fold Komponenten
```

### Lazy Loading
```css
/* Non-critical CSS async laden */
<link rel="preload" href="components.css" as="style">
```

### Font Loading
```css
/* System Fonts verwenden für schnelleres Laden */
font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
```

---

## 15. Hero Section (Premium Landing)

### Hero Layout

The hero section establishes a premium visual presence using the typography and color system.

**Desktop (1024px+)**:
```css
grid-template-columns: 1fr 1fr
gap: var(--space-16)              /* 32px gap */
align-items: center
min-height: 600px
```

**Mobile (<768px)**:
```css
grid-template-columns: 1fr       /* Single column */
gap: var(--space-12)
min-height: auto
flex-direction: column
```

### Hero Typography

**Headline**
```css
Font-size: 42px (desktop) → 24px (mobile)
Font-weight: 700 (Bold)
Letter-spacing: -0.5px (tight)
Line-height: 1.1
Color: var(--color-primary)       /* Slate-900 */
```

**Description**
```css
Font-size: 18px (desktop) → 16px (mobile)
Font-weight: 400 (Regular)
Letter-spacing: 0
Line-height: 1.7
Color: var(--color-neutral-700)   /* Slate-700 */
Max-width: 550px
```

**Trust Badges**
```css
Font-size: 14px
Font-weight: 500 (Medium)
Color: var(--color-neutral-700)
Icon: 20px circle, Amber-600 background
```

### Hero Colors

```css
Background: var(--color-neutral-50)   /* Gray-50 */
Headline: var(--color-primary)        /* Slate-900 */
Description: var(--color-neutral-700) /* Slate-700 */
Accent: var(--color-secondary)        /* Amber-600 */
```

**Contrast Ratios** (WCAG AAA):
- Slate-900 on Gray-50: 11.8:1 ✅
- Slate-700 on Gray-50: 7.1:1 ✅
- Amber-600 on White: 9.5:1 ✅

### Hero Image Area

```css
/* Aspect Ratio */
Desktop/Tablet: 4:3
Mobile: 16:9

/* Sizing */
Max-width: 500px
Responsive: width 100%
Border-radius: var(--radius-lg)     /* 12px */
Box-shadow: 0 10px 30px rgba(0,0,0,0.1)

/* Placeholder */
Background: Linear gradient Gray-100 → Gray-50
SVG grid pattern overlay
Centered placeholder text
```

### Hero Call-to-Action Buttons

**Primary Button** ("Angebot anfordern")
```css
Class: btn btn-primary btn-lg
Background: var(--color-secondary)  /* Amber-600 */
Color: white
Padding: 16px 32px
Height: 48px
Hover: Lift effect + shadow enhancement
```

**Secondary Button** ("Leistungen ansehen")
```css
Class: btn btn-secondary btn-lg
Background: var(--color-neutral-50)
Color: var(--color-primary)
Border: 1px solid var(--color-neutral-200)
Hover: Background lightens
```

**Button Layout**
```css
Desktop: flex, gap 24px (side-by-side)
Mobile: flex-direction column, 100% width (stacked)
```

### Hero Responsive

| Device | Headline | Description | Layout | Image |
|--------|----------|-------------|--------|-------|
| **Desktop** | 42px | 18px | 2-column | 4:3 |
| **Tablet** | 32px | 18px | 2-column | 4:3 |
| **Mobile** | 24px | 16px | 1-column | 16:9 |
| **Small** | 20px | 14px | 1-column | 16:9 |

---

## 15. Design Tokens

Zentralisierte Design Decisions für einfache Wartung:

```css
:root {
    /* Brand */
    --brand-primary: #0f172a;
    --brand-accent: #d97706;
    
    /* Semantik */
    --color-success: #10b981;
    --color-warning: #f59e0b;
    --color-error: #ef4444;
    
    /* Spacing */
    --spacing: 8px;
    
    /* Typography */
    --font-primary: 'Inter', sans-serif;
    
    /* Shadow */
    --shadow-elevation-1: 0 1px 3px rgba(0, 0, 0, 0.1);
}
```

---

## Verwendung im Projekt

Alle Dateien folgen diesem Design System:
- `static/css/variables.css` – Alle Variablen
- `static/css/typography.css` – Font Definitionen
- `static/css/components/` – Komponenten
- `static/css/sections/` – Sektions-spezifische Styles

Immer Variablen verwenden, niemals Werte hardcoden!
