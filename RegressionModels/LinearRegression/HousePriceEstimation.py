import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
import sklearn
from pathlib import Path
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler


file_path = Path().cwd()/f'Data/train.csv'

Raw_data = pd.read_csv(file_path)

#checking whether the coloumns contain more than 70% null values
null_value_sum = Raw_data.isnull().sum()
total_num_rows = Raw_data.shape[0] 
missingValue_columns =  Raw_data.columns[(null_value_sum/total_num_rows)>0.7]

#deleting null value columns
data = Raw_data.drop(missingValue_columns,axis=1)

#checking columns having more than 70%single values
fx = lambda x : max(data[x].value_counts())/data.shape[0]>.70
single_value_columns = single_value_columns = list(filter(fx,data.columns))

# Deleting single_value columns
data = data.drop(single_value_columns,axis=1)

#filling nan values with there coloumn mean
data.fillna(data.mean(), inplace=True)



#finding cato variables into labels
cato_columns = data.columns[data.dtypes == 'object']
#numarical values columns
num_col = data.columns[(data.dtypes == 'object')==False]


#filling catogorial columns with their mode
for i in cato_columns:
    data[i].fillna(data[i].mode()[0],inplace=True)

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
list(map(cat2numeric, [data[x] for x in cato_columns]))

# spliting the data frame into train data and test data 
train_data,test_data =  sklearn.model_selection.train_test_split(data)


# X and y values to fit model 
X_train =  train_data.drop('SalePrice',axis = 1)
Y_train = train_data['SalePrice']

# fitting X and y values 
reg = LinearRegression().fit(X_train.values, Y_train.values)

# regression score 
print(reg.score(X_train, Y_train))

# values of X and y for test data 
X_test = test_data.drop('SalePrice',axis = 1)
y_test = test_data['SalePrice']

#x and y values for standardization
X_train_stand = X_train.copy()
X_test_stand = X_test.copy()

#removing saleprice columns because we dont want it to standardize
num_col = num_col.drop('SalePrice')

# function to standardize each column  
for i in num_col:
    
    # fit on training data column
    scale = StandardScaler().fit(X_train_stand[[i]])
    
    # transform the training data column
    X_train_stand[i] = scale.transform(X_train_stand[[i]])
    
    # transform the testing data column
    X_test_stand[i] = scale.transform(X_test_stand[[i]])

#fitting model 
reg = LinearRegression().fit(X_train_stand.values, Y_train.values)

print(reg.score(X_train_stand, Y_train))

# predicting values of test data
y_hat = reg.predict(X_test_stand.values)


print(mean_squared_error(y_test.values,y_hat,multioutput='raw_values'))

plt.scatter(range(len(y_test.values)),y_test.values)
plt.plot(range(len(y_hat)),y_hat)
plt.show()