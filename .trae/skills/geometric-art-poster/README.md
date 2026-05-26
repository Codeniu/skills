# 几何艺术海报生成器 Skill 说明文档

## 一、Skill 介绍

### 1.1 概述

**几何艺术海报生成器**（Geometric Art Poster Generator）是一个基于 Python 的创意工具，能够根据用户输入的主题自动生成独特的几何艺术海报。该工具融合了色彩心理学与几何美学，为用户提供多样化的视觉体验。

### 1.2 核心特性

| 特性 | 描述 |
|------|------|
| **主题感知** | 智能分析用户输入主题，自动匹配合适的配色方案 |
| **多风格支持** | 提供抽象、极简、复杂、几何四种艺术风格 |
| **高度可定制** | 支持调整海报尺寸、复杂度、对称性等参数 |
| **高质量输出** | 生成高分辨率 PNG 格式海报 |
| **丰富主题库** | 内置 20+ 种主题配色方案 |

### 1.3 技术架构

```
┌─────────────────────────────────────────────────────────────┐
│                    PosterBuilder (核心)                     │
│  ┌─────────────────┐    ┌─────────────────────────────┐    │
│  │ geometry_generator│    │      theme_colors          │    │
│  │  - 圆形绘制      │    │  - 主题关键词分析          │    │
│  │  - 三角形绘制    │    │  - 配色方案映射            │    │
│  │  - 多边形绘制    │    │  - 色彩混合算法            │    │
│  │  - 渐变/网格生成 │    │  - 互补色计算              │    │
│  └─────────────────┘    └─────────────────────────────┘    │
└─────────────────────────────────────────────────────────────┘
```

## 二、应用场景

### 2.1 创意设计

- **海报制作**：快速生成活动海报、展览海报
- **社交媒体配图**：为社交媒体帖子创建独特视觉内容
- **品牌素材**：为品牌活动生成宣传物料

### 2.2 艺术创作

- **灵感激发**：为艺术家提供创作灵感起点
- **概念验证**：快速验证设计概念和配色方案
- **数字艺术**：生成可用于展览的数字艺术作品

### 2.3 教育与学习

- **色彩理论学习**：通过可视化方式理解色彩搭配
- **几何图形教学**：展示几何图形的组合美学
- **编程实践**：学习 Python 图形编程和 PIL 库使用

### 2.4 商业应用

- **广告设计**：生成广告横幅和宣传图
- **产品包装**：设计产品包装的视觉元素
- **UI/UX 设计**：为应用界面生成背景图案

## 三、使用 SOLO 的创作过程

### 3.1 需求分析

用户需求：创建一个可以根据主题生成几何艺术海报的工具，输出 PNG 格式。

### 3.2 架构设计

1. **模块划分**：
   - `poster_builder.py`：核心控制器，协调各模块
   - `geometry_generator.py`：几何图形绘制引擎
   - `theme_colors.py`：主题配色方案管理

2. **设计原则**：
   - 单一职责：每个模块专注于一个功能
   - 可扩展性：支持添加新主题和新风格
   - 用户友好：简单直观的 API 接口

### 3.3 实现步骤

#### 步骤 1：创建目录结构

```powershell
New-Item -ItemType Directory -Force -Path "geometric-art-poster/core"
```

#### 步骤 2：编写主题颜色模块

创建 `theme_colors.py`，实现：
- `ColorPalette` 数据类定义
- 20+ 种预设主题配色方案
- 主题关键词分析算法
- 色彩混合与互补色计算

#### 步骤 3：编写几何图形生成器

创建 `geometry_generator.py`，实现：
- 基础图形绘制（圆形、三角形、方形、多边形）
- 图案生成（网格、对角线、渐变）
- 高级效果（同心圆、散射圆、随机形状）

#### 步骤 4：编写海报生成器核心

创建 `poster_builder.py`，实现：
- 四种艺术风格生成算法
- 主题到配色的映射
- 海报保存功能

#### 步骤 5：编写技能文档

创建 `SKILL.md`，记录：
- 功能说明
- 使用示例
- API 参考

### 3.4 测试验证

```python
from core.poster_builder import PosterBuilder

builder = PosterBuilder()
poster = builder.generate("ocean sunset")
builder.save(poster, "test.png")
```

## 四、调用步骤

### 4.1 环境准备

```bash
# 安装依赖
pip install pillow numpy
```

### 4.2 基础调用

```python
from core.poster_builder import PosterBuilder

# 创建生成器实例
builder = PosterBuilder(width=800, height=1200, style="abstract")

# 生成海报
poster = builder.generate(
    theme="ocean sunset",    # 主题关键词
    complexity=3,            # 复杂度 1-5
    symmetry=True            # 是否对称
)

# 保存为 PNG
builder.save(poster, "my_poster.png")
```

### 4.3 高级用法

#### 自定义配色方案

```python
from core.poster_builder import PosterBuilder
from core.theme_colors import ColorPalette

# 自定义配色
custom_colors = ColorPalette(
    primary=(255, 100, 150),
    secondary=(100, 200, 255),
    accent=(255, 255, 100),
    background=(10, 10, 20),
    text=(255, 255, 255),
    all_colors=[(255, 100, 150), (100, 200, 255), (255, 255, 100)]
)

builder = PosterBuilder(style="geometric")
poster = builder.generate("custom theme", colors=custom_colors)
builder.save(poster, "custom_poster.png")
```

#### 多种风格对比

```python
styles = ["abstract", "minimalist", "complex", "geometric"]
theme = "cyberpunk"

for style in styles:
    builder = PosterBuilder(style=style)
    poster = builder.generate(theme, complexity=4)
    builder.save(poster, f"{theme}_{style}.png")
```

### 4.4 可用主题列表

| 主题分类 | 关键词 |
|----------|--------|
| **自然景观** | ocean, sea, water, sunset, sunrise, forest, nature, mountain, desert |
| **科技未来** | technology, digital, cyberpunk, neon |
| **时间氛围** | night, dawn, dark, mystery |
| **艺术风格** | abstract, geometric, minimalist, retro, vintage, elegant, modern |
| **元素主题** | fire, ice, galaxy, space |

### 4.5 参数说明

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `width` | int | 800 | 海报宽度（像素） |
| `height` | int | 1200 | 海报高度（像素） |
| `style` | str | "abstract" | 艺术风格 |
| `theme` | str | - | 主题关键词（必填） |
| `complexity` | int | 3 | 复杂度（1-5） |
| `symmetry` | bool | True | 是否对称构图 |

## 五、输出示例

### 输入

```python
builder = PosterBuilder(width=800, height=1200, style="abstract")
poster = builder.generate("galaxy", complexity=4, symmetry=True)
builder.save(poster, "galaxy_poster.png")
```

### 输出

```
Poster created successfully!
  Path: galaxy_poster.png
  Size: 87.4 KB (0.09 MB)
  Dimensions: 800x1200
  Format: PNG
```

## 六、扩展指南

### 6.1 添加新主题

在 `theme_colors.py` 中的 `THEME_COLORS` 字典添加新条目：

```python
"my_theme": {
    "primary": (R, G, B),
    "secondary": (R, G, B),
    "accent": (R, G, B),
    "background": (R, G, B),
    "text": (R, G, B)
}
```

并在 `THEME_KEYWORDS` 中添加关联关键词：

```python
"my_theme": ["keyword1", "keyword2", "keyword3"]
```

### 6.2 添加新风格

在 `poster_builder.py` 中添加新的生成方法：

```python
def _generate_my_style(self, frame, colors, complexity, symmetry):
    # 实现自定义生成逻辑
    return frame
```

并在 `generate()` 方法中添加风格判断。

## 七、常见问题

### Q1：如何调整海报尺寸？

```python
builder = PosterBuilder(width=1024, height=1024)  # 正方形
builder = PosterBuilder(width=1200, height=800)   # 横版
```

### Q2：如何生成极简风格海报？

```python
builder = PosterBuilder(style="minimalist")
poster = builder.generate("nature", complexity=1)
```

### Q3：主题不匹配怎么办？

如果输入的主题没有匹配到预设方案，系统会自动使用 `abstract` 主题作为默认配色。

---

**文档版本**: v1.0  
**创建时间**: 2026年5月  
**适用范围**: geometric-art-poster skill