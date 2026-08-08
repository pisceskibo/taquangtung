# Thư viện cần thiết
import streamlit as st
import json


ACTIVITY_DATASET = "datasets/activity_data.json"

@st.cache_data
def load_activity_data_json():
    with open(ACTIVITY_DATASET, "r", encoding="utf-8") as f:
        return json.load(f)


# Nội dung activities
def write_activitiy():
    # Load datasets
    activity_data = load_activity_data_json()

    st.write("""<hr style="border: 1px solid #ccc;">""", unsafe_allow_html=True)

    # Lấy danh sách tiêu đề Tabbar
    year_titles = [year_info.get("year_label") for year_info in activity_data.values()]
    year_tabs = st.tabs(year_titles)

    # Render for YEAR TAB
    for tab, (_, year_info) in zip(year_tabs, activity_data.items()):
        with tab:
            activities = year_info.get("activities")
            activity_contents = "\n".join(f"+ {item}" for item in activities)
            st.write(activity_contents)
