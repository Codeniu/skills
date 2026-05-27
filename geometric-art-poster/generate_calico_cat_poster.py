#!/usr/bin/env python3
"""
生成三花猫咪主题的几何艺术海报
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from core.poster_builder import PosterBuilder
from core.theme_colors import ColorPalette, get_theme_colors


def generate_calico_cat_poster(output_path):
    """
    生成三花猫咪主题海报
    
    Args:
        output_path: 输出海报路径
    """
    # 创建三花猫咪配色方案（黑色、白色、橙色）
    calico_colors = ColorPalette(
        primary=(245, 130, 49),    # 橙色 - 三花猫的橘色部分
        secondary=(45, 45, 45),     # 深灰色/黑色 - 三花猫的黑色部分
        accent=(255, 255, 255),     # 白色 - 三花猫的白色部分
        background=(20, 20, 25),    # 深色背景
        text=(255, 255, 255),
        all_colors=[(245, 130, 49), (45, 45, 45), (255, 255, 255), (20, 20, 25), (255, 255, 255)]
    )
    
    # 创建海报生成器，使用抽象风格
    builder = PosterBuilder(width=800, height=1200, style="abstract")
    
    # 生成海报
    print("正在生成三花猫咪主题海报...")
    poster = builder.generate(
        theme="calico cat",
        colors=calico_colors,
        complexity=4,
        symmetry=True
    )
    
    # 保存海报
    builder.save(poster, output_path)
    print(f"海报已保存到: {output_path}")


if __name__ == "__main__":
    # 确保poster目录存在
    poster_dir = os.path.join(os.path.dirname(__file__), 'poster')
    os.makedirs(poster_dir, exist_ok=True)
    
    # 设置输出路径
    output_path = os.path.join(poster_dir, 'calico_cat_poster.png')
    
    # 生成海报
    generate_calico_cat_poster(output_path)
