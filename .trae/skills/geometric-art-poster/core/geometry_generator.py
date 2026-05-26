#!/usr/bin/env python3
"""
Geometry Generator - Module for generating geometric shapes and patterns.

This module provides utilities for drawing various geometric shapes including
circles, triangles, squares, polygons, lines, and abstract patterns for poster generation.
"""

import math
import random
from typing import Optional, Tuple, List

from PIL import Image, ImageDraw


class GeometryGenerator:
    """Generator for creating geometric shapes and patterns."""

    def __init__(self, width: int = 800, height: int = 1200):
        """
        Initialize the geometry generator.

        Args:
            width: Canvas width in pixels
            height: Canvas height in pixels
        """
        self.width = width
        self.height = height

    def create_frame(self, background_color: Tuple[int, int, int] = (255, 255, 255)) -> Image.Image:
        """
        Create a blank frame with solid color background.

        Args:
            background_color: RGB color tuple for the background

        Returns:
            PIL Image with solid background
        """
        return Image.new("RGB", (self.width, self.height), background_color)

    def draw_circle(
        self,
        frame: Image.Image,
        center: Tuple[int, int],
        radius: int,
        color: Tuple[int, int, int],
        outline_color: Optional[Tuple[int, int, int]] = None,
        outline_width: int = 0,
        fill: bool = True
    ) -> Image.Image:
        """
        Draw a circle on the frame.

        Args:
            frame: PIL Image to draw on
            center: (x, y) center position
            radius: Circle radius in pixels
            color: RGB fill color
            outline_color: RGB outline color (None for no outline)
            outline_width: Outline width in pixels
            fill: Whether to fill the circle

        Returns:
            Modified frame with circle
        """
        draw = ImageDraw.Draw(frame)
        x, y = center
        bbox = [x - radius, y - radius, x + radius, y + radius]
        draw.ellipse(bbox, fill=color if fill else None, outline=outline_color, width=outline_width)
        return frame

    def draw_triangle(
        self,
        frame: Image.Image,
        points: List[Tuple[int, int]],
        color: Tuple[int, int, int],
        outline_color: Optional[Tuple[int, int, int]] = None,
        outline_width: int = 0,
        fill: bool = True
    ) -> Image.Image:
        """
        Draw a triangle on the frame.

        Args:
            frame: PIL Image to draw on
            points: List of 3 (x, y) points defining the triangle
            color: RGB fill color
            outline_color: RGB outline color (None for no outline)
            outline_width: Outline width in pixels
            fill: Whether to fill the triangle

        Returns:
            Modified frame with triangle
        """
        draw = ImageDraw.Draw(frame)
        draw.polygon(points, fill=color if fill else None, outline=outline_color, width=outline_width)
        return frame

    def draw_square(
        self,
        frame: Image.Image,
        center: Tuple[int, int],
        size: int,
        color: Tuple[int, int, int],
        outline_color: Optional[Tuple[int, int, int]] = None,
        outline_width: int = 0,
        fill: bool = True,
        rotation: float = 0.0
    ) -> Image.Image:
        """
        Draw a square on the frame.

        Args:
            frame: PIL Image to draw on
            center: (x, y) center position
            size: Side length in pixels
            color: RGB fill color
            outline_color: RGB outline color (None for no outline)
            outline_width: Outline width in pixels
            fill: Whether to fill the square
            rotation: Rotation angle in degrees

        Returns:
            Modified frame with square
        """
        draw = ImageDraw.Draw(frame)
        x, y = center
        half_size = size / 2
        
        points = [
            (x - half_size, y - half_size),
            (x + half_size, y - half_size),
            (x + half_size, y + half_size),
            (x - half_size, y + half_size)
        ]
        
        if rotation != 0:
            angle_rad = math.radians(rotation)
            cos = math.cos(angle_rad)
            sin = math.sin(angle_rad)
            points = [
                (x + (px - x) * cos - (py - y) * sin,
                 y + (px - x) * sin + (py - y) * cos)
                for px, py in points
            ]
        
        draw.polygon(points, fill=color if fill else None, outline=outline_color, width=outline_width)
        return frame

    def draw_rectangle(
        self,
        frame: Image.Image,
        top_left: Tuple[int, int],
        width: int,
        height: int,
        color: Tuple[int, int, int],
        outline_color: Optional[Tuple[int, int, int]] = None,
        outline_width: int = 0,
        fill: bool = True
    ) -> Image.Image:
        """
        Draw a rectangle on the frame.

        Args:
            frame: PIL Image to draw on
            top_left: (x, y) top-left corner position
            width: Rectangle width
            height: Rectangle height
            color: RGB fill color
            outline_color: RGB outline color (None for no outline)
            outline_width: Outline width in pixels
            fill: Whether to fill the rectangle

        Returns:
            Modified frame with rectangle
        """
        draw = ImageDraw.Draw(frame)
        x, y = top_left
        bbox = [x, y, x + width, y + height]
        draw.rectangle(bbox, fill=color if fill else None, outline=outline_color, width=outline_width)
        return frame

    def draw_polygon(
        self,
        frame: Image.Image,
        sides: int,
        center: Tuple[int, int],
        radius: int,
        color: Tuple[int, int, int],
        outline_color: Optional[Tuple[int, int, int]] = None,
        outline_width: int = 0,
        fill: bool = True,
        rotation: float = 0.0
    ) -> Image.Image:
        """
        Draw a regular polygon on the frame.

        Args:
            frame: PIL Image to draw on
            sides: Number of sides (3+)
            center: (x, y) center position
            radius: Radius from center to vertices
            color: RGB fill color
            outline_color: RGB outline color (None for no outline)
            outline_width: Outline width in pixels
            fill: Whether to fill the polygon
            rotation: Rotation angle in degrees

        Returns:
            Modified frame with polygon
        """
        draw = ImageDraw.Draw(frame)
        x, y = center
        points = []
        
        for i in range(sides):
            angle = math.radians(rotation + (i * 360 / sides) - 90)
            px = x + radius * math.cos(angle)
            py = y + radius * math.sin(angle)
            points.append((px, py))
        
        draw.polygon(points, fill=color if fill else None, outline=outline_color, width=outline_width)
        return frame

    def draw_line(
        self,
        frame: Image.Image,
        start: Tuple[int, int],
        end: Tuple[int, int],
        color: Tuple[int, int, int],
        width: int = 1
    ) -> Image.Image:
        """
        Draw a line on the frame.

        Args:
            frame: PIL Image to draw on
            start: (x, y) start point
            end: (x, y) end point
            color: RGB line color
            width: Line width in pixels

        Returns:
            Modified frame with line
        """
        draw = ImageDraw.Draw(frame)
        draw.line([start, end], fill=color, width=width)
        return frame

    def draw_arc(
        self,
        frame: Image.Image,
        center: Tuple[int, int],
        radius: int,
        start_angle: float,
        end_angle: float,
        color: Tuple[int, int, int],
        width: int = 1
    ) -> Image.Image:
        """
        Draw an arc on the frame.

        Args:
            frame: PIL Image to draw on
            center: (x, y) center position
            radius: Arc radius
            start_angle: Start angle in degrees
            end_angle: End angle in degrees
            color: RGB arc color
            width: Line width in pixels

        Returns:
            Modified frame with arc
        """
        draw = ImageDraw.Draw(frame)
        x, y = center
        bbox = [x - radius, y - radius, x + radius, y + radius]
        draw.arc(bbox, start=start_angle, end=end_angle, fill=color, width=width)
        return frame

    def draw_grid(
        self,
        frame: Image.Image,
        cell_size: int,
        color: Tuple[int, int, int],
        line_width: int = 1
    ) -> Image.Image:
        """
        Draw a grid pattern on the frame.

        Args:
            frame: PIL Image to draw on
            cell_size: Size of each grid cell in pixels
            color: RGB grid line color
            line_width: Line width in pixels

        Returns:
            Modified frame with grid
        """
        draw = ImageDraw.Draw(frame)
        
        for x in range(0, self.width, cell_size):
            draw.line([(x, 0), (x, self.height)], fill=color, width=line_width)
        
        for y in range(0, self.height, cell_size):
            draw.line([(0, y), (self.width, y)], fill=color, width=line_width)
        
        return frame

    def draw_diagonal_lines(
        self,
        frame: Image.Image,
        spacing: int,
        color: Tuple[int, int, int],
        line_width: int = 1,
        direction: str = "down"
    ) -> Image.Image:
        """
        Draw diagonal line pattern on the frame.

        Args:
            frame: PIL Image to draw on
            spacing: Distance between parallel lines
            color: RGB line color
            line_width: Line width in pixels
            direction: "down" (top-left to bottom-right) or "up" (bottom-left to top-right)

        Returns:
            Modified frame with diagonal lines
        """
        draw = ImageDraw.Draw(frame)
        slope = 1 if direction == "down" else -1
        
        for offset in range(-self.height, self.width + self.height, spacing):
            if direction == "down":
                start = (offset, 0) if offset >= 0 else (0, -offset)
                end = (self.width, self.width - offset) if offset <= self.width else (offset + self.height, self.height)
            else:
                start = (offset, self.height) if offset >= 0 else (0, self.height - offset)
                end = (self.width, self.height - self.width + offset) if offset <= self.width else (offset + self.height, 0)
            
            draw.line([start, end], fill=color, width=line_width)
        
        return frame

    def draw_gradient(
        self,
        frame: Image.Image,
        start_color: Tuple[int, int, int],
        end_color: Tuple[int, int, int],
        direction: str = "vertical"
    ) -> Image.Image:
        """
        Draw a gradient over the frame.

        Args:
            frame: PIL Image to draw on
            start_color: RGB start color
            end_color: RGB end color
            direction: "vertical", "horizontal", or "diagonal"

        Returns:
            Modified frame with gradient
        """
        draw = ImageDraw.Draw(frame)
        r1, g1, b1 = start_color
        r2, g2, b2 = end_color
        
        if direction == "vertical":
            for y in range(self.height):
                ratio = y / self.height
                r = int(r1 * (1 - ratio) + r2 * ratio)
                g = int(g1 * (1 - ratio) + g2 * ratio)
                b = int(b1 * (1 - ratio) + b2 * ratio)
                draw.line([(0, y), (self.width, y)], fill=(r, g, b))
        
        elif direction == "horizontal":
            for x in range(self.width):
                ratio = x / self.width
                r = int(r1 * (1 - ratio) + r2 * ratio)
                g = int(g1 * (1 - ratio) + g2 * ratio)
                b = int(b1 * (1 - ratio) + b2 * ratio)
                draw.line([(x, 0), (x, self.height)], fill=(r, g, b))
        
        elif direction == "diagonal":
            max_dist = math.sqrt(self.width ** 2 + self.height ** 2)
            for y in range(self.height):
                for x in range(self.width):
                    dist = math.sqrt(x ** 2 + y ** 2)
                    ratio = dist / max_dist
                    r = int(r1 * (1 - ratio) + r2 * ratio)
                    g = int(g1 * (1 - ratio) + g2 * ratio)
                    b = int(b1 * (1 - ratio) + b2 * ratio)
                    draw.point((x, y), fill=(r, g, b))
        
        return frame

    def draw_random_shapes(
        self,
        frame: Image.Image,
        num_shapes: int,
        colors: List[Tuple[int, int, int]],
        min_size: int = 20,
        max_size: int = 150
    ) -> Image.Image:
        """
        Draw random geometric shapes on the frame.

        Args:
            frame: PIL Image to draw on
            num_shapes: Number of shapes to draw
            colors: List of RGB colors to use
            min_size: Minimum shape size
            max_size: Maximum shape size

        Returns:
            Modified frame with random shapes
        """
        shape_types = ["circle", "triangle", "square", "polygon"]
        
        for _ in range(num_shapes):
            shape_type = random.choice(shape_types)
            color = random.choice(colors)
            size = random.randint(min_size, max_size)
            x = random.randint(size, self.width - size)
            y = random.randint(size, self.height - size)
            
            if shape_type == "circle":
                self.draw_circle(frame, (x, y), size // 2, color)
            elif shape_type == "triangle":
                points = [
                    (x, y - size // 2),
                    (x + size // 2, y + size // 2),
                    (x - size // 2, y + size // 2)
                ]
                self.draw_triangle(frame, points, color)
            elif shape_type == "square":
                self.draw_square(frame, (x, y), size, color, rotation=random.randint(0, 45))
            elif shape_type == "polygon":
                sides = random.randint(5, 8)
                self.draw_polygon(frame, sides, (x, y), size // 2, color, rotation=random.randint(0, 360))
        
        return frame

    def draw_concentric_circles(
        self,
        frame: Image.Image,
        center: Tuple[int, int],
        max_radius: int,
        colors: List[Tuple[int, int, int]],
        spacing: int = 20,
        fill: bool = False
    ) -> Image.Image:
        """
        Draw concentric circles on the frame.

        Args:
            frame: PIL Image to draw on
            center: (x, y) center position
            max_radius: Maximum radius of outer circle
            colors: List of RGB colors to cycle through
            spacing: Distance between circle radii
            fill: Whether to fill circles

        Returns:
            Modified frame with concentric circles
        """
        for i, radius in enumerate(range(spacing, max_radius + 1, spacing)):
            color = colors[i % len(colors)]
            self.draw_circle(frame, center, radius, color, fill=fill)
        
        return frame

    def draw_scattered_circles(
        self,
        frame: Image.Image,
        num_circles: int,
        colors: List[Tuple[int, int, int]],
        min_radius: int = 10,
        max_radius: int = 80
    ) -> Image.Image:
        """
        Draw scattered circles of varying sizes on the frame.

        Args:
            frame: PIL Image to draw on
            num_circles: Number of circles to draw
            colors: List of RGB colors to use
            min_radius: Minimum circle radius
            max_radius: Maximum circle radius

        Returns:
            Modified frame with scattered circles
        """
        for _ in range(num_circles):
            radius = random.randint(min_radius, max_radius)
            x = random.randint(radius, self.width - radius)
            y = random.randint(radius, self.height - radius)
            color = random.choice(colors)
            alpha = random.randint(50, 200)
            
            overlay = Image.new("RGBA", (self.width, self.height), (0, 0, 0, 0))
            overlay_draw = ImageDraw.Draw(overlay)
            overlay_draw.ellipse(
                [x - radius, y - radius, x + radius, y + radius],
                fill=(color[0], color[1], color[2], alpha)
            )
            frame.paste(overlay, (0, 0), overlay)
        
        return frame