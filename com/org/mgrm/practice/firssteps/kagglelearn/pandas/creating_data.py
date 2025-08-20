import pandas as pd

#DataFrame creation
''' A DataFrame is a table. It contains an array of individual entries, each of which has a certain value. 
Each entry corresponds to a row (or record) and a column.'''
dt = pd.DataFrame({'yes':[50, 21], 'no':[131, 2]})  # Create a DataFrame with two columns: 'yes' and 'no'
print(dt)  # Print the DataFrame

print("\n")  # Print a new line for better readability

dt_string = pd.DataFrame({'Bob':['I like it', 'It was awful'], 'Sue':['Pretty good', 'Bland']})  # Create a DataFrame with string values
print(dt_string)  # Print the DataFrame with string values

convention_dt = pd.DataFrame({'column1':['item1', 'item2', 'item3', '...'],
                              'column2':['item1', 'item2', 'item3', '...']})  # Create a DataFrame with a convention-like structure
print("\nStandard Convention DataFrame:\n", convention_dt)  # Print the convention-like DataFrame

# row labels is known as index
convention_dt_index = pd.DataFrame({'column1':['item1', 'item2', 'item3', '...'],
                              'column2':['item1', 'item2', 'item3', '...']},
                                index=['row1', 'row2', 'row3', '...'])

print("\nDataFrame with Custom Index:\n", convention_dt_index)  # Print the DataFrame with custom index
print("\n\nattribut column 1 \n", convention_dt.column1)
print("\n\nattribut column 1 - row 1\n", convention_dt["column1"][0])  # Access the first element of 'column1' using attribute access

# Series creation
''' A Series, It's a list. It is a one-dimensional array-like object that can hold any data type. '''
sr_int = pd.Series([1, 2, 3, 4, 5])  # Create a Series with integer values
print("\nSeries with Integer Values:\n", sr_int)  # Print the Series with

convention_sr_index = pd.Series([1, 2, 3, 4, 5], index=['indx1', 'indx2', 'indx3', 'indx4', 'indx5'], name= "Dinner")  # Create a Series with custom index
print("\nSeries with Custom Index:\n", convention_sr_index)  # Print the Series with custom index

print("\n Accesing index 0 from the series:\n")
#print(convention_sr_index[0])  # Access the first element of the Series