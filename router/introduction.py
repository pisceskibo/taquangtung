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
        Sinh viên năm cuối có đam mê và quan tâm đến lĩnh vực CNTT và phát triển phần mềm. Thuộc 
        tuýp người thích tìm tòi, sáng tạo và có những ý tưởng đột phá khi lên kế hoạch để giải
        quyết các vấn đề xung quanh công việc và cuộc sống hàng ngày. Có mong muốn định hướng 
        làm Kỹ sư phát triển phần mềm hoặc Lập trình viên Python FullStack.
    </div>
    <br>

    ### 2. Thông tin chi tiết:
    + Họ và tên: Tạ Quang Tùng (Kibo)
    + Năm sinh: 06/03/2003
    + Quê quán: Hà Nội, Việt Nam
    + SĐT: 039 846 3203
    + Email: taquangtung2003@gmail.com
    """, unsafe_allow_html=True
    )