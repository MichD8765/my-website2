import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images2/photo.png")

with col2:
    st.title("Michelle DSouza")
    content = """
    Hi, I am  Michelle! I am a coder by night and have a 9-5 by day. I enjoy creating new apps and fascinated about the world of coding.
    """
    st.info(content)

content2 = """ Here I have shared two apps that have been super benefical to me as I continue on my coding journey!!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df = pandas.read_csv("data2.csv", sep=";")

with col3:
    for index, row in df[:2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images2/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[1:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images2/" + row["image"])
