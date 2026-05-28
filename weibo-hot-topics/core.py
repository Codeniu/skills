"""
微博热搜榜获取模块
使用真实 API 获取实时热搜数据
"""
import requests
from datetime import datetime
from typing import List, Dict


def get_weibo_hot_topics() -> Dict:
    """
    获取微博热搜榜前十的实时数据
    
    Returns:
        包含热搜信息的字典，格式如下：
        {
            "success": bool,
            "data": [
                {
                    "rank": int,
                    "title": str,
                    "hot": str,
                    "url": str,
                    "summary": str
                }
            ],
            "timestamp": str,
            "error": str (可选)
        }
    """
    API_URL = "https://v2.xxapi.cn/api/weibohot"
    
    try:
        # 调用 API 获取热搜数据
        response = requests.get(API_URL, timeout=15)
        response.raise_for_status()
        
        data = response.json()
        
        if data.get("code") != 200:
            return {
                "success": False,
                "data": [],
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "error": data.get("msg", "Unknown error")
            }
        
        # 解析数据，按热度排序（API 返回的数据通常已按 index 排序）
        hot_topics = []
        topics_data = data.get("data", [])
        
        # 取前十条热搜
        for i, item in enumerate(topics_data[:10]):
            rank = i + 1
            title = item.get("title", "")
            hot = str(item.get("hot", ""))
            # 生成微博搜索链接
            url = f"https://s.weibo.com/weibo?q={title}"
            # 生成摘要
            summary = generate_summary(title, rank)
            
            hot_topics.append({
                "rank": rank,
                "title": title,
                "hot": hot,
                "url": url,
                "summary": summary
            })
        
        return {
            "success": True,
            "data": hot_topics,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
    except Exception as e:
        return {
            "success": False,
            "data": get_mock_hot_topics(),
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "error": str(e)
        }


def get_mock_hot_topics() -> List[Dict]:
    """
    生成模拟的热搜数据（用于备用）
    
    Returns:
        模拟的热搜列表
    """
    mock_data = [
        {"rank": 1, "title": "AI大模型新突破", "hot": "5230000", "url": "https://s.weibo.com/hot", "summary": "🔥 热搜榜首：AI大模型新突破，全网关注度最高的话题！"},
        {"rank": 2, "title": "科技新品发布会", "hot": "3870000", "url": "https://s.weibo.com/hot", "summary": "✨ 热门话题：科技新品发布会，正在持续升温！"},
        {"rank": 3, "title": "体育赛事精彩瞬间", "hot": "2980000", "url": "https://s.weibo.com/hot", "summary": "✨ 热门话题：体育赛事精彩瞬间，正在持续升温！"},
        {"rank": 4, "title": "环保政策新动态", "hot": "2450000", "url": "https://s.weibo.com/hot", "summary": "📌 热搜话题：环保政策新动态，获得广泛关注。"},
        {"rank": 5, "title": "教育改革方案", "hot": "2120000", "url": "https://s.weibo.com/hot", "summary": "📌 热搜话题：教育改革方案，获得广泛关注。"},
        {"rank": 6, "title": "明星热门话题", "hot": "1890000", "url": "https://s.weibo.com/hot", "summary": "📢 热议话题：明星热门话题，引发网友讨论。"},
        {"rank": 7, "title": "经济发展趋势", "hot": "1670000", "url": "https://s.weibo.com/hot", "summary": "📢 热议话题：经济发展趋势，引发网友讨论。"},
        {"rank": 8, "title": "旅游推荐攻略", "hot": "1450000", "url": "https://s.weibo.com/hot", "summary": "📢 热议话题：旅游推荐攻略，引发网友讨论。"},
        {"rank": 9, "title": "健康养生知识", "hot": "1230000", "url": "https://s.weibo.com/hot", "summary": "📢 热议话题：健康养生知识，引发网友讨论。"},
        {"rank": 10, "title": "文化艺术展览", "hot": "1080000", "url": "https://s.weibo.com/hot", "summary": "📢 热议话题：文化艺术展览，引发网友讨论。"}
    ]
    return mock_data


def generate_summary(title: str, rank: int) -> str:
    """
    根据标题和排名生成摘要
    
    Args:
        title: 热搜标题
        rank: 排名
    
    Returns:
        摘要字符串
    """
    if not title:
        return "暂无摘要"
    
    if rank == 1:
        return f"🔥 热搜榜首：{title}，全网关注度最高的话题！"
    elif rank <= 3:
        return f"✨ 热门话题：{title}，正在持续升温！"
    elif rank <= 5:
        return f"📌 热搜话题：{title}，获得广泛关注。"
    elif rank <= 10:
        return f"📢 热议话题：{title}，引发网友讨论。"
    else:
        return f"📰 {title}"


def format_hot_topics(topics: List[Dict]) -> str:
    """
    格式化热搜榜为可读文本
    
    Args:
        topics: 热搜列表
    
    Returns:
        格式化后的字符串
    """
    if not topics:
        return "暂无热搜数据"
    
    result = "【微博热搜榜前十】\n\n"
    for topic in topics:
        result += f"{topic['rank']}. {topic['title']}\n"
        # 格式化热度显示
        hot = topic['hot']
        if hot and hot.isdigit():
            hot_num = int(hot)
            if hot_num >= 10000:
                hot = f"{hot_num/10000:.1f}万"
        result += f"   🔥 热度: {hot}\n"
        result += f"   💬 {topic['summary']}\n"
        if topic['url']:
            result += f"   🔗 {topic['url']}\n"
        result += "\n"
    
    return result


if __name__ == "__main__":
    # 测试代码
    result = get_weibo_hot_topics()
    print(format_hot_topics(result['data']))
