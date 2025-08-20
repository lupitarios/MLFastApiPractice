import pandas as pd

from winemag_data import reviews

print("\n Reviews with no country \n")
print(reviews[pd.isnull(reviews.country)]) # returns all rows where the country column is null

#Replacing Missing Values
print("\n Replacing missing values in the country column with 'Unknown' \n")
print(reviews.region_2.fillna('Unknown')) # fillna() replaces all null values in the region_2 column with 'Unknown'

# Replace a non value with a value
print("\n Replacing non-null value  in the taster_twitter_handle column with kerino \n")
print(reviews.taster_twitter_handle.replace("@kerinokeefe", "@kerino"))

'''
The replace() method is worth mentioning here because it's handy for replacing missing data which 
is given some kind of sentinel value in the dataset: things like "Unknown", "Undisclosed", "Invalid"
'''
n_missing_prices = reviews.price.isnull().sum()

missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)

n_missing_prices = pd.isnull(reviews.price).sum()