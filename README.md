# App Rating Predictor 📱

This is a Python code for an "App Rating Predictor" web application. The application is built using the Streamlit framework and utilizes machine learning techniques to predict the ratings of mobile apps. It takes into account various features of the app, such as category, size, price, number of downloads, and other relevant metrics, to generate accurate rating predictions.

## Prerequisites

Before running the code, make sure you have the following dependencies installed:

- streamlit
- numpy
- pandas
- plotly.express
- streamlit_option_menu
- joblib

You can install the dependencies by running the following command:

```
pip install streamlit numpy pandas plotly streamlit_option_menu joblib
```

## Getting Started

1. Clone or download the code to your local machine.
2. Make sure you have the necessary dataset and model file:
   - The code expects a CSV file named "googleplaystore.csv" in the "Data" directory, containing the app data.
   - The code also expects a pre-trained model file named "catmodel.pb" in the same directory.
   Make sure to place these files in the appropriate locations.
3. Run the code using the following command:

```
streamlit run app.py
```

4. The application will start running, and you will see a browser window open with the "App Rating Predictor" web app.

## Usage

1. Once the web app is open, you will see a title "App Rating Predictor 📱".
2. Enter the name of the app in the text input field.
3. Select the category of the app from the dropdown menu.
4. Enter the number of reviews the app has received using the number input field.
5. Select the type of the app (Free or Paid) from the dropdown menu.
6. Enter the price of the app in dollars using the number input field.
7. Enter the size of the app in millions or thousands using the number input field.
8. Enter the number of installs the app has received using the number input field.
9. Select the content rating type from the dropdown menu.
10. Select the genres of the app from the dropdown menu.
11. Enter the latest date of the app update using the date input field.
12. Enter the current version of the app using the text input field.
13. Click the "Predict" button to generate the rating prediction for the app.
14. The predicted rating will be displayed in a success message below the button.

Note: Please make sure to enter valid and appropriate values for each input field to obtain accurate predictions.

## About

The "App Rating Predictor" web app is a machine learning-based application that leverages historical app data and various features to provide accurate predictions of app ratings. It utilizes the "googleplaystore.csv" dataset, which should be placed in the "Data" directory. The app also uses a pre-trained machine learning model, loaded from the "catmodel.pb" file. The model predicts the rating based on the input features provided by the user.

For any further questions or support, please contact [your contact information].
