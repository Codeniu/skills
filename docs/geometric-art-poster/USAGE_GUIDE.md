# 几何艺术海报生成器 - 调用指南

## 一、技能概述

**几何艺术海报生成器**（Geometric Art Poster Generator）是一个基于 Python 的创意工具，能够根据用户输入的主题自动生成独特的几何艺术海报。该工具融合了色彩心理学与几何美学，为用户提供多样化的视觉体验。

## 二、环境准备

### 2.1 安装依赖

```bash
pip install pillow numpy
```

### 2.2 项目结构

```
geometric-art-poster/
├── core/
│   ├── poster_builder.py    # 海报构建器核心模块
│   ├── theme_colors.py      # 主题配色管理
│   └── geometry_generator.py # 几何图形生成器
├── poster/                  # 海报输出目录
└── requirements.txt         # 依赖清单
```

## 三、基础调用方式

### 3.1 快速入门

```python
from core.poster_builder import PosterBuilder

# 创建海报生成器实例
builder = PosterBuilder(width=800, height=1200, style="abstract")

# 生成海报
poster = builder.generate(
    theme="ocean sunset",    # 主题关键词
    complexity=3,            # 复杂度 1-5
    symmetry=True            # 是否对称构图
)

# 保存为 PNG
builder.save(poster, "my_poster.png")
```

### 3.2 调用流程图

```
用户输入主题 → 主题分析 → 配色方案匹配 → 几何图形生成 → 海报渲染 → 保存输出
```

## 四、核心 API 详解

### 4.1 PosterBuilder 类

**初始化参数：**

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| width | int | 800 | 海报宽度（像素） |
| height | int | 1200 | 海报高度（像素） |
| style | str | "abstract" | 艺术风格 |

**支持的艺术风格：**
- `abstract` - 抽象风格（默认）
- `minimalist` - 极简风格
- `complex` - 复杂风格
- `geometric` - 几何风格

### 4.2 generate() 方法

```python
def generate(
    self,
    theme: str,              # 主题关键词（必填）
    colors: ColorPalette = None,  # 自定义配色方案
    complexity: int = 3,     # 复杂度 1-5
    symmetry: bool = True    # 是否对称构图
) -> Image.Image
```

### 4.3 save() 方法

```python
def save(self, image: Image.Image, path: str) -> None
```

## 五、主题与配色方案

### 5.1 内置主题列表

| 主题类别 | 主题名称 | 关键词示例 |
|----------|----------|------------|
| 自然景观 | ocean, sea, water | 海洋、波浪、蓝色 |
| 天空时刻 | sunset, sunrise, dawn | 日落、日出、黄昏 |
| 森林植物 | forest, nature, garden | 森林、自然、花园 |
| 科技未来 | technology, digital, cyberpunk | 科技、数码、赛博朋克 |
| 神秘夜晚 | night, dark, mystery | 夜晚、黑暗、神秘 |
| 抽象艺术 | abstract, geometric | 抽象、几何 |
| 极简风格 | minimalist, clean | 极简、简洁 |
| 自然地貌 | desert, mountain | 沙漠、山脉 |
| 宇宙星空 | galaxy, space | 银河、太空 |
| 复古霓虹 | retro, neon | 复古、霓虹 |

### 5.2 自定义配色方案

```python
from core.theme_colors import ColorPalette

custom_colors = ColorPalette(
    primary=(245, 130, 49),    # 主色调
    secondary=(45, 45, 45),    # 次要色调
    accent=(255, 255, 255),    # 强调色
    background=(20, 20, 25),   # 背景色
    text=(255, 255, 255),      # 文字颜色
    all_colors=[...]           # 所有颜色列表
)

builder = PosterBuilder()
poster = builder.generate(theme="custom", colors=custom_colors)
```

## 六、调用示例

### 示例 1：生成海洋日落主题海报

```python
from core.poster_builder import PosterBuilder

builder = PosterBuilder(width=800, height=1200, style="abstract")
poster = builder.generate("ocean sunset", complexity=4, symmetry=True)
builder.save(poster, "poster/ocean_sunset.png")
```

### 示例 2：生成极简风格自然海报

```python
from core.poster_builder import PosterBuilder

builder = PosterBuilder(width=1024, height=1024, style="minimalist")
poster = builder.generate("nature", complexity=1)
builder.save(poster, "poster/minimal_nature.png")
```

### 示例 3：生成三花猫咪主题海报

```python
from core.poster_builder import PosterBuilder
from core.theme_colors import ColorPalette

# 自定义三花猫配色
calico_colors = ColorPalette(
    primary=(245, 130, 49),    # 橙色
    secondary=(45, 45, 45),    # 黑色
    accent=(255, 255, 255),    # 白色
    background=(20, 20, 25),   # 深色背景
    text=(255, 255, 255),
    all_colors=[(245, 130, 49), (45, 45, 45), (255, 255, 255), (20, 20, 25), (255, 255, 255)]
)

builder = PosterBuilder(width=800, height=1200, style="abstract")
poster = builder.generate("calico cat", colors=calico_colors, complexity=4, symmetry=True)
builder.save(poster, "poster/calico_cat_poster.png")
```

### 示例 4：生成赛博朋克风格海报

```python
from core.poster_builder import PosterBuilder

builder = PosterBuilder(width=1200, height=800, style="complex")
poster = builder.generate("cyberpunk", complexity=5, symmetry=False)
builder.save(poster, "poster/cyberpunk_wide.png")
```

## 七、输出格式说明

### 7.1 海报尺寸预设

| 类型 | 尺寸（宽×高） | 适用场景 |
|------|--------------|----------|
| 标准竖版 | 800 × 1200 | 海报、宣传图 |
| 正方形 | 1024 × 1024 | 社交媒体头像、封面 |
| 横版 | 1200 × 800 | 横幅、网页横幅 |

### 7.2 输出示例

```
Poster created successfully!
  Path: poster/calico_cat_poster.png
  Size: 110.1 KB (0.11 MB)
  Dimensions: 800x1200
  Format: PNG
```

## 八、常见问题

### Q1：主题不匹配怎么办？

如果输入的主题没有匹配到预设方案，系统会自动使用 `abstract` 主题作为默认配色。

### Q2：如何调整海报复杂度？

`complexity` 参数控制海报元素数量，取值范围 1-5：
- 1-2：简洁风格，适合极简设计
- 3：平衡风格，推荐默认值
- 4-5：复杂风格，元素丰富

### Q3：如何禁用对称构图？

设置 `symmetry=False` 即可生成非对称的随机构图。

### Q4：支持哪些输出格式？

目前仅支持 PNG 格式，未来将扩展支持 JPEG、SVG 等格式。

## 九、扩展开发

### 9.1 添加新主题

在 `core/theme_colors.py` 的 `THEME_COLORS` 字典中添加新条目：

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

### 9.2 添加新风格

在 `core/poster_builder.py` 中添加新的生成方法：

```python
def _generate_my_style(self, frame, colors, complexity, symmetry):
    # 实现自定义生成逻辑
    return frame
```

---

**文档版本**: v1.0  
**创建时间**: 2026年5月  
**适用范围**: geometric-art-poster skill
