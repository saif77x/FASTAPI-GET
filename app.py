import streamlit as st
import requests

st.title('FastAPI GET Example')

# GET Request UI
st.header("GET Request Example")
if st.button("Fetch Greeting"):
    response = requests.get("http://localhost:8000/hello")
    st.write("Response from GET:", response.json())
if st.button("main"):
    response = requests.get("http://localhost:8000/")
    st.write("Response from GET:", response.json())