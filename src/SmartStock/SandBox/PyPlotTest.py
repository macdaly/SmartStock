'''
Created on Sep 19, 2015

@author: i056936
'''

import matplotlib.pyplot as plt
import numpy as np
from yahoo_finance import Share
from matplotlib.dates import MonthLocator, DateFormatter, DayLocator
from datetime import date

def dist(i,j):
    return abs(i-j)

def getLocalMaximumsImportance(maximums, signal):
    theMax = signal.max()
    length = len(signal)
    importances = []
    for maxIdx in maximums:
        if signal[maxIdx] == theMax:
            return max(maxIdx, length-maxIdx)
        il = maxIdx - 1
        ir = maxIdx + 1
        while signal[il] < signal[maxIdx] and signal[ir] < signal[maxIdx] :
            if il > 0 :
                il = il -1
            if ir < length-1:
                ir = ir +1
            if il == 0 and ir == length-1:
                break
        if signal[il] == signal[maxIdx]:
            importances.append(dist(maxIdx, il))
        importances.append(dist(maxIdx, ir))
    return importances
        
def getLocalMinumumImportance(minimums, signal):
    theMin = signal.min()
    length = len(signal)
    importances = []
    for minIdx in minimums:
        if signal[minIdx] == theMin:
            return max(minIdx, length-minIdx)
        il = minIdx - 1
        ir = minIdx + 1
        while signal[il] > signal[minIdx] and signal[ir] > signal[minIdx] :
            if il > 0 :
                il = il -1
            if ir < length-1:
                ir = ir +1
            if il == 0 and ir == length-1:
                break
        if signal[il] == signal[minIdx]:
            importances.append(dist(minIdx, il))
        importances.append(dist(minIdx, ir))
    return importances


def getLocalImportance(extremumIdx, signal, extremumType):
    il = extremumIdx - 1
    ir = extremumIdx + 1
    length = len(signal)   
    if extremumType == 'max' :
        while signal[il] < signal[extremumIdx] and signal[ir] < signal[extremumIdx] :
            if il > 0 :
                il = il -1
            if ir < length-1:
                ir = ir +1
            if il == 0 and ir == length-1:
                print 'its a max'
                return max(dist(extremumIdx, il), dist(extremumIdx, ir))
    elif extremumType == 'min' :
        while signal[il] > signal[extremumIdx] and signal[ir] > signal[extremumIdx] :
            if il > 0 :
                il = il -1
            if ir < length-1:
                ir = ir +1
            if il == 0 and ir == length-1:
                print 'its a min'
                return max(dist(extremumIdx, il), dist(extremumIdx, ir))
    else :
        raise Exception('bad parameter')
    if il == 0:
        print 'strict to the left'
        return dist(extremumIdx, ir)
    if ir == length -1:
        print 'strict to the riht'
        return dist(extremumIdx, il)
    if signal[il] == signal[extremumIdx]:
        print 'returning left'
        return dist(extremumIdx, il)
    print 'returning right'
    return dist(extremumIdx, ir)
    



def getAllLocalExtrema(closes):
    theMins = []
    theMaxes = []
    allIndices = []
    extrema = []
    for i in range(1,len(closes)-2):
        if closes[i] > closes[i-1] and closes[i] > closes[i+1]:
            theMaxes.append(i)
            allIndices.append(i)
        if closes[i] < closes[i-1] and closes[i] < closes[i+1]:
            theMins.append(i)
            allIndices.append(i)
    extrema.append(theMins)
    extrema.append(theMaxes)
    extrema.append(allIndices)
    return extrema

if __name__ == '__main__':
    sap = Share('SAP.DE')
    startDate = date(2015, 02, 12)
    endDate = date(2015,9,20)
    start = startDate.isoformat()
    end = endDate.isoformat()
    sapLastThreeMonths =  sap.get_historical(start, end)
    closes = []
    dates = []
    for info in sapLastThreeMonths :
        closes.append(float(info['Close']))
        dates.append(np.datetime64(info['Date']))
        
    allExtrema = getAllLocalExtrema(closes)
    
    plt.figure(1)
    stock = plt.subplot(211)
    stock.plot_date(dates, closes, '-')
    stock.xaxis.set_major_locator(MonthLocator())
    stock.xaxis.set_major_formatter(DateFormatter("%b"))
    stock.xaxis.set_minor_locator(DayLocator())
    title = 'SAP stock close price from {start} to {end} '.format(start=startDate.strftime("%d %B %Y"), end = endDate.strftime("%d %B %Y"))
    #stock.title(title)
    stock.grid(True)
    plt.title(title)
    indices = allExtrema[2]
    maxes = allExtrema[1]
    mins = allExtrema[0]
    for index in maxes:
        plt.plot(dates[index], closes[index], 'gD')
    for index in mins:
        plt.plot(dates[index], closes[index], 'rD')
        
    importances = {}
    for indMax in maxes:
        importances[indMax] = getLocalImportance(indMax, closes, 'max')
    for indMin in mins:
        importances[indMin] = getLocalImportance(indMin, closes, 'min')
        
    histImportance = []
    
    for index in indices:
        histImportance.append(importances[index])
        
    plt.subplot(212)
    
    print histImportance
    
    #n, bins, patches = plt.hist(histImportance, 50, normed=1, facecolor='g', alpha=0.75)
    #n, bins, patches = plt.hist(histImportance)
    plt.plot(histImportance)
    plt.title('Importances') 
 
    plt.show()
