import numpy as np
import pandas as pd
import math
import csv
from sklearn.ensemble import RandomForestRegressor

from sklearn import preprocessing
from sklearn import linear_model
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_squared_error



dataset = pd.read_csv("train.csv")
dataset_test  = pd.read_csv("test.csv")
testID = dataset_test["ID"]
dataset_test  = dataset_test.drop("ID",axis=1)
X = dataset.drop(["ID","Horizontal_Distance_To_Fire_Points"],axis=1)

d = X.shape[0]
d1 = dataset_test.shape[0]
ones = np.ones((d,1))
ones1 = np.ones((d1,1))

X['Bias'] = ones
dataset_test['Bias'] = ones1
Y = dataset["Horizontal_Distance_To_Fire_Points"]
X = X.iloc[:,:].values
Y = Y.iloc[:].values
Xtest = dataset_test.values




from sklearn.ensemble import RandomForestRegressor


regr = RandomForestRegressor(max_depth=30,n_estimators=200,min_samples_split = 2,min_samples_leaf= 1,oob_score=True,n_jobs =-1,max_features = 5,random_state=60)
regr.fit(X, Y)
kfold = KFold(n_splits=10, shuffle=True, random_state=1)
#cv_results = cross_val_score(regr, X,Y, cv= kfold)
y_pred=regr.predict(X)
from sklearn.metrics import mean_squared_error
#RMSE
RMSE=np.sqrt(mean_squared_error(y_pred,Y))
print(RMSE)
r2=regr.score(X, Y)
print(r2)
test_pred = regr.predict(Xtest)


r = testID.shape[0]
path = "submitFinalRF.csv"
with open(path,"w") as c:
    writer = csv.writer(c,delimiter=',')
    csv_head = ["ID","Horizontal_Distance_To_Fire_Points"]
    writer.writerow(csv_head)
    r = testID.shape[0]
    for i in range(r):
        csv_row = [str(testID[i]),str(test_pred[i])]
        writer.writerow(csv_row)
