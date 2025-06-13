import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

st.title("🎈 Image 3D Rotation Prototype")
uploaded_file = st.file_uploader(label="Choose an image",
                 type=["jpg", "jpeg", "png"],
                 accept_multiple_files=False)

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image_array = np.array(image)

    st.image(image, caption="Original Image", use_column_width=True)

    # Rotation sliders
    rotation_degree_Ox = st.slider('Slide to choose how far the object tilts forward or backward.', -180, 180, 0)
    rotation_degree_Oy = st.slider('Slide to choose how far the object swivels left or right.', -180, 180, 0)
    rotation_degree_Oz = st.slider('Slide to choose how far the object rolls clockwise or counter-clockwise', -180, 180, 0)

    # # Applying rotation on the Z-axis using OpenCV
    # def rotate_image(image, angle):
    #     (h, w) = image.shape[:2]
    #     center = (w // 2, h // 2)
    #     matrix = cv2.getRotationMatrix2D(center, angle, 1.0)
    #     rotated = cv2.warpAffine(image, matrix, (w, h))
    #     return rotated

    # rotated_image = rotate_image(image_array, rotation_degree_Oz)

    # st.image(rotated_image, caption="Rotated Image", use_column_width=True)


rotation_degree_Ox = st.slider('Slide to choose how far the object tilts forward or backward.')  # 👈 this is a widget
rotation_degree_Oy = st.slider('Slide to choose how far the object swivels left or right.')
rotation_degree_Oz = st.slider('Slide to choose how far the object rolls clockwise or counter-clockwise')


st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
