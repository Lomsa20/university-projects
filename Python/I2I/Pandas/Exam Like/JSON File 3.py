import pandas as pd
import json

with open('st.json','r') as f:
    data = json.load(f)
df = pd.json_normalize(data)

avg_eng = df['scores.english'].mean()
avg_math = df['scores.math'].mean()
avg_science = df['scores.science'].mean()

df['scores.english'] = df['scores.english'].fillna(avg_eng)
df['scores.math'] = df['scores.math'].fillna(avg_math)
df['scores.science'] = df['scores.science'].fillna(avg_science)

# add new column
df['total_scores'] = (df['scores.english'] + df['scores.math'] + df['scores.science'])

# it must be above filter
df.drop_duplicates(subset =['name'],inplace=True)

#filter total scores for each student
filter_total = df[df['total_scores'] >= 240]
filter_total = filter_total.sort_values(by = 'total_scores', ascending = False)
all_key = list(df.columns)

if not filter_total.empty:
    print(filter_total)
    filter_total.to_json('stu.json', index = False)
else:
    print(' students are filtered')
