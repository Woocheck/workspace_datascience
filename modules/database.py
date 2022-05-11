
import sqlite3
from sqlite3 import Error
import pandas as pd
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
        
    def insertManyIn( self,  tableName, dataList ):
        """Insert data from list in DBtable"""
        
        order = "insert into " + tableName + "values("
        for column in range( len(dataList.columns) ):
            order += "?,"
        order = order[:-1] + ")"
        
        self.cursor.executemany( order, dataList )
        
    def printWholeTable(self, tableName):
        
        order = "select * from " + tableName
        for row in self.cursor.execute( order ):
            print( row )
    
    def returnSearchResults(self, conditions ):
        pass #TODO function to return search reasults in pandas dataframe
    
    def print searchReasults( self, contitions ):
        pass #TODO function to print search reasults
