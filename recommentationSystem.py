import numpy as np
from fetch_lastfm import fetch_lastfm

from lightfm.datasets import fetch_movielens
from lightfm.datasets import fetch_stackexchange
from lightfm import LightFM

def sample_recommendation(mode, data, user_ids):
    #number of users and movies in training data
    n_users, n_items = data['train'].shape

    #generate recommendation for each user we input
    for user_id in user_ids:
        #movies they already like
        indices = data['train'].tocsr()[user_id].indices
        known_positives = data['item_labels'][indices]

        #movies our model predicts they will like
        scores = model.predict(user_id, np.arange(n_items))
        #rank them in order of most liked to least
        top_items = data['item_labels'][np.argsort(-scores)]

        #print out the results
        print("User %s" % user_id)
        print("\tKnown positiives:")

        for x in known_positives[:3]:
            print("\t\t%s" % x)

        print("\tRecommended:")

        for x in top_items[:3]:
            print("\t\t%s" % x)


#fetch data and format it
# data = fetch_movielens(min_rating=4.0)
data = fetch_lastfm()

#print training and testing data
print(repr(data['train']))
print(repr(data['test']))

#create model
model = LightFM(loss='warp')

#train model
model.fit(data['train'], epochs=30, num_threads=2)

sample_recommendation(model, data, [3, 25, 450])
