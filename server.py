import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, svm, tree
from sklearn.linear_model import LinearRegression
import socket
import pickle
import pprint


categories = []
price = []
rating = []

with open("user_data.dat", "rb") as f:
    restaurants = pickle.load(f)

pprint.pprint(restaurants)

print("\n\n\n\n\n\n")

for restaurant in restaurants:
    categories.append([restaurant['categories'][alias]['alias'] for alias in range(len(restaurant['categories']))])
    price.append(restaurant['price'].count('$'))
    rating.append(restaurant['rating']*10)
print(categories)

rest = [categories,price]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(rest, rating)

def get_new_rating(mrate):
    rating_pred = clf.predict(mrate)
    print(rating_pred)


get_new_rating(["mexican breakfast_brunch",1])
