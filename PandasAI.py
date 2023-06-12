import streamlit as st
from dotenv import load_dotenv
import os
import pandas as pd
from pandasai import PandasAI
from pandasai.llm.openai import OpenAI
import matplotlib
import matplotlib.pyplot as plt

#hide style
hide_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        </style>
        """
st.markdown(hide_style,unsafe_allow_html= True)


#load API keys from .env file
load_dotenv()
st.title("PandasAI: Promot driven data analysis Tool. (Powered By OpenAI) ")

#create connection to OpenAI API
API_KEY = os.environ['OPENAI_API_KEY']
llm = OpenAI(api_token= API_KEY)
pandas_ai = PandasAI(llm)

# Check if the file is already in the session state
if "uploaded_file" not in st.session_state:
    st.session_state["uploaded_file"] = None
uploaded_file = st.file_uploader("File Type Restricted:.csv &.xlsx file only", type=['csv','xlsx'])

# Check if a new file has been uploaded
if uploaded_file is not None:
    st.session_state["uploaded_file"] = uploaded_file

# If there is a file in the session state, display it
if st.session_state["uploaded_file"] is not None:
    df = pd.read_csv(st.session_state["uploaded_file"])
    st.session_state["df"] = df 
    st.write(df.head())
    # Enter the prompt
    prompt = st.text_area("Enter your Prompt:")

    #Generate Answers 
    if st.button("Generate"):
        if prompt:
            # call pandas_ai.run(), passing dataframe and prompt
            with st.spinner("Generating response..."):
                answer = pandas_ai.run(st.session_state.df,prompt)
                #If AI returns a image, display the plot or write the string

                fig_number = plt.get_fignums()
                if fig_number:
                    st.pyplot(plt.gcf())
                else:
                    st.write(answer)
        else:
            st.warning("Please enter a prompt")