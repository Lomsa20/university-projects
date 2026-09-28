def profile(name, age=30, *skills, **details):
    print(f"Name: {name}, age: {age}")
    print("skills", skills)
    print("details", details)

profile("maria", 35, "python", "data science", city = "kutaisi", job = "jobless")