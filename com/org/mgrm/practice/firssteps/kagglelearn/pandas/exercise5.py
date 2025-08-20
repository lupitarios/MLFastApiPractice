from winemag_data import reviews

#What is the data type of the `points` column in the dataset?
print("\n Data type of points column \n")
dtype = reviews.points.dtype

#Create a Series from entries in the `points` column, but convert the entries to strings. Hint: strings are `str` in native Python.
point_strings = reviews.points.astype('str')

#Sometimes the price column is null. How many reviews in the dataset are missing a price?
missing_prices = reviews[reviews.price.isnull()].shape[0]

''' What are the most common wine-producing regions? Create a Series counting the number of times each value 
occurs in the `region_1` field. This field is often missing data, so replace missing values with `Unknown`. 
Sort in descending order. 
'''
reviews_per_region = reviews.region_1.fillna('unknown').sort_values(ascending=False).value_counts()