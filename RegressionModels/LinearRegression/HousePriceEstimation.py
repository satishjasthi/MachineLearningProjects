import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import sklearn
from pathlib import Path

file_path = (Path().cwd()/f'Data/train.csv')

Raw_data = pd.read_csv(file_path)

#checking whether the coloumns contain more than 70% null values
null_value_sum = Raw_data.isnull().sum()
total_num_rows = Raw_data.shape[0]

#missing values more than 50 percentage
num_missing = (Raw_data[Raw_data.columns] == 0).sum()
# columns having 70%null values and 50% more missing values 
null_missingValues_columns =  Raw_data.columns[((null_value_sum/total_num_rows)>0.70) | (num_missing>500) ]

#deleting null values and missing values
Data0 = Raw_data.drop(null_missingValues_columns,axis=1)

#checking columns having more than 70%single values
fx = lambda x : max(Data0[x].value_counts())/Data0.shape[0]>.70
single_value_columns = []
for i in Data0.columns:
    if list(map(fx ,[i]))==[True]:
         single_value_columns.append(i)

# Deleting single_value columns
Data0 = Data0.drop(single_value_columns,axis=1)

#filling nan values with there coloumn mean
Data0.fillna(Data0.mean(), inplace=True)

#filling nan values with there coloumn mean
Data0.fillna(Data0.mean(), inplace=True)

#deleting null values
Data0 = Data0.dropna()

#converting cato variables into labels
cato_columns = Data0.columns[Data0.dtypes == 'object']

# function to convert catogorial variables with numarical variables
def cat2numeric(col:pd.Series)->None:
    """
    Convert catg column values to numeric values using 
    sklearns LabelEncoder
    """
    le = preprocessing.LabelEncoder()
    num_values = le.fit_transform(col.values)
    col.replace(col.values,num_values, inplace=True)
    
#mapping catogorial columns with catcat2numeric function    
list(map(cat2numeric, [Data0[x] for x in cato_columns]))

# spliting the data frame into train data and test data 
train_data =  sklearn.model_selection.train_test_split(Data0)[0]
test_data = sklearn.model_selection.train_test_split(Data0)[1]

# X and y values to fit model 
features = [x for x in train_data.columns if x not in ['SalePrice']]
X = train_data[features]
y = train_data['SalePrice']
# fitting X and y values 
reg = LinearRegression().fit(X.values, y.values)

# regression score 
print(reg.score(X, y))

# values of X and y for test data 
features = [x for x in test_data.columns if x not in ['SalePrice']]
X_test = test_data[features]
y_test = test_data['SalePrice']

# predicting values of test data
y_hat = reg.predict(X_test.values)

print(mean_squared_error(y_test.values,y_hat,multioutput='raw_values'))