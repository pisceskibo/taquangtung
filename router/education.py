# Thư viện cần thiết
import streamlit as st 

# Nội dung education
def write_education():
    st.write(
        """<hr style="border: 1px solid #ccc;">""", unsafe_allow_html=True
    )

    st.write(
        """
        ### 1. Trình độ hiện tại:
        + Trường: Đại học Khoa học Tự nhiên - ĐHQGHN
        + Chuyên ngành: Toán Tin (Mathematics and Computer Science)
        + GPA: 3.4/4.0 (Loại Giỏi)
        + Điểm rèn luyện: 93/100 (Xuất sắc)
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
                <p>Học sinh tiểu học tại trường</p>
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
                    <li>Lớp chuyên: ban T3 (Toán - Lý - Hóa - Sinh)</li>
                    <li>Khối xét tuyển: A01 (Toán - Lý - Anh)</li>
                    <li>Tổng điểm: 26.4/30</li>
                </ul>
            </div>
            <div style="position: absolute; left: 0; top: 10px; width: 20px; height: 20px; border-radius: 50%; background-color: #00bfff;"></div>
            <div style="position: absolute; left: 9px; top: 18px; width: 2px; height: 100%; background-color: #00bfff;"></div>
        </li>
        <li style="position: relative; padding-left: 40px; margin-bottom: 20px;">
            <div style="background-color: #006400; padding: 10px; border-radius: 6px; position: relative;">
                <h4>2021 - nay: Trường Đại học Khoa học Tự nhiên - ĐHQGHN</h4>
                <p>Sinh viên ngành Toán tin tại trường</p>
                <ul style="margin-top: 0;">
                    <li>Toán ứng dụng trong Khoa học máy tính và Tin học</li>
                    <li>Thiết kế thuật toán cho các sản phẩm App/Web</li>
                    <li>Xây dựng mô hình cho các bài toán tối ưu</li>
                </ul>
            </div>
            <div style="position: absolute; left: 0; top: 10px; width: 20px; height: 20px; border-radius: 50%; background-color: #00bfff;"></div>
            <div style="position: absolute; left: 9px; top: 18px; width: 2px; height: 100%; background-color: #00bfff;"></div>
        </li>
    </ul>
    """, unsafe_allow_html=True)
