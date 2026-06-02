"""
GIF 搜索和下载模块
使用 Tenor API 搜索 GIF 图片
"""
import requests
import argparse
import json
from typing import List, Dict


def search_gifs(query: str, max_results: int = 1, source: str = "auto") -> List[Dict]:
    """
    搜索 GIF 图片

    Args:
        query: 搜索关键词
        max_results: 最大结果数，默认为 1
        source: 搜索源（auto/tenor/giphy）

    Returns:
        包含 GIF 信息的字典列表
    """
    base_url = "https://api.tenor.com/v1/search"

    params = {
        "q": query,
        "key": "LIVDSRZULELA",
        "limit": max_results,
        "media_filter": "minimal"
    }

    try:
        response = requests.get(base_url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()

        results = []
        for result in data.get("results", []):
            media = result.get("media", [{}])[0] if result.get("media") else {}
            gif_data = media.get("gif", {})
            gif_info = {
                "id": result.get("id"),
                "title": result.get("title") or result.get("h1_title", ""),
                "url": result.get("url"),
                "preview_url": gif_data.get("url"),
                "tags": result.get("tags", []),
                "width": gif_data.get("width"),
                "height": gif_data.get("height")
            }
            results.append(gif_info)

        return results
    except Exception as e:
        print(f"搜索失败: {e}")
        return []


def get_gif_title(result: Dict, query: str = "") -> str:
    """
    获取 GIF 标题，如果标题为空则从标签或搜索关键词生成

    Args:
        result: GIF 信息字典
        query: 搜索关键词（可选）

    Returns:
        标题字符串
    """
    title = result.get("title", "")
    if title and title.strip():
        return title.strip()
    
    tags = result.get("tags", [])
    if tags:
        return " ".join(t.capitalize() for t in tags[:3])
    
    if query:
        return f"{query.title()} GIF"
    
    return "GIF 动图"


def format_gifs(results: List[Dict], output_format: str = "markdown", query: str = "") -> str:
    """
    格式化 GIF 搜索结果

    Args:
        results: GIF 结果列表
        output_format: 输出格式（markdown/json/url/title/id）
        query: 搜索关键词（可选）

    Returns:
        格式化后的字符串
    """
    if output_format == "json":
        return json.dumps(results, indent=2, ensure_ascii=False)
    elif output_format in ["url", "title", "id"]:
        return "\n".join([result.get(output_format, "") for result in results])
    else:
        output = []
        for i, result in enumerate(results, 1):
            title = get_gif_title(result, query)
            if len(results) > 1:
                output.append(f"## {i}. {title}")
            else:
                output.append(f"## {title}")
            output.append(f"![GIF]({result['preview_url']})")
            output.append(f"[查看原图]({result['url']})")
            if result['tags']:
                tags = ", ".join(result['tags'][:5])
                output.append(f"**标签:** {tags}")
            output.append("")
        return "\n".join(output)


def main():
    """
    主函数 - 命令行入口
    """
    parser = argparse.ArgumentParser(description="搜索和下载 GIF 动图")
    parser.add_argument("query", help="搜索关键词")
    parser.add_argument("--max", type=int, default=1, help="最大结果数，默认为 1")
    parser.add_argument("--json", action="store_true", help="以 JSON 格式输出")
    parser.add_argument("--format", choices=["url", "title", "id", "markdown"], help="输出格式")

    args = parser.parse_args()

    results = search_gifs(args.query, args.max)

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    elif args.format:
        print(format_gifs(results, args.format, args.query))
    else:
        print(format_gifs(results, "markdown", args.query))


if __name__ == "__main__":
    main()
