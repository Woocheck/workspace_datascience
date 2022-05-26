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
        """Funkcja pobiera dan z google trends dla wybranego rzedziału czasowego."""
        self.py
        #Formatowanie parametru 'timefrem z dat dla wybranego przedziału
        przedzial = dataBegin+' '+dataEnd
        self.pytrends.build_payload(passwordsList, cat=0, timeframe= przedzial, geo='', gprop='')
        result = self.pytrends.interest_over_time()
        #Usuwanie zbędnej kolumny przekazywanej w wynikach zapytania
        del result['isPartial']
        self.data = result    
        return self.data                    


    def obliczSrednia( self ):
        """Funkcja oblicza średnią i umieszcza wynik w osobnej kolumnie."""
        self.data['Średnia występowania haseł'] = self.data.mean(axis=1)
        return self.data

    def korelacja( self ):
        """Funkcja zwraca wyniki obliczeń korelacji."""
        korelacja = dane.corr()
        pd.set_option("display.precision", 4)
        return korelacja

    def wykresDlaListy( dane_dla_listy_hasel ):
        fig, ax = plt.subplots()
        loc = plticker.MultipleLocator(base=60)
        ax.xaxis.set_major_locator(loc)
        ax.grid()
        
        for element in dane_dla_listy_hasel.columns:
            dane_dla_listy_hasel[element].plot( kind = 'line',\
                        title = ('Wyniki Google Trends dla listy haseł'),\
                        grid = True,\
                        fontsize = 11,\
                        figsize = ( 8, 8 ) )
        ax.legend()
        plt.xlabel("Data")
        fig.savefig('trendsDaneWykres', dpi=None, facecolor='w', edgecolor='w',\
                    orientation='portrait', papertype='a4', format=None,\
                    transparent=False, bbox_inches=None, pad_inches=0.1,\
                    metadata=None)

    def wykresSrednia( dane ):
        daneSrednia = obliczSrednia( dane )
        
        fig, ax = plt.subplots()
        loc = plticker.MultipleLocator(base=60)
        ax.xaxis.set_major_locator(loc)
        ax.grid()
        daneSrednia['Średnia występowania haseł'].plot( kind = 'line', title = ('Średnia z wynikow Gooogle Trends'), grid = True, fontsize = 11, figsize = ( 8, 8 ) )
        ax.legend()
        plt.xlabel("Data")
        fig.savefig('trendsSrednia', dpi=None, facecolor='w', edgecolor='w',\
                    orientation='portrait', papertype='a4', format=None,\
                    transparent=False, bbox_inches=None, pad_inches=0.1,\
                    metadata=None)