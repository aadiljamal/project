#Mindreader AI Based webapp used to check few facts about a person by using art thereapy technique called MITR test.
You can check it here
https://share.streamlit.io/aadiljamal/project/main/app.py

This was my final year project based on MITR test, it is an art therapy test where the person is asked to drawn a man in the rain
Then according to the survey done on the south Korean university and by South korean army for military life adjustment.
Pictures speak lot about person than words because images contain lot of information of person for our case drawing drawn by a person can speak about his subconcous.

It might be a small step towords AI in physcology.


Steps to run this app 

crean a virtual environment and run pip install -r requiremnt.txt

Requirement.txt contains required library to run Mindreader application.

step 1.
Datacollection of hand drawn images containing MITR .
data was completely collected from human inputs which is currently very less as of now it is now available but we can use the trained model to do our job.

Step 2
Data preprocessing as we do with any other classification problem.
Reaserch.csv is the file which contians few results from the survay done in South Korean university.

Step 3
Pretrained tf lite model is saved in the folder ./modepoints/
All training related code is contained in the Mitr_training jupyter notebook file.

I got following batch loss and accuracy results during training.

![Tesnsorboard](https://storage.googleapis.com/mitr-data-bucket/mitr-data-bucket/testfiles/tensorboard.png)



step4 
Web Framework used is streamlit 
pip install streamlit will install it and we can test it using command 
streamlit run hello

For Canvas part i have streamlit drawable canvas same can installed using pip from its official webiste.

To infer the model inside webapp i have used label.py file which is contained inside the util folder.

Once all done just type the command 
streamlit run app.py
it will start streamlit local server on port 8501

Step5 
Make it live .
You can check our currently live version on https://share.streamlit.io/aadiljamal/project/main/app.py

TO do so you can use free share.streamlit.io account.
for related setup in share.streamlit.io check their official website.

Step6 
Cloud services for saving new image drawn by the used you can use any of your favourite cloud services.

Few Secreenshot of the app goes here









