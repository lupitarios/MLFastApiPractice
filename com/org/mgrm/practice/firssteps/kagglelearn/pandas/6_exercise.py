import pandas as pd

from winemag_data import reviews

print(reviews.head())

''' region_1 and region_2 are pretty uninformative names for locale columns in the dataset. Create a copy of reviews
 with these columns renamed to region and locale, respectively. 
'''
renamed = reviews.rename(columns={'region_1':'region', 'region_2':'locale'})

# Check the first few rows of the renamed DataFrame
print("\n Renamed DataFrame:\n")
print(renamed.head())

''' Set the index name in the dataset to wines.'''
renamed = reviews.rename_axis("wines")

''' The Things on Reddit dataset includes product links from a selection of top-ranked forums ("subreddits") 
on reddit.com. Run the cell below to load a dataframe of products mentioned on the /r/gaming subreddit and 
another dataframe for products mentioned on the r//movies subreddit.
'''
gaming = pd.read_csv("gaming.csv", index_col=0)
movies = pd.read_csv("movies.csv", index_col=0)

''' Rename the index of the gaming DataFrame to gaming_products and the index of the movies DataFrame to movie_products.'''
combined_products = pd.concat([gaming,movies])

''' Both tables include references to a `MeetID`, a unique key for each meet (competition) included in the database. 
Using this, generate a dataset combining the two tables into one.
'''
#powerlifting_combined = powerlifting_meets.set_index('MeetID').join(powerlifting_competitors.set_index('MeetID'))