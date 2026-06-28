# CSS Architecture Guide

**Location**: `static/css/`  
**Status**: Fully Implemented  
**Last Updated**: 2026-06-28

---

## 📚 CSS File Structure & Load Order

### 1. **variables.css** (Design Tokens)
- **Purpose**: Define all design tokens and CSS custom properties
- **Imports**: None (loaded first)
- **Contains**:
  - Color palettes (Slate, Amber, Semantic)
  - Typography scale and font definitions
  - Spacing scale (8px grid)
  - Border radius values
  - Shadows (box-shadow definitions)
  - Transitions and animations
  - Z-index scale
  - Breakpoint definitions
  - Component sizing

**Example**:
```css
:root {
    --primary-color: #0f172a;
    --space-4: 16px;
    --font-size-lg: 18px;
}
```

**Usage**: All other CSS files use these variables for consistency.

---

### 2. **style.css** (Global Styles)
- **Purpose**: Base styles and component resets
- **Imports**: variables.css
- **Contains**:
  - HTML element resets (* { margin: 0; padding: 0; })
  - Global typography rules (body, h1-h6, p, a)
  - Global button styling
  - Form element styling
  - Container and layout basics
  - Card components
  - Badge components
  - Utility classes (text-center, text-primary, etc)
  - Accessibility focus states

**Specificity**: Low (0,0,1 - mostly element selectors)

---

### 3. **typography.css** (Text Styling)
- **Purpose**: Advanced typography utilities
- **Contains**:
  - Display heading styles
  - Text utilities (text-truncate, text-clamp)
  - Font weight utilities
  - Line height utilities
  - Letter spacing utilities
  - Font size utilities
  - Code/Pre formatting
  - Blockquote styling
  - Table styling
  - List styling

**Usage**: Extensive text utility classes for flexible typography.

---

### 4. **layout.css** (Grid & Flexbox)
- **Purpose**: Layout system and spacing utilities
- **Contains**:
  - Flexbox utilities (flex, flex-col, justify-center, items-center)
  - Grid utilities (grid-cols-1, grid-cols-3, etc)
  - Gap utilities (gap-4, gap-x-8, etc)
  - Padding utilities (p-4, px-6, py-8, etc)
  - Margin utilities (m-4, mx-auto, mt-8, etc)
  - Container utilities (w-full, max-w-lg, etc)
  - Display utilities (block, flex, hidden, etc)
  - Responsive grid classes

**Specificity**: Low (0,0,1 - class selectors)

**Example**:
```css
.grid { display: grid; gap: var(--grid-gap-desktop); }
.grid-cols-3 { grid-template-columns: repeat(3, 1fr); }
.mx-auto { margin-left: auto; margin-right: auto; }
```

---

### 5. **Section Styles** (Component-Specific CSS)

#### **navbar.css**
- Sticky navigation bar
- Mobile menu toggle
- Logo styling
- Navigation links
- Responsive hamburger menu

#### **hero.css**
- Hero section background
- Large headline typography
- Call-to-action button
- Background gradient/image

#### **services.css**
- Service grid layout
- Service cards
- Hover effects
- Responsive columns

#### **contact.css**
- Contact form styling
- Form validation styles
- CTA (Call-to-Action) section
- Input focus states
- Error message styling

#### **footer.css**
- Footer layout
- Footer columns
- Footer links
- Copyright section

---

### 6. **utilities.css** (Helper Classes)
- **Purpose**: Miscellaneous utility classes
- **Contains**:
  - Cursor utilities (cursor-pointer, cursor-not-allowed)
  - Overflow utilities (overflow-hidden, overflow-x-auto)
  - Position utilities (absolute, relative, fixed, sticky)
  - Float utilities (float-left, float-right)
  - Opacity utilities (opacity-50, opacity-100)
  - Shadow utilities (shadow-md, shadow-lg)
  - Background utilities (bg-primary, bg-error)
  - Border utilities (border, rounded, rounded-lg)
  - Transform utilities (scale-105, rotate-90, translate-y-4)
  - Transition utilities (transition-all, duration-base)
  - Appearance utilities (appearance-none, select-none)
  - Centering patterns (center-flex, center-absolute)
  - Screen reader utilities (sr-only)

**Usage**: Fine-grained control without custom CSS.

---

## 📋 Loading Order in HTML

```html
<head>
    <!-- 1. Design Tokens (must be first!) -->
    <link rel="stylesheet" href="css/variables.css">
    
    <!-- 2. Base/Global Styles -->
    <link rel="stylesheet" href="css/style.css">
    
    <!-- 3. Typography -->
    <link rel="stylesheet" href="css/typography.css">
    
    <!-- 4. Layout & Grid -->
    <link rel="stylesheet" href="css/layout.css">
    
    <!-- 5. Section Styles (can be in any order) -->
    <link rel="stylesheet" href="css/navbar.css">
    <link rel="stylesheet" href="css/hero.css">
    <link rel="stylesheet" href="css/services.css">
    <link rel="stylesheet" href="css/contact.css">
    <link rel="stylesheet" href="css/footer.css">
</head>
```

**Important**: Load order matters for CSS cascading!

---

## 🎯 CSS Architecture Principles

### 1. **Cascade, Don't Override**
```css
/* Good: Use cascade */
.btn { color: blue; }
.btn-primary { background: blue; }

/* Bad: Override with !important */
.btn { color: blue !important; }
```

### 2. **Use Variables, Never Hardcode**
```css
/* Good */
color: var(--color-primary);
padding: var(--space-4);

/* Bad */
color: #0f172a;
padding: 16px;
```

### 3. **Low Specificity**
- Use classes, avoid IDs
- Use single classes when possible
- Avoid deep nesting

```css
/* Good: 0,0,1 specificity */
.card { }

/* Avoid: 0,1,1 specificity */
#sidebar .card { }
```

### 4. **BEM Naming Convention**
```css
.card { }                    /* Block */
.card__header { }            /* Element */
.card__header--primary { }   /* Modifier */
```

### 5. **Mobile-First Responsive Design**
```css
/* Base styles for mobile */
.grid { grid-template-columns: 1fr; }

/* Tablet and up */
@media (min-width: 768px) {
    .grid { grid-template-columns: 2fr 1fr; }
}

/* Desktop and up */
@media (min-width: 1024px) {
    .grid { grid-template-columns: 3fr 1fr; }
}
```

---

## 🔍 Specificity Reference

| Selector | Specificity |
|----------|-------------|
| `.class` | 0,0,1 |
| `element` | 0,0,1 |
| `.class.class` | 0,0,2 |
| `.class element` | 0,0,2 |
| `#id` | 0,1,0 |
| `.class:hover` | 0,0,2 |
| `!important` | Overrides all (avoid!) |

**Best Practice**: Aim for lowest possible specificity.

---

## 🎨 How to Use in HTML

### Example 1: Simple Button
```html
<button class="btn btn-primary">Click Me</button>
```

### Example 2: Card with Grid
```html
<div class="grid grid-cols-3 gap-8">
    <div class="card">
        <h3 class="card__header">Title</h3>
        <p class="card__body">Content</p>
    </div>
</div>
```

### Example 3: Flex Layout
```html
<div class="flex items-center justify-between gap-4 p-6">
    <h1>Title</h1>
    <button class="btn btn-primary">Action</button>
</div>
```

### Example 4: Responsive Grid
```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
    <!-- Items -->
</div>
```

---

## ✅ Common CSS Patterns

### Center Content Horizontally
```css
.container {
    max-width: 1200px;
    margin-left: auto;
    margin-right: auto;
}

<!-- Or use utility -->
<div class="mx-auto max-w-lg">...</div>
```

### Center Flex
```css
.flex-center {
    display: flex;
    align-items: center;
    justify-content: center;
}
```

### Card with Hover Effect
```css
.card {
    padding: var(--space-6);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-sm);
    transition: all var(--transition-base);
}

.card:hover {
    box-shadow: var(--shadow-lg);
    transform: translateY(-4px);
}
```

### Responsive Typography
```css
h1 {
    font-size: var(--font-size-2xl);
}

@media (min-width: 1024px) {
    h1 {
        font-size: var(--font-size-4xl);
    }
}
```

---

## 🔧 Customization Guide

### Adding a New Color
1. Add to `variables.css`:
```css
--slate-950: #030712;
```

2. Create utility class in `utilities.css`:
```css
.bg-slate-950 {
    background-color: var(--slate-950);
}
```

3. Use in HTML:
```html
<div class="bg-slate-950">...</div>
```

### Adding a New Spacing Value
1. Add to `variables.css`:
```css
--space-18: 72px;
```

2. Add utility in `layout.css`:
```css
.mt-18 { margin-top: var(--space-18); }
.mb-18 { margin-bottom: var(--space-18); }
```

### Adding a New Component
1. Create `static/css/components/newcomponent.css`
2. Import in `base.html`
3. Use BEM naming:
```css
.newcomponent { }
.newcomponent__item { }
.newcomponent--variant { }
```

---

## 🚀 Performance Tips

### 1. Use Variables Instead of Hardcoding
- Easier to update globally
- Reduces CSS size with proper minification
- Enables theme switching

### 2. Avoid Overriding
- Use cascade properly
- Don't use `!important`
- Respect specificity

### 3. Minimize Media Queries
- Mobile-first approach
- Reuse breakpoint variables
- Group similar queries

### 4. Remove Unused CSS
- Regularly audit utility classes
- Delete deprecated styles
- Monitor CSS file size

---

## 📊 File Statistics

| File | Lines | Purpose |
|------|-------|---------|
| **variables.css** | 350+ | Design Tokens |
| **style.css** | 400+ | Global Styles |
| **typography.css** | 250+ | Text Utilities |
| **layout.css** | 300+ | Grid & Flex |
| **utilities.css** | 350+ | Helper Classes |
| **navbar.css** | 100+ | Navigation |
| **hero.css** | 80+ | Hero Section |
| **services.css** | 60+ | Services |
| **contact.css** | 100+ | Contact Form |
| **footer.css** | 80+ | Footer |
| **TOTAL** | 2,000+ | Complete System |

---

## 🔗 Related Documentation

- [Design System](../docs/DesignSystem.md)
- [Architecture](../docs/Architecture.md)
- [Sprint 0 Report](../docs/Sprint-00-Designsystem.md)

---

## 💡 Best Practices Checklist

- [ ] All colors use CSS variables
- [ ] All spacing uses space scale
- [ ] All fonts use typography scale
- [ ] All breakpoints use defined breakpoints
- [ ] No hardcoded values
- [ ] BEM naming convention followed
- [ ] Low specificity maintained
- [ ] Mobile-first approach used
- [ ] Accessibility considered
- [ ] Performance optimized

---

**Last Updated**: 2026-06-28  
**Maintainer**: Lukas  
**Version**: 1.0.0
