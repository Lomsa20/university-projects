import pandas as pd
data = { 'apples': [1,2,3,4], 'orange': [ 4,5,6,7], 'pear': [ 8,9,10,11] }
df = pd.DataFrame.from_dict(data, orient ='columns', dtype = float)
df.index = ['antonio', 'gorno', 'zviadauri', 'qalau']
df = df.rename(index = {'antonio':'gio', 'gorno':'ale', 'qalau':'ano', 'zviadauri':'vivi'})
#left one that you want to change, right one that you want to insert at changed one place
print(df)
