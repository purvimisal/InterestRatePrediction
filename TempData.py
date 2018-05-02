from urllib.request import urlopen
import matplotlib.pyplot as plt
import pandas
import quandl
import time
import datetime
#from functools import reduce

time.sleep(60)

ccidata = quandl.get("OECD/KEI_CSCICP02_USA_ST_M")
finccidata = ccidata.reset_index()
finccidata1 = finccidata.rename(columns={"Value": "cci"})
print(finccidata1.head())

finccidata1.to_csv("finalinputccidata.csv", sep=",", header=True)