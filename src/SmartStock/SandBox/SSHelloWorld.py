'''
Created on Jun 27, 2015

@author: i056936
'''
from hdbcli import dbapi
from yahoo_finance import Share
import os

os.environ['http_proxy'] = 'http://proxy.wdf.sap.corp:8080'


if __name__ == '__main__':   
    yahoo = Share('YHOO')
    ibm = Share('IBM')
    siemens = Share('SIE.DE')
    sap = Share('SAP.DE')
    print yahoo.get_open()
    print yahoo.get_price()
    print 'Ibm : ' + ibm.get_price()
    print 'Siemens : ' + siemens.get_price()
    print 'SAP : ' + sap.get_price()
#     print yahoo.get_trade_datetime()
#     host = "lu187256"
#     port = 30215
#     conn = dbapi.connect(host, port, "system", "manager")
#     if conn.isconnected():
#         cursor = conn.cursor()
#     else:
#         print "connection failed!"
#     pass