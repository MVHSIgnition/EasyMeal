import pandas as pd
import numpy as np
from sklearn import preprocessing, cross_validation, svm, tree
from sklearn.linear_model import LinearRegression
import socket
import pickle
import pprint
import urllib.request
import json

# assign numbers to the categories
target_url = 'https://www.yelp.com/developers/documentation/v2/all_category_list/categories.json'
with urllib.request.urlopen(target_url) as url:
    data = json.loads(url.read().decode())

category_dict = {}

for i, category in enumerate(data):
    category_dict[category['alias']] = i
    

details = [] #categories and price of restaurant
price = []
rating = []

with open("user_data.dat", "rb") as f:
    restaurants = pickle.load(f)

#pprint.pprint(restaurants)

print("\n\n\n\n\n\n")

for restaurant in restaurants:
    details.append([])
    for i in range(3):
        try:
            details[-1].append(category_dict[restaurant['categories'][i]['alias']])
        except IndexError:
            details[-1].append(category_dict[restaurant['categories'][0]['alias']])

    #category = [category_dict[category['alias']] for category in restaurant['categories']]
    details[-1].append(restaurant['price'].count('$'))
    #print([ord(char) - 96 for char in categories[0]])
    #print(categories[0])
    #price.append(restaurant['price'].count('$'))
    rating.append(int(restaurant['rating'] * 10))
print(details)
print(rating)

#rest = [categories,price]
#print(rest)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(details, rating)

def get_new_rating(mrate):
    rating_pred = clf.predict(mrate)
    print(rating_pred)


get_new_rating([269, 828, 1152,3])
