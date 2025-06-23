import streamlit as st

# Atur lebar halaman
st.set_page_config(layout="wide")

st.title("📊 Infografis Survei Teh Cascara")

# Baca file HTML
with open("cascara_survey_infographic.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Tampilkan HTML di dalam Streamlit
st.components.v1.html(html_content, height=3000, scrolling=True)