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
