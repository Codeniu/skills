#!/usr/bin/env python3
"""
测试微博热搜榜技能
"""
import sys
sys.path.insert(0, '/workspace/weibo-hot-topics')

from core import get_weibo_hot_topics, format_hot_topics

print("=== 测试微博热搜榜技能 ===\n")

# 测试获取热搜榜
result = get_weibo_hot_topics()
print(f"获取时间: {result['timestamp']}")
print(f"成功: {result['success']}")
print(f"热搜数量: {len(result['data'])}\n")

# 格式化输出
print(format_hot_topics(result['data']))
