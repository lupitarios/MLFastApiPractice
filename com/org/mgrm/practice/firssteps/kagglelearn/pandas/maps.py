from winemag_data import reviews

#map
print("\n map \n")
'''return a transformed version of that value
returns a new Series where all the values have been transformed by your function.
'''
review_points_mean = reviews.points.mean()
print("Mean of points:", review_points_mean)
maps_results = reviews.points.map(lambda p: p - review_points_mean)
print("\n map results \n",maps_results)

#apply
print("\n apply \n")
''' apply a function along an axis of the DataFrame or on values in Series.
is the equivalent method if we want to transform a whole DataFrame by calling a custom method on each row. '''
def remean_points(row):
    row.points = row.points - review_points_mean
    return row

apply_results = reviews.apply(remean_points, axis='columns')
print("\n apply results \n", apply_results)

'''If we had called reviews.apply() with axis='index', then instead of passing a function to transform each row, 
we would need to give a function to transform each column.
'''

#Pandas mapping operations as built-ins.
print("\n Pandas mapping operations as built-ins \n")
# faster way of remeaning our points column
review_points_mean = reviews.points.mean()
mean_results_2 = reviews.points - review_points_mean
print("\n mean_results_2 \n", mean_results_2)

print("\n Series of equal length combination \n")
print(reviews.country + " - " + reviews.region_1)

''' These operators are faster than map() or apply() because they use speed ups built into pandas. 
 the standard Python operators (>, <, ==, and so on) work in this manner.
 they are not as flexible as map() or apply(), which can do more advanced things, like applying conditional logic, 
 which cannot be done with addition and subtraction alone.
'''
def star_classification(row):
    if row.points >= 95 or row.country == 'Canada':
        return 3
    if row.points >= 85 and row.points < 95:
        return 2
    return 1

star_ratings = reviews.apply(star_classification, axis='columns')