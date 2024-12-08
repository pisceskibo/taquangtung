# Xuất thư viện Python
import streamlit as st 

# Xuất Modulo
from router.function import make_circle
from router import introduction, education, experience, project, activities, certification


# Avatar tại Sidebar
image_path_avatar = "Image/avatarTQT.png"
image_avatar = make_circle(image_path_avatar)
st.sidebar.image(image_avatar, caption = "Tạ Quang Tùng", use_column_width = True)

# Các đầu mục Sidebar
menu = st.sidebar.selectbox("Giới thiệu chung (Overview)", 
                            ["Introduction", "Education", "Experience", "Projects",
                             "Activities", "Certifications"])
st.title(menu)


# Định tuyến tương ứng của Sidebar
if menu == "Education":
    education.write_education()
elif menu == "Experience":
    experience.write_experience()
elif menu == "Projects":
    project.write_project()
elif menu == "Activities":
    activities.write_activitiy()
elif menu == "Certifications":
    certification.write_certification()
else:
    introduction.write_introduction()


# Footer with social media icons
st.sidebar.markdown(
    """
    <hr>
    <div style="text-align: center;">
        <a href="https://www.facebook.com/pisceskibo" target="_blank" style="text-decoration: none;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/5/51/Facebook_f_logo_%282019%29.svg" alt="Facebook" style="width: 30px; height: 30px; margin-right: 10px;"/>
        </a>
        <a href="https://www.instagram.com/pisceskibo/" target="_blank" style="text-decoration: none;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/95/Instagram_logo_2022.svg" alt="Instagram" style="width: 30px; height: 30px; margin-right: 10px;"/>
        </a>
        <a href="https://github.com/pisceskibo" target="_blank" style="text-decoration: none;">
            <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" alt="GitHub" style="width: 30px; height: 30px;"/>
        </a>
    </div>
    <br>
    <p style="text-align: center; font-size: 12px;">Copyright © 2024 by Pisces Kibo</p>
    """,
    unsafe_allow_html=True
)
