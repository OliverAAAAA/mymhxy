# 开发人:
# 开发时间:2023/7/21 9:42
import autopy
from PIL import ImageGrab

if __name__ == '__main__':
    img_rgb = ImageGrab.grab()
    img_rgb.save('./test1.jpg', 'JPEG')  # 设置保存路径和图片格式
    width, height = autopy.screen.size()
    print(width, height)
    x = 1535
    y = 741
    autopy.mouse.smooth_move(100 * 1536 / 1920, 100 * 864 / 1080)
