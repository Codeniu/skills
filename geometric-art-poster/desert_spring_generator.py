#!/usr/bin/env python3
"""
荒漠清泉主题海报生成器

基于"荒漠清泉"主题生成独特的几何艺术海报，
融合沙漠的温暖色调和清泉的清凉色彩。
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from core.poster_builder import PosterBuilder
from core.theme_colors import get_theme_colors, mix_palettes, ColorPalette, THEME_COLORS


def create_desert_spring_palette() -> ColorPalette:
    """
    创建荒漠清泉主题的混合调色板
    结合沙漠的土黄色调和清泉的蓝绿色调
    """
    desert_colors = THEME_COLORS["desert"]
    water_colors = THEME_COLORS["ocean"]
    
    desert_palette = ColorPalette(
        primary=desert_colors["primary"],
        secondary=desert_colors["secondary"],
        accent=desert_colors["accent"],
        background=desert_colors["background"],
        text=desert_colors["text"],
        all_colors=[
            desert_colors["primary"],
            desert_colors["secondary"],
            desert_colors["accent"],
            desert_colors["background"],
            desert_colors["text"]
        ]
    )
    
    water_palette = ColorPalette(
        primary=water_colors["primary"],
        secondary=water_colors["secondary"],
        accent=water_colors["accent"],
        background=water_colors["background"],
        text=water_colors["text"],
        all_colors=[
            water_colors["primary"],
            water_colors["secondary"],
            water_colors["accent"],
            water_colors["background"],
            water_colors["text"]
        ]
    )
    
    return mix_palettes(desert_palette, water_palette, ratio=0.4)


def draw_desert_spring_composition(builder: PosterBuilder, colors: ColorPalette) -> any:
    """
    绘制荒漠清泉主题的独特构图
    使用几何形状表现沙漠与清泉的对比与融合
    """
    from PIL import Image, ImageDraw
    import random
    
    frame = builder.generator.create_frame(colors.background)
    
    shape_colors = [colors.primary, colors.secondary, colors.accent]
    
    # 绘制渐变背景，从底部沙漠色到顶部清泉色
    frame = builder.generator.draw_gradient(
        frame,
        start_color=colors.primary,
        end_color=colors.background,
        direction="vertical"
    )
    
    # 在底部绘制沙漠沙丘效果（三角形层叠）
    num_dunes = 5
    dune_heights = [frame.height * (0.85 - i * 0.08) for i in range(num_dunes)]
    dune_colors = [
        (180, 140, 80),  # 深沙色
        (200, 160, 100), # 中沙色
        (220, 180, 120), # 浅沙色
        (240, 200, 140), # 淡沙色
        (200, 150, 90),  # 温暖沙色
    ]
    
    for i in range(num_dunes):
        points = [
            (0, frame.height),
            (frame.width // 2 + (i - num_dunes // 2) * 100, int(dune_heights[i])),
            (frame.width, frame.height)
        ]
        frame = builder.generator.draw_triangle(frame, points, dune_colors[i])
    
    # 绘制清泉效果（圆形层叠，从中心向外扩散）
    spring_center_x = frame.width // 2
    spring_center_y = int(frame.height * 0.35)
    
    spring_colors = [
        (0, 180, 220),   # 清泉蓝
        (50, 200, 240),  # 浅清泉蓝
        (100, 220, 255), # 淡清泉蓝
        (150, 230, 255), # 极浅清泉蓝
    ]
    
    for i, radius in enumerate([80, 60, 40, 25]):
        frame = builder.generator.draw_circle(
            frame,
            (spring_center_x + random.randint(-20, 20), spring_center_y + random.randint(-10, 10)),
            radius,
            spring_colors[i % len(spring_colors)],
            fill=True
        )
    
    # 添加水波纹效果（弧线）
    for i in range(3):
        y_offset = spring_center_y + 100 + i * 30
        frame = builder.generator.draw_arc(
            frame,
            center=(spring_center_x, y_offset),
            radius=30 + i * 20,
            start_angle=180,
            end_angle=360,
            color=spring_colors[min(i, len(spring_colors) - 1)],
            width=2
        )
    
    # 添加几何装饰元素
    random.seed(42)  # 固定随机种子以保持一致性
    
    # 绘制分散的圆形代表沙粒
    for _ in range(30):
        x = random.randint(0, frame.width)
        y = random.randint(int(frame.height * 0.6), frame.height)
        radius = random.randint(2, 8)
        color = random.choice(dune_colors)
        frame = builder.generator.draw_circle(frame, (x, y), radius, color)
    
    # 绘制分散的圆形代表水珠
    for _ in range(20):
        x = random.randint(int(frame.width * 0.3), int(frame.width * 0.7))
        y = random.randint(int(frame.height * 0.2), int(frame.height * 0.6))
        radius = random.randint(3, 12)
        color = random.choice(spring_colors)
        frame = builder.generator.draw_circle(frame, (x, y), radius, color)
    
    # 添加对角线装饰（表现沙漠与清泉的交汇）
    for i in range(4):
        x1 = int(frame.width * (0.2 + i * 0.2))
        y1 = int(frame.height * 0.7)
        x2 = int(frame.width * (0.3 + i * 0.2))
        y2 = int(frame.height * 0.5)
        color = shape_colors[i % len(shape_colors)]
        frame = builder.generator.draw_line(frame, (x1, y1), (x2, y2), color, width=2)
    
    # 绘制多边形装饰（六边形代表和谐与完整）
    for i in range(3):
        center_x = int(frame.width * (0.3 + i * 0.2))
        center_y = int(frame.height * 0.15)
        size = 30 + i * 10
        color = shape_colors[(i + 1) % len(shape_colors)]
        frame = builder.generator.draw_polygon(
            frame,
            sides=6,
            center=(center_x, center_y),
            radius=size,
            color=color,
            rotation=i * 30
        )
    
    return frame


def generate_desert_spring_poster(
    output_path: str = "荒漠清泉_poster.png",
    width: int = 800,
    height: int = 1200
) -> dict:
    """
    生成荒漠清泉主题海报
    
    Args:
        output_path: 输出文件路径
        width: 海报宽度（像素）
        height: 海报高度（像素）
    
    Returns:
        包含生成信息的字典
    """
    print("正在生成『荒漠清泉』主题几何艺术海报...")
    print(f"主题描述: 沙漠与清泉的交融，温暖与清凉的碰撞")
    print()
    
    # 创建海报构建器
    builder = PosterBuilder(width=width, height=height, style="abstract")
    
    # 获取荒漠清泉混合调色板
    colors = create_desert_spring_palette()
    
    print("配色方案:")
    print(f"  主色 (Primary): {colors.primary}")
    print(f"  副色 (Secondary): {colors.secondary}")
    print(f"  强调色 (Accent): {colors.accent}")
    print(f"  背景色 (Background): {colors.background}")
    print()
    
    # 生成自定义构图
    poster = draw_desert_spring_composition(builder, colors)
    
    # 保存海报
    info = builder.save(poster, output_path)
    
    print()
    print("设计元素:")
    print("  ✓ 渐变背景 - 从清泉蓝渐变到沙漠土黄")
    print("  ✓ 三角形沙丘 - 多层次沙漠效果")
    print("  ✓ 圆形清泉 - 中心水源的柔和表现")
    print("  ✓ 水波纹 - 流动的泉水效果")
    print("  ✓ 分散装饰 - 沙粒与水珠的点缀")
    print("  ✓ 几何装饰 - 六边形与对角线的交汇")
    print("生成完成" * 1)
    
    return info


if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    # 生成标准竖版海报 (800x1200)
    output_file = "荒漠清泉_标准版.png"
    print("正在生成『荒漠清泉』主题海报...")
    print(f"尺寸: 800x1200 (竖版)")
    print()
    
    info = generate_desert_spring_poster(output_path=output_file, width=800, height=1200)
    
    print()
    print(f"✓ 输出文件: {info['path']}")
    print(f"✓ 文件大小: {info['size_kb']:.1f} KB")
    print(f"✓ 尺寸规格: {info['dimensions']}")
    print(f"✓ 图片格式: {info['format']}")
