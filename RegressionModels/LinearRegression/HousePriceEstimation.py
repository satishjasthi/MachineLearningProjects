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
from sklearn.preprocessing import RobustScaler
import math
from sklearn.metrics import mean_absolute_error


file_path ="/home/panther/Downloads/train.csv"

Raw_data = pd.read_csv(file_path,index_col='Id')

# Some of the non-numeric predictors are stored as numbers; convert them into strings 
Raw_data['MSSubClass'] = Raw_data['MSSubClass'].apply(str)
Raw_data['YrSold'] = Raw_data['YrSold'].astype(str)
Raw_data['MoSold'] = Raw_data['MoSold'].astype(str)
Raw_data['YearBuilt'] = Raw_data['YearBuilt'].astype(str)
Raw_data['YearRemodAdd'] = Raw_data['YearRemodAdd'].astype(str)

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
    

#removing outliers in catogorial features by vitulizing
data = data.drop(data[(data['GrLivArea'] > 4000)
                                  & (data['SalePrice'] < 200000)].index)
data = data.drop(data[(data['GarageArea'] > 1200)
                                  & (data['SalePrice'] < 200000)].index)
data = data.drop(data[(data['TotalBsmtSF'] > 3000)
                                  & (data['SalePrice'] > 320000)].index)    

#adding new features
data['GrgQual'] = (data['GarageType'] + data['GarageFinish'])
data['TotalQual'] = data['OverallQual']  + data['KitchenQual'] + data['HeatingQC']
data['TotalBsmQual'] = (data['BsmtQual'] + data['BsmtFinType1'])
data['YearBlRm'] = (data['YearBuilt'] + data['YearRemodAdd'])
data['TotalPorchSF'] = (data['OpenPorchSF']+ data['WoodDeckSF'])
data['TotalBathrooms'] = (data['FullBath'] +(0.5 * data['FullBath']) +data['BsmtFullBath'] )
data['TotalSF'] = (data['BsmtFinSF1'] + data['1stFlrSF'] + data['2ndFlrSF'])


#droping features which are merged
col_merged = ['GarageType','GarageFinish','OverallQual','KitchenQual','HeatingQC','BsmtQual','BsmtFinType1','YearBuilt','YearRemodAdd','OpenPorchSF','WoodDeckSF','FullBath','FullBath','BsmtFullBath','BsmtFinSF1','1stFlrSF','2ndFlrSF']
data = data.drop(col_merged,axis=1)

num_col = data.columns[(data.dtypes == 'object')==False]

#removing outliers in numarical features
for i in num_col:
    min_thersold,max_thersold = data[i].quantile([0.001,0.95])
    final_data = data[(data[i]<max_thersold) & (data[i]>min_thersold)]   




# spliting the data frame into train data and test data 
train_data,test_data =  sklearn.model_selection.train_test_split(final_data)


# X and y values to fit model 
X_train =  train_data.drop('SalePrice',axis = 1)
Y_train = train_data['SalePrice']


# values of X and y for test data 
X_test = test_data.drop('SalePrice',axis = 1)
y_test = test_data['SalePrice']

#x and y values for robust
X_train_robust = X_train.copy()
X_test_robust = X_test.copy()

num_col = num_col.drop('SalePrice')

#srobust scaling for numarical columns
X =  X_train_robust[num_col].values
transformer = RobustScaler().fit(X)
X_train_robust = transformer.transform(X)

#fitting model 
reg = LinearRegression().fit(X_train_robust, Y_train.values)

print(reg.score(X_train_robust, Y_train))


Xt =  X_test_robust[num_col].values
transformer = RobustScaler().fit(Xt)
X_test_robust = transformer.transform(Xt)

y_hat = reg.predict(X_test_robust)

#plot between y_hat and y values got by robust 
plt.scatter(range(len(y_test.values)),y_test.values)
plt.plot(range(len(y_hat)),y_hat)
mean_squared_error(y_test, y_hat, squared=False)
num_data = X_test.shape[0]
mse = mean_squared_error(y_test,y_hat)
rmse = math.sqrt(mse/num_data)
rse = math.sqrt(mse/(num_data-2))
mae=mean_absolute_error(y_test,y_hat)

print('mse=',mse)
print('RSE=',rse)
print('rmse=',rmse)
print('mae=',mae)
plt.show()