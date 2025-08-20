from winemag_data import reviews

# To get data in the order want it in we can sort it ourselves. The sort_values()
countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print("\n Number of reviews per country and province sorted by length \n")
print(countries_reviewed.sort_values(by='len'))

''' sort_values() defaults to an ascending sort, where the lowest values go first. 
However, most of the time we want a descending sort, where the higher numbers go first. '''
print("\n Number of reviews per country and province sorted by length in descending order \n")
# To sort in descending order, we can pass the ascending=False argument to sort_values().
print(countries_reviewed.sort_values(by='len', ascending=False))

''' sort by index values, use the companion method sort_index(). This method has the same arguments and default orde
'''
print("\n Number of reviews per country and province sorted by index \n")
print(countries_reviewed.sort_index())

''' If we want to sort by multiple columns, we can pass a list of column names to the by argument.
This will sort by the first column, then by the second column, and so on.
'''
print("\n Number of reviews per country and province sorted by country and province \n")
print(countries_reviewed.sort_values(by=['country', 'province']))