import streamlit as st
from core.auth.index import LdapAuth


def login():
    ldap_auth = LdapAuth()

    st.title("Sistema de Login")

    username = st.text_input("Usuário")
    password = st.text_input("Senha", type="password")

    if st.button("Entrar"):
        if ldap_auth.login(username, password):
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
        else:
            st.error("Nome de usuário ou senha incorretos.")
