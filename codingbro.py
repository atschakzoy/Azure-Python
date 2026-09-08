# ============================================================
# 1.2  Variables and Data Types — DONE
# ============================================================

# if False:
#     name = "Reza"
#     age = 28
#     height = 1.82
#     is_employed = True
#     result = None
#     print(name, age, height, is_employed, result)
#     print(type(name), type(age), type(height), type(is_employed), type(result))
#     greeting = f"Hello, {name}! You are {age} years old."
#     print(greeting)
#     num_as_string = "42"
#     print(int(num_as_string) + 8)
#     print(float("3.14") * 2)
#     print(str(100) + " points")
#     raw = "  Hello, World!  "
#     print(raw.strip())
#     print(raw.strip().lower())
#     print(raw.strip().upper())
#     print(raw.strip().replace("World", "Reza"))
#     print(raw.strip().split(", "))
#     city = "Hamburg"
#     print(f"{city.lower()}")
#     temperature = float("22")
#     print(f"The temperature is {temperature} degrees.")
#     sentence = " Python is awesome "
#     print(sentence.strip().upper().replace("AWESOME", "POWERFUL"))
#     print(type(True * 5))


# ============================================================
# 1.3  Data Structures
# ============================================================

# --- PART 1: List ---
cities = ["Hamburg", "Berlin", "Munich"]
print(cities[0])       # first item
print(cities[-1])      # last item
cities.append("Frankfurt")
print(cities)

# --- PART 2: Dictionary ---
person = {"name": "Reza", "age": 28, "city": "Hamburg"}
print(person["name"])
person["job"] = "Developer"
print(person)

# --- PART 3: Tuple ---
coordinates = (53.55, 10.00)
print(coordinates[0])
print(type(coordinates))

# --- PART 4: Set ---
tags = {"python", "data", "python", "azure"}
print(tags)             # "python" appears once only
tags.add("sql")
print("python" in tags) # True 


# ============================================================
# EXERCISES
# ============================================================

# 1. Create a list of 3 programming languages. Print the second one.
#    Then add a 4th language and print the full list.
prlan = ["python", "Java", "C++"]
prlan.append("Terraform")
print(prlan)

# 2. Create a dictionary for a job posting with keys:
#    title, company, location, and skills (skills should be a list).
#    Print the company and the first skill.
jobtitle = {"title": "Developer", "Company": "Bosch", "skills":["Azure", "Data science", "Data Engineering"]}
print (jobtitle["Company"], "and" ,jobtitle["skills"][0])

# 3. Create a set with these values: "excel", "python", "sql", "python", "excel"
#    Print the set — how many items does it have?
skills = {"excel", "python", "sql", "python", "excel"}
print(skills)
# 4. Create a tuple with your name and age. Try to change the age value.
#    What error do you get?
myinfo = ("Reza", 34)
fact = "Reza" in myinfo
print (fact)