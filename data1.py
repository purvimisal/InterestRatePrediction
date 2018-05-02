from urllib.request import urlopen
import matplotlib.pyplot as plt
import pandas
import quandl
import time
import datetime
#from functools import reduce

time.sleep(60)

def add_one_month(t):
    """Return a `datetime.date` or `datetime.datetime` (as given) that is
    one month earlier.

    Note that the resultant day of the month might change if the following
    month has fewer days:

        >>> add_one_month(datetime.date(2010, 1, 31))
        datetime.date(2010, 2, 28)
    """
    import datetime
    one_day = datetime.timedelta(days=1)
    one_month_later = t + one_day
    while one_month_later.month == t.month:  # advance to start of next month
        one_month_later += one_day
    target_month = one_month_later.month
    while one_month_later.day < t.day:  # advance to appropriate day
        one_month_later += one_day
        if one_month_later.month != target_month:  # gone too far
            one_month_later -= one_day
            break
    return one_month_later



#https://www.quandl.com/data/FRED/GDP-Gross-Domestic-Product (QUARTERLY) (GDP)
#GDP
#gdpdata = quandl.get("FRED/GDP", start_date="2001-12-31", end_date="2005-12-31")
gdpdata = quandl.get("FRED/GDP")
print(type(gdpdata))
print(gdpdata.shape)
print(gdpdata.head())

#C:\Users\vivekm\PycharmProjects\tests1
gdpdata.to_csv("inputgdpdata", sep=",", header=False)

filename = 'inputgdpdata'
list = []
l = []
newlist = []
f = open("newgdp.csv", 'w')
file = open(filename, 'r')

for line in file:
    line = line.strip('\n')

    l.append(line)

for i in l:
    list.append(i)
length = len(list)

newlist.append(list[0])

for i in range(0,length-1):
        vnextitem = (list[i+1].split(","))
        vcurrentitem = (list[i].split(","))

        diff = float(vnextitem[1]) - float(vcurrentitem[1])
        a = diff / 3.0
        b = float(vcurrentitem[1]) + a
        c = float(vcurrentitem[1]) + 2*a

        mydate=datetime.datetime.strptime(vcurrentitem[0], '%Y-%m-%d').date()
        x=add_one_month(mydate)
        y=add_one_month(x)

        newlist.append(x.strftime('%Y-%m-%d')+","+str(b))
        newlist.append(y.strftime('%Y-%m-%d') + "," + str(c))
        newlist.append(list[i+1])
        i = i+1

for i in newlist:
    f.writelines(str(i)+"\n")
fingdpdata = pandas.read_csv("newgdp.csv",names=['Date','gdp'])
print(type(fingdpdata))
print(fingdpdata.head())
print(fingdpdata.shape)

#plt.xlabel('Year')
#plt.xlabel('Date')
#plt.ylabel('Value')
#plt.legend().set_visible(False)
#plt.show()
#ndf = fingdpdata.merge(finulcbsdata,on='date')
time.sleep(60)

#https://www.quandl.com/data/FRED/ULCBS-Business-Sector-Unit-Labor-Cost  Employment Cost Index (QUARTERLY) (UNL)
ulcbsdata = quandl.get("FRED/ULCBS")
print(type(ulcbsdata))
print(ulcbsdata.head())
print(ulcbsdata.shape)

ulcbsdata.to_csv("inputuldata", sep=",", header=False)

filename = 'inputuldata'
list = []
l = []
newlist = []
f = open("newul.csv", 'w')
file = open(filename, 'r')

for line in file:
    line = line.strip('\n')
    l.append(line)

for i in l:
    list.append(i)
length = len(list)

newlist.append(list[0])

for i in range(0,length-1):
        vnextitem = (list[i+1].split(","))
        vcurrentitem = (list[i].split(","))

        diff = float(vnextitem[1]) - float(vcurrentitem[1])
        a = diff / 3.0
        b = float(vcurrentitem[1]) + a
        c = float(vcurrentitem[1]) + 2*a

        mydate=datetime.datetime.strptime(vcurrentitem[0], '%Y-%m-%d').date()
        x=add_one_month(mydate)
        y=add_one_month(x)

        #newlist.append(list[i])
        newlist.append(x.strftime('%Y-%m-%d')+","+str(b))
        newlist.append(y.strftime('%Y-%m-%d') + "," + str(c))
        newlist.append(list[i+1])
        i = i+1

for i in newlist:
    f.writelines(str(i)+"\n")
finulcbsdata = pandas.read_csv("newul.csv",names=['Date','ulc'])
print(type(finulcbsdata))
print(finulcbsdata.head())
print(finulcbsdata.shape)

df1 = fingdpdata.merge(finulcbsdata,on='Date')
time.sleep(60)


#https://fred.stlouisfed.org/series/INTDSRUSM193N#0 Interest Rate (IR)
urlint = "https://fred.stlouisfed.org/graph/fredgraph.csv?chart_type=line&recession_bars=on&log_scales=&bgcolor=%23e1e9f0&graph_bgcolor=%23ffffff&fo=Open+Sans&ts=12&tts=12&txtcolor=%23444444&show_legend=yes&show_axis_titles=yes&drp=0&cosd=1950-01-01&coed=2017-04-01&height=450&stacking=&range=&mode=fred&id=INTDSRUSM193N&transformation=lin&nd=1950-01-01&ost=-99999&oet=99999&lsv=&lev=&mma=0&fml=a&fgst=lin&fgsnd=2009-06-01&fq=Monthly&fam=avg&vintage_date=&revision_date=&line_color=%234572a7&line_style=solid&lw=2&scale=left&mark_type=none&mw=2&width=1168"
intcsv = urlopen(urlint)
intdata = pandas.read_csv(intcsv, index_col=0, parse_dates=True)
finintdata = intdata.reset_index()
finintdata1 = finintdata.rename(columns={"INTDSRUSM193N": "ir", "DATE" : "Date"})
print(finintdata1.head())


df2 = df1.merge(finintdata1,on='Date')
time.sleep(60)

#https://www.quandl.com/data/FRED/CPIAUCSL-Consumer-Price-Index-for-All-Urban-Consumers-All-Items (CPI)
cpidata = quandl.get("FRED/CPIAUCSL")
fincpidata = cpidata.reset_index()
fincpidata1 = fincpidata.rename(columns={"Value": "cpi"})
print(fincpidata1.head())
#dfs = [gdpdata, cpidata]
#df_final = reduce(lambda left,right: pd.merge(left,right,on='Date'), dfs)
#print(df_final.head())

#ndf = df1.merge(df2,on='Date').merge(df3,on='Date')
#ndf = df1.merge(df2,on='Date')
#print(type(ndf))
#print(ndf.head())
#print(ndf.shape)

df3 = df2.merge(fincpidata1,on='Date')
time.sleep(60)



#https://www.quandl.com/data/FRED/HSN1F-New-One-Family-Houses-Sold-United-States (NHS)
#New Home Sales (NHS)
nhsdata = quandl.get("FRED/HSN1F")
finnhsdata = nhsdata.reset_index()
finnhsdata1 = finnhsdata.rename(columns={"Value": "nhs"})
print(finnhsdata1.head())

df4 = df3.merge(finnhsdata1,on='Date')
time.sleep(60)
#https://www.quandl.com/data/FRED/TCU-Capacity-Utilization-Total-Industry Capacity Utilization (CU)
tcudata= quandl.get("FRED/TCU")
fintcudata = tcudata.reset_index()
fintcudata1 = fintcudata.rename(columns={"Value": "cu"})
print(fintcudata1.head())

df5 = df4.merge(fintcudata1,on='Date')
time.sleep(60)

#https://www.census.gov/retail/marts/historic_releases.html  Retail Sales (RS)
rsafsdata= quandl.get("FRED/RSAFS")
finrsafsdata = rsafsdata.reset_index()
finrsafsdata1 = finrsafsdata.rename(columns={"Value": "rs"})
print(finrsafsdata1.head())

df6 = df5.merge(finrsafsdata1,on='Date')
time.sleep(60)

#https://www.quandl.com/data/ISM/MAN_PMI-PMI-Composite-Index NAPM Index (NAPM)
pmidata = quandl.get("ISM/MAN_PMI")
finpmidata = pmidata.reset_index()
finpmidata1 = finpmidata.rename(columns={"Value": "napm"})
print(finpmidata1.head())



df7 = df6.merge(finpmidata1,on='Date')
time.sleep(60)
#https://www.quandl.com/data/FRED/PAYEMS-All-Employees-Total-Nonfarm-Payrolls (NFP)
#Non Farm Payrolls
nfpdata = quandl.get("FRED/PAYEMS")
finnfpdata = nfpdata.reset_index()
finnfpdata1 = finnfpdata.rename(columns={"Value": "nfp"})
print(finnfpdata1.head())

df8 = df7.merge(finnfpdata1,on='Date')
time.sleep(60)

#https://www.quandl.com/data/FRED/UNRATE-Civilian-Unemployment-Rate Unemployment Rate (UR)
urdata = quandl.get("FRED/UNRATE")
finurdata = urdata.reset_index()
finurdata1 = finurdata.rename(columns={"Value": "ur"})
print(finurdata1.head())

df9 = df8.merge(finurdata1,on='Date')
time.sleep(60)

#https://www.quandl.com/data/OECD/KEI_CSCICP02_USA_ST_M-Consumer-confidence-indicator-s-a-United-States-Level-ratio-or-index-Monthly (QUARTERLY) (CCI)
#Consumer Confidence Index
ccidata = quandl.get("OECD/KEI_CSCICP02_USA_ST_M")
finccidata = ccidata.rename(columns={"Value": "cci"})
print(finccidata.head())

dffinal = df9.merge(finccidata,on='Date')
dffinal.to_csv("FinalDataSet", sep=",", header=True)