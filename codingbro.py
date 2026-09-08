# ============================================================
# 1.2  Variables and Data Types
# ============================================================

# --- PART 1: Basic variables ---
name = "Reza"
age = 28
height = 1.82
is_employed = True
result = None

print(name)
print(age)
print(height)
print(is_employed)
print(result)


# --- PART 2: type() ---
print(type(name))        # <class 'str'>
print(type(age))         # <class 'int'>
print(type(height))      # <class 'float'>
print(type(is_employed)) # <class 'bool'>
print(type(result))      # <class 'NoneType'>


# --- PART 3: f-strings ---
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)


# --- PART 4: Type conversion ---
num_as_string = "42"
print(int(num_as_string) + 8)   # 50
print(float("3.14") * 2)        # 6.28
print(str(100) + " points")     # 100 points


# --- PART 5: String methods ---
raw = "  Hello, World!  "
print(raw.strip())              # removes leading/trailing spaces
print(raw.strip().lower())      # hello, world!
print(raw.strip().upper())      # HELLO, WORLD!
print(raw.strip().replace("World", "Reza"))  # Hello, Reza!
print(raw.strip().split(", "))  # ['Hello', 'World!']


# ============================================================
# EXERCISES — try these yourself, then run the file
# ============================================================

# 1. Create a variable `city` set to "Hamburg" and print it in lowercase.
city = "Hamburg"
print(F"{city.lower()}")
# 2. Create a variable `temperature` set to the string "22" and convert it
#    to a float. Then print: "The temperature is 22.0 degrees."
#    Use an f-string.
temperature = float("22")
print(f"the temperature is {temperature}")
# 3. Create a variable `sentence = "  Python is awesome  "` and print it
#    with whitespace stripped, all caps, and with "awesome" replaced by "powerful".
sentence = " Python is awesome "
print(sentence.strip().upper().replace("AWESOME","powerful"))
# 4. What is the type of True * 5?  Use type() to check, then print the result.
#    (Hint: booleans are a subclass of int in Python)
print(type(True * 5))
