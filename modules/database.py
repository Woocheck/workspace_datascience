
import sqlite3 



class localdatabase:
    """Class for database handling"""
    def __init__( self, name ) -> None:
        try: 
            dbconnection = sqlite3.connect(name)
        except:
            print(" DB connection without success.")
        else:
            print("Connection with database is done.")
        
        cursor = dbconnection.cursor()
    
    def tableCreate( name, columnsDictionary ):
        """Create new table in database""" 
        
        