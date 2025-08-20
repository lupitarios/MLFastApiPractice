from winemag_data import reviews

# The data type for a column in a DataFrame or a Series is known as the dtype.
# dtype of the price column in the reviews DataFrame:
print("\n Data type of price column \n")
print(reviews.price.dtypes)

# dtype of the entire reviews DataFrame:
print("\n Data types of all columns \n")
print(reviews.dtypes)

'''convert a column of one type into another wherever such a conversion makes sense by using the astype() function'''
print("\n Converting price column to string type \n")
print(reviews.points.astype('float64'))

# INDEX A DataFrame or Series index has its own dtype
print("\n Data type of the index \n")
print(reviews.index.dtype)