# Thư viện cần thiết
import streamlit as st
import json


EDUCATION_DATASET = "datasets/education_data.json"

@st.cache_data
def load_education_data_json():
    with open(EDUCATION_DATASET, "r", encoding="utf-8") as f:
        return json.load(f)


# Nội dung Education
def write_education():
    # Load datasets
    education_data = load_education_data_json()
    degree = education_data.get("current_degree")
    timeline = education_data.get("education_timeline")

    st.write("""<hr style="border: 1px solid #ccc;">""", unsafe_allow_html=True)

    # 1. Trình độ chuyên môn:
    st.markdown("### 1. Trình độ chuyên môn hiện tại:")
    st.markdown(
    f"""
    + **Trường:** {degree.get("university")}
    + **Chuyên ngành:** {degree.get("majority")}
    + **Trình độ:** {degree.get("level")}
    """
    )

    # 2. Timeline học vấn:
    st.markdown("### 2. Timeline học vấn:")

    timeline_items_html = ""
    for item_school in timeline:
        ## Danh sách danh mục details
        details_html = ""
        if item_school.get("details"):
            li_items = "".join([f"<li>{d}</li>" for d in item_school.get("details")])
            details_html = (
                f'<ul style="margin-top: 5px; padding-left: 20px;">{li_items}</ul>'
            )

        ## Danh sách danh mục achievement
        achievement_html = ""
        if item_school.get("achievement"):
            achievement_html = (
                f'<p style="margin: 0 0 5px 0;">{item_school.get("achievement")}</p>'
            )

        ## Merge HTML with Code Block
        timeline_items_html += f"""
<li style="position: relative; padding-left: 40px; margin-bottom: 20px;">
<div style="background-color: {item_school.get('color')}; padding: 10px; border-radius: 6px; position: relative; color: white;">
<h4>{item_school.get('time')}: {item_school['school']}</h4>
<p>{item_school.get('description')}</p>
{achievement_html}
{details_html}
</div>
<div style="position: absolute; left: 0; top: 10px; width: 20px; height: 20px; border-radius: 50%; background-color: #00bfff;"></div>
<div style="position: absolute; left: 9px; top: 28px; width: 2px; height: calc(100% - 10px); background-color: #00bfff;"></div>
</li>
"""

    full_timeline_html = f"""
<ul style="list-style-type: none; padding-left: 0;">
{timeline_items_html}
</ul>
"""

    st.markdown(full_timeline_html, unsafe_allow_html=True)
