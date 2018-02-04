# RecommendationSystems

Based on the tutorial and coding challenge from Siray Raval: https://github.com/llSourcell/recommender_system_challenge

## Dependencies

- numpy (http://www.numpy.org/)
- scipy (https://www.scipy.org/)
- lightfm (https://github.com/lyst/lightfm)

## lastfm

I choose to use [the lastFM data set from grouplens](https://grouplens.org/datasets/hetrec-2011/). 

`fetch_lastfm` reads the data set from a downloaded zip file, parse and convert it to work for the recommendation system.

Output:
```
User 3
	Known positiives:
		Pleq
		Segue
		Max Richter
	Recommended:
		Burzum
		Piero Umiliani
		Tim Hecker
User 25
	Known positiives:
		Kylie Minogue
		Madonna
		Lady Gaga
	Recommended:
		Britney Spears
		Christina Aguilera
		Katy Perry
User 450
	Known positiives:
		Porcupine Tree
		Pink Floyd
		Blackfield
	Recommended:
		Iron Maiden
		Led Zeppelin
		Pink Floyd
```
