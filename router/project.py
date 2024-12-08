# Thư viện cần thiết
import streamlit as st 

# Nội dung projects
def write_project():
    st.write(
        """<hr style="border: 1px solid #ccc;""", unsafe_allow_html=True
    )

    st.write(
        """
        > Link chi tiết: https://github.com/pisceskibo 
        
        ### 1. BOOK MANAGEMENT APP:
        + Project: Thiết kế giao diện phần mềm quản lý sách 
        + Programming Language: Python
        + Framework: Tkinter
        + Link mô tả: https://github.com/pisceskibo/BookManagement 

        ### 2. DOCUMENT MANAGEMENT:
        + Project: Hệ thống quản lý tài liệu Document
        + Programming Language: Python, HTML, CSS, JavaScript
        + Framework: Django
        + Link mô tả: https://github.com/pisceskibo/ManagerDocument 

        ### 3. LIBRARY MANAGEMENT:
        + Project: Hệ thống quản lý thư viện tài liệu điện tử số
        + Programming Language: Python, HTML, CSS, JavaScript
        + Framework: FastAPI, Tkinter, Streamlit
        + Link mô tả: https://github.com/pisceskibo/LibraryManagement 

        ### 4. TIME CHECKING:
        + Project: Hệ thống chấm công theo yêu cầu
        + Programming Language: Python
        + Framework: FastAPI
        + Link mô tả: https://github.com/pisceskibo/TimeChecking 
        """
    )