from modules import database as create
from modules import bsObject as importWebpage
import pandas as pd

release_list = [
    (1997, "Grand Theft Auto", "state of New Guernsey"),
    (1999, "Grand Theft Auto 2", "Anywhere, USA"),
    (2001, "Grand Theft Auto III", "Liberty City"),
    (2002, "Grand Theft Auto: Vice City", "Vice City"),
    (2004, "Grand Theft Auto: San Andreas", "state of San Andreas"),
    (2008, "Grand Theft Auto IV", "Liberty City"),
    (2013, "Grand Theft Auto V", "Los Santos")
]

city_list = [
    ("Liberty City", "New York"),
    ("state of New Guernsey", "state of New Jersey"),
    ("Anywhere, USA", "all USA cities"),
    ("Vice City", "Miami"),
    ("state of San Andreas", "state of California"),
    ("Los Santos", "Los Angeles")
]

columnsDictionary = { "release_year" : "integer", 
                      "release_name" : "text", 
                      "city" : "text"}

db = create.localdatabase("gta.db")
db.tableCreate( "gta", columnsDictionary )
db.insertManyIn( "gta", release_list )

db.printSearchReasults( "select * from gta where city=:c",{"c": "Liberty City"} )


webPage = importWebpage.bsObject( "https://docs.python.org/3/library/random.html"  )

function_names = webPage.findRegAll( 'dt', 'id="random.\w+' )
function_usage = webPage.findAll( 'dd' )

print('list of function names:',function_names[:5])
print('\nfunction description:', function_usage[0])
print('\nnumber of items in function names:', len(function_names))
print('number of items in function description:', len(function_usage))

#create a dataframe
data = pd.DataFrame({'function name': function_names, 'function usage': function_usage})
data.head()

data.to_csv('my_file.csv')