from winemag_data import reviews

print(reviews)

print("Before assing new value to 'critic' column\n")
#print(reviews['critic'])

reviews['critic'] = 'everyone'
print("\nAfter assing new value to 'critic' column\n")
print(reviews['critic'])

# with an iterable of values:
reviews['index_backwards'] = range(len(reviews), 0, -1)
print("\n\nAdding a new column 'index_backwards' with values from range(len(reviews), 0, -1)\n")
print(reviews['index_backwards'])

