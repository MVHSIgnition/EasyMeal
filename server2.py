import sys
try:
    sys.path.append('/opt/python3/lib/python3.4/site-packages')
except:
    pass
import yelp_api
import pickle
import calc

pub_key = 'pub-c-2c436bc0-666e-4975-baaf-63f16a61558d'
sub_key = 'sub-c-0442432a-3312-11e7-bae3-02ee2ddab7fe'
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
pnconfig = PNConfiguration()
pnconfig.subscribe_key = sub_key
pnconfig.publish_key = pub_key
pubnub = PubNub(pnconfig)

def publishCallback(result, status):
    pass

class subscribeCallback(SubscribeCallback):
    def status(self, pubnub, status):
        pass
    def presence(self, pubnub, presence):
        pass  # handle incoming presence data
    def message(self, pubnub, message):
        if message.message['cmdtype'] == "request":
            
            try:
                best_restaurants = calc.process(message.message['latitude'],message.message['longitude'])
            except:
                print(message.message)
                print(message.message['city'].replace("%20", "+"))
                best_restaurants = calc.process(city=message.message['city'].replace("%20", "+"))
            review = yelp_api.get_business_review(best_restaurants[0]['id'])
            review1 = yelp_api.get_business_review(best_restaurants[1]['id'])
            review2 = yelp_api.get_business_review(best_restaurants[2]['id'])
            id1 = best_restaurants[0]['id']
            id2 = best_restaurants[1]['id']
            id3 = best_restaurants[2]['id']
            loc = best_restaurants[0]['location']
            name = best_restaurants[0]['name']
            rating = best_restaurants[0]['rating']
            price = best_restaurants[0]['price']
            image = best_restaurants[0]['image_url']
            url = best_restaurants[0]['url']
            loc1 = best_restaurants[1]['location']
            name1 = best_restaurants[1]['name']
            rating1 = best_restaurants[1]['rating']
            price1 = best_restaurants[1]['price']
            image1 = best_restaurants[1]['image_url']
            url1 = best_restaurants[1]['url']
            loc2 = best_restaurants[2]['location']
            name2 = best_restaurants[2]['name']
            rating2 = best_restaurants[2]['rating']
            price2 = best_restaurants[2]['price']
            image2 = best_restaurants[2]['image_url']
            url2 = best_restaurants[2]['url']
            print(name,name1,name2)
            pubnub.publish().channel('main_channel').message([{"name":"U R HACKED GO TO PORNHUB.COM","rating":rating,"price":price,"loc":loc,"image":image,"url":url, "review":review, "id":id1},
                                                              {"name":name1,"rating":rating1,"price":price1,"loc":loc1,"image":image1,"url":url1, "review":review1, "id":id2}, 
                                                              {"name":name2,"rating":rating2,"price":price2,"loc":loc2,"image":image2,"url":url2, "review":review2, "id":id3}]).async(publishCallback)
        elif message.message['cmdtype'] == "append":
            print("new restaurant received")
            with open("restaurant_data.dat", "rb") as f:
                rl = pickle.load(f)
            rl.append(yelp_api.convertFormat(yelp_api.get_business_by_id(message.message['id'])))
            with open("restaurant_data.dat", "wb") as f:
                pickle.dump(rl,f)


pubnub.add_listener(subscribeCallback())
pubnub.subscribe().channels('secondary_channel').execute()


while True:
    pass
