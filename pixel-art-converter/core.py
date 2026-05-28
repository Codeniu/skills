"""
Core image processing module for pixel art conversion with animation effects.
"""
import io
import math
import random
import time
from typing import Optional, Tuple, List, Dict
import requests
from PIL import Image, ImageEnhance


def load_image(source: str, is_url: bool = False) -> Image.Image:
    """
    Load an image from file path or URL.
    
    Args:
        source: File path or URL
        is_url: Whether source is a URL
        
    Returns:
        PIL Image object
    """
    if is_url:
        response = requests.get(source, timeout=10)
        response.raise_for_status()
        image = Image.open(io.BytesIO(response.content))
    else:
        image = Image.open(source)
    
    if image.mode != 'RGB':
        image = image.convert('RGB')
    
    return image


def quantize_colors(image: Image.Image, colors: int = 256) -> Image.Image:
    """
    Quantize image colors using median cut algorithm.
    
    Args:
        image: Input PIL Image
        colors: Target number of colors (max 256)
        
    Returns:
        Quantized PIL Image
    """
    quantized = image.quantize(colors=colors, method=Image.Quantize.MEDIANCUT)
    return quantized.convert('RGB')


def resize_image(image: Image.Image, width: int, height: int) -> Image.Image:
    """
    Resize image to target dimensions using nearest neighbor for pixel art effect.
    
    Args:
        image: Input PIL Image
        width: Target width
        height: Target height
        
    Returns:
        Resized PIL Image
    """
    return image.resize((width, height), Image.Resampling.NEAREST)


def auto_calculate_resolution(original_width: int, original_height: int) -> Tuple[int, int]:
    """
    Calculate optimal resolution maintaining aspect ratio.
    Max total pixels: 4096 (64x64)
    
    Args:
        original_width: Original image width
        original_height: Original image height
        
    Returns:
        Tuple of (width, height)
    """
    max_pixels = 4096
    ratio = original_width / original_height
    
    if original_width >= original_height:
        target_width = int(math.sqrt(max_pixels * ratio))
        target_height = int(max_pixels / target_width)
    else:
        target_height = int(math.sqrt(max_pixels / ratio))
        target_width = int(max_pixels / target_height)
    
    target_width = max(8, min(64, target_width))
    target_height = max(8, min(64, target_height))
    
    target_width = (target_width // 8) * 8
    target_height = (target_height // 8) * 8
    
    if target_width < 8:
        target_width = 8
    if target_height < 8:
        target_height = 8
    
    return target_width, target_height


def analyze_image(image: Image.Image) -> Dict:
    """
    Analyze image features to generate appropriate animation effect.
    
    Args:
        image: Input PIL Image
        
    Returns:
        Dictionary with image analysis
    """
    img_array = list(image.getdata())
    width, height = image.size
    
    brightness_values = []
    colorfulness_values = []
    
    for r, g, b in img_array:
        brightness = (r + g + b) / 3
        brightness_values.append(brightness)
        
        max_rgb = max(r, g, b)
        min_rgb = min(r, g, b)
        colorfulness = max_rgb - min_rgb
        colorfulness_values.append(colorfulness)
    
    avg_brightness = sum(brightness_values) / len(brightness_values)
    avg_colorfulness = sum(colorfulness_values) / len(colorfulness_values)
    
    contrast = max(brightness_values) - min(brightness_values)
    
    dominant_r = sum(p[0] for p in img_array) / len(img_array)
    dominant_g = sum(p[1] for p in img_array) / len(img_array)
    dominant_b = sum(p[2] for p in img_array) / len(img_array)
    
    return {
        "brightness": avg_brightness,
        "colorfulness": avg_colorfulness,
        "contrast": contrast,
        "dominant_color": (dominant_r, dominant_g, dominant_b),
        "is_bright": avg_brightness > 128,
        "is_colorful": avg_colorfulness > 60
    }


def generate_animation_description(analysis: Dict) -> str:
    """
    Generate creative animation description based on image analysis.
    
    Args:
        analysis: Image analysis dictionary
        
    Returns:
        Creative animation description string
    """
    descriptions = []
    
    if analysis["is_bright"]:
        descriptions.append([
            "梦幻闪烁的星光",
            "发光的能量脉动",
            "闪烁的魔法光芒"
        ])
    else:
        descriptions.append([
            "神秘的阴影呼吸",
            "幽暗的灵魂微光",
            "深邃的宇宙脉动"
        ])
    
    if analysis["is_colorful"]:
        descriptions.append([
            "彩虹般的色彩轮回",
            "迷幻的色彩流动",
            "绚烂的色彩变换"
        ])
    else:
        descriptions.append([
            "简约的明暗渐变",
            "优雅的单色律动",
            "经典的黑白切换"
        ])
    
    if analysis["contrast"] > 80:
        descriptions.append([
            "强烈的明暗对比",
            "震撼的光影闪烁",
            "动感的对比度跃动"
        ])
    else:
        descriptions.append([
            "柔和的光影过渡",
            "舒缓的节奏变化",
            "平滑的渐入渐出"
        ])
    
    selected = [random.choice(d) for d in descriptions]
    return "✨ " + " + ".join(selected) + " ✨"


def create_animation_frames(
    base_image: Image.Image,
    effect_type: str = "auto",
    frame_count: int = 12,
    duration: int = 80
) -> Tuple[List[Image.Image], str, int]:
    """
    Create animation frames with various effects.
    
    Args:
        base_image: Base pixel art image
        effect_type: Type of animation effect
        frame_count: Number of frames in animation
        duration: Frame duration in milliseconds
        
    Returns:
        Tuple of (frames list, animation description, frame duration)
    """
    analysis = analyze_image(base_image)
    description = generate_animation_description(analysis)
    frames = []
    
    effects = {
        "pulse": _create_pulse_animation,
        "glow": _create_glow_animation,
        "shift": _create_shift_animation,
        "rainbow": _create_rainbow_animation,
        "breath": _create_breath_animation,
        "twinkle": _create_twinkle_animation
    }
    
    if effect_type == "auto":
        effect_type = random.choice(list(effects.keys()))
    
    if effect_type in effects:
        frames = effects[effect_type](base_image, frame_count, analysis)
    else:
        frames = _create_pulse_animation(base_image, frame_count, analysis)
    
    return frames, description, duration


def _create_pulse_animation(
    image: Image.Image,
    frame_count: int,
    analysis: Dict
) -> List[Image.Image]:
    frames = []
    for i in range(frame_count):
        intensity = (math.sin(i * 2 * math.pi / frame_count) + 1) / 2
        brightness = 0.6 + 0.4 * intensity
        enhancer = ImageEnhance.Brightness(image)
        frame = enhancer.enhance(brightness)
        frames.append(frame)
    return frames


def _create_glow_animation(
    image: Image.Image,
    frame_count: int,
    analysis: Dict
) -> List[Image.Image]:
    frames = []
    for i in range(frame_count):
        phase = i / frame_count
        brightness = 0.5 + 0.5 * math.sin(phase * 2 * math.pi)
        contrast = 1 + 0.3 * math.cos(phase * 2 * math.pi)
        
        frame = ImageEnhance.Brightness(image).enhance(brightness)
        frame = ImageEnhance.Contrast(frame).enhance(contrast)
        frames.append(frame)
    return frames


def _create_shift_animation(
    image: Image.Image,
    frame_count: int,
    analysis: Dict
) -> List[Image.Image]:
    frames = []
    width, height = image.size
    for i in range(frame_count):
        phase = i / frame_count
        shift = int(4 * math.sin(phase * 2 * math.pi))
        
        frame = Image.new('RGB', (width, height))
        frame.paste(image, (shift, 0))
        frames.append(frame)
    return frames


def _create_rainbow_animation(
    image: Image.Image,
    frame_count: int,
    analysis: Dict
) -> List[Image.Image]:
    frames = []
    for i in range(frame_count):
        frame = image.copy()
        pixels = frame.load()
        width, height = frame.size
        
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                
                hue_shift = (i / frame_count) * 255
                r = (r + int(hue_shift)) % 256
                g = (g + int(hue_shift * 0.7)) % 256
                b = (b + int(hue_shift * 0.5)) % 256
                
                pixels[x, y] = (r, g, b)
        
        frames.append(frame)
    return frames


def _create_breath_animation(
    image: Image.Image,
    frame_count: int,
    analysis: Dict
) -> List[Image.Image]:
    frames = []
    for i in range(frame_count):
        phase = i / frame_count
        scale = 1 + 0.05 * math.sin(phase * 2 * math.pi)
        
        width, height = image.size
        new_width = int(width * scale)
        new_height = int(height * scale)
        
        scaled = image.resize((new_width, new_height), Image.Resampling.NEAREST)
        
        frame = Image.new('RGB', (width, height))
        paste_x = (width - new_width) // 2
        paste_y = (height - new_height) // 2
        frame.paste(scaled, (paste_x, paste_y))
        
        frames.append(frame)
    return frames


def _create_twinkle_animation(
    image: Image.Image,
    frame_count: int,
    analysis: Dict
) -> List[Image.Image]:
    frames = []
    width, height = image.size
    
    twinkle_positions = []
    num_twinkles = min(10, width * height // 100)
    
    for _ in range(num_twinkles):
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)
        twinkle_positions.append((x, y))
    
    for i in range(frame_count):
        frame = image.copy()
        pixels = frame.load()
        
        for j, (x, y) in enumerate(twinkle_positions):
            if (i + j) % 2 == 0:
                if 0 <= x < width and 0 <= y < height:
                    r, g, b = pixels[x, y]
                    pixels[x, y] = (
                        min(255, r + 100),
                        min(255, g + 100),
                        min(255, b + 100)
                    )
        
        frames.append(frame)
    return frames


def create_pixel_art(
    source: str,
    width: Optional[int] = None,
    height: Optional[int] = None,
    is_url: bool = False,
    auto_resize: bool = False
) -> Tuple[Image.Image, int, int]:
    """
    Create pixel art from source image.
    
    Args:
        source: File path or URL
        width: Target width (None for auto)
        height: Target height (None for auto)
        is_url: Whether source is a URL
        auto_resize: Whether to auto-calculate resolution
        
    Returns:
        Tuple of (pixel_art_image, actual_width, actual_height)
    """
    image = load_image(source, is_url)
    
    if auto_resize or width is None or height is None:
        width, height = auto_calculate_resolution(image.width, image.height)
    
    resized = resize_image(image, width, height)
    pixel_art = quantize_colors(resized, colors=256)
    
    return pixel_art, width, height


def save_animated_gif(
    frames: List[Image.Image],
    duration: int = 80,
    output_dir: str = "./output"
) -> str:
    """
    Save list of frames as animated GIF.
    
    Args:
        frames: List of PIL Image frames
        duration: Frame duration in milliseconds
        output_dir: Output directory path
        
    Returns:
        Path to saved file
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = int(time.time())
    width, height = frames[0].size
    filename = f"pixel_art_animated_{width}x{height}_{timestamp}.gif"
    filepath = os.path.join(output_dir, filename)
    
    frames[0].save(
        filepath,
        format='GIF',
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0
    )
    
    return filepath


def save_gif(image: Image.Image, output_dir: str = "./output") -> str:
    """
    Save single frame as GIF file.
    
    Args:
        image: PIL Image to save
        output_dir: Output directory path
        
    Returns:
        Path to saved file
    """
    import os
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = int(time.time())
    filename = f"pixel_art_{image.width}x{image.height}_{timestamp}.gif"
    filepath = os.path.join(output_dir, filename)
    
    image.save(filepath, format='GIF')
    return filepath


def image_to_base64(image: Image.Image) -> str:
    """
    Convert PIL Image to base64 encoded string.
    
    Args:
        image: PIL Image to convert
        
    Returns:
        Base64 encoded string
    """
    buffer = io.BytesIO()
    image.save(buffer, format='GIF')
    buffer.seek(0)
    
    import base64
    return base64.b64encode(buffer.getvalue()).decode('utf-8')


def frames_to_base64(frames: List[Image.Image], duration: int = 80) -> str:
    """
    Convert animated GIF frames to base64 encoded string.
    
    Args:
        frames: List of PIL Image frames
        duration: Frame duration in milliseconds
        
    Returns:
        Base64 encoded string
    """
    buffer = io.BytesIO()
    
    frames[0].save(
        buffer,
        format='GIF',
        save_all=True,
        append_images=frames[1:],
        duration=duration,
        loop=0
    )
    
    buffer.seek(0)
    
    import base64
    return base64.b64encode(buffer.getvalue()).decode('utf-8')


def get_image_info(source: str, is_url: bool = False) -> dict:
    """
    Get basic information about an image.
    
    Args:
        source: File path or URL
        is_url: Whether source is a URL
        
    Returns:
        Dictionary with image info
    """
    image = load_image(source, is_url)
    
    ratio = round(image.width / image.height, 2)
    if ratio > 1:
        ratio_type = "横向"
    elif ratio < 1:
        ratio_type = "纵向"
    else:
        ratio_type = "正方形"
    
    return {
        "width": image.width,
        "height": image.height,
        "ratio": ratio,
        "ratio_type": ratio_type,
        "format": image.format,
        "mode": image.mode
    }
