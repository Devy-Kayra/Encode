import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbr

from sklearn import preprocessing
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

dataset = pd.read_csv("country.csv")

country = dataset.iloc[: , 0:1].values

le = preprocessing.LabelEncoder()
oh = preprocessing.OneHotEncoder()

country[: , 0] = le.fit_transform(dataset.iloc[: , 0])
country = oh.fit_transform(country).toarray()

countryDf = pd.DataFrame(data = country , columns = ["Turkish" , "South Korean" , "Japanese"])
