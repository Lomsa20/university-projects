import pandas as pd

df = pd.read_csv('data.csv')
df_copy = df.copy()

df.drop_duplicates(inplace = True)

avg_score = df['score'].mean()
df['score'] = df['score'].fillna(avg_score)

#romove duplicates based on their name
df.drop_duplicates(subset='name',inplace = True)

#convert  into upper bound
df['city'] = df['city'].str.upper()

above_avg = df[df['score'] > avg_score]
above_avg = above_avg.sort_values(by = 'score', ascending = False)
if not above_avg.empty:
    print(above_avg)
    above_avg.to_csv('exam1_cleaned.csv', index = False)
else:
    print('No score above average')

print(df_copy)
print(df.head())
