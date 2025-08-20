#Reading data files (csv)
import pandas as pd

sample_data_csv =  pd.read_csv("read_data.csv")  # Reading a CSV file into a DataFrame
print("Sample Data CSV:\n", sample_data_csv)  # Display the contents of the
# Check how large the DataFrame is
print("\nShape of Sample Data CSV:", sample_data_csv.shape)  # Print the shape

# Examine the first few rows of the DataFrame (5 default)
print("\nFirst 5 rows of Sample Data CSV:\n", sample_data_csv.head())  # Display the first 5 rows

#To make pandas use that column for the index (instead of creating a new one from scratch), we can specify an index_col.
wine_reviews = pd.read_csv("read_data.csv", index_col=0)  # Reading a CSV file with a custom index column
print("\nWine Reviews DataFrame with Custom Index:\n")  # Display the DataFrame with custom index
print(wine_reviews.head())  # Display the first 5 rows with the specified index column

