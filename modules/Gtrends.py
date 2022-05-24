from pytrends.request import TrendReq



class PyTrends:
    def __init__(self):
        pytrends = TrendReq(hl='en-US', tz=360)

    def overTime( self, keyword ):
        data = self.pytrends.interest_over_time() 
        data = data.reset_index()


