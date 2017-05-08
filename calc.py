#test predictor
import score
import pickle
import find_price
import yelp_api
import numpy as np
import pprint
import score

def process(coord_lat="", coord_long="", city=""):
    with open("restaurant_data.dat", "rb") as f:
        previous_restaurants = pickle.load(f)
        #print(previous_restaurants)
    previous_restaurants = previous_restaurants[-10:]
    x_vals = np.array([1,2,3,4,5,6,7,8,9,10])
    y_vals = np.array([a[1] for a in previous_restaurants])

    price = int(find_price.find_best_next(x_vals,y_vals))
    print('price: ',price)
    print(city)
    if city == "":
        businesses = yelp_api.get_nearby_restaurants(coord_lat,coord_long)
    else:
        print("searching sittyS")
        businesses = yelp_api.get_nearby_restaurants(city=city)
    #print(businesses)
    scorelist = []
    businesslist = []
    for business in businesses:
        #pprint.pprint(business)
        try:
            if business['price'].count('$') <= price + 1 and business['price'].count('$') >= price - 1:
                print(business['name'], score.calculate_score(yelp_api.convertFormat(business)))
                scorelist.append(score.calculate_score(yelp_api.convertFormat(business)))
                businesslist.append(business)
        except:
            # this means that the business does not have an entry for "price" 
            pass
    nblist = []
    
    for i in range(3):
        print(scorelist)
        try:
            index = scorelist.index(max(scorelist))
            nblist.append(businesslist[index])
            businesslist.pop(index)
            scorelist.pop(index)
        except:
            nblist.append(None)
        
    #print(nblist)
    return nblist
