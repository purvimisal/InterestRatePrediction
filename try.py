import pandas as pd
import numpy as np
from pandas import plotting
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from sklearn import metrics
from math import sqrt


df = pd.read_csv('data.csv',index_col=0)
y = df['IR']
x = df[['GDP','UR','CPI','NFP','NHS','CU','CCI','NAPM', 'UNL','RS']]
#y = y.astype('int')
#train test split
#X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = 0.3)

linreg = LinearRegression()
linreg.fit(x,y)


#logreg = LogisticRegression()
#logreg.fit(X_train, y_train)

y_pred = linreg.predict(x)

print('Coefficients: \n', linreg.coef_)
# The mean squared error
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y, y_pred))
rms = sqrt(mean_squared_error(y, y_pred))
print(y_pred)

#print(mean_squared_error(y_test,ytest_pred))
#print(y_test)

#plotting.scatter_matrix(df[['IR','GDP','UR','CPI','NFP','CCI','NAPM','UNL','CU','RS']])   

#plt.scatter(X_test, y_test, color='black')
plt.plot(x, y_pred, color='yellow', linewidth=1)
plt.xticks(())
plt.yticks(())
#plt.show()
#print(y_test.shape)
#print(X_test.shape)
#print(linreg.score(y_test, ytest_pred))
#print(ytest_pred.shape)
print(rms)
print(y_pred)

