import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn import linear_model
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import StandardScaler

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

reg = linear_model.RidgeCV(alphas=[0.1, 1.0, 10.0])
reg.fit(X_train, y_train)

ytest_pred = reg.predict(X_test)
print(ytest_pred)

print("alpha_ ", reg.alpha_)
print("Intercept= ", reg.intercept_)
print("Coeff= ", reg.coef_)
