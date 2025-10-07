# Thư viện cần thiết
import streamlit as st 

# Nội dung introduction
def write_introduction():
    st.write(
        """<hr style="border: 1px solid #ccc;">""", unsafe_allow_html=True
    )

    st.write(
    """
    ### 1. Tổng quan:
    <div style="text-align: justify;">
        Tôi là cử nhân chuyên ngành Toán Tin, có nền tảng vững chắc về Công nghệ Thông tin và đặc biệt 
        quan tâm đến lĩnh vực xây dựng phát triển phần mềm. Hiện tại, tôi cũng đang là học viên cao học
        trình độ Thạc sĩ Khoa học dữ liệu tại Đại học Quốc gia Hà Nội (VNU). Là người ham học hỏi, yêu thích 
        sáng tạo và luôn chủ động tìm kiếm giải pháp hiệu quả cho các vấn đề thực tiễn. Tôi có định hướng 
        trở thành Lập trình viên Python FullStack với khả năng phát triển ứng dụng đa lĩnh vực chuyên môn.
    </div>
    <br>

    ### 2. Thông tin chi tiết:
    + Họ và tên: Tạ Quang Tùng (Kibo)
    + Năm sinh: 06/03/2003
    + Quê quán: Hà Nội, Việt Nam
    + SĐT: 039 846 3203
    + Email: taquangtung2003@gmail.com

    ### 3. Giới thiệu chung (Overview):
    <table style="width: 100%; border: 1px solid black; border-collapse: collapse;">
            <tr style="background-color: #6699FF;">
                <th style="border: 1px solid black; padding: 8px; text-align: center;">Danh mục</th>
                <th style="border: 1px solid black; padding: 8px; text-align: center;">Mô tả</th>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 8px; text-align: center;">Học vấn (Education)</td>
                <td style="border: 1px solid black; padding: 8px; text-align: center;">Thông tin về quá trình học tập</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 8px; text-align: center;">Kinh nghiệm (Experience)</td>
                <td style="border: 1px solid black; padding: 8px; text-align: center;">Thông tin về các kinh nghiệm làm việc</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 8px; text-align: center;">Dự án (Projects)</td>
                <td style="border: 1px solid black; padding: 8px; text-align: center;">Danh sách các dự án đã thực hiện</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 8px; text-align: center;">Hoạt động (Activities)</td>
                <td style="border: 1px solid black; padding: 8px; text-align: center;">Thông tin về các hoạt động ngoại khóa</td>
            </tr>
            <tr>
                <td style="border: 1px solid black; padding: 8px; text-align: center;">Chứng chỉ (Certifications)</td>
                <td style="border: 1px solid black; padding: 8px; text-align: center;">Chứng chỉ và Giấy chứng nhận</td>
            </tr>
        </table>
    """, unsafe_allow_html=True
    )