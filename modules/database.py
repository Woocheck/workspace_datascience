
import sqlite3
import traceback



class localdatabase:
    """Class for database handling"""
    def __init__( self, db_file ) -> None:
        try: 
            self.dbconnection = sqlite3.connect(db_file)
        except Exception:
            print(" DB connection without success.")
            traceback.print_exc()
        else:
            print("Connection with database is done.")         
        
        self.cursor = self.dbconnection.cursor()
    
    def __del__(self):
        try: 
            self.dbconnection.close()
        except Exception:
            print("Closing a database with a failure.")
            traceback.print_exc()
        else:
            print("Database shutdown successfully completed.")
    
    
    def tableCreate( self, tablename, columnsDictionary ):
        """Create new table in database"""        
        order = 'CREATE TABLE IF NOT EXISTS ' + tablename +'('
        
        for key in columnsDictionary:
            order = order + key+' '+columnsDictionary[key]+', '
        
        order = order[:-2] + ')'
        print( "Prepared order:", order )
        self.cursor.execute( order )
        
    def insertManyIn( self,  tableName, dataList ):
        """Insert data from list in DBtable"""
        
        order = "insert into " + tableName + " values("
        for column in range( len(dataList[0]) ):
            order += "?,"
        order = order[:-1] + ")"
        print( "Insert Many order: ", order )
        self.cursor.executemany( order, dataList )
        
    def printWholeTable(self, tableName):
        
        order = "select * from " + tableName
        for row in self.cursor.execute( order ):
            print( row )
    
    def returnSearchResults(self, order ):
        self.cursor.execute( order )
        return self.cursor.fetchall()
        
    def printSearchReasults( self, order, orderArgumentsDictionary ):       
        self.cursor.execute( order, orderArgumentsDictionary )
        print( self.cursor.fetchall() )
        
