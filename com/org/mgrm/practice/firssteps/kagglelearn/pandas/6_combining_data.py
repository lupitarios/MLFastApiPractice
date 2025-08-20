import pandas as pd

canadian_youtube = pd.read_csv("data\\CAvideos.csv")
british_youtube = pd.read_csv("data\\GBvideos.csv")

# Concatenating DataFrames
# The concat() function is used to concatenate two or more DataFrames along a particular axis (
# rows or columns). By default, it concatenates along the rows (axis=0).
print("\n Concatenating Canadian and British YouTube DataFrames \n")
print(pd.concat([canadian_youtube, british_youtube]))

# Combining different DataFrame objects which have an index in common, we can use the join() method.
# The join() method combines two DataFrames based on their index.
print("\n Joining Canadian and British YouTube DataFrames on index \n")
left = canadian_youtube.set_index(['title', 'trending_date'])
right = british_youtube.set_index(['title', 'trending_date'])
print(left.join(right, lsuffix='_CA', rsuffix='_GB'))