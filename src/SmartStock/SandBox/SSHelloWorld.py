'''
Created on Jun 27, 2015

@author: i056936
'''
from hdbcli import dbapi

if __name__ == '__main__':
    print "SmartStock Hello World!"
    host = "lu187256"
    port = 30215
    conn = dbapi.connect(host, port, "system", "manager")
    if conn.isconnected():
        cursor = conn.cursor()
    else:
        print "connection failed!"
    pass