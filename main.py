#test predictor
import score
import pickle
import find_price

with open("restaurant_file.dat", "rb") as f:
    previous_restaurants = pickle.load(f)
previous_restaurants = previous_restaurants[-10:]
x_vals = np.array([1,2,3,4,5,6,7,8,9,10])
y_vals = np.array([a[1] for a in previous_restaurants])

price = find_price.find_best_next(x_vals,y_vals)
