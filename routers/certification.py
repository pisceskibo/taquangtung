# Thư viện cần thiết
import streamlit as st
import json


CERTIFICATION_DATASET = "datasets/certification_data.json"

@st.cache_data
def load_certification_data_json():
    with open(CERTIFICATION_DATASET, "r", encoding="utf-8") as f:
        return json.load(f)


# Nội dung Certifications
def write_certification():
    # Load datasets
    certificate_data = load_certification_data_json()

    st.write("""<hr style="border: 1px solid #ccc;">""", unsafe_allow_html=True)

    for section_info in certificate_data.values():
        certificate_title = section_info.get("title")
        certificate_details = section_info.get("items")

        with st.expander(certificate_title):
            if certificate_details:
                content_markdown = "\n".join(f"+ {item}" for item in certificate_details)
                st.markdown(content_markdown)
