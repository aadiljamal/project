#TF is the main ML/AI library and keras is its high level api
import tensorflow as tf
from keras.preprocessing.image import load_img
from keras.preprocessing.image import save_img
from keras.preprocessing.image import img_to_array


#argparse and time will be used to fetch labels from the .tflite file
import argparse
import time
import os


#Pandas and numpy will be used to fetch dataframes and to process numpy/array data
import pandas as pd
import numpy as np
#import matplotlib.pyplot as plot
#import seaborn as sns


#PIL or pillow will be used to perform different image transformation operations
from PIL import Image
#streamlit is the latest webapp framework for data driven apps
import streamlit as st
from streamlit_drawable_canvas import st_canvas

#""" ignore below imports used for different experiments  """
#import base64
#from io import BytesIO
#from pydrive.auth import GoogleAuth
#from pydrive.drive import GoogleDrive
#from google.cloud import storage
#import os
#import shutil

#dirpath = tempfile.mkdtemp()
# ... do stuff with dirpath




#def upload_blob(bucket_name, source_file_name, destination_blob_name):
    #Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

   # storage_client = storage.Client.from_service_account_json("arttherapist_key.json", project="arttherapist")
    #bucket = storage_client.bucket(bucket_name)
    #blob = bucket.blob(destination_blob_name)
    #blob.content_type = 'image/png'

    #blob.upload_from_filename(source_file_name)

    #print(
      #  "File {} uploaded to {}.".format(
       #     source_file_name, destination_blob_name
        #)
    #)



# Specifying canvas parameters in application
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
bg_image = st.sidebar.file_uploader("Background image:", type=["png", "jpg"])
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("freedraw", "line", "rect", "circle", "transform")
)
#Flatting ballons
st.balloons()

#saving filename typed in the text field
filename = st.text_input("Enter Drawing Name in the textfield below, start drawing Man in the ran if you want to know more about this test check belwo image")
st.write("I am requesting you to be a part of our project by drawing doodle in the canvas ")
#st.image('example.jpg')

#Making radio button realtime update by default false it will act as save or submit button in AI portion of the program
realtime_update = st.checkbox("CHECK_ME AFTER DRAWING IS DONE", False)

# Creating  a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    background_image=Image.open(bg_image) if bg_image else None,
    update_streamlit=realtime_update,
    height=450,
    drawing_mode=drawing_mode,
    key="canvas",
)

st.write("Thank you to be a part of our testing and  datacollection process")
#"""ignore below comments"""
#Download image function
# 
#def get_image_download_link(img):
  #              buffered=BytesIO()
   #             img.save(buffered, format='JPG')
    #            img_str = base64.b64encode(buffered.getvalue()).decode()
     #           href = f'<a href="data:file/jpg;base64,{img_str}">Download result</a>';mag
      #          return href
        

#Do something interesting with the image data and paths
#this portion will collect canvas data and convert it to required format of the Image classification model and predict the output 
#model labeller will display the percentage of the classification result
#finally the dataframe as per the predicted result will be displayed as the Mindreader result on the graph
analysis = pd.read_csv("./research_result_lite.csv")

cmd = "sudo chmod a+rwx ./testfiles/*"
dirpath = "./testfiles"  
if canvas_result.image_data is not None:
    if realtime_update == True:
        global test_image
                 #tempfile.mkdtemp()
        # ... do stuff with dirpath        
        X = (Image.fromarray((canvas_result.image_data).astype(np.uint8))).save(f'{dirpath}/{filename}.png') 
        os.system(cmd)
        test_image = load_img((f'{dirpath}/{filename}.png'), target_size = (224, 224)) 
        test_image = img_to_array(test_image)
        #test_image = np.expand_dims(test_image, axis = 0)
        save_img((f"{dirpath}/{filename}con.png") ,test_image)
        st.write("type:",test_image.dtype)

        #predict the result
        #result = model.predict(test_image)  
        

        #"""label_image for tflite."""       

        
        @st.cache()
        def load_labels(filename):
          time.sleep(2)
          with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]


        if __name__ == '__main__':
          parser = argparse.ArgumentParser()
          parser.add_argument(
              '-i',
              '--image',
              default=str(f"{dirpath}/{filename}con.png"),
              help= 'app _image help')
          parser.add_argument(
              '-m',
              '--model_file',
              default='./modelpoints/model.tflite',
              help='test lite file ')
          parser.add_argument(
              '-l',
              '--label_file',
              default='./modelpoints/labels.txt',
              help='name of file containing labels')
          parser.add_argument(
              '--input_mean',
              default=127.5, type=float,
              help='input_mean')
          parser.add_argument(
              '--input_std',
              default=127.5, type=float,
              help='input standard deviation')
          parser.add_argument(
              '--num_threads', default=None, type=int, help='number of threads')
          args = parser.parse_args()

          interpreter = tf.lite.Interpreter(
              model_path=args.model_file, num_threads=args.num_threads)
          interpreter.allocate_tensors()

          input_details = interpreter.get_input_details()
          output_details = interpreter.get_output_details()

          # check the type of the input tensor
          floating_model = input_details[0]['dtype'] == np.float32

          # NxHxWxC, H:1, W:2
          height = input_details[0]['shape'][1]
          width = input_details[0]['shape'][2]
          img = Image.open(args.image).resize((width, height))

          # add N dim
          input_data = np.expand_dims(img, axis=0)

          if floating_model:
            input_data = (np.float32(input_data) - args.input_mean) / args.input_std

          interpreter.set_tensor(input_details[0]['index'], input_data)

          start_time = time.time()
          interpreter.invoke()
          stop_time = time.time()

          output_data = interpreter.get_tensor(output_details[0]['index'])
          results = np.squeeze(output_data)
          st.line_chart(results, width=0, height=0, use_container_width=True)

          top_k = results.argsort()[-4:][::-1]
          st.write(top_k[0])
          st.write(top_k)
          labels = load_labels(args.label_file)
          #Creating result data from the analysis_csv file
          dashboard_data = analysis.iloc[[top_k[0] ]]
          #using builtin area_chart function of streamlit
          chart_data = pd.DataFrame(dashboard_data,
            columns = ["Protective_Mechanisms","Professional_Growth", "Confront_Difficult_Situations","Adaptation","Insecurity","Problem_Solving"])
          st.bar_chart(chart_data)
          for i in top_k:
            if floating_model:
              st.write('{:08.6f}: {}'.format(float(results[i]), labels[i]))
            else:
              st.write('{:08.6f}: {}'.format(float(results[i] / 255.0), labels[i]))

          st.write('time: {:.3f}ms'.format((stop_time - start_time) * 1000))


      
            
       
       






