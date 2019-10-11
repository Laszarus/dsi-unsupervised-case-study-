# BIGFOOT!!!

![alt text](http://groomsadvice.com/wp-content/uploads/2010/07/bigfoot-monster-truck.jpg "Bigfoot Truck")

or 

![alt text](https://dehayf5mhw1h7.cloudfront.net/wp-content/uploads/sites/816/2019/06/07102723/Big-Foot-1-832-832x476.jpg "Bigfoot Creature")

????

## Loading the Data

Data was originally in a json format that contained 487 html files.  Thse files were parsed for the ID information and html text.  Beatuiful soup was used to identify the paragraph of interest which contained the title ‘field’ .  For each document in the download, the field identifiers were parsed into their own dictionaries with the keys representing the fields.  These dictionaries were then converted into a single pandas dataframe that was used for EDA.

![a;t text](https://github.com/scottfeldmanpeabody/dsi-unsupervised-case-study/blob/master/images/dataframe.png "df")

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

## Topic modeling

We tries Clustering as well as Latent Dirichlet Allocation in order to discover hidden topics in the data. These analyses were applied over  the "observed" , "enviroment", "time and conditions", "other stories", and "also noticed"
