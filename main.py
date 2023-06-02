import streamlit as st
import pandas as pd
import os
from PIL import Image
from util import *
from collibra import *
import time
import torch
from transformers import pipeline
import json

answer = ""
generate_text_3 = None


def main():
    global answer
    global generate_text_3
    # Load the Model
    model_path = "\dolly-v2-7b"
    with st.spinner("Loading model..."):
        # Load the Model
        generate_text_3 = pipeline(model=model_path, torch_dtype=torch.bfloat16, trust_remote_code=True,
                                   device_map="auto")
        # delayed_return()
    # Once the model is loaded, remove the spinner and display the UI
    st.spinner()

    def dolly_gen(prompt):
        res = generate_text_3(prompt)
        return res[0]["generated_text"]

    def fn_without_data(prompt):
        question = str(prompt)

        ans = dolly_gen(question)
        return ans

    # Set page layout to center aligned
    st.markdown(
        """
        <style>
        .stApp {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            st.empty()

        # Display the image in the third column
        with col2:
            logo_path = r"fractal-logo.png"
            logo_image = Image.open(logo_path)
            logo_resized = logo_image.resize((298, 100))
            st.image(logo_resized, use_column_width=False)

        with col3:
            st.empty()

    with st.container():
        col1, col2, col3 = st.columns([1, 2, 1])

        with col1:
            st.empty()

        # Display the text in the third column
        with col2:
            st.subheader('Data Analysis using Dolly')

        with col3:
            st.empty()

    # Apply CSS to center align the image
    st.markdown(
        """
        <style>
        .st-ir {
            display: flex;
            justify-content: center;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Button to upload CSV file
    uploaded_file = st.file_uploader("Upload a CSV file")

    # Button to display CSV file's first 10 rows
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        if st.button("Display CSV"):
            st.write(df.head(10))

    # Input prompt space
    text_input = st.text_input("Enter text")
    with st.container():
        col1, col2, col3, col4 = st.columns([3, 3, 5, 3])
        with col1:
            st.empty()
        with col2:
            st.empty()
        # Button to save input to Excel file
        if col3.button("Submit"):
            if text_input:
                print(text_input)
                answer = fn_without_data(text_input)
                print("After input : " + answer)
                # st.success('Prompt Saved Successfully')
            else:
                st.warning("Please enter some text")
        with col4:
            st.empty()

    # Display output text area
    print(answer + "middle")
    output_slot = st.empty()
    text = output_slot.text_area('Output', value=answer)

    # Button to refresh output, update output, and invoke Collibra APIs
    with st.container():
        col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])
        with col1:
            st.empty()
        # Button to refresh output
        if col2.button("Refresh"):
            pass

        # new_string = output_slot.text_area('Output')

        # Button to update output in Excel file
        if col3.button("Update"):
            updated_text = ""
            if updated_text:
                tupdate = update_answer(updated_text)
                st.success(tupdate)
            else:
                st.warning("Please enter some text")

        # Button to invoke some function
        if col4.button("Collibra"):
            # Your function code here
            Patch()
            st.success("Collibra function invoked")

        with col5:
            st.empty()


# return "Hello"
if __name__ == "__main__":
    # generate_text_3 = None
    main()
