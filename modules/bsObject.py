import urllib.request
from bs4 import BeautifulSoup as bs
import re
import pandas as pd


class bsObject:
  
  def __init__(self, url ):
    
    self.page = urllib.request.urlopen( url )
    self.soup = bs( self.page )
  
  def findRegAll( self, bodyName, regString ):

    #find all regString objects in  bodyNames
    names = self.soup.body.find_all( bodyName )
    result = re.findall( regString , str(names) )
    result = [item[4:] for item in result]
    
    return result
  def findAll( self, name ):
    #find all name descriptions
    description = self.soup.body.findAll( name )
    result = []

    for item in description:
      item = item.text
      item = item.replace('\n', ' ')
      result.append(item)
    
    return result

