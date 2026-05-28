"""
Conversation handler for pixel art skill with animation effects.
"""
from enum import Enum
from typing import Optional, Tuple
import tempfile
import os
import requests

from . import core
from . import utils


class ConversationState(Enum):
    """Conversation states."""
    WAITING_IMAGE = "waiting_image"
    WAITING_RESOLUTION = "waiting_resolution"
    WAITING_ANIMATION = "waiting_animation"
    WAITING_OUTPUT = "waiting_output"
    PROCESSING = "processing"
    DONE = "done"
    ERROR = "error"


class ConversationHandler:
    """Handler for conversation flow."""
    
    RESOLUTION_OPTIONS = {
        "1": (16, 16),
        "2": (32, 32),
        "3": (64, 64),
        "4": None
    }
    
    ANIMATION_OPTIONS = {
        "1": "pulse",
        "2": "glow",
        "3": "rainbow",
        "4": "twinkle",
        "5": "breath",
        "6": "shift",
        "7": "auto"
    }
    
    OUTPUT_OPTIONS = {
        "1": "file",
        "2": "base64",
        "3": "both"
    }
    
    def __init__(self):
        self.state = ConversationState.WAITING_IMAGE
        self.image_source: Optional[str] = None
        self.is_url: bool = False
        self.resolution: Optional[Tuple[int, int]] = None
        self.auto_resize: bool = False
        self.animation_type: str = "auto"
        self.output_mode: str = "both"
        self.image_info: Optional[dict] = None
        self.temp_file: Optional[str] = None
        self.error_message: Optional[str] = None
    
    def reset(self):
        """Reset handler to initial state."""
        if self.temp_file and os.path.exists(self.temp_file):
            os.remove(self.temp_file)
        
        self.state = ConversationState.WAITING_IMAGE
        self.image_source = None
        self.is_url = False
        self.resolution = None
        self.auto_resize = False
        self.animation_type = "auto"
        self.output_mode = "both"
        self.image_info = None
        self.temp_file = None
        self.error_message = None
    
    def get_welcome_message(self) -> str:
        """Get welcome message."""
        return """🎨 **像素画转换器（动效版）**

欢迎使用像素画转换器！我可以将您的图片转换为带有炫酷动效的像素画GIF。

**支持功能：**
- 📁 本地文件上传
- 🔗 网络图片URL
- 📐 多种分辨率选择
- ✨ 6种动效模式 + 自动选择
- 📦 保存文件和Base64输出

请提供图片（上传文件或输入URL）："""
    
    def get_resolution_prompt(self) -> str:
        """Get resolution selection prompt."""
        if self.auto_resize and self.image_info:
            ratio = self.image_info.get('ratio', 1)
            ratio_type = self.image_info.get('ratio_type', '')
            return f"""📐 **选择分辨率**

检测到图片比例：{ratio}（{ratio_type}）
建议使用自动模式。

请选择分辨率：
  1. 16×16（微型像素画）
  2. 32×32（经典像素画）
  3. 64×64（精细像素画）
  4. 自动（保留原始比例）⭐"""
        
        return """📐 **选择分辨率**

请选择目标分辨率：
  1. 16×16（微型像素画）
  2. 32×32（经典像素画）
  3. 64×64（精细像素画）
  4. 自动（保留原始比例）⭐"""
    
    def get_animation_prompt(self) -> str:
        """Get animation effect selection prompt."""
        res_str = f"{self.resolution[0]}×{self.resolution[1]}" if self.resolution else "自动"
        return f"""✨ **选择动效**

已选分辨率：{res_str}

请选择动效模式：
  1. 脉动（Pulse）- 呼吸般的明暗变化
  2. 发光（Glow）- 渐变的光效闪烁
  3. 彩虹（Rainbow）- 色彩轮回变换
  4. 闪烁（Twinkle）- 像素点随机闪烁
  5. 呼吸（Breath）- 缩放的呼吸效果
  6. 位移（Shift）- 左右移动
  7. 自动（AI分析图片后选择）⭐"""
    
    def get_output_prompt(self) -> str:
        """Get output mode selection prompt."""
        res_str = f"{self.resolution[0]}×{self.resolution[1]}" if self.resolution else "自动"
        anim_names = {
            "pulse": "脉动",
            "glow": "发光",
            "rainbow": "彩虹",
            "twinkle": "闪烁",
            "breath": "呼吸",
            "shift": "位移",
            "auto": "自动"
        }
        anim_str = anim_names.get(self.animation_type, self.animation_type)
        return f"""📦 **选择输出方式**

已选参数：
  📐 分辨率：{res_str}
  ✨ 动效：{anim_str}

请选择输出方式：
  1. 保存文件（保存到 output/ 目录）
  2. 返回 Base64（直接在响应中返回）
  3. 两者都要 ⭐"""
    
    def get_next_prompt(self) -> str:
        """Get the next prompt based on current state."""
        if self.state == ConversationState.WAITING_IMAGE:
            return self.get_welcome_message()
        elif self.state == ConversationState.WAITING_RESOLUTION:
            return self.get_resolution_prompt()
        elif self.state == ConversationState.WAITING_ANIMATION:
            return self.get_animation_prompt()
        elif self.state == ConversationState.WAITING_OUTPUT:
            return self.get_output_prompt()
        elif self.state == ConversationState.DONE:
            return self.get_success_message()
        elif self.state == ConversationState.ERROR:
            return self.get_error_message()
        return ""
    
    def get_success_message(self) -> str:
        """Get success message."""
        return "✅ 像素画动效转换完成！"
    
    def get_error_message(self) -> str:
        """Get error message."""
        return f"❌ 错误：{self.error_message}"
    
    def handle_message(self, message: str) -> Tuple[str, dict]:
        """
        Handle user message and return response.
        
        Args:
            message: User message
            
        Returns:
            Tuple of (response_text, state_data)
        """
        if self.state == ConversationState.DONE:
            self.reset()
            return self.get_welcome_message(), self._get_state_data()
        
        if self.state == ConversationState.ERROR:
            self.reset()
            return self.get_welcome_message(), self._get_state_data()
        
        if self.state == ConversationState.WAITING_IMAGE:
            return self._handle_image_input(message)
        elif self.state == ConversationState.WAITING_RESOLUTION:
            return self._handle_resolution_input(message)
        elif self.state == ConversationState.WAITING_ANIMATION:
            return self._handle_animation_input(message)
        elif self.state == ConversationState.WAITING_OUTPUT:
            return self._handle_output_input(message)
        
        return self.get_next_prompt(), self._get_state_data()
    
    def _handle_image_input(self, message: str) -> Tuple[str, dict]:
        """Handle image input."""
        message = message.strip()
        
        if utils.is_valid_url(message):
            if not utils.is_image_url(message):
                return "⚠️ 警告：URL可能不是图片链接，但我会尝试处理。请确认链接指向PNG、JPG、GIF等图片格式。", self._get_state_data()
            
            try:
                core.get_image_info(message, is_url=True)
                self.image_source = message
                self.is_url = True
                self.image_info = core.get_image_info(message, is_url=True)
                self.state = ConversationState.WAITING_RESOLUTION
                return self.get_resolution_prompt(), self._get_state_data()
            except Exception as e:
                self.error_message = f"无法加载图片：{str(e)}"
                self.state = ConversationState.ERROR
                return self.get_error_message(), self._get_state_data()
        
        if os.path.exists(message):
            error = utils.validate_image_path(message)
            if error:
                self.error_message = error
                self.state = ConversationState.ERROR
                return self.get_error_message(), self._get_state_data()
            
            try:
                self.image_source = message
                self.is_url = False
                self.image_info = core.get_image_info(message, is_url=False)
                self.state = ConversationState.WAITING_RESOLUTION
                return self.get_resolution_prompt(), self._get_state_data()
            except Exception as e:
                self.error_message = f"无法加载图片：{str(e)}"
                self.state = ConversationState.ERROR
                return self.get_error_message(), self._get_state_data()
        
        return "❌ 请提供有效的图片文件路径或URL。", self._get_state_data()
    
    def _handle_resolution_input(self, message: str) -> Tuple[str, dict]:
        """Handle resolution selection."""
        message = message.strip()
        
        if message not in self.RESOLUTION_OPTIONS:
            return "⚠️ 无效选项，请输入 1-4。", self._get_state_data()
        
        resolution = self.RESOLUTION_OPTIONS[message]
        
        if resolution is None:
            self.auto_resize = True
            self.resolution = core.auto_calculate_resolution(
                self.image_info['width'],
                self.image_info['height']
            )
        else:
            self.auto_resize = False
            self.resolution = resolution
        
        self.state = ConversationState.WAITING_ANIMATION
        return self.get_animation_prompt(), self._get_state_data()
    
    def _handle_animation_input(self, message: str) -> Tuple[str, dict]:
        """Handle animation selection."""
        message = message.strip()
        
        if message not in self.ANIMATION_OPTIONS:
            return "⚠️ 无效选项，请输入 1-7。", self._get_state_data()
        
        self.animation_type = self.ANIMATION_OPTIONS[message]
        self.state = ConversationState.WAITING_OUTPUT
        return self.get_output_prompt(), self._get_state_data()
    
    def _handle_output_input(self, message: str) -> Tuple[str, dict]:
        """Handle output mode selection."""
        message = message.strip()
        
        if message not in self.OUTPUT_OPTIONS:
            return "⚠️ 无效选项，请输入 1-3。", self._get_state_data()
        
        self.output_mode = self.OUTPUT_OPTIONS[message]
        self.state = ConversationState.PROCESSING
        
        return self._process_image()
    
    def _process_image(self) -> Tuple[str, dict]:
        """Process the image and generate animated output."""
        try:
            pixel_art, width, height = core.create_pixel_art(
                source=self.image_source,
                width=self.resolution[0] if not self.auto_resize else None,
                height=self.resolution[1] if not self.auto_resize else None,
                is_url=self.is_url,
                auto_resize=self.auto_resize
            )
            
            frames, anim_description, duration = core.create_animation_frames(
                base_image=pixel_art,
                effect_type=self.animation_type,
                frame_count=12,
                duration=80
            )
            
            result = {
                "resolution": f"{width}×{height}",
                "colors": 256,
                "frame_count": len(frames),
                "animation_type": self.animation_type,
                "animation_description": anim_description,
                "file_path": None,
                "base64": None
            }
            
            response_parts = []
            response_parts.append("✅ 像素画动效转换完成！")
            response_parts.append("")
            response_parts.append(f"📐 分辨率：{width}×{height}")
            response_parts.append(f"🎨 颜色数：256")
            response_parts.append(f"🎬 帧数：{len(frames)}")
            response_parts.append(f"✨ 动效：{anim_description}")
            response_parts.append("")
            
            if self.output_mode in ("file", "both"):
                filepath = core.save_animated_gif(
                    frames,
                    duration=duration,
                    output_dir="./output"
                )
                result["file_path"] = filepath
                response_parts.append(f"📁 文件路径：{filepath}")
            
            if self.output_mode in ("base64", "both"):
                b64 = core.frames_to_base64(frames, duration=duration)
                result["base64"] = b64
                truncated = utils.truncate_base64(b64, 50)
                response_parts.append(f"📦 Base64：{truncated}")
            
            self.state = ConversationState.DONE
            return "\n".join(response_parts), result
            
        except Exception as e:
            self.error_message = str(e)
            self.state = ConversationState.ERROR
            return self.get_error_message(), self._get_state_data()
    
    def _get_state_data(self) -> dict:
        """Get current state data."""
        return {
            "state": self.state.value,
            "image_source": self.image_source,
            "is_url": self.is_url,
            "resolution": self.resolution,
            "auto_resize": self.auto_resize,
            "animation_type": self.animation_type,
            "output_mode": self.output_mode,
            "image_info": self.image_info
        }
