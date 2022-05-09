
import sqlite3
from sqlite3 import Error

from colorama import Cursor 



class localdatabase:
    """Class for database handling"""
    def __init__( self, db_file ) -> None:
        try: 
            self.dbconnection = sqlite3.connect(db_file)
        except Error as e:
            print(" DB connection without success.")
            print(e)
        else:
            print("Connection with database is done.")         
        
        self.cursor = self.dbconnection.cursor()
    
    def __del__(self):
        try: 
            self.dbconnection.close()
        except Error as e:
            print("Closing a database with a failure.")
            print(e)
        else:
            print("Database shutdown successfully completed.")
    
    
    def tableCreate(self, tablename, columnsDictionary ):
        """Create new table in database"""        
        order = 'CREATE TABLE IF NOT EXISTS' + tablename +'('
        
        for key in columnsDictionary:
            order = order + columnsDictionary(key)+' '+key+', '
        
        order = order[:-3] + ')'
        print( "Prepared order:", order )
        self.cursor.execute( order, self.cursor )
        
        
