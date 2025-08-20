from winemag_data import reviews

# groupby() operation
# We can replicate what value_counts() does by doing the following:
print(reviews.groupby('points').points.count())

'''We can use any of the summary functions we've used before with this data. For example, to get
the cheapest wine in each point value category, we can do the following:
'''
print("\n Minimum price for each points category \n")
# This will return a Series with the points as the index and the minimum price for each point
print(reviews.groupby('points').price.min())

''' Each group we generate as being a slice of our DataFrame containing only data with values that match. 
This DataFrame is accessible to us directly using the apply() method, and we can then manipulate the data 
in any way we see fit. '''
print("\n First wine of each winery \n")
print(reviews.groupby('winery').apply(lambda df: df.title.iloc[0])) # First wine of each winery

''' Group by more than one column. '''
print(reviews.groupby['country', 'province'].apply(lambda df: df.loc[df.points.idxmax()])) # Best wine of each country/province combination

''' agg(), which lets you run a bunch of different functions on your DataFrame simultaneously. '''
print("\n Aggregating price by country \n")
print(reviews.groupby(['country']).price.agg([len, min, max]))