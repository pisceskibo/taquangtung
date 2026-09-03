# Thư viện cần thiết
import streamlit as st
import base64
import json


INTRODUCTION_DATASET = "datasets/introduction_data.json"

@st.cache_data
def load_introduction_data_json():
    with open(INTRODUCTION_DATASET, "r", encoding="utf-8") as f:
        return json.load(f)


# Nội dung Introduction
def write_introduction():
    # Load datasets
    information_data = load_introduction_data_json()
    info = information_data.get("general_information")
    categories = information_data.get("overview_categories")

    st.write("""<hr style="border: 1px solid #ccc;">""", unsafe_allow_html=True)

    # 1. Tổng quan:
    st.markdown("### 1. Tổng quan:")
    st.write(
    """
    <div style="text-align: justify;">
        Tôi là cử nhân chuyên ngành Toán Tin, có nền tảng vững chắc về Công nghệ Thông tin và đặc biệt 
        quan tâm đến lĩnh vực xây dựng phát triển phần mềm. Hiện tại, tôi cũng đang là học viên cao học
        trình độ Thạc sĩ Khoa học dữ liệu tại Đại học Quốc gia Hà Nội (VNU). Là người ham học hỏi, yêu thích 
        sáng tạo và luôn chủ động tìm kiếm giải pháp hiệu quả cho các vấn đề thực tiễn. Tôi có định hướng 
        trở thành Lập trình viên Python FullStack với khả năng phát triển ứng dụng đa lĩnh vực chuyên môn.
    </div>
    <br>
    """, unsafe_allow_html=True)

    # 2. Thông tin chi tiết:
    st.markdown("### 2. Thông tin chi tiết:")
    st.write(
        f"""
        + **Họ và tên:** {info.get("full_name")}
        + **Năm sinh:** {info.get("date_of_birth")}
        + **Quê quán:** {info.get("hometown_address")}
        + **SĐT:** {info.get("phone_number")}
        + **Email:** {info.get("email")}
        """
    )

    # 3. Giới thiệu chung:
    st.markdown("### 3. Giới thiệu chung (Overview):")
    table_rows = "".join(
        [
            f'<tr><td style="border: 1px solid black; padding: 8px; text-align: center;">{item.get("category")}</td>'
            f'<td style="border: 1px solid black; padding: 8px; text-align: center;">{item.get("description")}</td></tr>'
            for item in categories
        ]
    )

    table_html = f"""
    <table style="width: 100%; border: 1px solid black; border-collapse: collapse;">
        <tr style="background-color: #6699FF; color: white;">
            <th style="border: 1px solid black; padding: 8px; text-align: center;">Danh mục</th>
            <th style="border: 1px solid black; padding: 8px; text-align: center;">Mô tả</th>
        </tr>
        {table_rows}
    </table>
    """
    st.write(table_html, unsafe_allow_html=True)

    # Load CV JSON
    load_cv_path(info.get("cv_path"))

# Load CV
def load_cv_path(pdf_cv_file_path):
    with open(pdf_cv_file_path, "rb") as f:
        pdf_bytes = f.read()

    with st.expander("**👉 Xem CV trực tiếp**"):
        base64_pdf = base64.b64encode(pdf_bytes).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}#toolbar=0" width="100%" height="500" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

        st.download_button(
            label="📥 Download (PDF)",
            data=pdf_bytes,
            file_name="CV_TaQuangTung_Python.pdf",
            mime="application/pdf"
        )
