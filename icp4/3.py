import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn import metrics
iris= pd.read_csv('iris.csv') #loading iris dataset
X_train,X_test = train_test_split(iris,test_size=0.2) # splitting data into training and test using cross validation
X_train1=X_train
X_train1=X_train1.drop(['class'],axis=1)
X_test1=X_test
X_test1=X_test1.drop(['class'],axis=1)
print(X_train1)
print("-----------------")
print(X_train['class'])
clf=svm.SVC(kernel='rbf')  #svc classifier using rbf kernal
clf.fit(X_train1,X_train['class'])
x=clf.predict(X_test1)
print("train accuracy",clf.score(X_train1,X_train['class'])) #calculating score on training data
print("test accuracy",clf.score(X_test1,X_test['class']))    #calculating score on test data