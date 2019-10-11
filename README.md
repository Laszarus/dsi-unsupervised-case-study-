# BIGFOOT!!!

![alt text](http://groomsadvice.com/wp-content/uploads/2010/07/bigfoot-monster-truck.jpg "Bigfoot Truck")

or 

![alt text](https://dehayf5mhw1h7.cloudfront.net/wp-content/uploads/sites/816/2019/06/07102723/Big-Foot-1-832-832x476.jpg "Bigfoot Creature")

????

## Loading the Data

Data was originally in a json format that contained 487 html files.  Thse files were parsed for the ID information and html text.  Beatuiful soup was used to identify the paragraph of interest which contained the title ‘field’ .  For each document in the download, the field identifiers were parsed into their own dictionaries with the keys representing the fields.  These dictionaries were then converted into a single pandas dataframe that was used for EDA.

![alt text](https://github.com/scottfeldmanpeabody/dsi-unsupervised-case-study/blob/master/images/dataframe.png "df")

### The Columns:
* __submitted:__ when the sighting was submitted to the website
* __title:__ title of sighting
* __year:__ year of sighting
* __season:__	season of sighting (sorta)
* __month:__ month of sighting
* __state:__ state in which sighting occurred
* __county:__ county in which sighting occurred
* __location details:__ details of where the sighting was
* __nearest town:__ nearest town to sighting
* __nearest road:__ nearest road to sighting
* __observed:__ account of what was observed
* __also noticed:__ in case they didn't finish writing what was above...maybe?
* __other witnesses:__ who else was there
* __other stories:__ inconsistent. Often it's none/nan. Sometimes it's other people who have sighted bigfoot, or other times this observer has seen bigfoot.
* __time and conditions:__ when and what was the weather like during observations
* __enviornment:__ physical description of where sighting occurred

## Exploratory Data Analysis

EDA and data exploration:
No duplicates were identified in the final data frame.  Bigfoot sightings by year (with non integer values dropped) showed that sightings started in the early 1800s and really took off in the 1970s and peaked in the early 2000s.
![](images/bigfoot_year.png)

Sightings by month and compared to season title showed that summer and early fall were the peak seasons for Bigfoot sightings (and that many people categorize month and season differently).
![](images/count_by_month.png)

Plotting data by state showed that Rhode Island had the fewest sightings and California had the most.

Conjectures based off the geographic perspective: bigfoot sighting reports are higher in states with large populations and large wooded areas
![alt text](https://github.com/scottfeldmanpeabody/dsi-unsupervised-case-study/blob/master/images/sightings_by_state.png "by state")

## Topic modeling

Prior to modeled, we applWe applied Clustering as well as Latent Dirichlet Allocation to the modelin order to discover hidden topics in the data. These analyses were applied over several columns including "observed" , "enviroment", "time and conditions", "other stories", and "also noticed." 

We noticed most of the results came out the same. We did not observe any more clarity from LDA vs. Clustering. Also, even though the examples below all show 5 different topics, we tried greater and fewer topics (from 2-10). Changing the number of topics did not yield any clearer results.

With the standard list of English stop words, many of the observations were the same:

_observations_ with standard English stop words:
1. night, sound, feet, tree, away, creature, got, went, left, large
2. went, got, night, looked, feet, away, sound, didn, thought, right
3. feet, got, mountain, tracks, way, camp, big, came, looked, old
4. looked, feet, went, large, night, got, creature, tall, seen, away
5. lake, forest, feet, near, night, summer, tent, kootenay, left, sasquatch

So, we augmented the standard list of English stop words with our own stop words. The result was that the latent topics still looked very similar, but with different words:

_observations_ with augmented stop words:
1. lake, feet, tracks, left, forest, mr, thought, bear, mountain, night
2. got, night, feet, away, sound, thought, didn, right, know, started
3. feet, large, got, creature, night, tall, seen, away, sound, thought
4. night, sound, tree, feet, got, camp, away, didn, left, trail
5. old, good, man, feet, got, came, water, rifle, day, way

In some cases, such as with _conditions_, we did not feel it was appropriate to remove words that showed up in many topics because these words were descriptive of what was going on (e.g. clear, night, sunny...):

Example latent clusters on _time and conditions_:
1. night, clear, moon, light, dark, 00, weather, 30, 10, late
2. clear, weather, morning, pm, sunny, 30, skies, warm, light, 00
3. day, sunny, clear, afternoon, bright, 00, pm, mid, early, summer
4. dark, clear, light, 30, weather, 00, pm, night, moon, evening
5. 30, 00, morning, pm, afternoon, early, light, sunny, 10, weather

There are similar results for _enviroment_, where clusters all sound the same:
1. ridge, campground, farm, south, land, forest, east, hill, creek, york
2. wooded, river, pine, lake, near, swamp, land, heavily, mountain, hills
3. trees, pine, river, lots, lake, forest, creek, brush, large, oak
4. forest, pine, lake, river, creek, near, dense, mountain, old, lots
5. creek, wooded, near, river, large, runs, mile, pine, old, heavily

Interestingly, though no one has ever captured a clear picture of Bigfoot, words like 'misty' or 'hazy' or something else connotating poor visibility do not show up as common words in any of the top words of these latent topics.

## Discussion

The fact that the latent topics all come out sounding similar may be seen as a null result for this study, or it could be looked at an analysis that all these accountings of Bigfoot are very similar to each other. Maybe too similar to each other? Either Bigfoot always appears in more or less the same way in the same conditions

Oh, and the data set was definitely about Bigfoot the Sasquatch, not Bigfoot the Monster Truck.
