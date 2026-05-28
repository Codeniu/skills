"""
Pixel Art Converter Skill

A skill that converts images to pixel art GIF animations with creative animation effects.
"""
from .handlers import ConversationHandler, ConversationState
from .core import (
    load_image,
    quantize_colors,
    resize_image,
    auto_calculate_resolution,
    create_pixel_art,
    analyze_image,
    generate_animation_description,
    create_animation_frames,
    save_gif,
    save_animated_gif,
    image_to_base64,
    frames_to_base64,
    get_image_info
)
from .utils import (
    is_valid_url,
    is_image_url,
    is_supported_format,
    validate_image_path
)


__version__ = "2.0.0"
__all__ = [
    "ConversationHandler",
    "ConversationState",
    "load_image",
    "quantize_colors",
    "resize_image",
    "auto_calculate_resolution",
    "create_pixel_art",
    "analyze_image",
    "generate_animation_description",
    "create_animation_frames",
    "save_gif",
    "save_animated_gif",
    "image_to_base64",
    "frames_to_base64",
    "get_image_info",
    "is_valid_url",
    "is_image_url",
    "is_supported_format",
    "validate_image_path"
]


def create_handler():
    """Create a new conversation handler instance."""
    return ConversationHandler()


def process_image(
    source: str,
    resolution: str = "auto",
    animation: str = "auto",
    output: str = "both",
    is_url: bool = False,
    output_dir: str = "./output"
):
    """
    Process an image directly without conversation flow.

    Args:
        source: Image file path or URL
        resolution: Resolution option ("16x16", "32x32", "64x64", "auto")
        animation: Animation type ("pulse", "glow", "rainbow", "twinkle", "breath", "shift", "auto")
        output: Output mode ("file", "base64", "both")
        is_url: Whether source is a URL
        output_dir: Output directory for file saving

    Returns:
        Dictionary with result data
    """
    resolution_map = {
        "16x16": (16, 16),
        "32x32": (32, 32),
        "64x64": (64, 64),
        "auto": None
    }

    auto_resize = resolution not in resolution_map or resolution_map[resolution] is None

    if not auto_resize:
        width, height = resolution_map[resolution]
    else:
        info = get_image_info(source, is_url)
        width, height = auto_calculate_resolution(info["width"], info["height"])

    pixel_art, actual_width, actual_height = create_pixel_art(
        source=source,
        width=width if not auto_resize else None,
        height=height if not auto_resize else None,
        is_url=is_url,
        auto_resize=auto_resize
    )
    
    frames, anim_description, duration = create_animation_frames(
        base_image=pixel_art,
        effect_type=animation,
        frame_count=12,
        duration=80
    )

    result = {
        "resolution": f"{actual_width}×{actual_height}",
        "colors": 256,
        "frame_count": len(frames),
        "animation_type": animation,
        "animation_description": anim_description,
        "file_path": None,
        "base64": None
    }

    if output in ("file", "both"):
        result["file_path"] = save_animated_gif(frames, duration=duration, output_dir=output_dir)

    if output in ("base64", "both"):
        result["base64"] = frames_to_base64(frames, duration=duration)

    return result
