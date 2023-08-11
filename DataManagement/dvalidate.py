import pandas as pd
import numpy as np

#Function to check data integrity
def data_integrity(data):
    #Check for missing values
    if data.isnull().values.any():
        print("Data contains missing values")
 
    #Check for duplicate rows
    unique_rows = data.drop_duplicates()
    if len(unique_rows) != len(data):
        print("Data contains duplicate rows")
    
    #Check for outliers
    data_mean = np.mean(data)
    data_std = np.std(data)
    lower_limit = data_mean - 3*data_std
    upper_limit = data_mean + 3*data_std
    outlier_count = 0
    for i in range(len(data)):
        if (data[i] < lower_limit or data[i] > upper_limit):
            outlier_count += 1
    if outlier_count > 0:
        print("Data contains {} outliers".format(outlier_count))
        
#Function to check data validity
def data_validity(data, data_type):
    valid_data = 0
    invalid_data = 0
    for i in range(len(data)):
        try:
            if type(data[i]) == data_type:
                valid_data += 1
            else:
                invalid_data += 1
        except:
            invalid_data += 1
    if invalid_data > 0:
        print("Data contains {} invalid entries".format(invalid_data))
    else:
        print("All data is valid")

#Main function
if __name__ == "__main__":
    #Read the data
    data = pd.read_csv("data.csv")
    
    #Check data integrity
    data_integrity(data)
    
    #Check data validity
    data_validity(data, int)