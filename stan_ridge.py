import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from math import sqrt
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

df = pd.read_csv('data.csv',index_col=0)
y = df['IR']
x = df[['GDP','UR','CPI','NFP','NHS','CU','CCI','NAPM', 'UNL','RS']]
#y = y.astype('int')
scaler = StandardScaler().fit(x)
rescaledX = scaler.transform(x)
np.set_printoptions(precision=3)
x= rescaledX
#train test split
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = 0.3)

reg = linear_model.BayesianRidge()
reg.fit(X_train, y_train)

ytest_pred = reg.predict(X_test)
print(ytest_pred)


print('Coefficients: \n', reg.coef_)
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, ytest_pred))
print('Variance score: %.2f' % r2_score(y_test, ytest_pred))
rms = sqrt(mean_squared_error(y_test, ytest_pred))
print('Root mean sq error: %.2f' % rms)
print('Mean absolute error score: %.2f' % mean_absolute_error(y_test, ytest_pred))
