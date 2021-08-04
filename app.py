import pandas as pd
from PIL import Image
import streamlit as st
import numpy as np
from streamlit_drawable_canvas import st_canvas
import base64
from io import BytesIO
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive



# Specify canvas parameters in application
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")
)
st.balloons()
filename = st.text_input("Enter Drawing Name in the textfield below, start drawing Man in the ran if you want to know more about this test check belwo image")
st.write("I am requesting you to be a part of our project by drawing doodle in the canvas ")
st.image('example.jpg')

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

st.write("Please share the saved image with us on my mail id mraadil.jamal@outlook.com or share with my team mate Aatif and Zainab on their whatsapp")
#Download image function
# 
#def get_image_download_link(img):
  #              buffered=BytesIO()
   #             img.save(buffered, format='JPG')
    #            img_str = base64.b64encode(buffered.getvalue()).decode()
     #           href = f'<a href="data:file/jpg;base64,{img_str}">Download result</a>';
      #          return href
        
#Do something interesting with the image data and paths
if canvas_result.image_data is not None:
    if realtime_update == True:
        result = Image.fromarray((canvas_result.image_data).astype(np.uint8))    
        st.image(result)
        result.save(f'./data/{filename}.png')
        
                 

