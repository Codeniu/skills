#!/usr/bin/env python3
"""
Theme Colors - Module for mapping themes to color palettes.

This module provides utilities for analyzing user input themes and generating
appropriate color schemes based on color psychology and theme keywords.
"""

import random
from dataclasses import dataclass
from typing import List, Tuple, Optional


@dataclass
class ColorPalette:
    """Represents a color palette with primary, secondary, and accent colors."""
    primary: Tuple[int, int, int]
    secondary: Tuple[int, int, int]
    accent: Tuple[int, int, int]
    background: Tuple[int, int, int]
    text: Tuple[int, int, int]
    all_colors: List[Tuple[int, int, int]]


# Theme-to-color mappings
THEME_COLORS = {
    "ocean": {
        "primary": (0, 150, 200),
        "secondary": (30, 200, 255),
        "accent": (255, 150, 100),
        "background": (5, 30, 50),
        "text": (255, 255, 255)
    },
    "sea": {
        "primary": (0, 100, 150),
        "secondary": (50, 180, 220),
        "accent": (255, 200, 150),
        "background": (10, 40, 60),
        "text": (255, 255, 255)
    },
    "water": {
        "primary": (100, 180, 220),
        "secondary": (150, 220, 255),
        "accent": (255, 180, 120),
        "background": (20, 60, 80),
        "text": (255, 255, 255)
    },
    "sunset": {
        "primary": (255, 100, 50),
        "secondary": (255, 180, 80),
        "accent": (180, 50, 120),
        "background": (20, 10, 30),
        "text": (255, 255, 255)
    },
    "sunrise": {
        "primary": (255, 150, 100),
        "secondary": (255, 200, 150),
        "accent": (200, 80, 150),
        "background": (30, 20, 40),
        "text": (255, 255, 255)
    },
    "dawn": {
        "primary": (200, 100, 150),
        "secondary": (255, 150, 200),
        "accent": (150, 200, 255),
        "background": (25, 15, 40),
        "text": (255, 255, 255)
    },
    "forest": {
        "primary": (50, 120, 50),
        "secondary": (80, 180, 100),
        "accent": (200, 150, 80),
        "background": (15, 30, 20),
        "text": (255, 255, 255)
    },
    "nature": {
        "primary": (60, 140, 80),
        "secondary": (100, 180, 120),
        "accent": (255, 200, 100),
        "background": (20, 40, 30),
        "text": (255, 255, 255)
    },
    "garden": {
        "primary": (180, 80, 120),
        "secondary": (220, 120, 160),
        "accent": (100, 200, 150),
        "background": (30, 20, 40),
        "text": (255, 255, 255)
    },
    "mountain": {
        "primary": (100, 120, 140),
        "secondary": (150, 170, 190),
        "accent": (255, 180, 100),
        "background": (30, 35, 45),
        "text": (255, 255, 255)
    },
    "technology": {
        "primary": (0, 200, 255),
        "secondary": (100, 150, 255),
        "accent": (255, 100, 200),
        "background": (10, 15, 25),
        "text": (255, 255, 255)
    },
    "digital": {
        "primary": (50, 200, 200),
        "secondary": (100, 180, 255),
        "accent": (200, 100, 255),
        "background": (5, 10, 20),
        "text": (255, 255, 255)
    },
    "cyberpunk": {
        "primary": (255, 50, 150),
        "secondary": (100, 200, 255),
        "accent": (255, 255, 100),
        "background": (10, 5, 20),
        "text": (255, 255, 255)
    },
    "night": {
        "primary": (80, 60, 150),
        "secondary": (120, 100, 200),
        "accent": (200, 150, 255),
        "background": (5, 5, 15),
        "text": (255, 255, 255)
    },
    "dark": {
        "primary": (100, 100, 120),
        "secondary": (150, 150, 180),
        "accent": (255, 100, 100),
        "background": (10, 10, 15),
        "text": (255, 255, 255)
    },
    "mystery": {
        "primary": (120, 80, 160),
        "secondary": (160, 120, 200),
        "accent": (255, 100, 150),
        "background": (15, 10, 30),
        "text": (255, 255, 255)
    },
    "abstract": {
        "primary": (255, 80, 80),
        "secondary": (80, 180, 255),
        "accent": (255, 200, 80),
        "background": (20, 20, 20),
        "text": (255, 255, 255)
    },
    "geometric": {
        "primary": (200, 50, 100),
        "secondary": (50, 150, 200),
        "accent": (255, 200, 50),
        "background": (25, 25, 30),
        "text": (255, 255, 255)
    },
    "minimalist": {
        "primary": (100, 100, 100),
        "secondary": (180, 180, 180),
        "accent": (0, 150, 200),
        "background": (245, 245, 245),
        "text": (30, 30, 30)
    },
    "clean": {
        "primary": (80, 80, 80),
        "secondary": (150, 150, 150),
        "accent": (50, 150, 100),
        "background": (250, 250, 250),
        "text": (20, 20, 20)
    },
    "desert": {
        "primary": (200, 150, 80),
        "secondary": (255, 200, 120),
        "accent": (150, 80, 50),
        "background": (40, 30, 20),
        "text": (255, 255, 255)
    },
    "fire": {
        "primary": (255, 80, 30),
        "secondary": (255, 150, 50),
        "accent": (255, 200, 100),
        "background": (30, 10, 10),
        "text": (255, 255, 255)
    },
    "ice": {
        "primary": (150, 200, 255),
        "secondary": (200, 230, 255),
        "accent": (100, 150, 200),
        "background": (230, 245, 255),
        "text": (20, 40, 60)
    },
    "galaxy": {
        "primary": (80, 50, 150),
        "secondary": (120, 80, 200),
        "accent": (255, 200, 150),
        "background": (5, 5, 15),
        "text": (255, 255, 255)
    },
    "space": {
        "primary": (60, 40, 100),
        "secondary": (100, 80, 150),
        "accent": (200, 180, 255),
        "background": (5, 5, 10),
        "text": (255, 255, 255)
    },
    "neon": {
        "primary": (50, 255, 150),
        "secondary": (255, 50, 200),
        "accent": (255, 255, 50),
        "background": (10, 10, 15),
        "text": (255, 255, 255)
    },
    "retro": {
        "primary": (255, 100, 150),
        "secondary": (255, 200, 100),
        "accent": (100, 200, 255),
        "background": (30, 20, 40),
        "text": (255, 255, 255)
    },
    "vintage": {
        "primary": (180, 120, 80),
        "secondary": (220, 180, 140),
        "accent": (100, 150, 80),
        "background": (40, 30, 25),
        "text": (255, 255, 255)
    },
    "elegant": {
        "primary": (180, 160, 180),
        "secondary": (220, 200, 220),
        "accent": (255, 200, 180),
        "background": (20, 15, 25),
        "text": (255, 255, 255)
    },
    "modern": {
        "primary": (50, 100, 150),
        "secondary": (100, 150, 200),
        "accent": (255, 150, 100),
        "background": (20, 25, 35),
        "text": (255, 255, 255)
    }
}

# Keywords that map to themes
THEME_KEYWORDS = {
    "ocean": ["ocean", "sea", "water", "wave", "blue", "aquatic", "marine"],
    "sunset": ["sunset", "sunrise", "dawn", "dusk", "orange", "golden", "twilight"],
    "forest": ["forest", "nature", "garden", "green", "leaf", "tree", "plant"],
    "technology": ["technology", "digital", "cyberpunk", "tech", "computer", "futuristic"],
    "night": ["night", "dark", "mystery", "midnight", "evening"],
    "abstract": ["abstract", "geometric", "art", "modern", "creative"],
    "minimalist": ["minimalist", "clean", "simple", "elegant", "sophisticated"],
    "desert": ["desert", "sand", "arid", "sun", "hot"],
    "fire": ["fire", "flame", "red", "orange", "burn"],
    "ice": ["ice", "snow", "winter", "cold", "frost"],
    "galaxy": ["galaxy", "space", "star", "cosmic", "universe"],
    "neon": ["neon", "glow", "bright", "electric"],
    "retro": ["retro", "vintage", "classic", "nostalgic"],
    "mountain": ["mountain", "peak", "hill", "alpine"]
}


def analyze_theme(theme: str) -> str:
    """
    Analyze a theme string and determine the best matching color theme.

    Args:
        theme: User input theme string

    Returns:
        The best matching theme key
    """
    theme_lower = theme.lower().strip()
    
    for theme_key, keywords in THEME_KEYWORDS.items():
        for keyword in keywords:
            if keyword in theme_lower:
                return theme_key
    
    return "abstract"


def get_theme_colors(theme: str) -> ColorPalette:
    """
    Get a color palette based on the input theme.

    Args:
        theme: User input theme string

    Returns:
        ColorPalette with appropriate colors for the theme
    """
    matched_theme = analyze_theme(theme)
    colors = THEME_COLORS.get(matched_theme, THEME_COLORS["abstract"])
    
    all_colors = [
        colors["primary"],
        colors["secondary"],
        colors["accent"],
        colors["background"],
        colors["text"]
    ]
    
    return ColorPalette(
        primary=colors["primary"],
        secondary=colors["secondary"],
        accent=colors["accent"],
        background=colors["background"],
        text=colors["text"],
        all_colors=all_colors
    )


def generate_random_palette() -> ColorPalette:
    """
    Generate a random color palette.

    Returns:
        Random ColorPalette
    """
    themes = list(THEME_COLORS.keys())
    random_theme = random.choice(themes)
    colors = THEME_COLORS[random_theme]
    
    all_colors = [
        colors["primary"],
        colors["secondary"],
        colors["accent"],
        colors["background"],
        colors["text"]
    ]
    
    return ColorPalette(
        primary=colors["primary"],
        secondary=colors["secondary"],
        accent=colors["accent"],
        background=colors["background"],
        text=colors["text"],
        all_colors=all_colors
    )


def mix_palettes(palette1: ColorPalette, palette2: ColorPalette, ratio: float = 0.5) -> ColorPalette:
    """
    Mix two color palettes together.

    Args:
        palette1: First color palette
        palette2: Second color palette
        ratio: Mix ratio (0.0 = palette1, 1.0 = palette2)

    Returns:
        Mixed ColorPalette
    """
    def mix_color(c1: Tuple[int, int, int], c2: Tuple[int, int, int]) -> Tuple[int, int, int]:
        return (
            int(c1[0] * (1 - ratio) + c2[0] * ratio),
            int(c1[1] * (1 - ratio) + c2[1] * ratio),
            int(c1[2] * (1 - ratio) + c2[2] * ratio)
        )
    
    primary = mix_color(palette1.primary, palette2.primary)
    secondary = mix_color(palette1.secondary, palette2.secondary)
    accent = mix_color(palette1.accent, palette2.accent)
    background = mix_color(palette1.background, palette2.background)
    text = mix_color(palette1.text, palette2.text)
    
    all_colors = [primary, secondary, accent, background, text]
    
    return ColorPalette(
        primary=primary,
        secondary=secondary,
        accent=accent,
        background=background,
        text=text,
        all_colors=all_colors
    )


def get_analogous_colors(base_color: Tuple[int, int, int], count: int = 3) -> List[Tuple[int, int, int]]:
    """
    Generate analogous colors based on a base color.

    Args:
        base_color: RGB base color
        count: Number of analogous colors to generate

    Returns:
        List of RGB color tuples
    """
    r, g, b = base_color
    analogous = [(r, g, b)]
    
    for i in range(1, count):
        offset = i * 30
        r_shift = int(20 * i * (1 if i % 2 == 0 else -1))
        g_shift = int(15 * i * (-1 if i % 2 == 0 else 1))
        b_shift = int(10 * i)
        
        new_r = max(0, min(255, r + r_shift))
        new_g = max(0, min(255, g + g_shift))
        new_b = max(0, min(255, b + b_shift))
        
        analogous.append((new_r, new_g, new_b))
    
    return analogous


def get_complementary_color(color: Tuple[int, int, int]) -> Tuple[int, int, int]:
    """
    Get the complementary color.

    Args:
        color: RGB color tuple

    Returns:
        Complementary RGB color tuple
    """
    return (255 - color[0], 255 - color[1], 255 - color[2])