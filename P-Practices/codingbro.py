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
# COMBINED EXERCISES — Control Flow + Data Structures — DONE
# ============================================================

# # 1. Loop through a dictionary
# person = {"name": "Reza", "city": "Hamburg", "job": "Developer", "age": 34}
# for a, b in person.items():
#     print(f"{a} -> {b}")

# # 2. Filter a list
# scores = [45, 88, 62, 91, 37, 74, 55, 83]
# high_scores = []
# for num in scores:
#     if num > 70:
#         high_scores.append(num)
# print(high_scores)

# # 3. Find an item with enumerate
# tools = ["excel", "sql", "python", "power bi", "azure"]
# for i, item in enumerate(tools):
#     if item == "python":
#         print(f"Found {item} at position {i}")
#         break

# # 4. Count occurrences
# responses = ["yes", "no", "yes", "yes", "no", "yes", "no"]
# answer = responses.count("yes")
# print(f"yes count: {answer}")

# # 5. Nested if inside a loop
# people = [
#     {"name": "Reza", "city": "Hamburg"},
#     {"name": "Ali", "city": "Berlin"},
#     {"name": "Sara", "city": "Hamburg"},
#     {"name": "Max", "city": "Munich"},
# ]
# for person in people:
#     if person["city"] == "Hamburg":
#         print(person["name"])


# ============================================================
# EXERCISES — Dict in List / List in Dict — DONE
# ============================================================

# # 1. Print only names of employees in the "Data" department
# employees = [
#     {"name": "Reza",  "department": "Data",    "salary": 4500},
#     {"name": "Ali",   "department": "DevOps",  "salary": 3800},
#     {"name": "Sara",  "department": "Data",    "salary": 4200},
#     {"name": "Max",   "department": "Finance", "salary": 3500},
# ]
# for persons in employees:
#     if persons["department"] == "Data":
#         print(persons["name"])

# # 2. Same list — print each employee like: Reza works in Data and earns 4500
# for persons in employees:
#     print(f"{persons['name']} works in {persons['department']} and earns {persons['salary']}")

# # 3. Dict with a list inside
# company = {
#     "name": "Bosch",
#     "locations": ["Hamburg", "Berlin", "Munich"],
#     "headcount": 5000
# }
# print(company["locations"][1])
# for location in company["locations"]:
#     print(location)


# ============================================================
# 1.5  Functions
# ============================================================

# --- EXAMPLES ---

# Basic function — def, parameters, return
def greet(name):
    return f"Hello, {name}!"

print(greet("Reza"))


# Default parameter — used when caller doesn't pass a value
def connect(host, port=5432):
    return f"Connecting to {host}:{port}"

print(connect("localhost"))          # uses default port
print(connect("localhost", 3306))    # overrides default


# Multiple return values
def min_max(numbers):
    return min(numbers), max(numbers)

high, low = min_max([4, 1, 9, 2, 7])
print(low, high)


# *args — accept any number of positional arguments
def total(*numbers):
    return sum(numbers)

print(total(10, 20, 30))


# **kwargs — accept any number of keyword arguments
def create_profile(**fields):
    return fields

print(create_profile(name="Reza", city="Hamburg", role="Data Engineer"))


# Lambda — short anonymous function, one expression only
double = lambda x: x * 2
print(double(5))


# --- EXERCISES ---

# 1. Write a function called `describe_person`
#    It takes name, age, city as parameters
#    It returns: "Reza is 34 years old and lives in Hamburg"
def describe_person(name,age,city):
    return f"{name} is {age} years old and lives in {city}"
print(describe_person(name="Reza", age=34, city="Hamburg"))

# 2. Write a function called `is_adult`
#    It takes age as a parameter
#    It returns True if age >= 18, False otherwise
#    Test it: print(is_adult(20)) → True, print(is_adult(15)) → False
def is_adult(age):
    if age > 18:
        return "True"
    else:
        return "False"
print(is_adult(13))
# 3. Write a function called `summarize`
#    It takes a list of numbers
#    It returns three values: total (sum), average, and count
#    Print all three on one line: Total: 30 | Avg: 10.0 | Count: 3
def summarize(numbers):
    return sum(numbers), sum(numbers)/len(numbers), numbers.count(12)
totla, average, count = summarize([3,5,7,3,1,4])
print(f"total: {totla}, average: {average} count: {count}")

# 4. Write a function called `filter_by_city`
#    It takes a list of employee dicts and a city name
#    It returns a new list with only employees from that city
#    Use this data:
employees = [
    {"name": "Reza",  "city": "Hamburg"},
    {"name": "Ali",   "city": "Berlin"},
    {"name": "Sara",  "city": "Hamburg"},
    {"name": "Max",   "city": "Munich"},
]
def filter_by_city(employees, city):
    result = []
    for person in employees:
        if person["city"] == city:
            result.append(person["name"])
    return result
print(filter_by_city(employees, "Hamburg"))
#    Expected: filter_by_city(employees, "Hamburg") → Reza and Sara dicts

# 5. Write a lambda that takes a number and returns True if it's even
#    Hint: use % — even means remainder of dividing by 2 is 0
#    Test: print(is_even(4)) → True, print(is_even(7)) → False