import pandas as pd
import json

st = {
  "student": {
    "name": "Lomsa",
    "age": 16,
    "school": "Military School Lyceum",
    "skills": ["Python", "Chess", "Bow Making"],
    "address": {
      "city": "Zaodi",
      "country": "Georgia"
    },
    "active": True
  },
  "courses": [
    {"name": "Programming", "level": "Intermediate", "completed": False},
    {"name": "Physical Training", "level": "Advanced", "completed": True}
  ]
}

# Save dictionary as JSON file
with open('st.json', 'w') as f:
    json.dump(st, f, indent=2)

# Load JSON into Python as dictionary
with open('st.json') as f:
    data = json.load(f)

# Flatten student data
df_student = pd.json_normalize(
    data['student'],
    sep='.',  # nested keys will be like address.city
)

# Flatten courses data
df_courses = pd.json_normalize(data['courses'])

# Flatten skills list into separate rows
df_skills = pd.DataFrame(data['student']['skills'], columns=['skill'])

# Print outputs
print("Student Data:")
print(df_student)
print("\nCourses Data:")
print(df_courses)
print("\nSkills Data:")
print(df_skills)
