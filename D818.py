# -*- coding: utf-8 -*-
"""
Created on Fri Mar  7 12:02:48 2025


"""
#https://realpython.com/python-dash/#what-is-dash

import yfinance as yahooFinance
import pandas as pd 

holdings = ['O',
'VHYL.L',
'MAIN',
'GAIN',
'EPR',
'PFLT',
'NNN',
'EUE',
'VFEM.L',
'ARCC',
'ADC',
'QYLD',
'SMIF.L',
'TMPL.L',
'WHR.L',
'BBOX.L',
'SGRO.L',
'JEPG.L']


hdata  = pd.DataFrame()

for h in holdings:
    
# Here We are getting Facebook financial information
# We need to pass O as argument for that
    stock = yahooFinance.Ticker(h)
 
    # whole python dictionary is printed here
    #print(stock.info)



    stockdata = pd.DataFrame.from_dict(stock.info, orient='index')
    stockdata = stockdata.transpose()
    hdata = pd.concat([hdata,stockdata])







#https://stackoverflow.com/questions/79007910/get-data-yahoos-pandas-data-reader
import yfinance as yf
stock_price_data = yf.download('O', start='2024-01-01', end='2025-03-26')
stock_price_data.reset_index(inplace=True)
stock_price_data.columns = ['Date','Close', 'High','Low','Open', 'Volume']
#print(stock_price_data)




#https://stackoverflow.com/questions/53697655/how-to-plot-candlesticks
import finplot as fplt
import pandas as pd
fplt.candlestick_ochl(stock_price_data[['Open', 'Close', 'High', 'Low']])
fplt.show()


