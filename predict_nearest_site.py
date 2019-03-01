import numpy as np
import pandas as pd
import math
import csv

from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.model_selection import KFold, cross_val_score, train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.linear_model import LassoCV
#%load data
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
#%data preprocessing
X[:,0:9] = preprocessing.scale(X[:,0:9])
Xtest[:,0:9] = preprocessing.scale(Xtest[:,0:9])
ohe = OneHotEncoder(sparse = False,categories='auto',handle_unknown='ignore')
X_dummies  = ohe.fit_transform(X[:,9].reshape(-1,1))
Xtest_dummies = ohe.transform(Xtest[:,9].reshape(-1,1))
X = X[:,0:9]
X  = np.hstack((X,X_dummies,ones))
Xtest = Xtest[:,0:9]
Xtest = np.hstack((Xtest,Xtest_dummies,ones1))



# resultCV = []
# alphas = np.linspace(0, 20, num=30)
# for apha in alphas:
#     kfold = KFold(n_splits=10, shuffle=True, random_state=1)
#     regRidge = linear_model.Ridge(alpha = apha)
#     cv_results = cross_val_score(regRidge, X1,Y, cv= kfold)
#     resultCV.append(cv_results.mean())
#     print("cv"+str(cv_results.mean()))
#



poly = PolynomialFeatures(degree=4)
X = poly.fit_transform(X)
Xtest= poly.fit_transform(Xtest)
regRidgeCv = linear_model.RidgeCV(alphas=[1e-3, 1e-2, 1e-1, 1,10], cv=4,normalize=False)
regRidgeCv.fit(X,Y)

predictionCv = regRidgeCv.predict(Xtest)

r = testID.shape[0]
path = "submitFinal.csv"
with open(path,"w") as c:
    writer = csv.writer(c,delimiter=',')
    csv_head = ["ID","Horizontal_Distance_To_Fire_Points"]
    writer.writerow(csv_head)
    r = testID.shape[0]
    for i in range(r):
        csv_row = [str(testID[i]),str(predictionCv[i])]
        writer.writerow(csv_row)







# for d in degree:
#     poly = PolynomialFeatures(degree= int (d))
#     X = poly.fit_transform(X)
#     kfold = KFold(n_splits=10, shuffle=True, random_state=1)
#     regRidge = linear_model.Ridge(alpha = 0.5)
#     cv_results = cross_val_score(regRidge, X,Y, cv= kfold)
#     resultCV.append(cv_results.mean())
#     print("cv"+str(cv_results.mean()))









# alphas = np.linspace(0, 20, num=30)
# ridgeScores = []
# for apha in alphas:
#     regRidge = linear_model.Ridge(alpha = apha)
#     regRidge.fit(trainX,trainY)
#     ridgeScores.append(regRidge.score(testX,testY))
#     print("regRidge "+ str(regRidge.score(testX,testY)))
#     # plt.plot(ridgeScores)
#     # plt.xlabel("regularizer")
#     # plt.ylabel("accuracy")
#
#
#     regRidge.predict(Xtest)
