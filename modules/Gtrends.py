from pytrends.request import TrendReq
import pandas as pd


class PyTrends:
    def __init__(self):
        pytrends = TrendReq(hl='en-US', tz=360)
        data = pd.DataFrame()
        
    def overTime( self, keyword ):
        self.data = self.pytrends.interest_over_time() 
        self.data = self.data.reset_index()
        
        return self.data
    


