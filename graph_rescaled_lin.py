import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.cross_validation import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
from math import sqrt
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv',index_col='KEY')
y = df['IR']
x = df[['GDP','UR','CPI','NFP','NHS','CU','CCI','NAPM', 'UNL','RS']]
#y = y.astype('int')
#print(x)
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(x)
x = rescaledX
#train test split
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size = 0.3,stratify = None)

#linreg = LinearRegression()
#linreg.fit(X_train, y_train)

linreg = LinearRegression()
linreg.fit(X_train, y_train)

ytest_pred = linreg.predict(X_test)


#ytest_pred.reset_index()
#print(ytest_pred)
#print(y_test)
#print(metrics.accuracy_score(y_test, ytest_pred))
print('Coefficients: \n', linreg.coef_)
print("Mean squared error: %.2f"
      % mean_squared_error(y_test, ytest_pred))
print('Variance score: %.2f' % r2_score(y_test, ytest_pred))
rms = sqrt(mean_squared_error(y_test, ytest_pred))
print('Root mean sq error: %.2f' % rms)
print('Mean absolute error score: %.2f' % mean_absolute_error(y_test, ytest_pred))


xyz = pd.DataFrame(ytest_pred, columns=["PREDIR"])
xx= xyz.reset_index()
print(xx.head(3))
z1 = xx['index'].tolist()
l1 = xx['PREDIR'].tolist()
#plt.plot(z1, l1)
#plt.xlabel('index')
#plt.ylabel('PREDIR')
#plt.legend().set_visible(True)
# plt.legend()
#plt.title("Prediction and Test Data")
#plt.show()


yy= y_test.reset_index()
yy1= yy.reset_index()
print(yy1.head(3))
zz1 = yy1['KEY'].tolist()
ll1 = yy1['IR'].tolist()
#plt.plot(zz1, ll1)
#plt.xlabel('index')
#plt.ylabel('IR')
#plt.legend().set_visible(True)
# plt.legend()
#plt.title("Prediction and Test Data")
#plt.show()

result = pd.merge(xx,yy1, on='index')
print(result.head(3))
keyx = result['KEY'].tolist()
ir1 = result['IR'].tolist()
ir2 = result['PREDIR'].tolist()
plt.plot(keyx, ir1)
#plt.plot(keyx, ir2)
plt.xlabel('index')
plt.ylabel('PRED & IR')
plt.legend().set_visible(True)
# plt.legend()
plt.title("Prediction and Test Data")
plt.show()

