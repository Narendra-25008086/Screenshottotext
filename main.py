import streamlit as st
import pytesseract
from PIL import Image
import os

# Windows Tesseract Path
if os.name == "nt":
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Page settings
st.set_page_config(
    page_title="Image Text Extractor",
    page_icon="📄",
    layout="centered"
)

# Title
st.title("📄 Image Text Extractor")
st.write("Upload an image and extract text from it.")

# Upload image
uploaded_file = st.file_uploader("Upload Image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:

    img = Image.open(uploaded_file)

    # Show uploaded image
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # OCR Processing
    with st.spinner("Extracting text..."):
        text = pytesseract.image_to_string(img)

    st.subheader("Extracted Text")

    # Text area for copy
    st.text_area("Extracted Text", text, height=250)

    # Copy instruction
   
# Footer
st.markdown("---")
st.markdown(
    "<center>Created by <b>Narendra Krishnan KS (AIML)</b></center>",
    unsafe_allow_html=True
)