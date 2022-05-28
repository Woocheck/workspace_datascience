from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker

class PyTrends:
    def __init__(self):
        self.pytrends = TrendReq(hl='', tz=360)
        self.data = pd.DataFrame()
        
    def overTime( self, keyword ):
        self.data = self.pytrends.interest_over_time() 
        self.data = self.data.reset_index()
        
        return self.data
    
    def trendsTimeLaps( self, dataBegin, dataEnd, passwordsList):
        """The function gets the data from google trends for the selected time period."""
        self.py
        #Formatting of the 'timefrem parameter with dates for the selected interval
        przedzial = dataBegin+' '+dataEnd
        self.pytrends.build_payload(passwordsList, cat=0, timeframe= przedzial, geo='', gprop='')
        result = self.pytrends.interest_over_time()
        #Removing a redundant column passed in query results
        del result['isPartial']
        self.data = result    
        return self.data                    


    def meanCalculate( self ):
        """The function calculates the average and puts the result in a separate column."""
        self.data['Średnia występowania haseł'] = self.data.mean(axis=1)
        return self.data

    def correlation( self ):
        """The function returns the results of the correlation calculation."""
        korelacja = self.data.corr()
        pd.set_option("display.precision", 4)
        return korelacja

    def listDiagram( passwordsListData ):
        fig, ax = plt.subplots()
        loc = plticker.MultipleLocator(base=60)
        ax.xaxis.set_major_locator(loc)
        ax.grid()
        
        for element in passwordsListData.columns:
            passwordsListData[element].plot( kind = 'line',\
                        title = ('Google Trends results for a list of keywords'),\
                        grid = True,\
                        fontsize = 11,\
                        figsize = ( 8, 8 ) )
        ax.legend()
        plt.xlabel("Data")
        fig.savefig('trendsDaneWykres', dpi=None, facecolor='w', edgecolor='w',\
                    orientation='portrait', papertype='a4', format=None,\
                    transparent=False, bbox_inches=None, pad_inches=0.1,\
                    metadata=None)

    def meanDiagram( self ):
        daneSrednia = self.meanCalculate()
        
        fig, ax = plt.subplots()
        loc = plticker.MultipleLocator(base=60)
        ax.xaxis.set_major_locator(loc)
        ax.grid()
        daneSrednia['Average occurrence of keywords'].plot( kind = 'line', title = ('Gooogle Trends average'), grid = True, fontsize = 11, figsize = ( 8, 8 ) )
        ax.legend()
        plt.xlabel("Data")
        fig.savefig('trendsMean', dpi=None, facecolor='w', edgecolor='w',\
                    orientation='portrait', papertype='a4', format=None,\
                    transparent=False, bbox_inches=None, pad_inches=0.1,\
                    metadata=None)