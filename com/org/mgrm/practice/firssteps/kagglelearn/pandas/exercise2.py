import pandas as pd

from winemag_data import reviews

#Create a variable df containing the country, province, region_1, and region_2 columns of the records
# with the index labels 0, 1, 10, and 100. In other words, generate the following DataFrame:
df = pd.DataFrame({"country": reviews.country,
                   "province": reviews.province,
                   "region_1": reviews.region_1,
                   "region_2": reviews.region_2},
                 index=[0,1,10,100])

#Create a variable df containing the country and variety columns of the first 100 records.
df = pd.DataFrame({"country":reviews.country.iloc[0:100],
                   "variety":reviews.variety.iloc[0:100]})

#Create a DataFrame italian_wines containing reviews of wines made in Italy. Hint: reviews.country equals what?
italian_wines = pd.DataFrame(reviews.loc[reviews.country == 'Italy'])


#Create a DataFrame top_oceania_wines containing all reviews with at least 95 points (out of 100) for wines from Australia or New Zealand.
top_oceania_wines = pd.DataFrame(reviews.loc[ (reviews.country.isin(['Australia','New Zealand'])) & (reviews.points >= 95) ])