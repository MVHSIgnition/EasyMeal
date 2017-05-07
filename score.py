#return score of restaurant
#[ [categories], price, rating, name, address ]
import pickle

def calculate_score(restaurant):
    score = 1
    with open("restaurant_file.dat", "rb") as f:
        previous_restaurants = pickle.load(f)
    previous_restaurants = previous_restaurants[-10:]
    category_list = []
    for r in previous_restaurants:
        for cat in r[0]:
            category_list.append(cat)
    for category in restaurant[0]:
        score += category_list.count(category)

    score *= restaurant[2]
    
