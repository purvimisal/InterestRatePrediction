import pandas as pd
import numpy as np
from sklearn import metrics
from sklearn.linear_model import LinearRegression, LogisticRegression
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

#linreg = LinearRegression()
#linreg.fit(X_train, y_train)


logreg = LogisticRegression()
logreg.fit(X_train, y_train)

ytest_pred = logreg.predict(X_test)
print(ytest_pred)
#print(y_test)
#print(metrics.accuracy_score(y_test, ytest_pred))
