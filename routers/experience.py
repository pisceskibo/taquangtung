# Thư viện cần thiết
import streamlit as st 
import json
import textwrap
from routers.function import caculate_year_experience


EXPERIENCE_DATASET = "datasets/experience_data.json"

@st.cache_data
def load_experience_data_json():
    with open(EXPERIENCE_DATASET, "r", encoding="utf-8") as f:
        return json.load(f)


# Nội dung Experience
def write_experience():
    # Load datasets
    experiences_data = load_experience_data_json()

    st.write("""<hr style="border: 1px solid #ccc;">""", unsafe_allow_html=True)

    for exp_item in experiences_data:
        if "phases" in exp_item:
            # Trường hợp chia nhiều giai đoạn
            write_multi_phase(exp_item)
        else:
            # Trường hợp thông thường
            write_mono_phase(exp_item)

        st.image(exp_item["image"], caption=exp_item.get("caption", ""))

# Nhiều giai đoạn
def write_multi_phase(exp_item):
    st.markdown(f"### {exp_item.get("id")}. {exp_item.get("title")}:")
    
    for phase in exp_item.get("phases"):
        exp_time = phase.get("time")
        exp_year = caculate_year_experience(exp_time)

        # List tasks of sub phases
        raw_tasks = "\n".join([f"+ {task}" for task in phase.get("tasks")])
        indented_tasks = textwrap.indent(raw_tasks, "    ")

        # Main multi experience
        task_label_header = f"""
        #### {phase.get("period")}: ({exp_time})   
        + **Chức vụ:** {phase.get("role")}
        + **Kinh nghiệm:** {exp_year}
        + **Nhiệm vụ:**
        """
        full_task_phase = textwrap.dedent(task_label_header).strip() + "\n" + indented_tasks

        st.write(full_task_phase)

# Một giai đoạn
def write_mono_phase(exp_item):
    exp_time = exp_item.get("time")
    exp_year = caculate_year_experience(exp_time)
    label_infor_arrays = []

    st.markdown(f"### {exp_item.get('id')}. {exp_item.get('title')}:")

    # Nếu có department keys 
    department = exp_item.get("department")
    if department:
        label_infor_arrays.append(f"+ **Ban chuyên môn:** {department}")

    # List tasks of phases
    raw_tasks = "\n".join([f"+ {task}" for task in exp_item.get("tasks")])
    indented_tasks = textwrap.indent(raw_tasks, "    ")

    # Main mono experience
    label_infor_arrays.extend(
        [
            f"+ **Chức vụ:** {exp_item.get('role')}",
            f"+ **Thời gian:** {exp_time}",
            f"+ **Kinh nghiệm:** {exp_year}",
            "+ **Nhiệm vụ:**",
        ]
    )
    label_information = "\n".join(label_infor_arrays)

    # All of experience
    full_exp_company = label_information + "\n" + indented_tasks

    st.write(full_exp_company)
