---
name: weibo-hot-topics
description: "获取微博热搜榜单，按热度排序。无需 API Key。使用真实 API 获取实时数据。"
license: MIT
homepage: https://v2.xxapi.cn
---

# 微博热搜榜技能

获取实时微博热搜榜单前十，按热度排序，**无需 API Key**。使用真实的 API 接口，包含标题、热度和智能摘要。

## 功能特性

- **实时获取**：从真实 API 获取当前微博热搜榜
- **智能排序**：按热度自动排序（热度高的在前）
- **完整信息**：包含热搜标题、热度值和智能摘要
- **简洁易用**：一键调用，快速返回结果
- **无需密钥**：API 无需认证即可使用

## 使用方法

```python
from weibo_hot_topics import get_weibo_hot_topics, format_hot_topics

# 获取热搜榜前十
result = get_weibo_hot_topics()
if result["success"]:
    print(format_hot_topics(result["data"]))
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
            "url": "https://s.weibo.com/weibo?q=热搜标题",
            "summary": "🔥 热搜榜首：热搜标题，全网关注度最高的话题！"
        },
        // ... 更多热搜
    ],
    "timestamp": "2026-05-28 12:00:00"
}
```

## API 说明

- **接口**: https://v2.xxapi.cn/api/weibohot
- **认证**: 无需 API Key
- **返回**: JSON 格式，包含 data 数组
- **字段**: 
  - `title`: 热搜标题
  - `hot`: 热度值（数字）

## 核心函数

### get_weibo_hot_topics()

获取微博热搜榜前十的实时数据。

**返回值**: 包含热搜信息的字典

### format_hot_topics(topics: List[Dict]) -> str

将热搜数据格式化为可读的文本。

**参数**:
- `topics`: 热搜列表

**返回值**: 格式化后的字符串

## 注意事项

- 有 API 调用频率限制
- 建议避免频繁调用
- 需要安装 `requests` 库

## 依赖

```bash
pip install requests>=2.31.0
```
