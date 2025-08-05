#step 2: selection and modeling using pandas
import pandas as pd

print("\n\n*** step 2: selection and modeling using pandas ***\n")

melbourne_file_path = '..\\introml\\input\\melb_data.csv'
melbourne_data = pd.read_csv(melbourne_file_path)
print(melbourne_data.describe())  # summary statistics

print(melbourne_data.columns)  #    print(melbourne_data.describe())  #summary statistics
melbourne_data = melbourne_data.dropna(axis=0)  # drop rows with missing values
print("after dropping missing values \n", melbourne_data.describe())  # summary statistics after dropping missing values
print(melbourne_data.columns)  # print columns after dropping missing values

y = melbourne_data.Price  # target variable  prediction target.
print("\n\nPrice y: \n", y)

melbourne_features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']  # features to use for prediction
X = melbourne_data[melbourne_features]  # features dataframe
print("\n\nX: \n", X)
print("\nSummary Statistics\n",X.describe())  # summary statistics of features
print("\nHEAD\n",X.head()) #shows the top few rows