import pandas as pd
from PIL import Image
import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Specify canvas parameters in application
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")
)
realtime_update = st.sidebar.checkbox("Update in realtime", True)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color="" if bg_image else bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=200,
    drawing_mode=drawing_mode,
    key="canvas",
)

image_data = canvas_result.image_data
jsonformat = canvas_result.json_data
#st.write(jsonformat)
#st.write(image_data)
rescaled = (255.0 / image_data.max() * (image_data - image_data.min())).astype(np.uint8)
im = Image.fromarray(rescaled)
im.save('test.png')
#directory = '/home/aadil/Desktop/project'
file = open(directory + image_data,'w')

file.write('image_data')

file.close()
# Do something interesting with the image data and paths
#if canvas_result.image_data is not None:
    #st.image(canvas_result.image_data)
if canvas_result.json_data is not None:
    st.dataframe(pd.json_normalize(canvas_result.json_data["objects"]))
