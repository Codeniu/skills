"""
微博热搜榜技能
获取微博热搜榜前十的实时数据
"""
from .core import get_weibo_hot_topics, format_hot_topics, generate_summary

__all__ = [
    "get_weibo_hot_topics",
    "format_hot_topics",
    "generate_summary"
]

__version__ = "1.0.0"
