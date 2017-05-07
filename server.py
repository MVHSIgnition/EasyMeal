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
        best_restaurants = calc.process(message.message['latitude'],message.message['longitude'])
        loc = best_restaurants[0]['location']
        name = best_restaurants[0]['name']
        rating = best_restaurants[0]['rating']
        price = best_restaurants[0]['price']
        image = best_restaurants[0]['image_url']
        loc1 = best_restaurants[1]['location']
        name1 = best_restaurants[1]['name']
        rating1 = best_restaurants[1]['rating']
        price1 = best_restaurants[1]['price']
        image1 = best_restaurants[1]['image_url']
        loc2 = best_restaurants[2]['location']
        name2 = best_restaurants[2]['name']
        rating2 = best_restaurants[2]['rating']
        price2 = best_restaurants[2]['price']
        image2 = best_restaurants[2]['image_url']
        print(name,name1,name2)
        pubnub.publish().channel('main_channel').message([{"name":name,"rating":rating,"price":price,"loc":loc,"image":image}, {"name":name1,"rating":rating1,"price":price1,"loc":loc1,"image":image1}, {"name":name2,"rating":rating2,"price":price2,"loc":loc2,"image":image2}]).async(publishCallback)
    


pubnub.add_listener(subscribeCallback())
pubnub.subscribe().channels('secondary_channel').execute()


while True:
    pass
