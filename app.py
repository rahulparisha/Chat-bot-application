from dotenv import load_dotenv

load_dotenv()

import streamlit as st 
import os 
import pathlib 
import textwrap 

import google.generativeai as genai 

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
    text = text.replace('.', '*')
    return Markdown(textwrap.indent(text, '>', predicate=lambda line: True))



def get_gemini_response(question):
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    response = model.generate_content(question)
    return response.text

st.set_page_config(page_title="AI APP")
st.header("gemini AI app aplication")
input = st.text_input("input : ",key ="input")
submit = st.button("ask question")

if submit:

    response = get_gemini_response(input)
    st.subheader("The responce is ")
    st.write(response)

