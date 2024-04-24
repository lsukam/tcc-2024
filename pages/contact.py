import streamlit as st

st.header("Contatos")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Nome:")
    st.write("Luiz Henrique Goes Rodrigues")
    st.write("Luana Brisola Mena")
    st.write("Lucas Marinelli Maciel")

with col2:
    st.header("E-mail:")
    st.write("200313@facens.br")
    st.write("200264@facens.br")
    st.write("200285@facens.br")