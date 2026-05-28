"""
Utility functions for pixel art skill.
"""
import base64
import os
import re
from typing import Optional


def is_valid_url(url: str) -> bool:
    """
    Check if string is a valid URL.
    
    Args:
        url: String to check
        
    Returns:
        True if valid URL
    """
    url_pattern = re.compile(
        r'^https?://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'
        r'localhost|'
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
        r'(?::\d+)?'
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return url_pattern.match(url) is not None


def is_image_url(url: str) -> bool:
    """
    Check if URL points to an image.
    
    Args:
        url: URL to check
        
    Returns:
        True if likely an image URL
    """
    image_extensions = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
    return any(url.lower().endswith(ext) for ext in image_extensions)


def get_file_extension(filepath: str) -> str:
    """
    Get file extension from path.
    
    Args:
        filepath: File path
        
    Returns:
        Extension without dot (e.g., 'png')
    """
    return os.path.splitext(filepath)[1].lstrip('.').lower()


def is_supported_format(filename: str) -> bool:
    """
    Check if file format is supported.
    
    Args:
        filename: File name or path
        
    Returns:
        True if supported format
    """
    supported = ('png', 'jpg', 'jpeg', 'gif', 'bmp')
    return get_file_extension(filename) in supported


def validate_image_path(path: str) -> Optional[str]:
    """
    Validate image file path.
    
    Args:
        path: File path to validate
        
    Returns:
        Error message if invalid, None if valid
    """
    if not os.path.exists(path):
        return f"文件不存在: {path}"
    
    if not os.path.isfile(path):
        return f"路径不是文件: {path}"
    
    if not is_supported_format(path):
        return f"不支持的图片格式。支持: PNG, JPG, JPEG, GIF, BMP"
    
    return None


def encode_base64(data: bytes) -> str:
    """
    Encode bytes to base64 string.
    
    Args:
        data: Bytes to encode
        
    Returns:
        Base64 encoded string
    """
    return base64.b64encode(data).decode('utf-8')


def decode_base64(data: str) -> bytes:
    """
    Decode base64 string to bytes.
    
    Args:
        data: Base64 string to decode
        
    Returns:
        Decoded bytes
    """
    return base64.b64decode(data)


def truncate_base64(base64_str: str, max_length: int = 50) -> str:
    """
    Truncate base64 string for display.
    
    Args:
        base64_str: Base64 string
        max_length: Max display length
        
    Returns:
        Truncated string with ellipsis
    """
    if len(base64_str) <= max_length:
        return base64_str
    return base64_str[:max_length] + "..."


def format_file_size(size_bytes: int) -> str:
    """
    Format file size in human readable format.
    
    Args:
        size_bytes: Size in bytes
        
    Returns:
        Formatted string (e.g., '1.5 MB')
    """
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def ensure_output_dir(path: str = "./output") -> str:
    """
    Ensure output directory exists.
    
    Args:
        path: Directory path
        
    Returns:
        Absolute path to directory
    """
    os.makedirs(path, exist_ok=True)
    return os.path.abspath(path)
