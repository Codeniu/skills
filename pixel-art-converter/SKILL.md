---
name: pixel-art-converter
description: A skill that converts images to pixel art style GIF animations with creative animation effects. Supports multiple resolution options and 6+ animation modes.
license: MIT
---

# Pixel Art Converter (Animation Edition)

A skill that transforms user-uploaded images into retro-style pixel art GIF animations with creative effects. Features multiple resolution options, automatic aspect ratio preservation, and 6+ animation modes.

## Features

- **Multiple input methods**: Local file upload and web image URL support
- **Resolution options**: 16×16, 32×32, 64×64, and auto mode
- **256-color palette**: Uses median cut algorithm for color quantization
- **6+ animation effects**: Pulse, Glow, Rainbow, Twinkle, Breath, Shift
- **AI-driven animation selection**: Analyzes image to suggest effects
- **Flexible output**: File save and Base64 encoding support
- **Conversational interface**: Smart guided workflow for users

## Resolution Options

| Option | Dimensions | Description |
|--------|------------|-------------|
| 1 | 16×16 | Micro pixel art |
| 2 | 32×32 | Classic pixel art |
| 3 | 64×64 | Detailed pixel art |
| 4 | Auto | Preserves original aspect ratio |

## Animation Effects

| Option | Effect Name | Description |
|--------|-------------|-------------|
| 1 | Pulse | Breathing brightness variation |
| 2 | Glow | Gradient light flickering |
| 3 | Rainbow | Color cycle transformation |
| 4 | Twinkle | Random pixel point sparkle |
| 5 | Breath | Zoom-in zoom-out effect |
| 6 | Shift | Horizontal movement |
| 7 | Auto | AI analyzes and chooses best effect |

## Core Workflow

```python
from pixel_skill import ConversationHandler

# 1. Create conversation handler
handler = ConversationHandler()

# 2. Get welcome message
response = handler.get_welcome_message()

# 3. Handle image input (file path or URL)
response, data = handler.handle_message("image.png")
# or
response, data = handler.handle_message("https://example.com/photo.jpg")

# 4. Handle resolution selection (1-4)
response, data = handler.handle_message("2")  # 32×32

# 5. Handle animation effect selection (1-7)
response, data = handler.handle_message("7")  # Auto mode

# 6. Handle output mode (1-3)
response, data = handler.handle_message("3")  # both file and base64
```

## Quick Start

```python
from pixel_skill import process_image

# Basic usage
result = process_image(
    source="image.png",
    resolution="auto",
    animation="auto",
    output="both"
)

print(result)
# {
#     "resolution": "32×32",
#     "colors": 256,
#     "frame_count": 12,
#     "animation_type": "glow",
#     "animation_description": "✨ 梦幻闪烁的星光 + 彩虹般的色彩轮回 + 强烈的明暗对比 ✨",
#     "file_path": "./output/pixel_art_animated_32x32_1234567.gif",
#     "base64": "R0lGODlhQABAAIYA..."
# }
```

## Available Utilities

### ConversationHandler

```python
from pixel_skill import ConversationHandler

handler = ConversationHandler()

# Get current prompt based on state
response = handler.get_next_prompt()

# Process user message
response, data = handler.handle_message("user input")

# Reset handler
handler.reset()
```

### Image Processing & Animation

```python
from pixel_skill import (
    create_pixel_art,
    analyze_image,
    generate_animation_description,
    create_animation_frames,
    save_animated_gif,
    save_gif,
    frames_to_base64,
    image_to_base64,
    auto_calculate_resolution,
    get_image_info
)

# Create pixel art
pixel_art, width, height = create_pixel_art(
    source="image.png",
    width=32,
    height=32,
    is_url=False,
    auto_resize=False
)

# Analyze image features
analysis = analyze_image(pixel_art)

# Generate animation description
description = generate_animation_description(analysis)

# Create animated frames
frames, desc, duration = create_animation_frames(
    base_image=pixel_art,
    effect_type="auto",  # or "pulse", "glow", "rainbow", etc.
    frame_count=12,
    duration=80
)

# Save animated GIF
filepath = save_animated_gif(frames, duration=duration, output_dir="./output")

# Convert animated frames to Base64
b64 = frames_to_base64(frames, duration=duration)
```

### Utility Functions

```python
from pixel_skill import (
    is_valid_url,
    is_image_url,
    is_supported_format,
    validate_image_path
)

# Validate URL
is_valid_url("https://example.com/image.png")  # True

# Check if image URL
is_image_url("https://example.com/photo.jpg")   # True

# Check file format
is_supported_format("image.png")               # True
is_supported_format("image.gif")                # True
is_supported_format("document.pdf")             # False
```

## Auto Resolution Mapping

The auto mode calculates optimal resolution while preserving aspect ratio:

| Original Ratio | Example | Calculated Resolution |
|----------------|---------|----------------------|
| 16:9 | 1920×1080 | 64×48 |
| 4:3 | 800×600 | 64×56 |
| 1:1 | 1000×1000 | 64×64 |
| 3:4 | 600×800 | 56×64 |
| 9:16 | 1080×1920 | 48×64 |

## Conversation States

| State | Description |
|-------|-------------|
| WAITING_IMAGE | Waiting for image input |
| WAITING_RESOLUTION | Waiting for resolution selection |
| WAITING_ANIMATION | Waiting for animation effect selection |
| WAITING_OUTPUT | Waiting for output mode selection |
| PROCESSING | Processing image |
| DONE | Complete |
| ERROR | Error occurred |

## Parameters

### process_image

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| source | str | required | Image file path or URL |
| resolution | str | "auto" | 16x16, 32x32, 64x64, auto |
| animation | str | "auto" | pulse, glow, rainbow, twinkle, breath, shift, auto |
| output | str | "both" | file, base64, both |
| is_url | bool | False | Whether source is URL |
| output_dir | str | "./output" | Output directory |

### ConversationHandler.handle_message

Returns `tuple[str, dict]`:
- `str`: Response message for user
- `dict`: State data with current context

## Error Handling

| Error | Handling |
|-------|----------|
| Invalid URL | Prompt user to check link |
| Unsupported format | List supported formats |
| Network timeout | Retry 2 times, then prompt |
| File not found | Prompt to check path |
| Processing failed | Return error message |

## Dependencies

```bash
pip install Pillow>=10.0.0 requests>=2.31.0
```
