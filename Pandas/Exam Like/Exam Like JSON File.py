import pandas as pd

df = pd.read_json('st.json')
df = df.drop_duplicates()
        # OR
df.drop_duplicates(inplace=True)
df_copy = df.copy()
avg = df['score'].mean()
above_avg = df[df['score'] > avg]
if not above_avg.empty: # if above_avg is empty it will not execute it so if it is not then it will be executed
    print(above_avg[['name', 'score']])
else:
    print('below avg')
print(df_copy)
print(df.drop_duplicates())
print(df.head())