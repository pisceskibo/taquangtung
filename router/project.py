# Thư viện cần thiết
import streamlit as st 

# Nội dung projects
def write_project():
    st.write("""<hr style="border: 1px solid #ccc;">""", unsafe_allow_html=True)

    st.write(
        """ 
        <div style="text-align: center;">
            <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=pisceskibo&theme=radical&hide_border=false&include_all_commits=false&count_private=false&layout=compact" alt="Most Used Languages" style="width: 70%;">
        </div>
        """, unsafe_allow_html=True)

    st.write("""> Link chi tiết: https://github.com/pisceskibo""")
    st.write("<br>", unsafe_allow_html=True)

    # Bố cục CARD điều hướng lựa chọn LOGIC TOGGLE (MỞ/ĐÓNG)
    if "selected_project_type" not in st.session_state:
        st.session_state.selected_project_type = None

    card_col1, card_col2 = st.columns(2)

    with card_col1:
        with st.container(border=True):
            st.markdown("### 🗂️ DỰ ÁN THỰC TẾ")
            st.caption("Hệ thống quy mô lớn được triển khai trong môi trường thực tế tại các công ty doanh nghiệp.")
            label_company = "Thu gọn danh mục ↩" if st.session_state.selected_project_type == "company" else "Khám phá Company Projects ↗"
            
            if st.button(label_company, use_container_width=True, type="primary" if st.session_state.selected_project_type == "company" else "secondary"):
                if st.session_state.selected_project_type == "company":
                    st.session_state.selected_project_type = None
                else:
                    st.session_state.selected_project_type = "company"
                st.rerun()

    with card_col2:
        with st.container(border=True):
            st.markdown("### 🗂️ DỰ ÁN CÁ NHÂN")
            st.caption("Các ứng dụng độc lập, giải thuật thông minh và sản phẩm dự án cá nhân mang tính thực tế.")
            label_personal = "Thu gọn danh mục ↩" if st.session_state.selected_project_type == "personal" else "Khám phá Personal Projects ↗"
            
            if st.button(label_personal, use_container_width=True, type="primary" if st.session_state.selected_project_type == "personal" else "secondary"):
                if st.session_state.selected_project_type == "personal":
                    st.session_state.selected_project_type = None
                else:
                    st.session_state.selected_project_type = "personal"
                st.rerun()

    st.write("<hr>", unsafe_allow_html=True)

    if st.session_state.selected_project_type == "company":
        get_company_project()
    elif st.session_state.selected_project_type == "personal":
        get_personal_projects()
    else:
        st.markdown("<p style='text-align: center; font-style: italic;'>💡 Bấm vào một trong hai thẻ danh mục phía trên để xem danh sách dự án chi tiết.</p>", unsafe_allow_html=True)


# Thông tin dữ liệu các dự án
def get_personal_projects():
    st.write(
        """
        ## 🗃️ PERSONAL PROJECTS
        >> *Dưới đây là các dự án cá nhân được triển khai trong môi trường thực tế.*
        
        ---
        
        ### 1. BOOK MANAGEMENT APP:
        + Project: Thiết kế giao diện phần mềm quản lý sách 
        + Programming Language: Python
        + Framework: Tkinter
        + Link mô tả: https://github.com/pisceskibo/BookManagement 

        ---

        ### 2. DOCUMENT MANAGEMENT:
        + Project: Hệ thống quản lý tài liệu Document
        + Programming Language: Python, HTML, CSS, JavaScript
        + Framework: Django
        + Link mô tả: https://github.com/pisceskibo/ManagerDocument 

        ---

        ### 3. LIBRARY MANAGEMENT:
        + Project: Hệ thống quản lý thư viện tài liệu điện tử số
        + Programming Language: Python, HTML, CSS, JavaScript
        + Framework: FastAPI, Tkinter, Streamlit
        + Link mô tả: https://github.com/pisceskibo/LibraryManagement 

        ---

        ### 4. TIME CHECKING:
        + Project: Hệ thống chấm công theo yêu cầu
        + Programming Language: Python
        + Framework: FastAPI
        + Link mô tả: https://github.com/pisceskibo/TimeChecking 

        ---

        ### 5. SUDOKU GAME:
        + Project: Mô hình hóa các phiên bản game Sudoku
        + Programming Language: Python
        + Thư viện: PuLP, Gurobipy
        + Link mô tả: https://github.com/pisceskibo/SudokuGame

        ---

        ### 6. CREDIT CARD APPROVAL PREDICTION:
        + Project: Hệ thống phân tích và dự đoán mô hình phê duyệt thẻ tín dụng ngân hàng
        + Programming Language: Python, Cython
        + Framework: Streamlit
        + Link mô tả: https://github.com/pisceskibo/CreditCardApprovalPrediction

        ---

        ### 7. OCR DOCUMENT SYSTEM:
        + Project: Hệ thống trích xuất dữ liệu Document OCR
        + Programming Language: Python, HTML, CSS
        + Framework: Pyramid
        + Link mô tả: https://github.com/pisceskibo/SystemDocumentOCR

        ---
        
        ### 8. SENTIMENT ANALYSIS SYSTEM:
        + Project: Hệ thống phân tích cảm xúc bình luận
        + Programming Language: Python, VueJS, CSS, JavaScript
        + Framework: Flask
        + Link mô tả: https://github.com/pisceskibo/SentimentAnalysisSystem
        """
    )

def get_company_project():
    st.write(
        """
        ## 🗃️ COMPANY PROJECTS
        >> *Dưới đây là các hệ thống quy mô lớn đã được triển khai trong môi trường doanh nghiệp thực tế.*

        ---
        
        ### 1. SOCIAL ACCOUNT MANAGEMENT:
        + Project: Hệ thống quản lý thông tin mạng xã hội
        + Role: Python Developer
        + Programming Language: Python, HTML, CSS, JavaScript
        + Framework: Flask
        + Description & Result: Thiết kế hệ thống tổng hợp dữ liệu tài khoản mạng xã hội và tạo báo cáo thống kê danh mục tài khoản.

        ---

        ### 2. AUTOMOTIVE TESTING TOOL OF CANOE FOR LINUX DEVICE:
        + Project: Hệ thống xử lý và kiểm thử ô tô của CANoe trên thiết bị LINUX
        + Role: Python Developer
        + Programming Language: Python, C/C++
        + Framework: PyQT
        + Description & Result: Xây dựng và phát triển ứng dụng Software/Firmware hỗ trợ cho việc kiểm thử tự động hóa quá trình tổng hợp các lỗi sửa sai trên thiết bị xe ô tô.

        ---

        ### 3. MULTILINGUAL ZOOM MEETING MINUTES EXTRACTION:
        + Project: Hệ thống trích xuất và trao đổi cuộc họp Meeting đa ngôn ngữ
        + Role: Python Developer
        + Programming Language: Python, VueJS, SCSS, JavaScript
        + Framework: FastAPI
        + Description & Result: Phát triển các tính năng cuộc họp cốt lõi bao gồm việc truyền phát dữ liệu âm thanh/video chất lượng cao theo thời gian thực.

        ---

        ### 4. SOCIAL BLOG MANAGEMENT SYSTEM:
        + Project: Hệ thống quản lý bài đăng mạng xã hội
        + Role: Python Developer
        + Programming Language: Python, VueJS, SCSS, JavaScript
        + Framework: FastAPI
        + Description & Result: Thiết kế hệ thống quản lý và kiếm soát các bài đăng trên mạng xã hội có kiểm duyệt theo tiêu chuẩn cộng đồng.

        ---

        ### 5. LEAVE HUB ATTENDANCE SYSTEM WITH HRMS:
        + Project: Hệ thống quản lý chấm công và nghỉ phép của nhân viên 
        + Role: Python Developer
        + Programming Language: Python, CSS, TypeScript, JavaScript
        + Framework: FastAPI, Frappe
        + Description & Result: Thiết kế hệ thống Website quản lý chấm công, thời gian làm việc và các đơn xin nghỉ phép của nhân viên trong công ty.

        ---

        ### 6. NEXT SUPPLY CHAIN MANAGEMENT OF NSCM:
        + Project: Hệ thống quản lý chuỗi cung ứng thế hệ mới 
        + Role: Python Developer
        + Programming Language: Python, SQL
        + Framework: Pandas, Polars
        + Description & Result: Thiết kế và chuyển đổi thông tin dữ liệu chuỗi cung ứng theo các phiên bản của hệ thống.
        """
    )