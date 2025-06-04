# Thư viện cần thiết
import streamlit as st 
from router.function import caculate_year_experience


# Nội dung experience
def write_experience():
    st.write(
        """<hr style="border: 1px solid #ccc;">""", unsafe_allow_html=True
    )

    time_space_mimmedia = "10/2021 - 04/2025"
    st.write(
        f"""
        ### 1. CLB MIM Media:
        + Chức vụ: Phó Chủ nhiệm CLB
        + Thời gian hoạt động: {time_space_mimmedia}
        + Kinh nghiệm: {caculate_year_experience(time_space_mimmedia)}
        + Nhiệm vụ: Quản lý và tổ chức các hoạt động về mảng truyền thông của Khoa 
        """)
    st.image("image/mimmedia.jpg", caption="CLB MIM Media")

    time_space_hamic = "12/2022 - 08/2024"
    st.write(
        f"""
        ### 2. CLB Toán Tin - HAMIC:
        + Chức vụ: Trưởng nhóm
        + Ban chuyên môn: Ban thiết kế và Lập trình Web
        + Thời gian hoạt động: {time_space_hamic}
        + Kinh nghiệm: {caculate_year_experience(time_space_hamic)}
        + Nhiệm vụ: 
            + Thiết kế giao diện Website cho các đơn vị tổ chức
            + Tổ chức hoạt động giảng dạy những kỹ năng chuyên môn về Lập trình
            + Tổ chức cuộc thi Lập trình Web và Phân tích dữ liệu lớn
        """)
    st.image("image/hamic.jpg", caption="CLB Toán Tin - HAMIC")

    time_space_mim = "08/2023 - 01/2025"
    st.write(
        f"""
        ### 3. Khoa Toán - Cơ - Tin học:
        + Chức vụ: Ủy viên BCH Liên Chi Hội 
        + Thời gian hoạt động: {time_space_mim}
        + Kinh nghiệm: {caculate_year_experience(time_space_mim)}
        + Nhiệm vụ: Thiết kế ấn phẩm và Đầu mối sự kiện
        """)
    st.image("image/mim.jpg", caption="Khoa Toán - Cơ - Tin học")

    time_space_smartlog = "12/2022 - 02/2023"
    st.write(
        f"""
        ### 4. Công ty Smartlog:
        + Chức vụ: Lập trình viên Python (Python Developer)
        + Thời gian: {time_space_smartlog}
        + Kinh nghiệm: {caculate_year_experience(time_space_smartlog)}
        + Nhiệm vụ: 
            + Quản lý và phát triển thuật toán tối ưu hóa chiến lược định kỳ
            + Phân tích và xây dựng Website trực quan hóa dữ liệu
        """)
    st.image("image/smartlog.jpg", caption="Công ty Smartlog")

    time_space_rikkeisoft = "05/2024 - 09/2024"
    st.write(
        f"""
        ### 5. Công ty Rikkeisoft:
        + Chức vụ: Lập trình viên Python (Python Developer)
        + Thời gian: {time_space_rikkeisoft}
        + Kinh nghiệm: {caculate_year_experience(time_space_rikkeisoft)}
        + Nhiệm vụ: 
            + Phân tích và thiết kế hệ thống Website
            + Xây dựng và bảo trì dự án
        """)
    st.image("image/rikkei.jpg", caption="Công ty Rikkeisoft")

    time_space_gtsystem = "12/2024 - nay"
    st.write(
        f"""
        ### 6. Công ty GTS - Green Technology and System:
        + Chức vụ: Lập trình viên Python (Python Developer)
        + Thời gian: {time_space_gtsystem}
        + Kinh nghiệm: {caculate_year_experience(time_space_gtsystem)}
        + Nhiệm vụ: 
            + Phân tích và thiết kế hệ thống Window
            + Xây dựng và quản trị hệ thống dự án
        """)
    st.image("image/gtsystem.jpg", caption="Công ty GTS - Green Technology and System")