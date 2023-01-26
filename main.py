# %% [markdown]
# Importing the Dependencies

# %%
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# %% [markdown]
# Data Collection and Processing

# %%
# loading the csv data to a Pandas DataFrame
heart_data = pd.read_csv("../dataset/heart.csv")

# %%
# print first 5 rows of the dataset
heart_data.head()

# %%
# print last 5 rows of the dataset
heart_data.tail()

# %%
# number of rows and columns in the dataset
heart_data.shape

# %%
# getting some info about the data
heart_data.info()

# %%
# checking for missing values
heart_data.isnull().sum()

# %%
# statistical measures about the data
heart_data.describe()

# %%
# checking the distribution of Target Variable
heart_data["target"].value_counts()

# %% [markdown]
# 1 --> Defective Heart
#
# 0 --> Healthy Heart

# %% [markdown]
# Splitting the Features and Target

# %%
X = heart_data.drop(columns="target", axis=1)
Y = heart_data["target"]

# %%
print(X)

# %%
print(Y)

# %% [markdown]
# Splitting the Data into Training data & Test Data

# %%
X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, stratify=Y, random_state=2
)

# %%
print(X.shape, X_train.shape, X_test.shape)

# %% [markdown]
# Model Training

# %% [markdown]
# Logistic Regression

# %%
model = LogisticRegression()

# %%
# training the LogisticRegression model with Training data
model.fit(X_train, Y_train)

# %% [markdown]
# Model Evaluation

# %% [markdown]
# Accuracy Score

# %%
# accuracy on training data
X_train_prediction = model.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction, Y_train)

# %%
print("Accuracy on Training data : ", training_data_accuracy)

# %%
# accuracy on test data
X_test_prediction = model.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction, Y_test)

# %%
print("Accuracy on Test data : ", test_data_accuracy)

# %% [markdown]
# Building a Predictive System

# %%
input_data = (62, 0, 0, 140, 268, 0, 0, 160, 0, 3.6, 0, 2, 2)

# change the input data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

prediction = model.predict(input_data_reshaped)
print(prediction)

if prediction[0] == 0:
    print("The Person does not have a Heart Disease")
else:
    print("The Person has Heart Disease")

# %% [markdown]
# Saving the trained model

# %%
import pickle

# %%
filename = "../models/heart_disease_model.sav"
pickle.dump(model, open(filename, "wb"))

# %%
# loading the saved model
loaded_model = pickle.load(open("../models/heart_disease_model.sav", "rb"))

# %%
for column in X.columns:
    print(column)
