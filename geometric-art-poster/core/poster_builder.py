#!/usr/bin/env python3
"""
Poster Builder - Core module for generating geometric art posters.

This module combines the geometry generator and theme colors to create
beautiful geometric art posters based on user-provided themes.
"""

import random
import math
from pathlib import Path
from typing import Optional, Tuple, List

from PIL import Image

from .geometry_generator import GeometryGenerator
from .theme_colors import ColorPalette, get_theme_colors, generate_random_palette


class PosterBuilder:
    """Builder for creating geometric art posters."""

    def __init__(self, width: int = 800, height: int = 1200, style: str = "abstract"):
        """
        Initialize the poster builder.

        Args:
            width: Poster width in pixels (default: 800)
            height: Poster height in pixels (default: 1200)
            style: Art style - "abstract", "minimalist", "complex", "geometric"
        """
        self.width = width
        self.height = height
        self.style = style.lower()
        self.generator = GeometryGenerator(width, height)

    def generate(
        self,
        theme: str,
        colors: Optional[ColorPalette] = None,
        complexity: int = 3,
        symmetry: bool = True
    ) -> Image.Image:
        """
        Generate a geometric art poster based on the theme.

        Args:
            theme: User input theme string
            colors: Color palette to use (None = auto-generate based on theme)
            complexity: Complexity level (1-5, higher = more elements)
            symmetry: Enable symmetric composition

        Returns:
            PIL Image with the generated poster
        """
        if colors is None:
            colors = get_theme_colors(theme)
        
        frame = self.generator.create_frame(colors.background)
        
        shape_colors = [colors.primary, colors.secondary, colors.accent]
        
        if self.style == "minimalist":
            frame = self._generate_minimalist(frame, colors, complexity)
        elif self.style == "complex":
            frame = self._generate_complex(frame, colors, complexity, symmetry)
        elif self.style == "geometric":
            frame = self._generate_geometric(frame, colors, complexity, symmetry)
        else:
            frame = self._generate_abstract(frame, colors, complexity, symmetry)
        
        return frame

    def _generate_minimalist(
        self,
        frame: Image.Image,
        colors: ColorPalette,
        complexity: int
    ) -> Image.Image:
        """Generate a minimalist poster design."""
        shape_colors = [colors.primary, colors.accent]
        
        num_shapes = max(1, complexity)
        
        for i in range(num_shapes):
            shape_type = random.choice(["circle", "square", "triangle"])
            color = random.choice(shape_colors)
            
            if shape_type == "circle":
                radius = int(min(self.width, self.height) * (0.1 + i * 0.05))
                x = self.width // 2
                y = self.height // 2 + (i - num_shapes // 2) * 50
                frame = self.generator.draw_circle(frame, (x, y), radius, color)
            
            elif shape_type == "square":
                size = int(min(self.width, self.height) * (0.1 + i * 0.05))
                x = self.width // 2 + (i - num_shapes // 2) * 80
                y = self.height // 2
                rotation = 45 if i % 2 == 0 else 0
                frame = self.generator.draw_square(frame, (x, y), size, color, rotation=rotation)
            
            elif shape_type == "triangle":
                size = int(min(self.width, self.height) * (0.15 + i * 0.05))
                x = self.width // 2
                y = self.height // 2 + (i - num_shapes // 2) * 60
                points = [
                    (x, y - size // 2),
                    (x + size // 2, y + size // 2),
                    (x - size // 2, y + size // 2)
                ]
                frame = self.generator.draw_triangle(frame, points, color)
        
        return frame

    def _generate_complex(
        self,
        frame: Image.Image,
        colors: ColorPalette,
        complexity: int,
        symmetry: bool
    ) -> Image.Image:
        """Generate a complex, layered poster design."""
        shape_colors = [colors.primary, colors.secondary, colors.accent]
        
        frame = self.generator.draw_grid(frame, cell_size=50 + complexity * 10, 
                                        color=(100, 100, 100, 50), line_width=1)
        
        num_layers = complexity + 2
        
        for layer in range(num_layers):
            num_shapes = (layer + 1) * 3
            
            for _ in range(num_shapes):
                shape_type = random.choice(["circle", "triangle", "polygon", "square"])
                color = random.choice(shape_colors)
                size = int(min(self.width, self.height) * (0.05 + layer * 0.03))
                
                if symmetry:
                    x = self.width // 2 + random.randint(-self.width // 3, self.width // 3)
                    y = self.height // 2 + random.randint(-self.height // 3, self.height // 3)
                else:
                    x = random.randint(size, self.width - size)
                    y = random.randint(size, self.height - size)
                
                if shape_type == "circle":
                    frame = self.generator.draw_circle(frame, (x, y), size // 2, color)
                
                elif shape_type == "triangle":
                    points = [
                        (x, y - size // 2),
                        (x + size // 2, y + size // 2),
                        (x - size // 2, y + size // 2)
                    ]
                    frame = self.generator.draw_triangle(frame, points, color)
                
                elif shape_type == "polygon":
                    sides = random.randint(5, 8)
                    frame = self.generator.draw_polygon(frame, sides, (x, y), size // 2, 
                                                       color, rotation=random.randint(0, 360))
                
                elif shape_type == "square":
                    frame = self.generator.draw_square(frame, (x, y), size, color, 
                                                      rotation=random.randint(0, 45))
        
        frame = self.generator.draw_scattered_circles(frame, num_circles=20 + complexity * 5,
                                                      colors=shape_colors,
                                                      min_radius=5, max_radius=30)
        
        return frame

    def _generate_geometric(
        self,
        frame: Image.Image,
        colors: ColorPalette,
        complexity: int,
        symmetry: bool
    ) -> Image.Image:
        """Generate a geometric pattern-based poster design."""
        shape_colors = [colors.primary, colors.secondary, colors.accent]
        
        frame = self.generator.draw_grid(frame, cell_size=40, 
                                        color=(80, 80, 80, 30), line_width=1)
        
        grid_size = complexity + 2
        cell_w = self.width // grid_size
        cell_h = self.height // grid_size
        
        for i in range(grid_size):
            for j in range(grid_size):
                x = (i + 0.5) * cell_w
                y = (j + 0.5) * cell_h
                size = min(cell_w, cell_h) * 0.3
                
                if random.random() > 0.3:
                    shape_type = random.choice(["circle", "triangle", "square", "polygon"])
                    color = random.choice(shape_colors)
                    
                    if shape_type == "circle":
                        frame = self.generator.draw_circle(frame, (int(x), int(y)), 
                                                          int(size), color)
                    
                    elif shape_type == "triangle":
                        points = [
                            (x, y - size),
                            (x + size, y + size),
                            (x - size, y + size)
                        ]
                        frame = self.generator.draw_triangle(frame, points, color)
                    
                    elif shape_type == "square":
                        frame = self.generator.draw_square(frame, (int(x), int(y)), 
                                                          int(size * 1.5), color, 
                                                          rotation=45 if random.random() > 0.5 else 0)
                    
                    elif shape_type == "polygon":
                        sides = random.randint(5, 6)
                        frame = self.generator.draw_polygon(frame, sides, (int(x), int(y)), 
                                                           int(size), color, 
                                                           rotation=random.randint(0, 60))
        
        frame = self.generator.draw_concentric_circles(
            frame, 
            center=(self.width // 2, self.height // 2),
            max_radius=min(self.width, self.height) // 3,
            colors=shape_colors,
            spacing=20,
            fill=False
        )
        
        return frame

    def _generate_abstract(
        self,
        frame: Image.Image,
        colors: ColorPalette,
        complexity: int,
        symmetry: bool
    ) -> Image.Image:
        """Generate an abstract poster design."""
        shape_colors = [colors.primary, colors.secondary, colors.accent]
        
        frame = self.generator.draw_gradient(frame, colors.background, colors.primary, 
                                            direction="diagonal")
        
        frame = self.generator.draw_random_shapes(frame, num_shapes=5 + complexity * 3,
                                                  colors=shape_colors,
                                                  min_size=30, max_size=100)
        
        if symmetry:
            for _ in range(2 + complexity):
                center_x = self.width // 2
                center_y = self.height // 2
                size = random.randint(50, 200)
                
                frame = self.generator.draw_concentric_circles(
                    frame,
                    center=(center_x, center_y),
                    max_radius=size,
                    colors=shape_colors,
                    spacing=15,
                    fill=False
                )
        
        frame = self.generator.draw_scattered_circles(frame, num_circles=15 + complexity * 5,
                                                      colors=shape_colors,
                                                      min_radius=10, max_radius=60)
        
        for _ in range(3 + complexity):
            x1 = random.randint(0, self.width)
            y1 = random.randint(0, self.height)
            x2 = random.randint(0, self.width)
            y2 = random.randint(0, self.height)
            color = random.choice(shape_colors)
            frame = self.generator.draw_line(frame, (x1, y1), (x2, y2), color, width=2)
        
        return frame

    def save(self, image: Image.Image, output_path: str) -> dict:
        """
        Save the poster image to disk.

        Args:
            image: PIL Image to save
            output_path: Path to save the image (including filename)

        Returns:
            Dictionary with file info (path, size, dimensions)
        """
        output_path = Path(output_path)
        
        if not output_path.parent.exists():
            output_path.parent.mkdir(parents=True, exist_ok=True)
        
        if not output_path.suffix.lower() == ".png":
            output_path = output_path.with_suffix(".png")
        
        image.save(output_path, format="PNG")
        
        file_size_kb = output_path.stat().st_size / 1024
        file_size_mb = file_size_kb / 1024
        
        info = {
            "path": str(output_path),
            "size_kb": file_size_kb,
            "size_mb": file_size_mb,
            "dimensions": f"{self.width}x{self.height}",
            "format": "PNG"
        }
        
        print(f"\nPoster created successfully!")
        print(f"  Path: {output_path}")
        print(f"  Size: {file_size_kb:.1f} KB ({file_size_mb:.2f} MB)")
        print(f"  Dimensions: {self.width}x{self.height}")
        print(f"  Format: PNG")
        
        return info

    def set_dimensions(self, width: int, height: int):
        """
        Set new dimensions for the poster.

        Args:
            width: New width in pixels
            height: New height in pixels
        """
        self.width = width
        self.height = height
        self.generator = GeometryGenerator(width, height)

    def set_style(self, style: str):
        """
        Set the art style for the poster.

        Args:
            style: Art style - "abstract", "minimalist", "complex", "geometric"
        """
        self.style = style.lower()