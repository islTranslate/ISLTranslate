
import cv2
import numpy as np
import streamlit as st
import requests
import os

# Home UI 

def main():

    st.set_page_config(layout="wide")

    font_css = """
        <style>
        button[data-baseweb="tab"] {
        font-size: 26px;
        }
        </style>
        """

    st.write(font_css, unsafe_allow_html=True)
    translate()

# Pre-process Image
def preProcessImg(img):
    # Pre-processing image: resize image
    height, width, _ = img.shape
    width = int(720/height*width)
    height = 720
    img = cv2.resize(img,(width,height))
    return img


def translate():

    st.header("English to ISL Translation")

    engText = st.text_input('Engligh Text')

    # Original Image
    st.subheader("English Text")

      
    st.subheader("ISL Gloss")
    st.subheader("ISL Vid")

   
if __name__ == "__main__":
    main()
