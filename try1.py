import pandas as pd
import numpy as np
from pandas import plotting
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression, LogisticRegression, 
from sklearn.cross_validation import train_test_split
import matplotlib.pyplot as plt
from sklearn import metrics
from math import sqrt

df = pd.read_csv('data.csv',index_col=0)
y = df['IR']
x = df[['GDP','UR','CPI','NFP','NHS','CU','CCI','NAPM', 'UNL','RS']]
y = y.astype('int')

linreg = LogisticRegression()
linreg.fit(x,y)

y_pred = linreg.predict(x)

print('Coefficients: \n', linreg.coef_)
print("Mean squared error: %.2f"
      % mean_squared_error(y, y_pred))
print('Variance score: %.2f' % r2_score(y, y_pred))
rms = sqrt(mean_squared_error(y, y_pred))
print(x,y_pred)
#print(x,y)


