# Thư viện cần thiết
import streamlit as st
import json


PROJECT_DATASET = "datasets/project_data.json"

@st.cache_data
def load_project_data_json():
    with open(PROJECT_DATASET, "r", encoding="utf-8") as f:
        return json.load(f)


# Nội dung projects
def write_project():
    # Load datasets
    project_data = load_project_data_json()

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
        get_company_project(project_data[0])
    elif st.session_state.selected_project_type == "personal":
        get_personal_projects(project_data[1])
    else:
        st.markdown("<p style='text-align: center; font-style: italic;'>💡 Bấm vào một trong hai thẻ danh mục phía trên để xem danh sách dự án chi tiết.</p>", unsafe_allow_html=True)

# Thông tin dữ liệu các dự án cá nhân
def get_personal_projects(personal_project_dataset):
    # Load datasets
    personal_project_list = personal_project_dataset.get("projects")

    st.markdown("## 🗃️ PERSONAL PROJECTS")
    st.write(f">> *{personal_project_dataset.get("caption")}*")

    for item_personal in personal_project_list:
        detail_personal_array = [
            f"### {item_personal.get('id')}. {item_personal.get('title')}:",
            f"+ **Project:** {item_personal.get('project')}",
            f"+ **Programming Language:** {item_personal.get('lang')}",
            f"+ **Framework:** {item_personal.get('framework')}",
            f"+ **Link mô tả:** [{item_personal.get('link')}]({item_personal.get('link')})"
        ]
        st.markdown("---")
        st.write("\n".join(detail_personal_array))

# Thông tin dữ liệu các dự án doanh nghiệp
def get_company_project(company_project_dataset):
    # Load datasets
    company_project_list = company_project_dataset.get("projects")

    st.markdown("## 🗃️ COMPANY PROJECTS")
    st.write(f">> *{company_project_dataset.get("caption")}*")

    for item_company in company_project_list:
        detail_company_array = [
            f"### {item_company.get('id')}. {item_company.get('title')}:",
            f"+ **Project:** {item_company.get('project')}",
            f"+ **Role:** {item_company.get('role')}",
            f"+ **Programming Language:** {item_company.get('lang')}",
            f"+ **Framework:** {item_company.get('framework')}",
            f"+ **Description & Result:** {item_company.get('description')}",
        ]
        st.markdown("---")
        st.write("\n".join(detail_company_array))
