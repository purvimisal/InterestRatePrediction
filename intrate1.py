import tkinter as tk
from tkinter import *
#from urllib.request import urlopen
import matplotlib.pyplot as plt
import pandas as pd
#import quandl
from tkinter import messagebox
import datetime as dt
import matplotlib.dates as mdates
import matplotlib.image as mpimg

#dates = ['01/02/1991','01/03/1991','01/04/1991']
#x = [dt.datetime.strptime(d,'%m/%d/%Y').date() for d in dates]
#y = range(len(x)) # many thanks to Kyss Tao for setting me straight here
#Then plot:
#import matplotlib.pyplot as plt
#import matplotlib.dates as mdates
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
#plt.plot(x,y)
#plt.gcf().autofmt_xdate()


#### vk-start

#from tkFileDialog import askopenfilename

def gdp1():
#    gdpdata = quandl.get("FRED/GDP")
    gdpdata = pd.read_csv("finalinputgdpdata.csv", names=['date', 'gdp'])
    #gdpdata.plot(y='Value')
    gdpdata.plot(y='gdp')
    #plt.xlabel('Year')
    plt.xlabel('date')
    plt.ylabel('gdp')
    plt.legend().set_visible(False)
    plt.title("GDP Over the Years")
    plt.show()

def cpi1():
#    cpidata = quandl.get("FRED/CPIAUCSL")
    cpidata = pd.read_csv("finalinputcpidata.csv", names=['date', 'cpi'])
    cpidata.plot(y='cpi')
    plt.xlabel('date')
    plt.ylabel('cpi')
    plt.legend().set_visible(False)
    plt.title("CPI Over the Years")
    plt.show()

def nhs1():
#    nhsdata = quandl.get("FRED/HSN1F")
    nhsdata = pd.read_csv("finalinputnhsdata.csv", names=['date', 'nhs'])
    nhsdata.plot(y='nhs')
    plt.xlabel('date')
    plt.ylabel('nhs')
    plt.legend().set_visible(False)
    plt.title("NHS Over the Years")
    plt.show()

def tcu1():
#    tcudata = quandl.get("FRED/TCU")
    tcudata = pd.read_csv("finalinputtcudata.csv", names=['date', 'cu'])
    tcudata.plot(y='cu')
    plt.xlabel('date')
    plt.ylabel('cu')
    plt.legend().set_visible(False)
    plt.title("TCU Over the Years")
    plt.show()

def int1():
#    urlint = "https://fred.stlouisfed.org/graph/fredgraph.csv?chart_type=line&recession_bars=on&log_scales=&bgcolor=%23e1e9f0&graph_bgcolor=%23ffffff&fo=Open+Sans&ts=12&tts=12&txtcolor=%23444444&show_legend=yes&show_axis_titles=yes&drp=0&cosd=1950-01-01&coed=2017-04-01&height=450&stacking=&range=&mode=fred&id=INTDSRUSM193N&transformation=lin&nd=1950-01-01&ost=-99999&oet=99999&lsv=&lev=&mma=0&fml=a&fgst=lin&fgsnd=2009-06-01&fq=Monthly&fam=avg&vintage_date=&revision_date=&line_color=%234572a7&line_style=solid&lw=2&scale=left&mark_type=none&mw=2&width=1168"
#    intcsv = urlopen(urlint)
#    intdata = pd.read_csv(intcsv, index_col=0, parse_dates=True)
#    finintdata = intdata.rename(columns={"INTDSRUSM193N": "ir"})
    finintdata = pd.read_csv("finalinputintdata.csv", names=['date', 'ir'])
    finintdata.plot(y='ir')
    plt.xlabel('date')
    plt.ylabel('ir')
    plt.legend().set_visible(False)
    plt.title("Intrest Rates Over the Years")
    plt.show()


def rsa1():
#    rsafsdata = quandl.get("FRED/RSAFS")
    rsafsdata = pd.read_csv("finalinputrsafsdata.csv", names=['date', 'rs'])
    rsafsdata.plot(y='rs')
    plt.xlabel('date')
    plt.ylabel('rs')
    plt.legend().set_visible(False)
    plt.title("RSA Over the Years")
    plt.show()

def pmi1():
#    pmidata = quandl.get("ISM/MAN_PMI")
    pmidata = pd.read_csv("finalinputpmidata.csv", names=['date', 'napm'])
    pmidata.plot(y='napm')
    plt.xlabel('date')
    plt.ylabel('napm')
    plt.legend().set_visible(False)
    plt.title("PMI Over the Years")
    plt.show()

def ulcbs1():
#    ulcbsdata = quandl.get("FRED/ULCBS")
    ulcbsdata = pd.read_csv("finalinputuldata.csv", names=['date', 'ulc'])
    ulcbsdata.plot(y='ulc')
    plt.xlabel('date')
    plt.ylabel('ulc')
    plt.legend().set_visible(False)
    plt.title("ULCBS Over the Years")
    plt.show()

def ur1():
#    urdata = quandl.get("FRED/UNRATE")
    urdata = pd.read_csv("finalinputurdata.csv", names=['date', 'ur'])
    urdata.plot(y='ur')
    plt.xlabel('date')
    plt.ylabel('ur')
    plt.legend().set_visible(False)
    plt.title("UR Over the Years")
    plt.show()

def cci1():
#    ccidata = quandl.get("OECD/KEI_CSCICP02_USA_ST_M")
    ccidata = pd.read_csv("newtempccidata2.csv", names=['date', 'cci'])
    ccidata.plot(y='cci')
    plt.xlabel('date')
    plt.ylabel('cci')
    plt.legend().set_visible(False)
    plt.title("CCI Over the Years")
    plt.show()

def nfp1():
#    nfpdata = quandl.get("FRED/PAYEMS")
    nfpdata = pd.read_csv("finalinputnfpdata.csv", names=['date', 'nfp'])
    nfpdata.plot(y='nfp')
    plt.xlabel('date')
    plt.ylabel('nfp')
    plt.legend().set_visible(False)
    plt.title("NFP Over the Years")
    plt.show()

def rmsecompare():
    rmsedata = pd.read_csv("mrmse.csv", names=['Regression', 'RMSE'])
    fig, ax = plt.subplots()
    # hide axes
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    u = rmsedata['Regression'].tolist()
    v = rmsedata['RMSE'].tolist()
    nlist = u + v
#    df = pd.DataFrame(np.random.randn(10, 4), columns=list('ABCD'))
#    ax.table(cellText=df.values, colLabels=df.columns, loc='center')
    ax.table(cellText=nlist, colLabels=rmsedata.columns, loc='center')
    fig.tight_layout()
    plt.show()

def rmsecompare1():
    img=mpimg.imread('RMSECompare.png')
    imgplot = plt.imshow(img)
    plt.axis('off')
    plt.show()



def all1():
#    alldata = pd.read_csv("FinalDataSetnn.csv", names=['date',  'gdp','ulc','ir','cpi','nhs','cu','rs','napm','nfp','ur','cci'])
    alldata1 = pd.read_csv("data.csv", names=['KEY', 'IR', 'GDP', 'UR', 'CPI', 'NFP', 'NHS', 'CU', 'CCI', 'NAPM', 'UNL', 'RS'])
    alldata2=alldata1.convert_objects(convert_numeric=True)
    x = alldata2['KEY'].tolist()
    l1 = alldata2['IR'].tolist()
    l2 = alldata2['GDP'].tolist()
    l3 = alldata2['UR'].tolist()
    l4 = alldata2['CPI'].tolist()
    l5 = alldata2['NFP'].tolist()
    l6 = alldata2['NHS'].tolist()
    l7 = alldata2['CU'].tolist()
    l8 = alldata2['CCI'].tolist()
    l9 = alldata2['NAPM'].tolist()
    l10 = alldata2['UNL'].tolist()
    l11 = alldata2['RS'].tolist()
    plt.plot(x,l1)
    plt.plot(x,l2)
    plt.plot(x,l3)
    plt.plot(x,l4)
    plt.plot(x,l5)
    plt.plot(x,l6)
    plt.plot(x,l7)
    plt.plot(x,l8)
    plt.plot(x,l9)
    plt.plot(x,l10)
    plt.plot(x,l11)
    plt.xlabel('KEY')
    plt.ylabel('IR')
    plt.ylabel('GDP')
    plt.ylabel('UR')
    plt.ylabel('CPI')
    plt.ylabel('NFP')
    plt.ylabel('NHS')
    plt.ylabel('CU')
    plt.ylabel('CCI')
    plt.ylabel('NAPM')
    plt.ylabel('UNL')
    plt.ylabel('RS')
    plt.legend().set_visible(True)
    #plt.legend()
    plt.title("Interest Rate & Features Over the Years")
    plt.show()






def showdata():

#    par1.append(name.get())
    x =  entry1.get()
    print(x)
    print(par1)
    print("Got it")

def NewFile():
	print("New File!")


def OpenFile():
	name = askopenfilename()
	print(name)


def About():
    print("This is a About Option of a menu")
    tk.messagebox.showinfo("Interest Rate Predictor", "A Final Year Project by B.Tech 2018 Students - Purvi Misal, Vinaya & Avichal under the Guidance of Shri Professor of Computer Science ")


def EntryWindow():
#    name = tk.StringVar()
#	window1 = tk.Tk()
#	window1.resizable(width=False, height=False)
#	window1.geometry('{}x{}'.format(700, 700))
#	window1.wm_title("INTEREST RATE PREDICTOR")
#	window1.configure(background='lavender')
#	window1_text = tk.Text(window1, height=10, padx=150, bg='lavender', font='bold')
#	window1_text.insert(tk.INSERT, "INTEREST RATE PREDICTOR")
#	window1_text.pack(side='top')

    #name = IntVar()
    window2 = tk.Tk()
    window2.configure(background='lavender')
    window2.resizable(width=False, height=False)
    window2.geometry('{}x{}'.format(600, 600))
    window2.wm_title("DATA ENTRY")

    label1 = Label(window2, text="GDP", bg='Lavender', font=20)
    label2 = Label(window2, text="Unemployment Rate", bg='Lavender', font=20)
    label3 = Label(window2, text="Consumer Price Index", bg='Lavender', font=20)
    label4 = Label(window2, text="Non Farm Payroll", bg='Lavender', font=20)
    label5 = Label(window2, text="New Home Sales", bg='Lavender', font=20)
    label6 = Label(window2, text="Capacity Utilization", bg='Lavender', font=20)
    label7 = Label(window2, text="Consumer Cost Index", bg='Lavender', font=20)
    label8 = Label(window2, text="NAPM Index", bg='Lavender', font=20)
    label9 = Label(window2, text="Unit Labor Cost", bg='Lavender', font=20)
    label10 = Label(window2, text="Retail Sales", bg='Lavender', font=20)

	# ent = Entry(root, textvariable=sv)
	# ent.pack()

    entry1 = Entry(window2, textvariable=name, font=20)
    entry2 = Entry(window2, font=20)
    entry3 = Entry(window2, font=20)
    entry4 = Entry(window2, font=20)
    entry5 = Entry(window2, font=20)
    entry6 = Entry(window2, font=20)
    entry7 = Entry(window2, font=20)
    entry8 = Entry(window2, font=20)
    entry9 = Entry(window2, font=20)
    entry10 = Entry(window2, font=20)

    label1.grid(row=2, sticky=E, padx=10, pady=5)
    label2.grid(row=3, sticky=E, padx=10, pady=5)
    label3.grid(row=4, sticky=E, padx=10, pady=5)
    label4.grid(row=5, sticky=E, padx=10, pady=5)
    label5.grid(row=6, sticky=E, padx=10, pady=5)
    label6.grid(row=7, sticky=E, padx=10, pady=5)
    label7.grid(row=8, sticky=E, padx=10, pady=5)
    label8.grid(row=9, sticky=E, padx=10, pady=5)
    label9.grid(row=10, sticky=E, padx=10, pady=5)
    label10.grid(row=11, sticky=E, padx=10, pady=5)
    entry1.grid(row=2, column=1)
    entry2.grid(row=3, column=1)
    entry3.grid(row=4, column=1)
    entry4.grid(row=5, column=1)
    entry5.grid(row=6, column=1)
    entry6.grid(row=7, column=1)
    entry7.grid(row=8, column=1)
    entry8.grid(row=9, column=1)
    entry9.grid(row=10, column=1)
    entry10.grid(row=11, column=1)


    # reg = top.register(correct)
    # entry1.config(validate="key", validatecommand=(reg,'%P'))
    B = tk.Button(window2, text='Submit', bg='purple' , fg='white', command=lambda: showdata(), width=10, height=5)
    B.grid(row=12, column=1, sticky=S, padx=50, pady=10)

"""
	C = tk.Button(window2, text='Show Graph', command=lambda: doNothing(), width=10, height=5)
	D = tk.Button(window2, text='Predict \n for one Model', command=lambda: doNothing(), width=10, height=5)


	C.grid(row=1, column=2, sticky=S, pady=10)
	D.grid(row=1, column=3, sticky=S, padx=50, pady=10)
"""




def main():


    root = Tk()
    root.resizable(width=False, height=False)
    root.geometry('{}x{}'.format(800, 800))
    root.wm_title("Interest Rate Predictor Software")
#root.configure(background='yellow')
#root_text = tk.Text(root, height = 10, padx = 250, bg = 'yellow', font = 'bold')
#root_text.insert(tk.INSERT, "INTEREST RATE PREDICTOR")
#root_text.pack(side = 'top')

    w = Label(root, text = "INTEREST RATE PREDICTOR", font = "Times, 30",pady=20 )
    w1 = Label(root, text = "Description: \n 1. This software displays data graphs of various features used to Interest rate. \n 2. It predicts interest rate for given values for 10 features inputted by the user by the 5 machine learning models (model can be chosen). \n 3. It plots a graph showing performance of 5 machine learning models we used to predict interest rate. \n 4. It prints a graph showing the difference between tradtional IR prediction and machine learning IR prediction. ", font = "Times, 10", wraplength =800, justify="left", pady=30)
    w2 = Label(root, text = "\u00a9 Built by Purvi Misal, Vinaya Patil and Avichal Agrawal \n College of Engineering, Pune ", font = "Times, 10", justify="left", pady=80)
    w.pack()
    w1.pack()
    w2.pack(side="bottom")
    
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New Input ", command=EntryWindow)
    filemenu.add_command(label="Open...", command=OpenFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)


    graphmenu = Menu(menu)
    menu.add_cascade(label="Feature Data Graphs", menu=graphmenu)
    graphmenu.add_command(label="GDP Data Graph as of Date", command=gdp1)
    graphmenu.add_command(label="CPI Data Graph as of Date", command=cpi1)
    graphmenu.add_command(label="NHS Data Graph as of Date", command=nhs1)
    graphmenu.add_command(label="TCU Graph as of Date", command=tcu1)
    graphmenu.add_command(label="Interest Rates Graph as of Date", command=int1)
    graphmenu.add_command(label="RSA Data Graph as of Date", command=rsa1)
    graphmenu.add_command(label="PMI Data Graph as of Date", command=pmi1)
    graphmenu.add_command(label="ULCBS Data Graph as of Date", command=ulcbs1)
    graphmenu.add_command(label="UR Data Graph as of Date", command=ur1)
    graphmenu.add_command(label="CCI Data Graph as of Date", command=cci1)
    graphmenu.add_command(label="NFP Data  as of Date", command=nfp1)
    graphmenu.add_command(label="All Features Data  as of Date", command=all1)


    reportmenu = Menu(menu)
    menu.add_cascade(label="Model Predictions ", menu=reportmenu)
    reportmenu.add_command(label="Model Comparison", command=rmsecompare1)
    reportmenu.add_command(label="Linear", command=About)
    reportmenu.add_command(label="Lasso", command=About)
    reportmenu.add_command(label="LarsLasso", command=About)
    reportmenu.add_command(label="Ridge", command=About)
    reportmenu.add_command(label="RidgeCV", command=About)

    helpmenu = Menu(menu)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About...", command=About)



    mainloop()
##### vk-end


### Main Program starts here

par1 = []
#entry1 = Entry()
#entry2 = Entry(tk)
#entry3 = Entry(tk)
#entry4 = Entry(tk)
#entry5 = Entry(tk)
#entry6 = Entry(tk)
#entry7 = Entry(tk)
#entry8 = Entry(tk)
#entry9 = Entry(tk)
#entry10 = Entry(tk)

name = tk.StringVar

if __name__ == "__main__":
    # execute only if run as a script
    main()




def correct(inp):
	if inp.isdigit():
		return True
	elif inp is "":
		return True
	else: 
		return False


def doNothing():
    print("ok")
    
#A = tk.Button(window1, text = 'Go Ahead-->', command = lambda: EntryWindow(window1), width = 40, height = 20)
#A.pack(side = 'bottom')

#window1.mainloop()




"""

def UploadCallBack(top):
    upload = tk.Tk()
    upload.configure(background='lavender')
    upload.resizable(width=False, height=False)
    upload.geometry('{}x{}'.format(1000, 1000))
    upload.wm_title("Upload Data values")
    uploader_text = tk.Text(upload, height = 5, padx = 150, bg = 'lavender', font = 'bold')
    #uploader_text.insert(tk.INSERT, "Please choose a file")
    D = tk.Button(upload, text = 'Go ahead', command = lambda: FeedbackCallBack(top), width = 20, height = 10)
    D.pack()
    top.destroy()

def doNothing():
    print("ok")

def FeedbackCallBack(top): #Function to generate a Feedback page where original text can be entered
    feedback = tk.Tk()
    feedback.configure(background='lavender')
    feedback.resizable(width=False, height=False)
    feedback.geometry('{}x{}'.format(1000, 1000))
    feedback.wm_title("Entry Page")
    #upload.destroy() 
    l1 = Label(feedback, text="GDP")
    l2 = Label(feedback, text="GDP") 
    l3 = Label(feedback, text="GDP")
    l4 = Label(feedback, text="GDP")
    l5 = Label(feedback, text="GDP")
    l6 = Label(feedback, text="GDP")
    l7 = Label(feedback, text="GDP")
    l8 = Label(feedback, text="GDP")
    l9 = Label(feedback, text="GDP")
    l10 = Label(feedback, text="GDP")
    f1_entry = tk.Entry(feedback)
    f2_entry = tk.Entry(feedback)
    f3_entry = tk.Entry(feedback)
    f4_entry = tk.Entry(feedback)
    f5_entry = tk.Entry(feedback)
    f6_entry = tk.Entry(feedback)
    f7_entry = tk.Entry(feedback)
    f8_entry = tk.Entry(feedback)
    f9_entry = tk.Entry(feedback)
    f10_entry = tk.Entry(feedback)
    l1.grid(row=0, sticky=E)
    l2.grid(row=1, sticky=E)
    l3.grid(row=2, sticky=E)
    l4.grid(row=3, sticky=E)
    l5.grid(row=4, sticky=E)
    l6.grid(row=5, sticky=E)
    l7.grid(row=6, sticky=E)
    l8.grid(row=7, sticky=E)
    l9.grid(row=8, sticky=E)
    l10.grid(row=9, sticky=E)
    f1_entry.grid(row=0, column=1)
    f2_entry.grid(row=0, column=1)
    f3_entry.grid(row=0, column=1)
    f4_entry.grid(row=0, column=1)
    f5_entry.grid(row=0, column=1)
    f6_entry.grid(row=0, column=1)
    f7_entry.grid(row=0, column=1)
    f8_entry.grid(row=0, column=1)
    f9_entry.grid(row=0, column=1)
    f10_entry.grid(row=0, column=1)
    l1.pack(side="left")
    l2.pack(side="left")
    l3.pack(side="left")
    l4.pack(side="left")
    l5.pack(side="left")
    l6.pack(side="left")
    l7.pack(side="left")
    l8.pack(side="left")
    l9.pack(side="left")
    l10.pack(side="left")
    f1_entry.pack()
    f2_entry.pack()
    f3_entry.pack()
    f4_entry.pack()
    f5_entry.pack()
    f6_entry.pack()
    f7_entry.pack()
    f8_entry.pack()
    f9_entry.pack()
    f10_entry.pack()
    f_submit = tk.Button(feedback,text='Predict',command=lambda:doNothing())
    f_graph = tk.Button(feedback,text='Plot Graphs',command=lambda:doNothing())
    f_submit.pack()
    f_graph.pack()
    
    
def doNothing():
    print("ok")

C = tk.Button(top, text = 'go ahead to uploader page', command = lambda: UploadCallBack(top), width = 20, height = 10)

text = tk.Text(top, height = 5, padx = 150, bg = 'lavender', font = 'bold')
text.insert(tk.INSERT, "Predictor Softare:")
text.pack(side = 'top')


C.pack(side = 'bottom')
top.mainloop()  
"""
