import pandas as pd

df_scores = pd.read_csv('data.csv')

#print(df_scores.head())
df_scores.drop_duplicates(inplace=True)
avg_math = df_scores['math'].mean()
avg_eng = df_scores['english'].mean()
avg_science = df_scores['science'].mean()

df_scores['math'] = df_scores['math'].fillna(avg_math)
df_scores['english'] = df_scores['english'].fillna(avg_eng)
df_scores['science'] = df_scores['science'].fillna(avg_science)
#print(df_scores)
df_scores['total_scores'] = (df_scores['math'] + df_scores['english'] + df_scores['science'])

#filter scores
filter_total = df_scores[df_scores['total_scores'] >= 240]

#remove duplicates by their name
df_scores.drop_duplicates(subset = 'name', inplace = True)
df_scores.sort_values(by = 'total_scores', ascending = False, inplace = True)
if not filter_total.empty:
    print(filter_total)
else:
    print('Nothing')

def assign_grade(total):
    if total >= 270:
        return "A"
    elif 250 <= total <= 269:
        return "B"
    else:
        return "C"

df_scores['grade'] = df_scores['total_scores'].apply(assign_grade)
print(df_scores)
filter_total.to_csv('data1.csv', index = False)