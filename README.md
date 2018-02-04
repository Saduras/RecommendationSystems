# RecommendationSystems

Based on the tutorial and coding challenge from Siray Raval: https://github.com/llSourcell/recommender_system_challenge

## Dependencies

- numpy (http://www.numpy.org/)
- scipy (https://www.scipy.org/)
- lightfm (https://github.com/lyst/lightfm)

## lastfm

I choose to use [the lastFM data set from grouplens](https://grouplens.org/datasets/hetrec-2011/). 

`fetch_lastfm` reads the data set from a downloaded zip file, parse and convert it to work for the recommendation system.
