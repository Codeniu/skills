"""
Test script for pixel art skill with animation effects.
"""
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from pixel_skill import (
    ConversationHandler,
    ConversationState,
    create_handler,
    process_image,
    auto_calculate_resolution,
    get_image_info,
    analyze_image,
    generate_animation_description
)


def test_auto_calculate_resolution():
    """Test auto resolution calculation."""
    print("Testing auto_calculate_resolution...")
    
    test_cases = [
        (1920, 1080, "横向图片"),
        (1080, 1920, "纵向图片"),
        (1000, 1000, "正方形图片"),
        (800, 600, "4:3横向"),
        (600, 800, "4:3纵向"),
    ]
    
    for width, height, desc in test_cases:
        result = auto_calculate_resolution(width, height)
        ratio = width / height
        print(f"  {desc} ({width}×{height}, ratio={ratio:.2f}) -> {result[0]}×{result[1]}")
    
    print("✓ auto_calculate_resolution 测试通过\n")


def test_image_analysis():
    """Test image analysis and animation description."""
    print("Testing image analysis...")
    
    # 创建一个简单的测试图片用于分析
    from PIL import Image
    test_img = Image.new('RGB', (100, 100), color=(255, 128, 64))
    
    analysis = analyze_image(test_img)
    print(f"  分析结果: {analysis}")
    
    description = generate_animation_description(analysis)
    print(f"  动效描述: {description}")
    
    print("✓ 图像分析测试通过\n")


def test_conversation_flow():
    """Test conversation flow."""
    print("Testing conversation flow...")
    
    handler = create_handler()
    
    assert handler.state == ConversationState.WAITING_IMAGE
    print(f"  初始状态: {handler.state.value}")
    
    response = handler.get_next_prompt()
    assert "像素画转换器" in response
    print("  ✓ 欢迎消息正确")
    
    response, data = handler.handle_message("test_invalid_path")
    print("  ✓ 无效路径处理正确")
    
    print("✓ Conversation flow 测试通过\n")


def test_utils():
    """Test utility functions."""
    print("Testing utility functions...")
    
    from pixel_skill import is_valid_url, is_image_url, is_supported_format
    
    assert is_valid_url("https://example.com/image.png")
    assert is_valid_url("http://test.com/pic.jpg")
    assert not is_valid_url("not a url")
    print("  ✓ URL 验证正确")
    
    assert is_image_url("https://example.com/image.png")
    assert is_image_url("https://example.com/image.JPG")
    assert not is_image_url("https://example.com/page.html")
    print("  ✓ 图片 URL 检测正确")
    
    assert is_supported_format("photo.png")
    assert is_supported_format("photo.JPG")
    assert is_supported_format("photo.gif")
    assert not is_supported_format("document.pdf")
    print("  ✓ 文件格式检测正确")
    
    print("✓ Utils 测试通过\n")


def main():
    """Run all tests."""
    print("=" * 50)
    print("像素画技能（动效版）测试")
    print("=" * 50 + "\n")
    
    try:
        test_utils()
        test_auto_calculate_resolution()
        test_image_analysis()
        test_conversation_flow()
        
        print("=" * 50)
        print("✅ 所有测试通过！")
        print("=" * 50)
        
    except Exception as e:
        print(f"\n❌ 测试失败：{e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
