from winemag_data import reviews

# Renaming Index and Columns
# The rename() method is used to rename the index or columns of a DataFrame.
print(reviews.head())
print("\n Renaming index and columns using rename() method \n")
print(reviews.rename(columns={'points':'score'}))

# The rename() method can also be used to rename the index.
print("\n Renaming index using rename() method \n")
print(reviews.rename(index={0:'first', 1:'second', 2:'third'}))

# The rename() method can also be used to rename both the index and columns at the same time.
print("\n Renaming both index and columns using rename() method \n")
print(reviews.rename(index={0:'first', 1:'second', 2:'third'}, columns={'points':'score', 'price':'cost'}))

# Rename the index and columns using the set_axis() method
print("\n Renaming index and columns using rename_axis() method \n")
print(reviews.rename_axis("wines", axis='rows').rename_axis("fields", axis='columns'))