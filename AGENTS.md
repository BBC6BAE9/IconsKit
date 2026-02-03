# AGENTS.md

> AI Programming Assistant Guide - IconsKit Icon Library

## Project Overview

IconsKit is a Swift Package icon library providing 6 different icon styles in SVG format, designed for iOS/macOS app development.

## Development Commands

```bash
# Build project
swift build

# Run tests
swift test

# Auto-generate icon resources
python auto_generate.py
```

## Project Structure

```
IconsKit/
├── Sources/IconsKit/     # Icon resources (SVG + JSON)
├── Tests/                # Test files
├── pic/                  # Style preview images
├── Package.swift         # Swift Package configuration
└── auto_generate.py      # Icon generation script
```

---

## Icon Style Usage Guide

### 1. Bold (Solid Fill)

**Visual Characteristics:** Fully filled solid icons with maximum visual weight

**Best Use Cases:**
- Tab Bar selected state
- Primary action buttons
- Feature entry points that need emphasis
- Icons on dark backgrounds
- Important toolbar actions

**Design Guidelines:**
```
✅ Recommended: Tab selected state, FAB buttons, key feature entries
❌ Avoid: Dense list icons, secondary information icons
```

---

### 2. Broken (Gap Line Style)

**Visual Characteristics:** Lines with gaps/breaks, strong modern aesthetic

**Best Use Cases:**
- Fashion/trendy app overall styling
- Creative application icon systems
- Youth-oriented product UI design
- Scenarios requiring differentiated visuals
- Decorative icons for empty states

**Design Guidelines:**
```
✅ Recommended: Creative apps, trendy e-commerce, social media, empty state illustrations
❌ Avoid: Serious finance/government apps, icons requiring clear recognition
```

---

### 3. Bulk (Dual-tone Block)

**Visual Characteristics:** Partial fill + partial transparency, creating depth

**Best Use Cases:**
- Scenarios needing visual hierarchy without heaviness
- Dashboard data card icons
- Feature module entry icons
- Settings page category icons
- Complex icons requiring primary/secondary distinction

**Design Guidelines:**
```
✅ Recommended: Dashboards, feature entries, settings categories, card decorations
❌ Avoid: Small sizes (<16px), single-color-only environments
```

---

### 4. Light-Border (Thin Line with Border)

**Visual Characteristics:** Thin strokes + rounded borders, light and orderly

**Best Use Cases:**
- Form input field prefix icons
- List item auxiliary icons
- Icons on light/white backgrounds
- Scenarios with many icons that shouldn't dominate
- Utility app feature lists

**Design Guidelines:**
```
✅ Recommended: Form icons, list auxiliary icons, settings item icons, info display
❌ Avoid: Dark backgrounds, primary actions needing emphasis
```

---

### 5. Light-Outline (Thin Outline)

**Visual Characteristics:** Pure outline strokes, minimalist style

**Best Use Cases:**
- Minimalist app overall icon system
- Tab Bar unselected state
- Reading apps (reducing visual distraction)
- Content-focused page auxiliary icons
- Premium/luxury product UI

**Design Guidelines:**
```
✅ Recommended: Tab unselected state, reading apps, minimalist design, content support
❌ Avoid: Complex backgrounds, urgent actions requiring quick recognition
```

---

### 6. Two-Tone (Dual Color)

**Visual Characteristics:** Two colors/opacity levels creating foreground-background depth

**Best Use Cases:**
- Brand color system icon expression
- Status indicators (e.g., completed/in-progress)
- Scenarios requiring distinction between icon elements
- Onboarding page featured icons
- Designs needing finer hierarchy control than Bulk

**Design Guidelines:**
```
✅ Recommended: Brand icons, status indicators, onboarding pages, featured functions
❌ Avoid: Single-color print scenarios, color-restricted environments
```

---

## Style Selection Decision Tree

```
Need to choose an icon style?
│
├─ Need emphasis?
│   ├─ Yes → Bold
│   └─ No → Continue
│
├─ Want trendy/creative feel?
│   ├─ Yes → Broken
│   └─ No → Continue
│
├─ Need visual hierarchy?
│   ├─ Yes → Need brand colors?
│   │       ├─ Yes → Two-Tone
│   │       └─ No → Bulk
│   └─ No → Continue
│
└─ Minimalist/auxiliary icons?
    ├─ Need border feel → Light-Border
    └─ Pure outline works → Light-Outline
```

## Common Style Combinations

| Scenario | Selected State | Unselected State | Notes |
|----------|----------------|------------------|-------|
| Tab Bar | Bold | Light-Outline | Classic combo, clear contrast |
| Tab Bar (Modern) | Bulk | Broken | Strong trendy feel |
| Settings Page | - | Light-Border | Unified, clean and tidy |
| Dashboard | Bulk | - | Rich hierarchy, not heavy |

---

## AI Programming Guidelines

### Adding New Icons

1. Ensure all 6 styles have corresponding files
2. Place SVG files in appropriate `Sources/IconsKit/` subdirectory
3. Run `python auto_generate.py` to update resources
4. Naming convention: `icon-name.svg` (lowercase + hyphens)

### Code Style

- Swift code follows Swift API Design Guidelines
- File naming uses PascalCase
- Icon resource naming uses kebab-case

### Testing Requirements

- New features require corresponding test cases
- Run `swift test` to ensure all tests pass

---

## Related Resources

- Preview images located in `pic/` directory
- Style examples in README.md
