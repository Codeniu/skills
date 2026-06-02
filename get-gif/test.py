"""
get-gif 技能测试文件
"""
from core import search_gifs, format_gifs


def test_search_gifs():
    """
    测试 GIF 搜索功能
    """
    print("=== 测试 GIF 搜索功能 ===\n")

    # 搜索 "girl" 相关的 GIF
    results = search_gifs("girl", max_results=3)

    if results:
        print(f"✓ 成功找到 {len(results)} 个 GIF\n")
        print(format_gifs(results, "markdown"))
    else:
        print("✗ 未找到 GIF 或搜索失败")


if __name__ == "__main__":
    test_search_gifs()
