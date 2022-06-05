from modules import bsObject as importWebpage
import pandas as pd

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