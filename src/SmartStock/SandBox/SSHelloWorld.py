'''
Created on Jun 27, 2015

@author: i056936
'''
from hdbcli import dbapi
from yahoo_finance import Share
import os
import operator

os.environ['http_proxy'] = 'http://proxy.wdf.sap.corp:8080'


if __name__ == '__main__':   
    yahoo = Share('YHOO')
    ibm = Share('IBM')
    siemens = Share('SIE.DE')
    sap = Share('SAP.DE')
    commerz = Share('CBK.DE')
    
    listOfStocksDAX = ['SIE.DE', 'SAP.DE', 'CBK.DE', 'ADS.DE', 'ALV.DE', 'BAS.DE', 'BAYN.DE', 'BEI.DE', 'BMW.DE', 'CON.DE', 'DAI.DE', 'DB1.DE', 'DBK.DE', 'DPW.DE',
                     'DTE.DE', 'EOAN.DE', 'FME.DE', 'FRE.DE', 'HEI.DE', 'HEN3.DE', 'IFX.DE', 'LHA.DE', 'LIN.DE', 'LXS.DE', 'MRK.DE', 'MUV2.DE', 'RWE.DE', 'SDF.DE', 'TKA.DE', 'VOW3.DE']
    
    stockPESMap = {}
    stockPERMap = {}
    stockMCAP_BVALUE_Diff_Map = {}
    
    print 'creating dictionaries...'
    for stock in listOfStocksDAX:
        stockPESMap[stock] = ( float(Share(stock).get_earnings_share())/float(Share(stock).get_price()) )*100
        perNumber = 0 
        perString = Share(stock).get_price_earnings_ratio()
        if perString is not None:
            perNumber = float(perString)
            
        stockPERMap[stock] = perNumber
        marketCap =  Share(stock).get_market_cap().translate(None, 'B')
        bookValue =  Share(stock).get_book_value().translate(None, 'B')
        stockMCAP_BVALUE_Diff_Map[stock] = (float(marketCap) - float(bookValue))/float(marketCap) * 100
        
    print 'dictionaries created'
    print 'sorting dictionaries'
    sorted_stockPESMap = sorted(stockPESMap.items(), key=operator.itemgetter(1))
    sorted_stockPERMap = sorted(stockPERMap.items(), key=operator.itemgetter(1))
    sorted_stockMCAP_BVALUE_Diff_Map = sorted(stockMCAP_BVALUE_Diff_Map.items(), key=operator.itemgetter(1))
    
    print 'printing dictionaries'
    print ''
    print 'Stock and PES percentage'
    print sorted_stockPESMap
    print ''
    print 'stock and PER ratios'
    print sorted_stockPERMap
    print ''
    print 'difference between Market Cap and Book Value in Billion '
    print sorted_stockMCAP_BVALUE_Diff_Map
    
#     print yahoo.get_trade_datetime()
#     host = "lu187256"
#     port = 30215
#     conn = dbapi.connect(host, port, "system", "manager")
#     if conn.isconnected():
#         cursor = conn.cursor()
#     else:
#         print "connection failed!"
#     pass