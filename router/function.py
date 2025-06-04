# Thư viện cần thiết
from PIL import Image, ImageDraw

# Hàm để tạo ảnh hình tròn
def make_circle(image_path):
    img = Image.open(image_path).convert("RGBA")
    width, height = img.size
    mask = Image.new("L", (width, height), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, width, height), fill=255)
    result = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    result.paste(img, (0, 0), mask)
    return result
