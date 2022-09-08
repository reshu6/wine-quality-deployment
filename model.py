# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

df=pd.read_csv('F:\\data science\\wine model deploy\\data\\winequality-red.csv')

X = df.drop('quality',axis=1)
Y = df['quality'].apply(lambda y_value: 1 if y_value >= 7 else 0)

from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import warnings
warnings.simplefilter('ignore')

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

model = RandomForestClassifier()
model.fit(X_train, Y_train)
save = pickle.dump(model,open('model.pkl','wb'))
# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
pred=model.predict([[7.3,0.65,0.0,1.2,0.065,15.0,21.0,0.9946,3.39,0.47,10.0]])
