import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn.metrics import mean_squared_error

#file path of the data
file_path = "/home/panther/Downloads/train.csv"

#making pandas data frame
Data = pd.read_csv(file_path)

#Identify Columns That Contain a Single Value
Data.nunique()[Data.nunique()==1]

#checking whether the coloumns contain more than 70% null values
Data.columns[((Data.isnull().sum()/Data.shape[0])*100)>70]
#deleting coloumns containg more than 70% of null values
Data_removed_null = Data.drop(['Alley', 'PoolQC', 'Fence', 'MiscFeature'],axis=1)

#this coloumn contains more than 90% of the single value so we are delinting this columns
Data_removed_null['Street'].value_counts()
Data_removed_null['Utilities'].value_counts()
Data_removed_null['CentralAir'].value_counts()
Data_updated = Data_removed_null.drop(['Street','Utilities','CentralAir'],axis=1)

#checking for duplicate rows and deleting them
Data_updated.drop_duplicates(inplace=True)

#to find columns whcih caontaing more than 70% of single values
for i in Data.columns:
    print(Data[i].value_counts()[(((Data[i].value_counts())/Data.shape[0]*100)>70)])

#this coloumn contains more than 70% of the single values
Data_updated = Data_updated.drop(['MSZoning','LandContour','Condition1','BldgType','RoofStyle','RoofMatl','ExterCond','LotConfig','LandSlope','Condition2','BsmtCond','BsmtFinType2','Heating','Electrical','LowQualFinSF','BsmtHalfBath','KitchenAbvGr','Functional','GarageQual','GarageCond','PavedDrive','EnclosedPorch','3SsnPorch','PoolArea','MiscVal','SaleType','SaleCondition'],axis=1)

#missing values more than 50 percentage
num_missing = (Data_updated[Data_updated.columns] == 0).sum()
#checking coloummns which conatin more than 50% of values
missing_value_columns =  Data_updated.columns[num_missing>500]
Data_updated = Data_updated.drop(missing_value_columns,axis=1)

#removing coloumns which contain more null values 
Data_updated = Data_updated.drop('FireplaceQu',axis=1)


#filling nan values with there coloumn mean
Data_updated.fillna(Data_updated.mean(), inplace=True)
print(Data_updated.shape)

#labeling categorial variabes with numbers
labels = Data_updated['LotShape'].astype('category').cat.categories.tolist()
replace_map_comp = {'LotShape' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

#making a copy of the data frame
Data_updated_replace = Data_updated.copy()

#replacing the categorial varialbs
Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['Neighborhood'].astype('category').cat.categories.tolist()
replace_map_comp = {'Neighborhood' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['HouseStyle'].astype('category').cat.categories.tolist()
replace_map_comp = {'HouseStyle' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['Exterior1st'].astype('category').cat.categories.tolist()
replace_map_comp = {'Exterior1st' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['Exterior2nd'].astype('category').cat.categories.tolist()
replace_map_comp = {'Exterior2nd' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['MasVnrType'].astype('category').cat.categories.tolist()
replace_map_comp = {'MasVnrType' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['ExterQual'].astype('category').cat.categories.tolist()
replace_map_comp = {'ExterQual' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['Foundation'].astype('category').cat.categories.tolist()
replace_map_comp = {'Foundation' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['BsmtQual'].astype('category').cat.categories.tolist()
replace_map_comp = {'BsmtQual' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['BsmtExposure'].astype('category').cat.categories.tolist()
replace_map_comp = {'BsmtExposure' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['BsmtFinType1'].astype('category').cat.categories.tolist()
replace_map_comp = {'BsmtFinType1' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['HeatingQC'].astype('category').cat.categories.tolist()
replace_map_comp = {'HeatingQC' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['GarageType'].astype('category').cat.categories.tolist()
replace_map_comp = {'GarageType' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['GarageFinish'].astype('category').cat.categories.tolist()
replace_map_comp = {'GarageFinish' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

labels = Data_updated['KitchenQual'].astype('category').cat.categories.tolist()
replace_map_comp = {'KitchenQual' : {k: v for k,v in zip(labels,list(range(1,len(labels)+1)))}}
print(replace_map_comp)

Data_updated_replace.replace(replace_map_comp, inplace=True)

Data_updated_replace = Data_updated_replace.dropna()

# train data set 
train_data = Data_updated_replace.head(n=1168)

# X and y values to fit model 
features = [x for x in train_data.columns if x not in ['SalePrice']]
X = train_data[features]
y = train_data['SalePrice']

# fitting X and y values 
reg = LinearRegression().fit(X.values, y.values)

# regression score 
print(reg.score(X, y))

# test data set 
test_data = Data_updated_replace[-292:]

# values of X and y for test data 
features = [x for x in test_data.columns if x not in ['SalePrice']]
X_test = test_data[features]
y_test = test_data['SalePrice']

# predicting values of test data
y_hat = reg.predict(X_test.values)
print(y_hat)
print(y_test)
print(mean_squared_error(y_test.values,y_hat,multioutput='raw_values'))

