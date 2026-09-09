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
cities[0] = "Köln"          # update: replace item at position 0
len(cities)                 # count how many items are in the list
"Hamburg" in cities         # check if a value exists — returns True or False
```

**Dictionary**
```python
person = {"name": "Reza", "age": 28}

person["name"]              # get value by key — like looking up a word in a dictionary
person["city"] = "Hamburg"  # add a new key, or update it if it already exists
del person["age"]           # delete a key and its value completely
person.keys()               # returns all keys: dict_keys(["name", "city"])
person.values()             # returns all values: dict_values(["Reza", "Hamburg"])
"name" in person            # check if a key exists — True / False
```

**Tuple**
```python
coords = (53.55, 10.00)

coords[0]        # indexing — same as list, get by position
coords[0:1]      # slicing — same as list, get a range
len(coords)      # count how many items
53.55 in coords  # check if a value exists
# nothing else — tuples are read-only, you can only look at them
```

**Set**
```python
tags = {"python", "data", "azure"}

tags.add("sql")          # add a new item (ignored if already exists)
tags.remove("data")      # remove an item
"python" in tags         # check if value exists — very fast, faster than list
tags1 & tags2            # intersection: only items that appear in BOTH sets
tags1 | tags2            # union: all items from both sets combined (no duplicates)
# no indexing or slicing — sets have no position
```
