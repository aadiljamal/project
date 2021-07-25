from numpy.lib.npyio import NpzFile
import pandas as pd
from PIL import Image
import numpy as np
import streamlit as st
from streamlit_drawable_canvas import st_canvas
import streamlit.components.v1 as components  # Import Streamlit
from google.cloud import firestore
from firebase_admin import *
#Binary Parser
import struct
from struct import unpack
import json
from google.oauth2 import service_account


def unpack_drawing(file_handle):
    key_id, = unpack('Q', file_handle.read(8))
    country_code, = unpack('2s', file_handle.read(2))
    recognized, = unpack('b', file_handle.read(1))
    timestamp, = unpack('I', file_handle.read(4))
    n_strokes, = unpack('H', file_handle.read(2))
    image = []
    for i in range(n_strokes):
        n_points, = unpack('H', file_handle.read(2))
        fmt = str(n_points) + 'B'
        x = unpack(fmt, file_handle.read(n_points))
        y = unpack(fmt, file_handle.read(n_points))
        image.append((x, y))

    return {
        'key_id': key_id,
        'country_code': country_code,
        'recognized': recognized,
        'timestamp': timestamp,
        'image': image
    }


def unpack_drawings(filename):
    with open(filename, 'rb') as f:
        while True:
            try:
                yield unpack_drawing(f)
            except struct.error:
                break





# Authenticate to Firestore with the JSON account key.
#db = firestore.Client.from_service_account_json("mindreader-firestore-key.json")

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.Credentials.from_service_account_info(key_dict)
db = firestore.Client(credentials=creds, project="MindReader")
# Create a reference to the image data.
doc_ref = db.collection("MITR").document("mitr-happy-without-umbrella")




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
    height=500,
    drawing_mode=drawing_mode,
    key="canvas",
)

#st.button("save drawing")
image_data = canvas_result.image_data
#ndarray to array conversion
#json to ndjson
json_data = canvas_result.json_data

#firestore_imagedata = image_data.flatten()

if canvas_result.json_data is not None:
    st.dataframe(pd.json_normalize(canvas_result.json_data["objects"]))
st.write(canvas_result.json_data)
# Then get the data at that reference.
firestore_data = np.save('/home/aadil/Desktop/project/data/test_data', image_data, allow_pickle=True, fix_imports=True)
doc = doc_ref.set( 
    { 
    "drawing":firestore_data
    }
)    

# Let's see what we got!
#st.write("The id is: ", doc.id)
st.write("The Drawing data are: ",  doc)  