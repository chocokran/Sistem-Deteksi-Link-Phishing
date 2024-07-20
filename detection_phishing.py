import numpy as np
import pandas as pd
import feature_extraction
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from flask import jsonify


def getResult(url):

    # Importing dataset
    df = pd.read_csv("dataset_v3.csv")

    # Separating features and labels
    x = df.iloc[:, :-1]
    y = df.iloc[:, -1]

    # Separating training features, testing features, training labels & testing labels
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=7)
    
    # Using Random Forest Classifier
    rf = RandomForestClassifier(n_estimators=100, random_state=7)
    rf.fit(x_train, y_train)
    score = rf.score(x_test, y_test)
    
    print('Akurasi : ', score * 100)

    X_new = []

    X_input = url
    X_new = feature_extraction.generate_data_set(X_input)
    X_new = np.array(X_new).reshape(1, -1)

    try:
        prediction = rf.predict(X_new)
        if prediction == 1:
            print("Bukan Website Phishing")
            return "Bukan Website Phishing"
        else:
            print("Terindikasi Website Phishing")
            return "Terindikasi Website Phishing"
    except:
        print("Terindikasi Website Phishing")
        return "Terindikasi Website Phishing"
