import streamlit as st

st.set_page_config("DermAI", layout="wide")

col1, col2, col3 = st.columns(3)

with col1:
    ()
with col2:
    st.image("imgs/Logo.png",)
with col3:
    ()

with st.sidebar:
    st.header("Oi header do sidebar aqui")
    st.button("botao")