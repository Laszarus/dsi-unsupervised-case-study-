# BIGFOOT!!!

![alt text](http://groomsadvice.com/wp-content/uploads/2010/07/bigfoot-monster-truck.jpg "Bigfoot Truck")

or 

![alt text](https://dehayf5mhw1h7.cloudfront.net/wp-content/uploads/sites/816/2019/06/07102723/Big-Foot-1-832-832x476.jpg "Bigfoot Creature")

????

## Loading the Data

Data was originally in a json format that contained a 487 html files.  Thse files were parsed for the ID information and html text.  Beatuiful soup was used to identify the paragraph of interest which contained the title ‘field’ .  For each document in the download, the field identifiers were parsed into their own dictionaries with the keys representing the fields.  These dictionaries were then converted into a single pandas dataframe that was used for EDA.

### The Columns:
* _submitted:_  
* _title:_ 
* _year:_ 
* _season:_	
* _month:_ 
* _state:_ 
* _county:_
* _location details:_
* _nearest town:_
* _nearest road:_
* _observed:_
* _also noticed:_
* _other witnesses:_
* _other stories:_
* _time and conditions:_
* _enviornment:_


## Exploratory Data Analysis

## Topic modeling

We tries Clustering as well as Latent Dirichlet Allocation in order to discover hidden topics in the data. These analyses were applied over  the "observed" , "
