# -*- coding: utf-8 -*-


import pandas as pd
from matplotlib import pyplot as plt
import pandas_datareader as dr
import getpass
from datetime import date
from tkinter import *
from tkinter import simpledialog
from tkinter import messagebox
from matplotlib import dates as mdates
from mpl_finance import candlestick_ohlc 
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
                                               NavigationToolbar2Tk)
user_name = getpass.getuser()
end_date = date.today()
start_date='01-03-2020'
c = 'No value entered'
def get_stockname():
    ticker = simpledialog.askstring('input_string','Please enter Stock Sign: -->')
    global c
    c = (ticker)
    c= c.split(",")
    return(c)

def error_proc():
    root=Tk()
    root.withdraw()
    messagebox.showwarning('Invalid Stock ID entered',c)
    root.deiconify()
    root.destroy()
    root.quit()
    df ='sap'
    return(df)
def plotdraw():
    # the figure that will contain the plot
    fig = Figure(figsize = (15, 15),
                 dpi = 100)
    
    # list of squares
#    y = [i**2 for i in range(101)]
#    beg = '04-01-2020'
#    end1 = date.today()
    yah_new = yah.loc[:,'Close']
    sma_10 = yah_new.rolling(window=10).mean()
    sma_30 = yah_new.rolling(window=30).mean()
#    ema15 = yah_new.ewm(15).mean()
    yah_data = yah[['Open','High', 'Low','Close']]
#convert date index to column in df in order to change dates to numerical value
    yah_data.reset_index(inplace=True)
#    yah_new1 = yah_data[['Date', 'Open','High','Low', 'Close']]
    yah_data['Date'] = yah_data.loc[:,'Date'].map(mdates.date2num)
#    ax = plt.subplot()
#show true date, not numerical numbers that are required for the candlestick plot
#
#    ax.xaxis_date()
#    ax.grid()
#    ax.set_xlabel('Date')
#    ax.set_ylabel('Price in US $')
#    ax.set_axisbelow(True)
#    plt.title('Stock SMA and Movement for : ' + c + ' by ' + user_name.upper())
# #   candlestick_ohlc(ax,yah_data.values,width=0.5,colorup='g')
#    ax.plot(sma_10,label ='SMA10')
#    ax.plot(sma_30,label='SMA 30')
#    ax.plot(ema15,label='EMA15', linestyle='--',color='black')
#   ax.legend()
#    plt.show()
    # adding the subplot
    plot1 = fig.add_subplot(211)
    plot2 = fig.add_subplot(211)
    plot3 = fig.add_subplot(212)
  
    # plotting the graph
    plot1.plot(sma_10,color='green',label='SMA10')
    leg=plot1.legend()
    plot2.plot(sma_30,color='blue',label='SMA30')
    leg=plot2.legend()
    candlestick_ohlc(plot3,yah_data.values,width=0.5,colorup='g')
    titlemain = 'Stock Average, High, Low performace for: '+ str(c).upper()
    fig.suptitle(titlemain)
    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig,
                               master = window)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()
  
 
root =Tk()
b1=Button(root,text='Click to Enter Stock',command=get_stockname)
Button(root, text="Click here to Quit", command=root.destroy).pack()
b1.pack()
root.geometry('300x300')
root.mainloop()
try:
    yah = dr.data.get_data_yahoo(c,start= start_date,end= end_date)
except:
   
    df=error_proc()
else:
    window = Tk()
  
    window.title('Graph')
  
# the main window
    window.geometry("800x800")
  
# button to display the graph 
    plot_button = Button(master = window,
                     command=plotdraw,    
                     height = 2,
                     width = 10,
                    text = "Plot")
# place the button
# into the window
    plot_button.pack()
  
# run the gui
    window.mainloop()
    print('it worked for:',c)
        