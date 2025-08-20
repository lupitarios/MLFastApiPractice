from winemag_data import reviews

#A multi-index differs from a regular index in that it has multiple levels.

countries_reviewed = reviews.groupby(['country', 'province']).description.agg([len])
print("\n Number of reviews per country and province \n")
print(countries_reviewed)

mi = countries_reviewed.index
print("\n MultiIndex object type: ")
print(type(mi))

''' Multi-indices have several methods for dealing with their tiered structure which are absent for single-level indices. 
They also require two levels of labels to retrieve a value.'''
# The multi-index method you will use most often is the one for converting back to a regular index, the reset_index() method
countries_reviewed_reset = countries_reviewed.reset_index()
print("\n After reset_index() \n")
print(countries_reviewed_reset)