"""
get-gif 技能
搜索和下载 GIF 动图
"""
from .core import search_gifs, format_gifs, get_gif_title

__all__ = [
    "search_gifs",
    "format_gifs",
    "get_gif_title"
]

__version__ = "1.0.2"
