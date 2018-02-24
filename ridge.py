import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn import linear_model
from sklearn.cross_validation import train_test_split

df = pd.read_csv('data.csv',index_col=0)
y = df['IR']
x = df[['GDP','UR','CPI','NFP','NHS','CU','CCI','NAPM', 'UNL','RS']]
y = y.astype('int')
#train test split
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = 0.3)

reg = linear_model.BayesianRidge()
reg.fit(X_train, y_train)

ytest_pred = reg.predict(X_test)
print(ytest_pred)

print("Coeff= ", reg.coef_)
#print("Intercept= ", reg.intercept_)