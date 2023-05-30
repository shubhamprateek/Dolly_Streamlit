import streamlit as st
import pandas as pd
import os
from PIL import Image
from util import *
from collibra import *



def main():
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
        col1, col2, col3 = st.columns([3, 5, 3])

        with col1:
            st.empty()

        # Display the image in the third column
        with col2:
            logo_path = r"fractal-logo.jpg"
            logo_image = Image.open(logo_path)
            logo_resized = logo_image.resize((300, 100))
            st.image(logo_resized, use_column_width=False)

        with col3:
            st.empty()

    st.subheader('Data Analysis using Dolly')

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
                message = submit_prompt(text_input)
                st.success(message)
            else:
                st.warning("Please enter some text")
        with col4:
            st.empty()

    # Display output text area
    output = ""
    output_slot = st.empty()
    text = output_slot.text_area('Output')

    # Button to refresh output, update output, and invoke Collibra APIs
    with st.container():
        col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])
        with col1:
            st.empty()
        # Button to refresh output
        if col2.button("Refresh"):
            output = refresh_output()
            output_slot.text_area('Output',value=output)

        # Button to update output in Excel file
        if col3.button("Update"):
            updated_text = output_slot
            if updated_text:
                tupdate = update_answer(text)
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


if __name__ == "__main__":
    main()
