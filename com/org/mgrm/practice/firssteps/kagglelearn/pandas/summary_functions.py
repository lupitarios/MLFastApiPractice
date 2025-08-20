from winemag_data import reviews

#restructure the data in some useful way
print("describe() method shows a quick statistic summary of your data\n")
print(reviews.describe())

print("\n\nIt is type-aware, meaning that its output changes based on the data type of the input. \n")
print(reviews.taster_name.describe())

print("\n\n to see the mean of the points allotted \n")
print(reviews.points.mean())

print("\n\n To see a list of unique values we can use the unique() \n")
print(reviews.taster_name.unique())

print("\n\n To see a list of unique values and how often they occur in the dataset, we can use the value_counts() \n")
print(reviews.taster_name.value_counts())