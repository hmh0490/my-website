import streamlit as st
import pandas

st.set_page_config(layout="wide", initial_sidebar_state="expanded")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg") # width=600

with col2:
    st.title("Hoang Minh Hanh")
    content = """
    Hi, I am Hanh!
     
    I am an accomplished finance professional with a diverse international background in banking and finance. 
    I have gained extensive experience in various roles, allowing me to develop a comprehensive understanding of 
    financial markets and strategies. Notably, I have also successfully passed the rigorous examination for the 
    Chartered Financial Analyst (CFA) certificate, highlighting my commitment to professional excellence.
    
    Throughout my career, I have developed a strong passion for programming and have acquired valuable experience in this
    area. I also proactively pursued coding skills to complement my finance background. Through self-study and 
    practical application, I have acquired a strong foundation in programming languages relevant to my profession.
    
    I am now driven to combine my profound knowledge of finance with my software development capabilities, aiming to leverage
    technology to optimize processes, automate tasks, and develop sophisticated models for data analysis and forecasting, 
    and deliver innovative solutions.
    """
    # st.write(content)
    st.info(content)

content2 = """
Below you find some of the apps I have built in Python. Feel free to contact me!
To access the Contact Me page on mobile, please tap the menu icon (">") located in the top left corner of this website.
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:7].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[7:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

