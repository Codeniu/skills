---
name: weibo-hot-topics
description: 获取微博热搜榜前十的技能，返回标题和摘要信息
license: MIT
---

# 微博热搜榜技能

获取微博实时热搜榜前十的技能，包含标题和摘要信息，帮助用户快速了解当前热门话题。

## 功能特性

- **实时获取**：获取当前微博热搜榜前十
- **完整信息**：包含热搜标题、热度和摘要
- **简单易用**：一键调用，快速返回结果

## 使用方法

```python
from weibo_hot_topics import get_weibo_hot_topics

# 获取热搜榜前十
result = get_weibo_hot_topics()
print(result)
```

## 返回结果格式

```python
{
    "success": True,
    "data": [
        {
            "rank": 1,
            "title": "热搜标题",
            "hot": "热度值",
            "url": "链接",
            "summary": "摘要信息"
        },
        // ... 更多热搜
    ],
    "timestamp": "2026-05-28 12:00:00"
}
```

## 核心函数

### get_weibo_hot_topics()

获取微博热搜榜前十的实时数据。

**返回值**: 包含热搜信息的字典

## 依赖

```bash
pip install requests>=2.31.0 beautifulsoup4>=4.12.0
```
