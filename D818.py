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
'EUEAA.XD',
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



# Reordering columns by passing a list
hdata = hdata[['symbol',
'quoteType',
'longName',
'fullExchangeName',
'marketState',
'industry',
'sector',
'averageAnalystRating',
'currency',
'open',
'previousClose',
'dayLow',
'dayHigh',
'dividendRate',
'dividendYield',
'exDividendDate',
'payoutRatio',
'fiveYearAvgDividendYield',
'beta',
'trailingPE',
'forwardPE',
'volume',
'marketCap',
'priceToSalesTrailing12Months',
'fiftyDayAverage',
'twoHundredDayAverage',
'trailingAnnualDividendRate',
'trailingAnnualDividendYield',
'profitMargins',
'sharesPercentSharesOut',
'heldPercentInsiders',
'heldPercentInstitutions',
'shortRatio',
'bookValue',
'priceToBook',
'earningsQuarterlyGrowth',
'trailingEps',
'forwardEps',
'enterpriseToRevenue',
'enterpriseToEbitda',
'52WeekChange',
'SandP52WeekChange',
'lastDividendValue',
'lastDividendDate',
'regularMarketChange',
'regularMarketDayRange',
'averageDailyVolume3Month',
'fiftyTwoWeekLowChange',
'fiftyTwoWeekLowChangePercent',
'fiftyTwoWeekRange',
'fiftyTwoWeekHighChange',
'fiftyTwoWeekHighChangePercent',
'fiftyTwoWeekChangePercent',
'dividendDate',
'epsTrailingTwelveMonths',
'epsForward',
'epsCurrentYear',
'priceEpsCurrentYear',
'fiftyDayAverageChange',
'fiftyDayAverageChangePercent',
'twoHundredDayAverageChange',
'twoHundredDayAverageChangePercent',
'currentPrice',
'targetLowPrice',
'targetHighPrice',
'targetMeanPrice',
'recommendationKey',
'totalCashPerShare',
'quickRatio',
'currentRatio',
'debtToEquity',
'revenuePerShare',
'returnOnAssets',
'returnOnEquity',
'earningsGrowth',
'revenueGrowth',
'grossMargins',
'ebitdaMargins',
'operatingMargins',
'corporateActions',
'longBusinessSummary',
'website']]


from datetime import datetime

hdata['dividendDate'] = pd.to_datetime(hdata['dividendDate'])

print(hdata['dividendDate'])

#https://stackoverflow.com/questions/79007910/get-data-yahoos-pandas-data-reader
import yfinance as yf
stock_price_data = yf.download('O', start='2024-01-01', end='2025-0-26')
stock_price_data.reset_index(inplace=True)
stock_price_data.columns = ['Date','Close', 'High','Low','Open', 'Volume']
#print(stock_price_data)




#https://stackoverflow.com/questions/53697655/how-to-plot-candlesticks
import finplot as fplt
import pandas as pd
fplt.candlestick_ochl(stock_price_data[['Open', 'Close', 'High', 'Low']])
fplt.show()


