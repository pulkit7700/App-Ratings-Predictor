import streamlit as st
import numpy as np 
import pandas as pd
import plotly.express as px
from streamlit_option_menu import option_menu
import joblib
import os

st.title("App Rating Predictor 📱")

model = joblib.load("catmodel.pb")

######################################
dataset = pd.read_csv("Data/googleplaystore.csv")
dataset = dataset.dropna()

df = dataset

# Helper Functions

CategoryString = df["Category"]
categoryVal = df["Category"].unique()
categoryValCount = len(categoryVal)
category_dict = {}
for i in range(0, categoryValCount):
    category_dict[categoryVal[i]] = i

def removung(size):
    if "M" in size:
        X = size[:-1]
        X = float(X) * 1000000
        return X
    if "k" in size:
        X = size[:-1]
        X = float(X) * 1000
        return X
    else:
        return None

def type_cat(types):
    if types == "Free":
        return 0
    else:
        return 1

GenresL = df.Genres.unique()
GenresDict = {}
for i in range(len(GenresL)):
    GenresDict[GenresL[i]] = i

df.drop(
    labels=["Last Updated", "Current Ver", "Android Ver", "App"], axis=1, inplace=True
)
def price_clean(price):
    if price == "0":
        return 0
    else:
        price = price[1:]
        price = float(price)
        return price
    
    
RatingL = df["Content Rating"].unique()
RatingDict = {}
for i in range(len(RatingL)):
    RatingDict[RatingL[i]] = i

    




st.info("The App Rating Prediction web app is a machine learning-based application that predicts the ratings of mobile apps. It leverages historical app data and various features to provide accurate predictions of app ratings. Users can input the relevant attributes of an app, such as its category, size, price, number of downloads, and other relevant metrics, and the web app will generate an estimated rating for the app.")

text = st.text_input(label='Write the Name of App')
category  = st.selectbox(label='Category', options=list(dataset.Category.unique())) 
reviews = st.number_input(label="Write the Nummber of Revies your app has received")
type = st.selectbox(label='Type', options=list(dataset.Type.unique()))
price = st.number_input(label="Write the Price in Dollors")
Size = st.number_input(label="Write the Size of App, in millions or thousands")
install = st.number_input(label="Write the number of Installs")
Content_rating = st.selectbox(label= "Enter your rating type", options=list(dataset["Content Rating"].unique()))
Genres = st.selectbox(label= "Enter your Genres", options=list(dataset.Genres.unique()))
last_update = st.date_input('Enter Your Latest Date to Update the App')
Current_Version = st.text_input('Write the Version of the App')

colummns = ["Category", 'Reviews', 'Size', 'Installs', 'Type', 'Price', 'Content Rating', 'Genres']

def predict():
    row = np.array([category, reviews, Size, install, type, price, Content_rating, Genres])
    X = pd.DataFrame([row], columns= colummns)
    
    X["Category"] = X["Category"].map(category_dict).astype(int)
    X["Type"] = X["Type"].map(type_cat).astype(int)
    X["Content Rating"] = X["Content Rating"].map(RatingDict).astype(int)
    X["Genres"] = X["Genres"].map(GenresDict).astype(int)
    prediction = model.predict(X)[0]
    prediction = np.round(prediction, decimals=2)
    st.success("The Predicted Rating for the App would be {}".format(prediction))
    return prediction



if st.button('Predict', on_click=predict):
    predict()