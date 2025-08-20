from winemag_data import reviews

print(reviews)

''' NATIVE ACCESS METHODS
Native Python objects provide good ways of indexing data. Pandas carries all of these over, which helps make it easy to start with.
'''
print("Accessing a column by label\n")
print(reviews.country)  # Accessing a column by label

print("\n\nAccessing a column by label with brackets\n")
print(reviews['country'])  # Accessing a column by label with brackets

print("\n\nAccessing multiple columns by label \n")
print(reviews[['country', 'points']])  # Accessing multiple columns by label

print("\n\nSlicing rows by index position \n")
print(reviews[0:3])  # Slicing rows by index position

print("\n\nFiltering rows based on a condition \n")
print(reviews[reviews.country == 'Italy'])  # Filtering rows based on a condition

print("\n\nFiltering rows based on a condition \n")
print(reviews[reviews.points > 90])  # Filtering rows based on a condition

print("\n\nFiltering rows based on multiple conditions \n")
print(reviews[reviews.country.isin(['Italy', 'France'])])  # Filtering rows based on multiple conditions

print("\n\nAccessing specific rows and columns using .loc \n")
print(reviews.loc[0:3, ['country', 'points']])  # Accessing specific rows and columns using .loc

print("\n\n \n")
print(reviews.iloc[0]) # Accessing the first row using .iloc index-based selection

print("\n\nAccessing the last 5 rows using .iloc \n")
print(reviews.iloc[-5:])  # Accessing the last 5 rows using .iloc

print("\n\nAccessing specific rows and columns using .iloc \n")
print(reviews.iloc[:3, 0])  # Accessing specific rows and columns using .iloc

print("\n\nAccessing specific rows and a single column using .iloc \n")
print(reviews.iloc[0:3, 0])  # Accessing specific rows and a single column using .iloc

print("\n\nAccessing specific rows and multiple columns using .iloc \n")
print(reviews.iloc[0:3, [0, 1]])  # Accessing specific rows and multiple columns using .iloc

print("\n\nAccessing specific rows and columns \n")
print(reviews.iloc[[0, 1, 2], [0, 1]])  # Accessing specific rows and columns

print("\n\nAccessing specific rows and a single column using .iloc \n")
print(reviews.iloc[[0, 1, 2], 0])  # Accessing specific rows and a single column using .iloc

print("\n\nAccessing specific rows and multiple columns using .iloc \n")
print(reviews.iloc[[0, 1, 2], [0, 1]])  # Accessing specific rows and multiple columns using .iloc

print("\n\nAccessing specific rows and columns using .iloc \n")
print(reviews.iloc[0:3, 0:2])  # Accessing specific rows and columns using .iloc

# Manipulating index
print("\n\nManipulating index \n")
print(reviews.set_index("title")) # Displaying the index of the DataFrame