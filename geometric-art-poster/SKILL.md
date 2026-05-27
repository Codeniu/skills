---
name: geometric-art-poster
description: A toolkit for generating geometric art posters based on user input themes. Creates beautiful PNG format posters with geometric shapes and theme-based color schemes.
license: MIT
---

# Geometric Art Poster Generator

A toolkit for creating stunning geometric art posters based on user-provided themes. This skill generates unique, visually appealing PNG posters using various geometric shapes and theme-inspired color palettes.

## Features

- **Theme-based generation**: Analyzes user input themes to generate relevant visual compositions
- **Diverse geometric shapes**: Supports circles, triangles, squares, polygons, lines, and abstract patterns
- **Color psychology**: Maps themes to appropriate color schemes
- **Poster formats**: Generates high-quality PNG images in standard poster sizes

## Poster Dimensions

- **Standard**: 800x1200 pixels (portrait)
- **Square**: 1024x1024 pixels
- **Wide**: 1200x800 pixels (landscape)

## Core Workflow

```python
from core.poster_builder import PosterBuilder
from core.theme_colors import get_theme_colors

# 1. Get theme colors based on user input
colors = get_theme_colors("ocean sunset")

# 2. Create builder with desired dimensions
builder = PosterBuilder(width=800, height=1200)

# 3. Generate the poster
poster = builder.generate(theme="ocean sunset", colors=colors)

# 4. Save as PNG
builder.save(poster, "ocean_sunset_poster.png")
```

## Quick Start

```python
from core.poster_builder import PosterBuilder

builder = PosterBuilder()
poster = builder.generate("abstract technology")
builder.save(poster, "tech_poster.png")
```

## Available Utilities

### PosterBuilder (`core.poster_builder`)

```python
builder = PosterBuilder(width=800, height=1200, style="abstract")
poster = builder.generate(
    theme="nature",
    colors=None,  # Auto-generate based on theme
    complexity=3,  # 1-5, higher = more elements
    symmetry=True  # Enable/disable symmetric composition
)
builder.save(poster, "output.png")
```

### Theme Colors (`core.theme_colors`)

```python
from core.theme_colors import get_theme_colors, ColorPalette

# Get colors for a theme
colors = get_theme_colors("night sky")
# Returns: ColorPalette with primary, secondary, accent colors

# Available themes:
# - nature, ocean, sunset, forest, desert
# - technology, digital, cyberpunk
# - abstract, minimalist, geometric
# - sunset, sunrise, night, dawn
# - ocean, mountain, forest, garden
```

### Geometry Generator (`core.geometry_generator`)

```python
from core.geometry_generator import GeometryGenerator

gen = GeometryGenerator(width=800, height=1200)

# Draw individual shapes
frame = gen.create_frame()
frame = gen.draw_circle(frame, center=(400, 600), radius=100, color=(255, 100, 50))
frame = gen.draw_triangle(frame, points=[(400, 200), (600, 800), (200, 800)], color=(100, 200, 255))
frame = gen.draw_polygon(frame, sides=6, center=(400, 600), radius=80, color=(200, 50, 150))
```

## Theme-to-Color Mapping

The generator analyzes keywords in the theme and maps them to appropriate color palettes:

| Theme Keywords | Color Scheme |
|----------------|--------------|
| ocean, sea, water | Blues, teals, aquas |
| sunset, sunrise, dawn | Oranges, pinks, purples |
| forest, nature, garden | Greens, browns, earth tones |
| technology, digital | Cyans, grays, neon accents |
| night, dark, mystery | Deep blues, purples, blacks |
| abstract, geometric | Vibrant contrasts, bold colors |
| minimalist, clean | Whites, grays, muted tones |

## Geometric Shapes

The generator uses these shapes to create compositions:

- **Circles**: Perfect for organic, flowing designs
- **Triangles**: Dynamic, angular compositions
- **Squares/Rectangles**: Structured, modern looks
- **Polygons**: Hexagons, octagons for complexity
- **Lines**: Diagonals, grids, and abstract patterns
- **Patterns**: Stripes, grids, gradients

## Design Principles

- **Balance**: Symmetric or asymmetric composition
- **Contrast**: Color and shape contrast for visual interest
- **Hierarchy**: Main focal point with supporting elements
- **Rhythm**: Repeating patterns and shapes
- **Proportion**: Harmonious sizing relationships

## Dependencies

```bash
pip install pillow numpy
```