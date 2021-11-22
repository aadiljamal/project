#Mindreader AI Based webapp used to check few facts about a person by using art thereapy technique called MITR test.
You can check it here
https://share.streamlit.io/aadiljamal/project/main/app.py

This was my final year project based on MITR test, it is an art therapy test where the person is asked to drawn a man in the rain
Then according to the survey done on the south Korean university and by South korean army for military life adjustment.Art therapy uses drawing to interpret the subconcious mind of human
Pictures speak lot about person than words because images contain lot of information of person for our case MITR drawing drawn by a person can speak about his subconcious as per this table.
Note the below interpretation is based on survey and data collected only , so please consider it my version of analysis you are welcome to correct incase it not so right.

Cat	Protective_Mechanisms	Professional_Growth	Confront_Difficult_Situations	Adaptation	Insecurity	Problem_Solving
0	1	1	1	1	0.5	1
1	1	0	0.5	1	0	1
2	0	1	1	0	0.5	0
3	1	1	0	0.5	1	0.5
4	0	0	0	0	0	0



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

TO do so you can us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e free share.streamlit.io account.
for related setup in share.streamlit.io check their official website.

Step6 
Cloud services for saving new image drawn by the used you can use any of your favourite cloud services.

Few Secreenshot of the app goes here


[!Canvas for Drawing](https://storage.googleapis.com/mitr-data-bucket/mitr-data-bucket/testfiles/canvas.png)
[!graph comparing the type of catagory of sketch](https://storage.googleapis.com/mitr-data-bucket/mitr-data-bucket/testfiles/graph1.png)
[!graph showing the traits of the person as per class of  drawing](https://storage.googleapis.com/mitr-data-bucket/mitr-data-bucket/testfiles/graph2.png)








