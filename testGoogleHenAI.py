import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image

import google.generativeai as genai


# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
# genai.configure(api_key="AIzaSyBzf0bkSuLUmsK1cpFlfzIqRumzbVLpAHk")

## Function to load OpenAI model and get respones

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input!="":
       response = model.generate_content([input,image])
    else:
       response = model.generate_content(image)
    return response.text

##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")
with st.sidebar:
    GOOGLE_API_KEY = st.text_input("Gemini API Key", key="input", type="password")
    "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/2_Chat_with_search.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

if not GOOGLE_API_KEY:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()
else:
    genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

st.header("Image Q&A APP - Gemini Gen AI")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

## If ask button is clicked

if submit:
    
    response=get_gemini_response(input,image)
    st.subheader("The Response is")
    st.write(response)
