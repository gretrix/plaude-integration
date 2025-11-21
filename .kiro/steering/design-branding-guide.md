# Design & Branding Guide - Plaud Integration

## Brand Identity

### Brand Essence
**Voice-First Personal Intelligence**
- Modern, clean, and intelligent
- Effortless productivity through voice
- AI-powered insights from everyday conversations
- Personal, not corporate

### Brand Personality
- **Smart**: AI-powered, intelligent, insightful
- **Effortless**: Simple, intuitive, frictionless
- **Personal**: Tailored, private, yours
- **Modern**: Contemporary, fresh, forward-thinking
- **Trustworthy**: Reliable, secure, consistent

## Visual Identity

### Color Palette

#### Primary Colors
```css
/* Deep Purple - Primary Brand Color */
--primary: #6366F1;           /* Indigo-600 - Main actions, headers */
--primary-dark: #4F46E5;      /* Indigo-700 - Hover states */
--primary-light: #818CF8;     /* Indigo-400 - Accents */
--primary-subtle: #EEF2FF;    /* Indigo-50 - Backgrounds */

/* Accent Purple - Secondary */
--accent: #8B5CF6;            /* Violet-500 - Highlights */
--accent-dark: #7C3AED;       /* Violet-600 - Hover */
--accent-light: #A78BFA;      /* Violet-400 - Soft accents */
```

#### Semantic Colors
```css
/* Success - Diet/Health */
--success: #10B981;           /* Emerald-500 - Positive actions */
--success-light: #D1FAE5;     /* Emerald-100 - Backgrounds */

/* Warning - Tasks/Pending */
--warning: #F59E0B;           /* Amber-500 - Attention needed */
--warning-light: #FEF3C7;     /* Amber-100 - Backgrounds */

/* Error - Critical */
--error: #EF4444;             /* Red-500 - Errors, deletions */
--error-light: #FEE2E2;       /* Red-100 - Backgrounds */

/* Info - CRM/Contacts */
--info: #3B82F6;              /* Blue-500 - Information */
--info-light: #DBEAFE;        /* Blue-100 - Backgrounds */
```

#### Neutral Colors
```css
/* Grays - Modern, clean palette */
--gray-50: #F9FAFB;           /* Lightest backgrounds */
--gray-100: #F3F4F6;          /* Card backgrounds */
--gray-200: #E5E7EB;          /* Borders, dividers */
--gray-300: #D1D5DB;          /* Disabled states */
--gray-400: #9CA3AF;          /* Placeholder text */
--gray-500: #6B7280;          /* Secondary text */
--gray-600: #4B5563;          /* Body text */
--gray-700: #374151;          /* Headings */
--gray-800: #1F2937;          /* Dark headings */
--gray-900: #111827;          /* Darkest text */
```

#### Gradient Backgrounds
```css
/* Hero Gradients */
--gradient-primary: linear-gradient(135deg, #6366F1 0%, #8B5CF6 100%);
--gradient-warm: linear-gradient(135deg, #F59E0B 0%, #EF4444 100%);
--gradient-cool: linear-gradient(135deg, #3B82F6 0%, #6366F1 100%);
--gradient-success: linear-gradient(135deg, #10B981 0%, #059669 100%);

/* Subtle Backgrounds */
--gradient-subtle: linear-gradient(180deg, #FFFFFF 0%, #F9FAFB 100%);
--gradient-card: linear-gradient(145deg, #FFFFFF 0%, #F9FAFB 100%);
```

### Typography

#### Font Stack
```css
/* Primary Font - System UI (Modern, Fast) */
--font-primary: -apple-system, BlinkMacSystemFont, 'Segoe UI', 
                'Roboto', 'Helvetica Neue', Arial, sans-serif;

/* Monospace - Code, Data */
--font-mono: 'SF Mono', 'Monaco', 'Cascadia Code', 
             'Courier New', monospace;

/* Optional: Add Inter or Plus Jakarta Sans for more personality */
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
--font-modern: 'Inter', var(--font-primary);
```

#### Type Scale
```css
/* Headings */
--text-xs: 0.75rem;      /* 12px - Labels, captions */
--text-sm: 0.875rem;     /* 14px - Small text, badges */
--text-base: 1rem;       /* 16px - Body text */
--text-lg: 1.125rem;     /* 18px - Large body */
--text-xl: 1.25rem;      /* 20px - Small headings */
--text-2xl: 1.5rem;      /* 24px - Section headings */
--text-3xl: 1.875rem;    /* 30px - Page headings */
--text-4xl: 2.25rem;     /* 36px - Hero headings */
--text-5xl: 3rem;        /* 48px - Large hero */

/* Font Weights */
--font-normal: 400;
--font-medium: 500;
--font-semibold: 600;
--font-bold: 700;

/* Line Heights */
--leading-tight: 1.25;
--leading-normal: 1.5;
--leading-relaxed: 1.75;
```

### Spacing System

```css
/* Consistent spacing scale (4px base) */
--space-1: 0.25rem;   /* 4px */
--space-2: 0.5rem;    /* 8px */
--space-3: 0.75rem;   /* 12px */
--space-4: 1rem;      /* 16px */
--space-5: 1.25rem;   /* 20px */
--space-6: 1.5rem;    /* 24px */
--space-8: 2rem;      /* 32px */
--space-10: 2.5rem;   /* 40px */
--space-12: 3rem;     /* 48px */
--space-16: 4rem;     /* 64px */
--space-20: 5rem;     /* 80px */
```

### Border Radius

```css
/* Modern, soft corners */
--radius-sm: 0.375rem;    /* 6px - Small elements */
--radius-md: 0.5rem;      /* 8px - Buttons, inputs */
--radius-lg: 0.75rem;     /* 12px - Cards */
--radius-xl: 1rem;        /* 16px - Large cards */
--radius-2xl: 1.5rem;     /* 24px - Hero sections */
--radius-full: 9999px;    /* Pills, avatars */
```

### Shadows

```css
/* Elevation system */
--shadow-sm: 0 1px 2px 0 rgba(0, 0, 0, 0.05);
--shadow-md: 0 4px 6px -1px rgba(0, 0, 0, 0.1),
             0 2px 4px -1px rgba(0, 0, 0, 0.06);
--shadow-lg: 0 10px 15px -3px rgba(0, 0, 0, 0.1),
             0 4px 6px -2px rgba(0, 0, 0, 0.05);
--shadow-xl: 0 20px 25px -5px rgba(0, 0, 0, 0.1),
             0 10px 10px -5px rgba(0, 0, 0, 0.04);
--shadow-2xl: 0 25px 50px -12px rgba(0, 0, 0, 0.25);

/* Colored shadows for depth */
--shadow-primary: 0 10px 25px -5px rgba(99, 102, 241, 0.3);
--shadow-success: 0 10px 25px -5px rgba(16, 185, 129, 0.3);
```

## Component Design Patterns

### Cards

```css
.card {
  background: var(--gradient-card);
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  box-shadow: var(--shadow-md);
  border: 1px solid var(--gray-200);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.card:hover {
  box-shadow: var(--shadow-lg);
  transform: translateY(-2px);
}

.card-header {
  font-size: var(--text-2xl);
  font-weight: var(--font-semibold);
  color: var(--gray-900);
  margin-bottom: var(--space-4);
}
```

### Buttons

```css
/* Primary Button */
.btn-primary {
  background: var(--gradient-primary);
  color: white;
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-weight: var(--font-medium);
  box-shadow: var(--shadow-sm);
  transition: all 0.2s ease;
}

.btn-primary:hover {
  box-shadow: var(--shadow-primary);
  transform: translateY(-1px);
}

/* Secondary Button */
.btn-secondary {
  background: white;
  color: var(--primary);
  border: 2px solid var(--primary);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
  font-weight: var(--font-medium);
}

/* Ghost Button */
.btn-ghost {
  background: transparent;
  color: var(--gray-600);
  padding: var(--space-3) var(--space-6);
  border-radius: var(--radius-md);
}

.btn-ghost:hover {
  background: var(--gray-100);
}
```

### Badges

```css
.badge {
  display: inline-flex;
  align-items: center;
  padding: var(--space-1) var(--space-3);
  border-radius: var(--radius-full);
  font-size: var(--text-sm);
  font-weight: var(--font-medium);
  line-height: 1;
}

.badge-success {
  background: var(--success-light);
  color: var(--success);
}

.badge-warning {
  background: var(--warning-light);
  color: var(--warning);
}

.badge-info {
  background: var(--info-light);
  color: var(--info);
}
```

### Input Fields

```css
.input {
  width: 100%;
  padding: var(--space-3) var(--space-4);
  border: 2px solid var(--gray-200);
  border-radius: var(--radius-md);
  font-size: var(--text-base);
  transition: all 0.2s ease;
  background: white;
}

.input:focus {
  outline: none;
  border-color: var(--primary);
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.1);
}

.input::placeholder {
  color: var(--gray-400);
}
```

### Tables

```css
.table {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
}

.table thead th {
  background: var(--gray-50);
  padding: var(--space-4);
  text-align: left;
  font-weight: var(--font-semibold);
  color: var(--gray-700);
  font-size: var(--text-sm);
  text-transform: uppercase;
  letter-spacing: 0.05em;
  border-bottom: 2px solid var(--gray-200);
}

.table tbody td {
  padding: var(--space-4);
  border-bottom: 1px solid var(--gray-100);
  color: var(--gray-600);
}

.table tbody tr:hover {
  background: var(--gray-50);
}
```

## Icon System

### Recommended Icon Library
**Lucide Icons** or **Heroicons** (modern, consistent, open-source)

```html
<!-- Example: Add to HTML head -->
<script src="https://unpkg.com/lucide@latest"></script>

<!-- Usage -->
<i data-lucide="mic"></i>        <!-- Voice/Plaud -->
<i data-lucide="utensils"></i>   <!-- Diet -->
<i data-lucide="check-square"></i> <!-- Tasks -->
<i data-lucide="users"></i>      <!-- CRM -->
<i data-lucide="activity"></i>   <!-- Dashboard -->
```

### Icon Sizes
```css
--icon-xs: 16px;
--icon-sm: 20px;
--icon-md: 24px;
--icon-lg: 32px;
--icon-xl: 48px;
```

## Layout Patterns

### Dashboard Layout

```css
.dashboard-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: var(--space-8);
  background: var(--gray-50);
  min-height: 100vh;
}

.dashboard-header {
  background: white;
  border-radius: var(--radius-2xl);
  padding: var(--space-8);
  margin-bottom: var(--space-8);
  box-shadow: var(--shadow-md);
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: var(--space-6);
  margin-bottom: var(--space-8);
}

.stat-card {
  background: white;
  border-radius: var(--radius-xl);
  padding: var(--space-6);
  box-shadow: var(--shadow-md);
  border-left: 4px solid var(--primary);
}
```

### Navigation

```css
.nav {
  display: flex;
  gap: var(--space-2);
  flex-wrap: wrap;
}

.nav-item {
  padding: var(--space-3) var(--space-5);
  border-radius: var(--radius-md);
  font-weight: var(--font-medium);
  color: var(--gray-600);
  transition: all 0.2s ease;
  text-decoration: none;
}

.nav-item:hover {
  background: var(--primary-subtle);
  color: var(--primary);
}

.nav-item.active {
  background: var(--primary);
  color: white;
  box-shadow: var(--shadow-primary);
}
```

## Animation & Transitions

### Timing Functions
```css
--ease-in-out: cubic-bezier(0.4, 0, 0.2, 1);
--ease-out: cubic-bezier(0, 0, 0.2, 1);
--ease-in: cubic-bezier(0.4, 0, 1, 1);
--ease-bounce: cubic-bezier(0.68, -0.55, 0.265, 1.55);
```

### Common Animations
```css
/* Fade in */
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

/* Slide in */
@keyframes slideIn {
  from { transform: translateX(-20px); opacity: 0; }
  to { transform: translateX(0); opacity: 1; }
}

/* Pulse (for notifications) */
@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

/* Usage */
.animate-fade-in {
  animation: fadeIn 0.3s var(--ease-out);
}
```

## Responsive Design

### Breakpoints
```css
/* Mobile first approach */
--breakpoint-sm: 640px;   /* Small devices */
--breakpoint-md: 768px;   /* Tablets */
--breakpoint-lg: 1024px;  /* Laptops */
--breakpoint-xl: 1280px;  /* Desktops */
--breakpoint-2xl: 1536px; /* Large screens */
```

### Mobile Optimizations
```css
@media (max-width: 768px) {
  .dashboard-container {
    padding: var(--space-4);
  }
  
  .stats-grid {
    grid-template-columns: 1fr;
    gap: var(--space-4);
  }
  
  .nav {
    flex-direction: column;
  }
  
  .card {
    padding: var(--space-4);
  }
}
```

## Accessibility

### Focus States
```css
*:focus-visible {
  outline: 2px solid var(--primary);
  outline-offset: 2px;
}

button:focus-visible,
a:focus-visible {
  box-shadow: 0 0 0 3px rgba(99, 102, 241, 0.3);
}
```

### Color Contrast
- All text must meet WCAG AA standards (4.5:1 for normal text)
- Interactive elements must be clearly distinguishable
- Don't rely on color alone to convey information

### Screen Reader Support
```html
<!-- Add aria labels -->
<button aria-label="Mark task as complete">
  <i data-lucide="check"></i>
</button>

<!-- Use semantic HTML -->
<nav aria-label="Main navigation">
  <!-- navigation items -->
</nav>
```

## Brand Voice & Messaging

### Tone of Voice
- **Conversational**: "Your voice notes, organized"
- **Empowering**: "Capture everything, forget nothing"
- **Simple**: "Just speak. We'll handle the rest."
- **Personal**: "Your personal AI assistant"

### Microcopy Examples
```
Empty States:
- "No tasks yet. Start by recording a voice note!"
- "Your diet log is empty. Tell us what you ate today."
- "No contacts yet. Mention someone in your next recording."

Success Messages:
- "✓ Task completed! Nice work."
- "✓ Diet entry saved"
- "✓ Contact added to your network"

Error Messages:
- "Oops! Couldn't save that. Try again?"
- "Connection lost. Retrying..."
```

## Implementation Priority

### Phase 1: Core Updates (High Impact)
1. Update color palette to new primary colors
2. Modernize card designs with new shadows and borders
3. Update button styles with gradients
4. Improve typography scale and weights

### Phase 2: Polish (Medium Impact)
5. Add smooth transitions and animations
6. Update badge designs
7. Improve table styling
8. Add icon system

### Phase 3: Enhancement (Nice to Have)
9. Add subtle background gradients
10. Implement advanced hover effects
11. Add loading states and skeletons
12. Create custom illustrations

## Design Resources

### Tools
- **Figma**: For mockups and prototypes
- **Coolors.co**: Color palette generation
- **Lucide Icons**: Icon library
- **Google Fonts**: Typography (Inter recommended)

### Inspiration
- Linear.app (clean, modern SaaS)
- Notion (personal productivity)
- Superhuman (email, focus on speed)
- Height (project management, beautiful UI)

## Quick Reference

### Do's
✅ Use consistent spacing (multiples of 4px)
✅ Maintain high contrast for readability
✅ Add smooth transitions (0.2-0.3s)
✅ Use semantic colors (green=success, red=error)
✅ Keep mobile-first approach
✅ Add hover states to interactive elements

### Don'ts
❌ Don't use more than 3 font weights
❌ Don't mix border radius styles
❌ Don't use pure black (#000000)
❌ Don't forget focus states
❌ Don't use animations longer than 0.5s
❌ Don't sacrifice accessibility for aesthetics
