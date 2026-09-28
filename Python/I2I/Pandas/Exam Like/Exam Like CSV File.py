# name age city score
import pandas as pd

df = pd.read_csv('data.csv')
df_clean = df.copy()
df.drop_duplicates()
avg_score = df['score'].mean()
above_avg = df[df['score'] > avg_score]
if not above_avg.empty:
    print(above_avg[['name', 'score']],)
    print(above_avg.shape)
    above_avg.to_csv('students_cleaned.csv', index=False) # index = False prevents Pandas from writing the row numbers
else:
    print('Loooseeeersss')
#print(df['score'].mean())
#print(df.drop_duplicates())
#print(df_clean)
#print(df.info())
#print(df.head())
