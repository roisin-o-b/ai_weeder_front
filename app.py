import streamlit as st
from PIL import Image
import numpy as np
import requests


# Center-aligned style for headers and titles
header_style = """
<style>
.centered-header {
    text-align: center;
}
.centered-header-orange {
    text-align: center;
    color: #ff5733;
}
.stButton>button {
    width: 100%;
    font-size: 20px;
    background-color: #ff5733;
    color: white;
}
.stButton>button:hover {
    background-color: white;
    color: #ff5733;
}
</style>
"""


st.markdown(header_style, unsafe_allow_html=True)

# Title of the app (centered)
st.markdown('<h1 class="centered-header-orange">Seedling Type Prediction App</h1>', unsafe_allow_html=True)

st.markdown('''
Upload an image of a plant, and this app will predict its type using a pre-trained model via API.
''')

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:

    # Display uploaded image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)
    st.write("")

    if st.markdown('<div style="text-align: center;">', unsafe_allow_html=True):
        if st.button('Predict'):

            img_bytes = uploaded_file.read()


            # Make API request
            api_url = 'http://localhost:8000/upload_image'
            # Send the image to the API
            response = requests.post(api_url, files={'img': img_bytes})

            if response.status_code == 200:
                result = response.json()
                predicted_class_label = result.get('predicted_class')
                probability = result.get('probability')
                st.write(result)
                # Display the prediction
                st.write(f"**Predicted Plant:** {predicted_class_label}")
                st.write(f"**Probability:** {probability:.2f}")
            else:
                st.write("Error: Unable to get a prediction from the API.")
