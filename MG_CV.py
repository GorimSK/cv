from pathlib import Path
import streamlit as st
from PIL import Image

# --- Path Settings ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic_path = current_dir / "assets" / "profile-pic.png"

# --- General Settings ---
PAGE_TITLE = "Digital CV | Miroslav Gregor"
PAGE_ICON = ":wave:"
NAME = "Miroslav Gregor"
DESCRIPTION = """
Senior PPC Specialist and enthusiast Marketing Data Analyst"""
EMAIL = "gregor@gorim.sk"
SOCIAL_MEDIA = {
    "LinkedIN": "https://www.linkedin.com/in/miroslav-gregor-mg"
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

#st.title("Hi and Hello!")

# --- Load CSS, PDF & Profile Pic ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic_path)

# --- Hero Section ---
col1, col2 = st.columns(2)

with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="📩 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )

st.write("📧", EMAIL)
st.write("📞", "+421 904 329 454")

# --- Social Links ---
st.markdown('<p style="font-size:18px; font-weight:bold;">Let\'s Connect!</p>', unsafe_allow_html=True)
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].markdown(f"[{platform}]({link})")

# --- Experience & Qualification---
st.write("#")
st.subheader("Experience & Qualification")
st.write(
    """
    - ✔ More than 10 years of experience in digital marketing
    - ✔ 5 years experience in performance marketing
    - ✔ Good understandig of marketing data and analytics
    - ✔ Team-player with strong sense of initiative on tasks
    """
        )

# --- Skills ---
st.write("#")
st.subheader("Hard Skills")
st.write(
    """
    - 🔎 Google Ads - Expert
    - 📈 Google Analytics - Intermediate
    - 📱  Facebook Ads - Intermediate
    - ☑ Google Tag Manager - Intermediate
    - 📊 Looker Studio - Intermediate
    - 🔁 Google BiqQuery - basics
    - 🐍 Python - basics
    - 💻 SQL - basics
    """
)

# --- Work History ---
st.write("#")
st.subheader("Work History")
st.write("---")

# --- Job 1 ---
st.write("🛠️", "**PPC Specialist | VIAMEDIA**")
st.write("01/2015 - 07/2015")

# --- Job 2 ---
st.write("🛠️", "**PPC Specialist | daren&curtis**")
st.write("07/2015 - 06/2018")

# --- Job 3 ---
st.write("↗️", "**Head of Performance | PTA group**")
st.write("06/2018 - 06/2019")

# --- Job 3 ---
st.write("🤝️", "**Head of Digital Marketing | Salve group**")
st.write("07/2019 - 05/2021")

# --- Job 3 ---
st.write("⏩", "**Digital Marketing Manager | Media & Digital Services**")
st.write("06/2021 - current")