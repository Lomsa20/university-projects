import pandas as pd

# Load JSON
df = pd.read_json('st.json')

# Calculate means correctly
avg_score = df['score'].mean()
avg_day = df['days_present'].mean()
avg_absent = df['days_absent'].mean()

# Fill missing values
df['score'] = df['score'].fillna(avg_score)
df['days_present'] = df['days_present'].fillna(avg_day)
df['days_absent'] = df['days_absent'].fillna(avg_absent)

# Add attendance_rate column
df['attendance_rate'] = df['days_present'] / (df['days_present'] + df['days_absent'])

# Filter students who meet both conditions
filtered_df = df[(df['score'] > 80) & (df['attendance_rate'] > 0.9)]

# Get all column names
all_keys = list(df.columns)

# Print filtered DataFrame with all columns
if not filtered_df.empty:
    print(filtered_df[all_keys])
    