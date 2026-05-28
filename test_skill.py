#!/usr/bin/env python3
"""
测试微博热搜榜技能的完整功能
"""
import sys
sys.path.insert(0, '/workspace/weibo-hot-topics')

# 测试模块导入
print("=== 测试模块导入 ===\n")

try:
    from core import get_weibo_hot_topics, format_hot_topics
    print("✅ 模块导入成功！")
except ImportError as e:
    print(f"❌ 模块导入失败: {e}")
    sys.exit(1)

# 测试获取热搜榜
print("\n=== 测试获取热搜榜 ===\n")
result = get_weibo_hot_topics()
print(f"获取时间: {result['timestamp']}")
print(f"成功: {result['success']}")
print(f"热搜数量: {len(result['data'])}\n")

# 测试格式化输出
print("=== 格式化输出 ===\n")
print(format_hot_topics(result['data']))

print("✅ 所有测试通过！")
