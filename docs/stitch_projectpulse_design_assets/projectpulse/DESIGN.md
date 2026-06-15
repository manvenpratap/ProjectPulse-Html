---
name: ProjectPulse
colors:
  surface: '#f7f9fb'
  surface-dim: '#d8dadc'
  surface-bright: '#f7f9fb'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#f2f4f6'
  surface-container: '#eceef0'
  surface-container-high: '#e6e8ea'
  surface-container-highest: '#e0e3e5'
  on-surface: '#191c1e'
  on-surface-variant: '#3c4a46'
  inverse-surface: '#2d3133'
  inverse-on-surface: '#eff1f3'
  outline: '#6c7a76'
  outline-variant: '#bbcac4'
  surface-tint: '#006b5c'
  primary: '#006b5c'
  on-primary: '#ffffff'
  primary-container: '#00c2a8'
  on-primary-container: '#00493e'
  inverse-primary: '#41ddc2'
  secondary: '#00658c'
  on-secondary: '#ffffff'
  secondary-container: '#5bc6ff'
  on-secondary-container: '#005170'
  tertiary: '#525f71'
  on-tertiary: '#ffffff'
  tertiary-container: '#a0aec2'
  on-tertiary-container: '#344252'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#65fade'
  primary-fixed-dim: '#41ddc2'
  on-primary-fixed: '#00201b'
  on-primary-fixed-variant: '#005045'
  secondary-fixed: '#c5e7ff'
  secondary-fixed-dim: '#7fd0ff'
  on-secondary-fixed: '#001e2d'
  on-secondary-fixed-variant: '#004c6a'
  tertiary-fixed: '#d6e4f9'
  tertiary-fixed-dim: '#bac8dc'
  on-tertiary-fixed: '#0f1c2c'
  on-tertiary-fixed-variant: '#3a4859'
  background: '#f7f9fb'
  on-background: '#191c1e'
  surface-variant: '#e0e3e5'
typography:
  display:
    fontFamily: Plus Jakarta Sans
    fontSize: 48px
    fontWeight: '800'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 32px
    fontWeight: '700'
    lineHeight: '1.3'
    letterSpacing: -0.01em
  headline-lg-mobile:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '700'
    lineHeight: '1.3'
  headline-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.4'
  body-lg:
    fontFamily: Plus Jakarta Sans
    fontSize: 18px
    fontWeight: '400'
    lineHeight: '1.6'
  body-md:
    fontFamily: Plus Jakarta Sans
    fontSize: 16px
    fontWeight: '400'
    lineHeight: '1.5'
  body-sm:
    fontFamily: Plus Jakarta Sans
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
  label-caps:
    fontFamily: Plus Jakarta Sans
    fontSize: 12px
    fontWeight: '700'
    lineHeight: '1'
    letterSpacing: 0.05em
  code:
    fontFamily: JetBrains Mono
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.5'
rounded:
  sm: 0.25rem
  DEFAULT: 0.5rem
  md: 0.75rem
  lg: 1rem
  xl: 1.5rem
  full: 9999px
spacing:
  unit: 4px
  xs: 4px
  sm: 8px
  md: 16px
  lg: 24px
  xl: 40px
  gutter: 24px
  margin-desktop: 64px
  margin-mobile: 16px
---

## Brand & Style

The design system is engineered for executive-level oversight and high-fidelity project management. It balances the precision of an engineering tool with the clarity required for board-level presentations. The aesthetic is **Corporate / Modern**, leaning heavily into high-density information display without sacrificing breathing room.

The emotional response should be one of "controlled momentum"—efficient, transparent, and authoritative. It utilizes a refined color palette and precise geometry to signal reliability and technical sophistication.

## Colors

The color strategy uses a light-mode foundation to ensure maximum readability and a clean "canvas" feel. 

- **Primary Teal** is the core action color, representing progress and vitality.
- **Sky Blue** and **Navy** provide structural depth, used for categorization and navigation elements.
- **Functional Colors** (Success, Warning, Danger, Purple) follow standard semantic patterns but are slightly desaturated to maintain a professional, "engineering-grade" appearance rather than a consumer-playful vibe.
- **Backgrounds** use a very light slate to reduce eye strain compared to pure white, creating a subtle contrast with card elements.

## Typography

The typography system relies on **Plus Jakarta Sans** for its contemporary, approachable, yet professional character. It features a slightly wider stance which aids legibility in data-heavy views. 

- **Headlines** utilize tighter letter-spacing and heavier weights to create a strong visual anchor.
- **Body text** maintains a generous line-height to ensure long-form project descriptions remain readable.
- **JetBrains Mono** is reserved for technical identifiers, ID numbers, and data points that require character-level clarity, reinforcing the "engineering-grade" aesthetic.

## Layout & Spacing

The layout is built on a **Fluid Grid** system using a 4px base unit. 
- **Desktop:** A 12-column grid with 24px gutters. Use wide 64px outer margins to create a "dashboard" feel that centers the user's focus.
- **Canvas Areas:** For diagrams and infographics, use a fixed-aspect ratio container (1600px width) that scales proportionally to fit the viewport.
- **Spacing Rhythm:** Use `md` (16px) for internal component padding and `lg` (24px) for spacing between major UI blocks.

## Elevation & Depth

This design system uses a **Tonal Layering** approach combined with **Ambient Shadows** to create a structured hierarchy. 

- **Level 0 (Canvas):** The #F8FAFC background.
- **Level 1 (Cards/Panels):** Pure white (#FFFFFF) surfaces with a subtle border (#E2E8F0) and a soft ambient shadow (`0 4px 20px rgba(0,0,0,0.05)`).
- **Level 2 (Modals/Popovers):** Pure white surfaces with a more pronounced shadow and a 1px border to separate the element from the Level 1 background.

Avoid heavy blacks or high-opacity shadows. Depth is communicated through the transition from the slate background to the white card surface.

## Shapes

The shape language is varied to distinguish between "containers" and "nodes." 
- **Major Containers (Cards, Modals):** Use a 12px to 16px radius (`rounded-lg` or `rounded-xl`). This softens the executive dashboard and makes the interface feel modern.
- **Interactive Nodes (Buttons, Inputs, Nodes):** Use a tighter 6px to 8px radius. This sharper look conveys precision and technical accuracy.

## Components

- **Buttons:** Primary buttons use the Teal (#00C2A8) background with white text. Secondary buttons use a Navy (#0D1B2A) outline or ghost style. Use 8px corner radius.
- **Cards:** White background, 16px corner radius, 24px internal padding. Always include the subtle 0.05 opacity shadow.
- **Inputs:** 1px border (#E2E8F0), 6px corner radius. On focus, the border shifts to Teal with a soft 2px outer glow.
- **Chips/Badges:** Use a light tint of the status color for the background and the full-saturation color for the text (e.g., Success badge: Light Green bg, Dark Green text). 
- **Nodes (Diagramming):** 8px corner radius, white background, 1px Navy or Sky Blue border. Use JetBrains Mono for ID labels within the node.
- **Data Tables:** Use horizontal dividers only (#E2E8F0). Header cells use `label-caps` typography with a Navy text color.