
import sqlite3

from colorama import Cursor 



class localdatabase:
    """Class for database handling"""
    def __init__( self, name ) -> None:
        try: 
            dbconnection = sqlite3.connect(name)
        except:
            print(" DB connection without success.")
        else:
            print("Connection with database is done.")
        
        self.cursor = dbconnection.cursor()
    
    def tableCreate(self, tablename, columnsDictionary ):
        """Create new table in database"""        
        order = 'CREATE TABLE IF NOT EXISTS' + tablename +'('
        
        for key in columnsDictionary:
            order = order + columnsDictionary(key)+' '+key+', '
        
        order = order[:-3] + ')'
        
        self.cursor.execute( order )
        
        
