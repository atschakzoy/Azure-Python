# Python Quick Reference

---

## 1.2 — Variables & Data Types

### Data Types
```python
name = "Reza"      # str
age = 28           # int
height = 1.82      # float
is_employed = True # bool
result = None      # NoneType
```

### type()
```python
type(name)   # <class 'str'>
```

### print() parameters
```python
print("a", "b", "c")              # a b c  — space is default separator
print("a", "b", "c", sep=", ")    # a, b, c
print("a", "b", "c", sep="\n")    # each on its own line
print("done", end="!")             # end replaces the newline — prints: done!
```

### Type Conversion
```python
int("42")      # 42
float("3.14")  # 3.14
str(100)       # "100"
# input() always returns str — convert before using as number
int(input("Age: ")) + 1
```
> Data enters your program from the outside world (user, file, API) — the outside world doesn't know Python's types. You convert so Python can work with the data correctly.

### f-strings
```python
f"Hello {name}, you are {age} years old."
f"Pi: {3.14159:.2f}"    # 2 decimal places
f"Total: {1500000:,}"   # thousands separator
```
> Anytime you'd write `"text" + str(variable) + "more text"` — use an f-string instead. Cleaner, shorter, easier to read.

### String Methods
```python
s = "  Hello, World!  "
s.strip()                    # "Hello, World!"
s.lower() / s.upper()        # lowercase / uppercase
s.replace("World", "Reza")   # "Hello, Reza!"
s.split(", ")                # ["Hello", "World!"]
" ".join(["a", "b"])         # "a b"
s.find("World")              # index or -1
s.startswith("Hello")        # True / False
s.endswith("!")              # True / False
s.count("l")                 # 3
```
> There are 47 string methods — you only need these 11. Look up the rest when you need them, even senior devs Google string methods.

---

## 1.3 — Data Structures

| Structure | Ordered | Changeable | Duplicates | Use for |
|-----------|---------|-----------|------------|---------|
| `list` | yes | yes | yes | any ordered collection |
| `dict` | yes | yes | keys: no | labeled data, JSON, records |
| `tuple` | yes | **no** | yes | fixed data that shouldn't change |
| `set` | **no** | yes | **no** | unique values, fast membership check |

```python
# list — ordered, use most of the time
cities = ["Hamburg", "Berlin", "Munich"]
cities[0]            # "Hamburg"
cities.append("Frankfurt")
cities[-1]           # last item

# dict — key-value pairs
person = {"name": "Reza", "age": 28}
person["name"]       # "Reza"
person["city"] = "Hamburg"   # add new key

# tuple — locked, can't change after creation
coordinates = (53.55, 10.00)
coordinates[0]       # 53.55

# set — no duplicates, no index
tags = {"python", "data", "python"}   # stores 2, not 3
tags.add("azure")
"python" in tags     # True
```

> 80% of the time you'll use `list` and `dict`. Tuple and set are situational.
> Mutable = changeable (list, dict, set). Immutable = locked (tuple, str, int, float).

### Operations

**List**
```python
cities = ["Hamburg", "Berlin", "Munich"]

cities[0]           # "Hamburg" — indexing: get item by position (starts at 0)
cities[-1]          # "Munich"  — negative index: count from the end (-1 = last)
cities[0:2]         # ["Hamburg", "Berlin"] — slicing: get a range [start:end] (end not included)
cities.append("Frankfurt")  # add a new item to the end
cities.remove("Berlin")     # remove item by value
cities[0] = "Köln"                        # update: replace item at position 0
cities[cities.index("Munich")] = "Köln"  # update by value: find position first, then replace
len(cities)                 # count how many items are in the list
"Hamburg" in cities         # check if a value exists — returns True or False
cities.sort()               # sort low to high — modifies the original list
cities.sort(reverse=True)   # sort high to low
sorted(cities)              # returns a sorted copy — original stays unchanged
cities + ["Munich"]         # operator: combine two lists into one
cities * 2                  # operator: repeat the list
cities.count("Hamburg")     # how many times a value appears in the list
cities.index("Berlin")      # returns the position of a value
cities.reverse()            # reverses the order in place
```

**Dictionary**
```python
person = {"name": "Reza", "age": 28}

person["name"]              # get value by key — like looking up a word in a dictionary
person["skills"][1]         # access nested list inside a dict — get key first, then index
person["city"] = "Hamburg"  # add a new key, or update it if it already exists
del person["age"]           # delete a key and its value completely
person.keys()               # returns all keys
person.values()             # returns all values
person.items()              # returns all key-value pairs as tuples — [("name","Reza"), ...]

for key, value in person.items():   # loop through every key and value
    print(f"{key} → {value}")

# access a list inside a dict — get the key first, then loop the list
company = {"name": "Bosch", "locations": ["Hamburg", "Berlin", "Munich"]}
for location in company["locations"]:
    print(location)
person.get("name")          # safe get — returns None instead of error if key doesn't exist
person.get("age", 0)        # safe get with default — returns 0 if "age" missing
person.update({"city": "Berlin"})  # merge another dict into this one — adds or updates keys
a | b                       # operator: merge two dicts into a new one (Python 3.9+)
"name" in person            # check if a key exists — True / False
```

**Tuple**
```python
coords = (53.55, 10.00)

coords[0]        # indexing — same as list, get by position
coords[0:1]      # slicing — same as list, get a range
len(coords)      # count how many items
53.55 in coords  # check if a value exists
coords + (99,)   # operator: combine two tuples into a new one
coords * 2       # operator: repeat the tuple
coords.count(53.55)  # how many times a value appears
coords.index(10.00)  # returns the position of a value
# nothing else — tuples are read-only, you can only look at them
```

**Set**
```python
tags = {"python", "data", "azure"}

tags.add("sql")      # add a new item — ignored if already exists
tags.remove("data")  # remove an item — error if not found
"python" in tags     # check if value exists — very fast, faster than list
a & b                # operator — intersection: items that appear in BOTH sets       → Shift + 7
a | b                # operator — union: all items from both sets combined             → Shift + \
a - b                # operator — difference: items in a but NOT in b                 → - key
a ^ b                # operator — symmetric difference: items in either but NOT both  → Shift + 6
# no indexing or slicing — sets have no position
```

---

## 1.4 — Control Flow

### if / elif / else — make decisions
```python
if age < 18:
    print("minor")
elif age < 65:    # already know >= 18, only check upper bound
    print("adult")
else:
    print("senior")
```
> Python checks conditions in order — once one is True it skips the rest.
> `elif` and `else` are optional — you can have just `if` alone.
> Indentation is not optional — Python uses it to know what's inside the block (4 spaces or 1 tab).

### for loop — repeat for each item
```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit.upper())

# filter a list into a new list
scores = [45, 88, 62, 91, 37, 74]
high_scores = []
for num in scores:
    if num > 70:
        high_scores.append(num)
print(high_scores)   # [88, 91, 74]

# loop through a list of dicts — nested if
people = [{"name": "Reza", "city": "Hamburg"}, {"name": "Ali", "city": "Berlin"}]
for person in people:
    if person["city"] == "Hamburg":
        print(person["name"])   # only prints Reza
```
> Use `for` when you know the items — works on any collection: list, tuple, set, dict, string, range.

### while loop — repeat until condition is False
```python
count = 10
while count > 0:
    print(count)
    count -= 1    # -= means: count = count - 1  (also: += to add)
```
> Use `while` when you don't know how many times — loop until something changes.
> Always make sure the condition eventually becomes False — otherwise it runs forever.

### range() — generate a sequence of numbers
```python
range(5)           # 0, 1, 2, 3, 4
range(2, 10)       # 2 to 9
range(0, 11, 2)    # 0, 2, 4, 6, 8, 10 — start, stop, step
```
> `stop` is never included. `range(5)` starts at 0 by default.

### break / continue — control loop flow
```python
for i in range(10):
    if i < 5:
        continue   # skip — go to next iteration
    if i == 8:
        break      # stop — exit loop completely
    print(i)       # prints 5, 6, 7
```
> `break` exits the whole loop. `continue` skips only the current iteration and keeps going.

### enumerate() — loop with index and value together
```python
for i, skill in enumerate(["Python", "SQL", "Azure"]):
    print(f"{i}: {skill}")   # 0: Python / 1: SQL / 2: Azure

# find an item and print its position
tools = ["excel", "sql", "python", "azure"]
for i, item in enumerate(tools):
    if item == "python":
        print(f"Found {item} at position {i}")
        break
```
> Use when you need both the position and the value while looping.

---

## 1.5 — Functions

### Anatomy of a function
```
def greet(name):
─┬─ ──┬── ──┬──
 │    │     └── parameter — placeholder variable, gets value when called
 │    └──────── function name — what you call to run it
 └────────────── def keyword — tells Python a function is being defined

    return f"Hello, {name}!"
    ──┬──  ─────────────────
      │    └── return value — what gets sent back to the caller
      └──────── return keyword — sends the value out of the function

print(greet("Reza"))
      ──┬──  ──┬──
        │      └── argument — the actual value passed in ("Reza" → name)
        └────────── function call — runs the function
```

| Part | Name | Example |
|---|---|---|
| `def` | keyword | signals a function definition |
| `greet` | function name | what you type to call it |
| `(name)` | parameter | placeholder inside the function |
| `:` | block start | marks start of function body |
| indented lines | function body | the code that runs |
| `return` | keyword | sends a value back out |
| `f"Hello, {name}!"` | return value | what the function gives back |
| `greet("Reza")` | function call | runs the function |
| `"Reza"` | argument | the actual value passed to the parameter |

### def — define a function
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Reza"))   # Hello, Reza!
```
> `def` tells Python you're defining a function. `return` sends a value back to whoever called it. Without `return`, the function returns `None`.

### Parameters
```python
def greet(name):       # name is the parameter — a placeholder variable
    return f"Hello, {name}!"

greet("Reza")          # "Reza" is the argument — the actual value passed in
```
> Parameters are empty boxes with labels. When you call the function, you drop a value into each box.

### Multiple parameters — what each one receives
```python
def filter_by_city(employees, city):
    ...

filter_by_city(employees, "Hamburg")
#              ↑            ↑
#    argument 1        argument 2
```

| Parameter | Receives | What it is |
|-----------|----------|------------|
| `employees` | the list of dicts | your data |
| `city` | `"Hamburg"` | the filter value |

Arguments are matched to parameters **left to right by position** — first argument goes to first parameter, second to second.

> Parameters are just placeholders. It doesn't matter that the global variable and the parameter are both called `employees` — they are separate things. The parameter only gets a value when the function is called.

### Default parameters
```python
def connect(host, port=5432):
    return f"Connecting to {host}:{port}"

connect("localhost")          # uses default: Connecting to localhost:5432
connect("localhost", 3306)    # overrides default: Connecting to localhost:3306
```
> Required parameters come first, default parameters come after — always.

### Multiple return values + unpacking
```python
def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 9, 2, 7])   # unpacking — left to right
print(low, high)   # 1 9
```
> A function can return more than one value separated by a comma. Unpack them into separate variables on the left — order matters.

### *args — any number of positional arguments
```python
def total(*numbers):      # * collects all values into a tuple
    return sum(numbers)

total(10, 20, 30)         # numbers = (10, 20, 30) → returns 60
total(5)                  # numbers = (5,)          → returns 5
```
> Use `*args` when you don't know how many values the caller will pass.

### **kwargs — any number of keyword arguments
```python
def create_profile(**fields):   # ** collects all key=value pairs into a dict
    return fields

create_profile(name="Reza", city="Hamburg", role="Data Engineer")
# fields = {"name": "Reza", "city": "Hamburg", "role": "Data Engineer"}
```

| | Syntax | Collects into | How you pass values |
|---|---|---|---|
| `*args` | one star | tuple | `total(10, 20, 30)` |
| `**kwargs` | two stars | dict | `create_profile(name="Reza")` |

### Lambda — short anonymous function
```python
double = lambda x: x * 2
double(5)   # 10

# same as:
def double(x):
    return x * 2
```
> Lambda is one line only — no loops, no multiple conditions. Use `def` the moment you need more than one expression.

### When to use a function
```python
# without function — logic repeated 3 times
print(f"Hello, Reza!")
print(f"Hello, Ali!")
print(f"Hello, Sara!")

# with function — logic lives in one place
def greet(name):
    return f"Hello, {name}!"

print(greet("Reza"))
print(greet("Ali"))
print(greet("Sara"))
```
> Write once, call anywhere. If the logic needs to change, change it in one place and everything updates.
