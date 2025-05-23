# Thư viện cần thiết
import streamlit as st 

# Nội dung experience
def write_experience():
    st.write(
        """<hr style="border: 1px solid #ccc;">""", unsafe_allow_html=True
    )

    st.write(
        """
        ### 1. CLB MIM Media:
        + Chức vụ: Phó Chủ nhiệm CLB
        + Thời gian hoạt động: 10/2021 - 04/2025
        + Nhiệm vụ: Quản lý và tổ chức các hoạt động về mảng truyền thông của Khoa 
        """)
    st.image("image/mimmedia.jpg", caption="CLB MIM Media")

    st.write("""
        ### 2. CLB Toán Tin - HAMIC:
        + Chức vụ: Trưởng nhóm
        + Ban chuyên môn: Ban thiết kế và Lập trình Web
        + Thời gian hoạt động: 12/2022 - 08/2024
        + Nhiệm vụ: 
            + Thiết kế giao diện Website cho các đơn vị tổ chức
            + Tổ chức hoạt động giảng dạy những kỹ năng chuyên môn về Lập trình
            + Tổ chức cuộc thi Lập trình Web và Phân tích dữ liệu lớn
        """)
    st.image("image/hamic.jpg", caption="CLB Toán Tin - HAMIC")

    st.write(
        """
        ### 3. Khoa Toán - Cơ - Tin học:
        + Chức vụ: Ủy viên BCH Liên Chi Hội 
        + Thời gian hoạt động: 08/2023 - 01/2025
        + Nhiệm vụ: Thiết kế ấn phẩm và Đầu mối sự kiện
        """)
    st.image("image/mim.jpg", caption="Khoa Toán - Cơ - Tin học")

    st.write(
        """
        ### 4. Công ty Smartlog:
        + Chức vụ: Lập trình viên Python (Python Developer)
        + Thời gian: 12/2022 - 02/2023
        + Nhiệm vụ: 
            + Quản lý và phát triển thuật toán tối ưu hóa chiến lược định kỳ
            + Phân tích và xây dựng Website trực quan hóa dữ liệu
        """)
    st.image("image/smartlog.jpg", caption="Công ty Smartlog")

    st.write(
        """
        ### 5. Công ty Rikkeisoft:
        + Chức vụ: Lập trình viên Python (Python Developer)
        + Thời gian: 05/2024 - 09/2024
        + Nhiệm vụ: 
            + Phân tích và thiết kế hệ thống Website
            + Xây dựng và bảo trì dự án
        """)
    st.image("image/rikkei.jpg", caption="Công ty Rikkeisoft")

    st.write(
        """
        ### 6. Công ty GTS - Green Technology and System:
        + Chức vụ: Lập trình viên Python (Python Developer)
        + Thời gian: 12/2024 - nay
        + Nhiệm vụ: 
            + Phân tích và thiết kế hệ thống Window
            + Xây dựng và quản trị hệ thống dự án
        """)
    st.image("image/gtsystem.jpg", caption="Công ty GTS - Green Technology and System")
