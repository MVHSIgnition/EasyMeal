import pickle

with open("restaurant_data.dat", "rb") as f:
    rl = pickle.load(f)
rl = rl[:-1]
with open("restaurant_data.dat", "wb") as f:
    pickle.dump(rl,f)
