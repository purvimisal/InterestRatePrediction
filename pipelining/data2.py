#from urllib.request import urlopen
import matplotlib.pyplot as plt
import pandas as pd
import quandl
#from functools import reduce

fingdpdata = pd.read_csv("finalinputgdpdata.csv",names=['date','gdp'])
finulcbsdata = pd.read_csv("finalinputuldata.csv",names=['date','ulc'])

print(finulcbsdata.head())
print(finulcbsdata.shape)
print(fingdpdata.head())
print(fingdpdata.shape)

df1 = fingdpdata.merge(finulcbsdata,on='date')

print(df1.head())
print(df1.shape)


finintdata = pd.read_csv("finalinputintdata.csv",names=['date','ir'])
print(finintdata.head())

df2 = df1.merge(finintdata,on='date')
print(df2.head())

fincpidata = pd.read_csv("finalinputcpidata.csv",names=['date','cpi'])
print(fincpidata.head())

df3 = df2.merge(fincpidata,on='date')
print(df3.head())

finnhsdata = pd.read_csv("finalinputnhsdata.csv",names=['date','nhs'])
print(finnhsdata.head())

df4 = df3.merge(finnhsdata,on='date')
print(df4.head())

fincudata = pd.read_csv("finalinputtcudata.csv",names=['date','cu'])
print(fincudata.head())

df5 = df4.merge(fincudata,on='date')
print(df5.head())


finrsafsdata = pd.read_csv("finalinputrsafsdata.csv",names=['date','rs'])
print(finrsafsdata.head())

df6 = df5.merge(finrsafsdata,on='date')
print(df6.head())

finpmidata = pd.read_csv("finalinputpmidata.csv",names=['date','napm'])
print(finpmidata.head())

df7 = df6.merge(finpmidata,on='date')
print(df7.head())


finnfpdata = pd.read_csv("finalinputnfpdata.csv",names=['date','nfp'])
print(finnfpdata.head())

df8 = df7.merge(finnfpdata,on='date')
print(df8.head())

finurdata = pd.read_csv("finalinputurdata.csv",names=['date','ur'])
print(finurdata.head())

df9 = df8.merge(finurdata,on='date')
print(df9.head())

finccidata = pd.read_csv("newtempccidata2.csv",names=['date','cci'])
print(finccidata.head())

dffinal = df9.merge(finccidata,on='date')
print(dffinal.head())
dffinal.to_csv("FinalDataSet.csv", sep=",", header=True)
