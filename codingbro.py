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
# 1.3  Data Structures — DONE
# ============================================================

# cities = ["Hamburg", "Berlin", "Munich"]
# print(cities[0])
# print(cities[-1])
# cities.append("Frankfurt")
# print(cities)
# person = {"name": "Reza", "age": 28, "city": "Hamburg"}
# print(person["name"])
# person["job"] = "Developer"
# print(person)
# coordinates = (53.55, 10.00)
# print(coordinates[0])
# print(type(coordinates))
# tags = {"python", "data", "python", "azure"}
# print(tags)
# tags.add("sql")
# print("python" in tags)
# prlan = ["python", "Java", "C++"]
# prlan.append("Terraform")
# print(prlan)
# jobtitle = {"title": "Developer", "Company": "Bosch", "skills":["Azure", "Data science", "Data Engineering"]}
# print(jobtitle["Company"], "and", jobtitle["skills"][0])
# skills = {"excel", "python", "sql", "python", "excel"}
# print(skills)
# myinfo = ("Reza", 34)
# fact = "Reza" in myinfo
# print(fact)


# ============================================================
# 1.3  Operations — List & Dictionary — DONE
# ============================================================

# movies = ["Inception", "Interstellar", "Dune", "Oppenheimer", "Tenet"]
# print(movies[0])
# print(movies[-1])
# print(movies[1:3])
# movies.append("Dunkirk")
# movies.remove("Dune")
# movies[movies.index("Tenet")] = "The Dark Knight"
# print(len(movies))
# print("Inception" in movies)
# print(movies)
# scores = [88, 95, 70, 60, 99, 45]
# scores.sort()
# print(scores[-1])
# print(len(scores))
# print(100 in scores)
# pinfo = {"name": "Reza", "age":34, "city":"Hamburg", "skills":["Azure", "Python","Eng"]}
# print(pinfo["name"])
# print(pinfo["skills"][1])
# pinfo["goal"] = "death"
# del pinfo["age"]
# print(pinfo.keys())
# print(pinfo.values())
# print("city" in pinfo)
# product = {"name": "Laptop", "price": 999, "in_stock": True}
# print(f"the Item you added is a/an {product['name']}")
# product["price"] = 849
# product["brand"] = "Dell"
# print(product)


# ============================================================
# EXERCISES — Tuple & Set — DONE
# ============================================================

# person = ("Reza", 34, "Hamburg", "Python")
# print(person[0], person[-1])
# print(person[1:3])
# print("Hamburg" in person)
# print(len(person))
# rgb = (255, 128, 0)
# print(rgb[0], rgb[1], rgb[-1], sep="\n")
# print(0 in rgb)
# tools = {"python", "sql", "excel", "python", "sql"}
# print(tools)
# tools.add("power bi")
# tools.remove("excel")
# print("python" in tools)
# team_a = {"python", "sql", "azure"}
# team_b = {"sql", "excel", "power bi"}
# print(team_a & team_b)
# print(team_a | team_b)


# ============================================================
# 1.4  Control Flow — DONE
# ============================================================

# score = 85
# if score >= 90:
#     print("Excellent")
# elif score >= 70:
#     print("Good")
# else:
#     print("Keep practicing")
# skills = ["Python", "SQL", "Azure"]
# for skill in skills:
#     print(f"Learning: {skill}")
# count = 0
# while count < 5:
#     print(count)
#     count += 1
# for i in range(5):
#     print(i)
# for i in range(10):
#     if i == 3:
#         continue
#     if i == 6:
#         break
#     print(i)
# for i, skill in enumerate(skills):
#     print(f"{i}: {skill}")
# age = 20
# if age < 18:
#     print("minor")
# elif 18 <= age < 64:
#     print("adult")
# else:
#     print("senior")
# fruits = ["apple", "banana", "cherry", "mango"]
# for items in fruits:
#     print(items.upper())
# count = 10
# while count > 0:
#     print(count)
#     count -= 1
# for i in range(0, 11, 2):
#     print(i)
# numbers = [4, 7, 2, 9, 1, 8, 3]
# for num in numbers:
#     if num < 5:
#         continue
#     elif num == 8:
#         break
#     else:
#         print(num)


# 6. enumerate — DONE
# cities = ["Hamburg", "Berlin", "Munich", "Frankfurt"]
# for i, city in enumerate(cities, start=1):
#     print(f"{i}: {city}")


# ============================================================
# COMBINED EXERCISES — Control Flow + Data Structures
# ============================================================

# 1. Loop through a dictionary
#    You have this dict:
#    person = {"name": "Reza", "city": "Hamburg", "job": "Developer", "age": 34}
#    Use a for loop to print every key and value like this:
#    name → Reza
#    city → Hamburg
#    (Hint: use .items())


# 2. Filter a list
#    You have this list: scores = [45, 88, 62, 91, 37, 74, 55, 83]
#    Loop through it and collect only scores above 70 into a new list called `high_scores`.
#    Print high_scores at the end.
#    (Hint: start with high_scores = [] and use .append() inside the loop)


# 3. Find an item with enumerate
#    You have this list: tools = ["excel", "sql", "python", "power bi", "azure"]
#    Loop through it using enumerate. When you find "python", print its position and break.
#    Expected output: Found python at position 2


# 4. Count occurrences
#    You have this list: responses = ["yes", "no", "yes", "yes", "no", "yes", "no"]
#    Loop through it and count how many times "yes" appears.
#    Print: "yes count: 4"


# 5. Nested if inside a loop
#    You have this list of dicts:
#    people = [
#        {"name": "Reza", "city": "Hamburg"},
#        {"name": "Ali", "city": "Berlin"},
#        {"name": "Sara", "city": "Hamburg"},
#        {"name": "Max", "city": "Munich"},
#    ]
#    Loop through it and print only the names of people from "Hamburg".