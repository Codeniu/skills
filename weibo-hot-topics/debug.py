#!/usr/bin/env python3
"""
调试微博热搜榜技能
"""
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from typing import List, Dict

def get_mock_hot_topics() -> List[Dict]:
    """
    生成模拟的热搜数据（用于演示）
    
    Returns:
        模拟的热搜列表
    """
    mock_data = [
        {"rank": 1, "title": "AI大模型新突破", "hot": "523万", "url": "https://s.weibo.com/hot", "summary": "🔥 热搜榜首：AI大模型新突破，全网关注度最高的话题！"},
        {"rank": 2, "title": "科技新品发布会", "hot": "387万", "url": "https://s.weibo.com/hot", "summary": "✨ 热门话题：科技新品发布会，正在持续升温！"},
        {"rank": 3, "title": "体育赛事精彩瞬间", "hot": "298万", "url": "https://s.weibo.com/hot", "summary": "✨ 热门话题：体育赛事精彩瞬间，正在持续升温！"},
        {"rank": 4, "title": "环保政策新动态", "hot": "245万", "url": "https://s.weibo.com/hot", "summary": "📌 热搜话题：环保政策新动态，获得广泛关注。"},
        {"rank": 5, "title": "教育改革方案", "hot": "212万", "url": "https://s.weibo.com/hot", "summary": "📌 热搜话题：教育改革方案，获得广泛关注。"},
        {"rank": 6, "title": "明星热门话题", "hot": "189万", "url": "https://s.weibo.com/hot", "summary": "📢 热议话题：明星热门话题，引发网友讨论。"},
        {"rank": 7, "title": "经济发展趋势", "hot": "167万", "url": "https://s.weibo.com/hot", "summary": "📢 热议话题：经济发展趋势，引发网友讨论。"},
        {"rank": 8, "title": "旅游推荐攻略", "hot": "145万", "url": "https://s.weibo.com/hot", "summary": "📢 热议话题：旅游推荐攻略，引发网友讨论。"},
        {"rank": 9, "title": "健康养生知识", "hot": "123万", "url": "https://s.weibo.com/hot", "summary": "📢 热议话题：健康养生知识，引发网友讨论。"},
        {"rank": 10, "title": "文化艺术展览", "hot": "108万", "url": "https://s.weibo.com/hot", "summary": "📢 热议话题：文化艺术展览，引发网友讨论。"}
    ]
    return mock_data

def format_hot_topics(topics: List[Dict]) -> str:
    """
    格式化热搜榜为可读文本
    
    Args:
        topics: 热搜列表
    
    Returns:
        格式化后的文本
    """
    if not topics:
        return "暂无热搜数据"
    
    result = "【微博热搜榜前十】\n\n"
    for topic in topics:
        result += f"{topic['rank']}. {topic['title']}\n"
        result += f"   🔥 热度: {topic['hot']}\n"
        result += f"   💬 {topic['summary']}\n"
        if topic['url']:
            result += f"   🔗 {topic['url']}\n"
        result += "\n"
    
    return result

# 直接使用模拟数据
print("=== 微博热搜榜技能 (演示模式) ===")
print(format_hot_topics(get_mock_hot_topics()))
