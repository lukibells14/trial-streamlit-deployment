import mysql.connector
import streamlit as st

def get_connection():
    return mysql.connector.connect(
        host=st.secrets["mysql"]["host"],
        user=st.secrets["mysql"]["user"],
        port = st.secrets["mysql"]["port"],
        password=st.secrets["mysql"]["password"],
        database=st.secrets["mysql"]["database"]
    )
