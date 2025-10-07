# Thư viện cần thiết
import streamlit as st 

# Nội dung education
def write_education():
    st.write(
        """<hr style="border: 1px solid #ccc;">""", unsafe_allow_html=True
    )

    st.write(
        """
        ### 1. Trình độ chuyên môn hiện tại:
        + Trường: Đại học Quốc gia Hà Nội (VNU)
        + Chuyên ngành: Toán Tin và Khoa học dữ liệu (Computational Mathematics and Data Science)
        + Trình độ: Thạc sĩ định hướng nghiên cứu
        """
    )

    st.write(
    """
    ### 2. Timeline học vấn:
    <ul style="list-style-type: none; padding-left: 0;">
        <li style="position: relative; padding-left: 40px; margin-bottom: 20px;">
            <div style="background-color: #66CC66; padding: 10px; border-radius: 6px; position: relative;">
                <h4>2009 - 2010: Trường Tiểu học Minh Khai - Hà Nội</h4>
                <p>Học sinh tiểu học tại trường</p>
            </div>
            <div style="position: absolute; left: 0; top: 10px; width: 20px; height: 20px; border-radius: 50%; background-color: #00bfff;"></div>
            <div style="position: absolute; left: 9px; top: 18px; width: 2px; height: 100%; background-color: #00bfff;"></div>
        </li>
        <li style="position: relative; padding-left: 40px; margin-bottom: 20px;">
            <div style="background-color: #ADD8E6; padding: 10px; border-radius: 6px; position: relative;">
                <h4>2010 - 2014: Trường Tiểu học Tô Hoàng - Hà Nội</h4>
                <p>Học sinh lớp chuyên tiểu học tại trường</p>
            </div>
            <div style="position: absolute; left: 0; top: 10px; width: 20px; height: 20px; border-radius: 50%; background-color: #00bfff;"></div>
            <div style="position: absolute; left: 9px; top: 18px; width: 2px; height: 100%; background-color: #00bfff;"></div>
        </li>
        <li style="position: relative; padding-left: 40px; margin-bottom: 20px;">
            <div style="background-color: #FFD700; padding: 10px; border-radius: 6px; position: relative;">
                <h4>2014 - 2018: Trường THCS Ngô Gia Tự - Hà Nội</h4>
                <p>Học sinh trung học cơ sở tại trường</p>
            </div>
            <div style="position: absolute; left: 0; top: 10px; width: 20px; height: 20px; border-radius: 50%; background-color: #00bfff;"></div>
            <div style="position: absolute; left: 9px; top: 18px; width: 2px; height: 100%; background-color: #00bfff;"></div>
        </li>
        <li style="position: relative; padding-left: 40px; margin-bottom: 20px;">
            <div style="background-color: #FFA07A; padding: 10px; border-radius: 6px; position: relative;">
                <h4>2018 - 2021: Trường THPT Thăng Long - Hà Nội</h4>
                <p>Học sinh trung học phổ thông tại trường</p>
                <p>Thí sinh đạt giải khuyến khích đội tuyển Olympic Toán học cấp trường năm 2020</p>
                <ul style="margin-top: 0;">
                    <li>Lớp chuyên Tự Nhiên: ban T3 (Toán - Lý - Hóa - Sinh)</li>
                    <li>Khối xét tuyển: A01 (Toán - Lý - Anh)</li>
                    <li>Tổng điểm: 26.35/30.00</li>
                </ul>
            </div>
            <div style="position: absolute; left: 0; top: 10px; width: 20px; height: 20px; border-radius: 50%; background-color: #00bfff;"></div>
            <div style="position: absolute; left: 9px; top: 18px; width: 2px; height: 100%; background-color: #00bfff;"></div>
        </li>
        <li style="position: relative; padding-left: 40px; margin-bottom: 20px;">
            <div style="background-color: #006400; padding: 10px; border-radius: 6px; position: relative;">
                <h4>2021 - 2025: Trường Đại học Khoa học Tự nhiên - ĐHQGHN</h4>
                <p>Sinh viên ngành Toán tin tại trường</p>
                <p>Tam khoa đầu ra của ngành (top 3 cử nhân xuất sắc ngành Toán tin)</p>
                <ul style="margin-top: 0;">
                    <li>Chuyên ngành: Toán tin (Mathematics and Computer Science)</li>
                    <li>Trình độ: Cử nhân đại học</li>
                    <li>Tổng CPA: 3.43/4.00 (loại Giỏi)</li>
                    <li>Điểm rèn luyện: 92/100 (Xuất sắc)</li>
                </ul>
            </div>
            <div style="position: absolute; left: 0; top: 10px; width: 20px; height: 20px; border-radius: 50%; background-color: #00bfff;"></div>
            <div style="position: absolute; left: 9px; top: 18px; width: 2px; height: 100%; background-color: #00bfff;"></div>
        </li>
        <li style="position: relative; padding-left: 40px; margin-bottom: 20px;">
            <div style="background-color: #8A2BE2; padding: 10px; border-radius: 6px; position: relative;">
                <h4>2025 - nay: Đại học Quốc gia Hà Nội (VNU)</h4>
                <p>Học viên cao học ngành Khoa học dữ liệu tại trường</p>
                <ul style="margin-top: 0;">
                    <li>Chuyên ngành: Khoa học dữ liệu (Master in Data Science)</li>
                    <li>Trình độ: Thạc sĩ</li>
                </ul>
            </div>
            <div style="position: absolute; left: 0; top: 10px; width: 20px; height: 20px; border-radius: 50%; background-color: #00bfff;"></div>
            <div style="position: absolute; left: 9px; top: 18px; width: 2px; height: 100%; background-color: #00bfff;"></div>
        </li>
    </ul>
    """, unsafe_allow_html=True)