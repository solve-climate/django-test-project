# Solve Climate - Homepage

A single-page website for the Solve Climate community, built with [FastHTML](https://fastht.ml/) and [DaisyUI](https://daisyui.com/) (Tailwind CSS).

## Prerequisites

- Python 3.10+
- pip

## Setup

### 1. Clone the repository

```bash
git clone <repo-url>
cd solve-climate
```

### 2. Create and activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate
```

On Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install python-fasthtml
```

## Running the website

```bash
python app.py
```

The site will be available at `http://localhost:5001`.

## Project structure

```
.
├── app.py          # Main application - all routes, components, and styling
├── README.md       # This file
└── .venv/          # Virtual environment (not committed)
```

## How the app is organized

`app.py` contains everything in one file:

1. **Headers & theme** - DaisyUI and Tailwind CDN imports, plus a custom dark theme defined via CSS variables (oklch colors)
2. **Icons** - Inline SVG icons (lightbulb, slack, calendar, mailbox) using Lucide icon paths
3. **Form components** - Email input with validation and a message textarea
4. **Sections** - Five "hero" sections that stack vertically:
    - `hero` - Welcome message with a "Get Started" button
    - `hero2` - "The idea" section with lightbulb icon
    - `hero3` - "The platform we use" with Slack link
    - `hero4` - "When is the next solvaton?" with calendar icon
    - `hero5` - Contact form with email input, textarea, and send button
5. **Route** - A single `/` route that returns all sections combined

## Making changes

### Editing text content

Each section has a `title` and `text` variable near the section definition. Update those strings to change the content.

### Changing colors

The theme is defined in the `custom_theme` `Style()` block at the top of `app.py`. Colors use the [oklch](https://oklch.com/) color space. Key variables:

- `--color-primary` - Main accent color (buttons, highlights)
- `--color-secondary` - Secondary accent
- `--color-base-100` / `200` / `300` - Background shades (darkest to lightest)
- `--color-base-content` - Text color

See [DaisyUI theming docs](https://daisyui.com/docs/themes/) for the full list.

### Adding a new section

1. Define a new `heroN` div using the same pattern as existing sections
2. Add it to the `Div(hero, hero2, ...)` return in the `home()` function

## Troubleshooting

**Port already in use**: Change the port by adding `port=8000` to the `serve()` call at the bottom of `app.py`.

**Styles not loading**: Make sure you have an internet connection — DaisyUI and Tailwind are loaded from CDN.

**Changes not showing**: Hard refresh your browser (Ctrl+Shift+R / Cmd+Shift+R).

## Tech stack

- [FastHTML](https://fastht.ml/) - Python web framework
- [DaisyUI 5](https://daisyui.com/) - Tailwind CSS component library
- [Tailwind CSS 4](https://tailwindcss.com/) - Utility-first CSS framework
- [Lucide Icons](https://lucide.dev/) - SVG icon set (inline)