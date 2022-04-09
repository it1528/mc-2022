import streamlit as st
import pandas as pd
import pickle
from sklearn.ensemble import  RandomForestClassifier

from sklearn import datasets
#Kaggle api is installed on the project
import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
from sklearn import datasets
hide_menu = """
<style>
#MainMenu {
    visibility:hidden;
}

footer{
    visibility:hidden;
}
</style>
"""



st.title("Dashboard App")
st.write("This is an application for educational purposes.")
st.header("Explore different machine learning algorithms")
st.markdown(hide_menu, unsafe_allow_html=True)



# Collects user input features into dataframe
with st.sidebar.header('Upload your CSV data'):
    dataset_name = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])

example_db = st.sidebar.button('Use example CSV file')
def load_dataset(dataset_name):
    if dataset_name == "Diabetes dataset":
        data = datasets.load_diabetes()
    elif dataset_name == "Iris dataset":
        data = datasets.load_iris()
    elif dataset_name == "Boston dataset":
        data = datasets.load_boston()

    X = data.data
    Y = data.target
    return X, Y
if example_db:
    # Select box
    dataset_name = st.sidebar.selectbox("Select Dataset",
                                        ("Diabetes dataset", "Iris dataset", "Boston dataset", "Titanic dataset"))
    X, Y = load_dataset(dataset_name)
    st.write("shape of dataset", X.shape)
    st.write(dataset_name)




#We could also mutliselect in the algorithm section to show the comparisson between the algorithms
algorithm_name = st.sidebar.selectbox("Select Algorithm/Classifier", ("Logistic Regression", "Linear Regression", "Random Forest Classifier", "KNN", "SVM"))

#st.markdown

#Titanic can be used for logistic regression



#nav = st.sidebar.radio("Navigation",["Home","Prediction"])




#main()
