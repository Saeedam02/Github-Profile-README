import streamlit as st
from pathlib import Path 
from src.git_profile import generate_profile

st.title(":zap: Github Profile README")
# personal info
st.header("personaal info")
with st.expander("Personal Info"):
    col1,col2=st.columns(2)
    name=col1.text_input("Name")
    email=col2.text_input("Email")
    location=st.text_input("location")
    phone=col1.text_input("phone")
    homepage=col2.text_input("homepage")

#social media
st.header("Social Media")
with st.expander("Social media"):
    st.markdown("Enter your usernames not links")
    col1,col2=st.columns(2)
    github=col1.text_input('Github')
    Linkdin=col2.text_input('Linkdin')
    twitter=col1.text_input('Twitter')
    Instagram=col2.text_input('Instagram')
    YouTube=col1.text_input('YouTube')
    Medium=col2.text_input('Medium')


# select theme
st.header("Theme")
themes=Path("src/themes").iterdir()
themes=[theme.name for theme in themes]
theme=st.selectbox("select Theme",themes)
st.markdown(f"selected Theme : {theme}")

#generate Readme
st.header("Generate README")
if st.button("Generate Readme"):
    st.markdown("Generating Readme ...")
    profile=generate_profile(theme, name=name , email=email , Linkdin=Linkdin) 
    st.code(profile)
    st.markdown("Done!")
