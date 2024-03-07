

from io import StringIO
import pandas as pd  

def transform(content):    
    file= pd.read_csv(StringIO(content))
    count = file["Country"].value_counts()    
    result = count.reset_index() 
    result.columns=['Country','Total']
    result_top5 = result[:5]
    result_others=  pd.DataFrame(data = {'Country' : ['others'],'Total' :[result['Total'][5:].sum()]})
    df=pd.concat([result_top5,result_others])
    return df