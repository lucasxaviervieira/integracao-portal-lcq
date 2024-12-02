import streamlit as st
from content import *


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False


placeholder = st.empty()

if not st.session_state["logged_in"]:
    with placeholder.container():
        login()
else:
    with placeholder.container():
        st.write("Bem-vindo, {}!".format(st.session_state["username"]))
        main_app()
