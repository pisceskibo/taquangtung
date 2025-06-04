# Thư viện cần thiết
from PIL import Image, ImageDraw
from datetime import datetime


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


# Tính toán số năm kinh nghiệm
def caculate_year_experience(time_space):
    start_time, end_time = time_space.split(" - ")

    start_datetime = datetime.strptime(start_time, "%m/%Y")
    if end_time == "nay":
        end_datetime = datetime.now()
    else:
        end_datetime = datetime.strptime(end_time, "%m/%Y")
    
    total_months = (end_datetime.year - start_datetime.year) * 12 + (end_datetime.month - start_datetime.month)

    # Chuyển đổi sang X năm Y tháng
    years = total_months // 12
    months = total_months % 12

    if years == 0:
        return f"{months} tháng"
    else:
        return f"{years} năm, {months} tháng"