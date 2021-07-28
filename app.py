import pandas as pd
from PIL import Image
import streamlit as st
import numpy as np
from streamlit_drawable_canvas import st_canvas
import matplotlib.pyplot as plt


# Specify canvas parameters in application
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")
)
st.balloons()
filename = st.text_input("Enter Drawing Name and start drawing Man in the ran if you want to know more about this test check belwo image")
st.image('./example.jpg')

realtime_update = st.checkbox("CHECK_ME AFTER DRAWING IS DONE", False)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=450,
    drawing_mode=drawing_mode,
    key="canvas",
)

#contributer instructions


# Do something interesting with the image data and paths
if canvas_result.image_data is not None:
    #image_data_result = st.image(canvas_result.image_data)
    npdata = canvas_result.image_data
    #st.write(type(npdata))
    #st.write(canvas_result) 

if realtime_update == True:
    plt.imsave(filename+".png", npdata.astype(np.uint8), cmap='Greys')
#st.write(type(test1.png))

st.write("Please share the saved image with me on my mail id mraadil.jamal@outlook.com Else share with my collaques Aatif and Zainab on their whatsapp")