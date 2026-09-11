# ============================================================
# EXERCISES — Control Flow + Data Structures (mixed)
# ============================================================

# 1. Loop through this list and print only tools that start with "p"
#    tools = ["python", "power bi", "sql", "excel", "pandas", "azure"]
#    Expected: python, power bi, pandas
tools = ["python", "power bi", "sql", "excel", "pandas", "azure"]


# 2. You have this list of orders — loop through and separate them:
#    collect completed ones into done = []
#    collect pending ones into waiting = []
#    print both lists at the end
orders = [
    {"id": 1, "status": "completed"},
    {"id": 2, "status": "pending"},
    {"id": 3, "status": "completed"},
    {"id": 4, "status": "pending"},
    {"id": 5, "status": "completed"},
]


# 3. Loop through numbers 1 to 20 using range()
#    - skip any number divisible by 3 (hint: use % — remainder operator)
#    - stop completely when you hit 15
#    - print the rest
#    Expected: 1 2 4 5 7 8 10 11 13 14


# 4. You have this dict of products — loop through .items()
#    and print only products where price is above 100
#    Expected:
#    Laptop: 999
#    Monitor: 349
products = {
    "Mouse": 25,
    "Laptop": 999,
    "Keyboard": 79,
    "Monitor": 349,
    "Webcam": 59,
}


# 5. You have this list of students — find the first one who passed (score >= 60)
#    print their name and stop — don't print the rest
#    Expected: First pass: Sara
students = [
    {"name": "Ali",  "score": 45},
    {"name": "Max",  "score": 38},
    {"name": "Sara", "score": 72},
    {"name": "Reza", "score": 91},
]
