#step 1 data exploration
import os
import pandas as pd

print("\n\n*** step 1: data exploration ***\n")
melbourne_file_path = '..\\introml\\input\\melb_data.csv'

workd_directory = os.getcwd()
print("Current Working Directory:", os.getcwd())
print("melbourne_file_path:", melbourne_file_path)
path_file = workd_directory + melbourne_file_path

if os.path.exists(melbourne_file_path):
    print("melbourne_file_path to:", melbourne_file_path)
    melbourne_data = pd.read_csv(melbourne_file_path)
    print("file loaded successfully")
    print(melbourne_data.describe())  #summary statistics
else:
    print("File not found:", melbourne_file_path)
'''
if os.access(melbourne_file_path, os.R_OK):
    print("File is readable")
else:
    print("File is not readable")
'''