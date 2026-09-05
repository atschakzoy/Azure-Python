# Python Learning Path — Data Engineering, Data Science & AI on Azure

**Goal:** Become job-ready for Data Engineer, Data Scientist, or AI Engineer roles in Hamburg.  
**Cloud focus:** Microsoft Azure

---

## Overview

| # | Topic | Status |
|---|---|---|
| 1 | Python Fundamentals | ✅ Done |
| 2 | pandas + SQL | ✅ Done |
| 3 | FastAPI + APIs | ✅ Done |
| 4 | LangChain / Azure OpenAI — RAG & AI Solutions | ✅ Done |
| 5 | Azure Cloud for Data & AI | ✅ Done |

---

## Step 1 — Python Fundamentals
**Estimated time:** 3–4 weeks (1–2 hours/day)

This is the foundation. Everything else builds on this. Do not skip or rush it.

---

### 1.1 Setup (Day 1)

- Install **Python 3.11+** from [python.org](https://python.org)
- Install **VS Code** as your editor
- Install the **Python extension** in VS Code
- Learn to run a `.py` file from the terminal:
  ```
  python my_file.py
  ```
- Understand what a **virtual environment** is and how to create one:
  ```
  python -m venv venv
  source venv/bin/activate   # Mac/Linux
  venv\Scripts\activate      # Windows
  ```

---

### 1.2 Variables and Data Types (Days 2–3)

Learn the basic building blocks of any Python program.

```python
# Strings
name = "Reza"
greeting = f"Hello, {name}"   # f-strings are essential

# Numbers
age = 28          # integer
height = 1.82     # float

# Boolean
is_employed = True

# None (like null in other languages)
result = None
```

**Key concepts:**
- `type()` — check what type a variable is
- Type conversion: `int("42")`, `str(123)`, `float("3.14")`
- String methods: `.lower()`, `.upper()`, `.strip()`, `.replace()`, `.split()`

---

### 1.3 Data Structures (Days 4–6)

These four structures are used constantly in data work.

```python
# List — ordered, changeable, allows duplicates
cities = ["Hamburg", "Berlin", "Munich"]
cities.append("Frankfurt")
cities[0]          # Hamburg
cities[-1]         # Frankfurt (last item)

# Dictionary — key-value pairs (like JSON)
person = {
    "name": "Reza",
    "age": 28,
    "city": "Hamburg"
}
person["name"]     # Reza
person["skills"] = ["Python", "SQL"]  # add new key

# Tuple — ordered, unchangeable
coordinates = (53.55, 10.00)   # latitude, longitude of Hamburg

# Set — unordered, no duplicates
unique_tags = {"python", "data", "azure", "python"}   # stores 3, not 4
```

**Practice:** Create a dictionary representing a job posting with keys like `title`, `company`, `skills`, `location`.

---

### 1.4 Control Flow (Days 7–8)

```python
# If / elif / else
score = 85

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Keep practicing")

# For loop
skills = ["Python", "SQL", "Azure"]
for skill in skills:
    print(f"Learning: {skill}")

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Loop with range
for i in range(10):      # 0 to 9
    print(i)
```

**Key concepts:**
- `break` — stop the loop early
- `continue` — skip to the next iteration
- `enumerate()` — get index and value together
  ```python
  for i, skill in enumerate(skills):
      print(f"{i}: {skill}")
  ```

---

### 1.5 Functions (Days 9–11)

Functions are how you organize and reuse code.

```python
# Basic function
def greet(name):
    return f"Hello, {name}"

print(greet("Reza"))

# Default parameters
def connect_to_db(host, port=5432):
    return f"Connecting to {host}:{port}"

# Multiple return values
def get_min_max(numbers):
    return min(numbers), max(numbers)

low, high = get_min_max([3, 1, 9, 2])

# *args — accept any number of arguments
def sum_all(*numbers):
    return sum(numbers)

# **kwargs — accept any number of keyword arguments
def create_record(**fields):
    return fields

record = create_record(name="Reza", city="Hamburg", role="Data Engineer")
```

**Key concept — Lambda (short anonymous function):**
```python
double = lambda x: x * 2
double(5)   # 10

# Used a lot with pandas later
```

---

### 1.6 List Comprehensions (Day 12)

A concise way to create lists — used constantly in data work.

```python
# Without comprehension
squares = []
for x in range(10):
    squares.append(x ** 2)

# With comprehension (preferred)
squares = [x ** 2 for x in range(10)]

# With condition
even_squares = [x ** 2 for x in range(10) if x % 2 == 0]

# Dictionary comprehension
word_lengths = {word: len(word) for word in ["Python", "Azure", "Data"]}
# {"Python": 6, "Azure": 5, "Data": 4}
```

---

### 1.7 File I/O (Day 13)

Reading and writing files is core to data engineering.

```python
# Write to a file
with open("output.txt", "w") as f:
    f.write("Hello from Python\n")

# Read from a file
with open("output.txt", "r") as f:
    content = f.read()

# Read line by line
with open("data.txt", "r") as f:
    for line in f:
        print(line.strip())

# Working with CSV (before pandas)
import csv

with open("data.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)   # each row is a dictionary
```

**Key concept:** Always use `with open(...)` — it automatically closes the file.

---

### 1.8 Error Handling (Day 14)

Pipelines and AI solutions must handle errors gracefully — they should never just crash.

```python
# Basic try / except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Catch any error
try:
    data = int("not a number")
except ValueError as e:
    print(f"Error: {e}")

# Finally — runs no matter what
try:
    file = open("data.txt")
    content = file.read()
except FileNotFoundError:
    print("File not found")
finally:
    print("Done attempting to read file")

# Raise your own error
def load_data(path):
    if not path.endswith(".csv"):
        raise ValueError(f"Expected a .csv file, got: {path}")
```

---

### 1.9 Modules and Packages (Days 15–16)

In real projects, code is split across multiple files.

```python
# math — built-in module
import math
math.sqrt(144)   # 12.0
math.ceil(4.2)   # 5

# os — interact with the operating system
import os
os.getcwd()                  # current directory
os.listdir(".")              # list files
os.path.join("data", "file.csv")  # safe path building

# datetime — work with dates (critical for data engineering)
from datetime import datetime, timedelta

now = datetime.now()
yesterday = now - timedelta(days=1)
formatted = now.strftime("%Y-%m-%d")   # "2026-08-26"

# json — read and write JSON (used everywhere in APIs and Azure)
import json

data = {"name": "Reza", "role": "Data Engineer"}
json_string = json.dumps(data)          # dict → string
parsed = json.loads(json_string)        # string → dict

with open("data.json", "w") as f:
    json.dump(data, f, indent=2)        # write to file
```

---

### 1.10 Classes and OOP — basics only (Days 17–18)

You don't need to be an OOP expert, but you need to read and write basic classes.

```python
class DataPipeline:

    def __init__(self, name, source):
        self.name = name
        self.source = source
        self.records_processed = 0

    def run(self):
        print(f"Running pipeline: {self.name}")
        print(f"Reading from: {self.source}")

    def log_progress(self, count):
        self.records_processed += count
        print(f"Processed {self.records_processed} records so far")


pipeline = DataPipeline("Sales ETL", "Azure Blob Storage")
pipeline.run()
pipeline.log_progress(500)
```

---

### 1.11 pip and Virtual Environments (Day 19)

Managing packages is a daily task.

```bash
# Install a package
pip install requests

# Install a specific version
pip install pandas==2.2.0

# Save all dependencies to a file
pip freeze > requirements.txt

# Install from a requirements file (used to reproduce environments)
pip install -r requirements.txt

# List installed packages
pip list
```

---

### Practice Projects for Step 1

Do at least one before moving to Step 2.

| Project | What you practice |
|---|---|
| Read a CSV, filter rows, write results to a new CSV | File I/O, loops, conditions |
| Build a CLI tool that asks for user input and logs it to a file | Functions, input(), file I/O |
| Fetch JSON from a public API and print specific fields | `requests` library, JSON, dictionaries |
| Build a simple contact book (add, search, delete) | Dictionaries, functions, file I/O |

**Recommended free API for practice:** `https://restcountries.com/v3.1/all` — returns country data as JSON, no key needed.

---

### Resources for Step 1

| Resource | Type | Cost |
|---|---|---|
| [Python.org Official Tutorial](https://docs.python.org/3/tutorial/) | Docs | Free |
| [freeCodeCamp Python Course](https://www.youtube.com/watch?v=rfscVS0vtbw) | Video | Free |
| [Automate the Boring Stuff with Python](https://automatetheboringstuff.com) | Book | Free online |
| [Exercism.io — Python track](https://exercism.org/tracks/python) | Practice | Free |

---

✅ **You are ready for Step 2 when you can:**
- Write a function that reads a CSV, filters rows based on a condition, and returns a list of dictionaries
- Handle errors with try/except
- Use list comprehensions and dictionary comprehensions confidently
- Import and use `os`, `json`, and `datetime` modules

---

---

## Step 2 — pandas + SQL
**Estimated time:** 3–4 weeks (1–2 hours/day)

This is the core of data engineering and data science work. pandas lets you manipulate data in Python. SQL lets you query databases. Together they cover 80% of what a data engineer or data scientist does daily.

---

### 2.1 What is pandas and why does it matter?

pandas gives you a **DataFrame** — think of it as an Excel spreadsheet inside Python. Every row is a record, every column is a field. You can filter, sort, group, join, and transform data with just a few lines of code.

```bash
pip install pandas openpyxl
```

```python
import pandas as pd
```

The alias `pd` is universal — every data engineer uses it.

---

### 2.2 Creating and Loading DataFrames (Days 1–2)

```python
import pandas as pd

# Create from a dictionary
df = pd.DataFrame({
    "name": ["Reza", "Anna", "Tom"],
    "city": ["Hamburg", "Berlin", "Munich"],
    "salary": [60000, 72000, 55000]
})

# Load from CSV (most common)
df = pd.read_csv("employees.csv")

# Load from Excel
df = pd.read_excel("report.xlsx", sheet_name="Sheet1")

# Load from JSON
df = pd.read_json("data.json")

# Quick inspection — always do these first
df.shape          # (rows, columns)
df.head()         # first 5 rows
df.tail()         # last 5 rows
df.info()         # column names, types, null counts
df.describe()     # statistics: mean, min, max, etc.
df.columns        # list of column names
df.dtypes         # data type of each column
```

---

### 2.3 Selecting Data (Days 3–4)

```python
# Select a single column → returns a Series
df["salary"]

# Select multiple columns → returns a DataFrame
df[["name", "salary"]]

# Select rows by index number
df.iloc[0]        # first row
df.iloc[0:5]      # rows 0 to 4
df.iloc[-1]       # last row

# Select rows by label/condition
df.loc[df["city"] == "Hamburg"]

# Select specific rows AND columns
df.loc[df["salary"] > 60000, ["name", "salary"]]
```

**Key difference:**
- `.iloc` — select by **position** (integer index)
- `.loc` — select by **label or condition**

---

### 2.4 Filtering Data (Day 5)

```python
# Single condition
high_earners = df[df["salary"] > 65000]

# Multiple conditions — use & (and) | (or)
hamburg_high = df[(df["city"] == "Hamburg") & (df["salary"] > 55000)]

# Filter with a list of values
selected_cities = df[df["city"].isin(["Hamburg", "Berlin"])]

# Filter out null values
df_clean = df[df["salary"].notna()]

# String filtering
df[df["name"].str.startswith("R")]
df[df["name"].str.contains("anna", case=False)]
```

---

### 2.5 Adding and Modifying Columns (Day 6)

```python
# Add a new column
df["salary_eur"] = df["salary"] / 1.1    # convert from gross

# Conditional column — like IF in Excel
df["level"] = df["salary"].apply(lambda x: "Senior" if x > 65000 else "Junior")

# Using np.where (faster for large datasets)
import numpy as np
df["level"] = np.where(df["salary"] > 65000, "Senior", "Junior")

# Rename columns
df = df.rename(columns={"name": "full_name", "city": "location"})

# Drop columns
df = df.drop(columns=["salary_eur"])

# Change data type
df["salary"] = df["salary"].astype(float)
```

---

### 2.6 Handling Missing Data (Day 7)

Real data always has gaps. Knowing how to handle them is essential.

```python
# Check for nulls
df.isnull().sum()          # count nulls per column
df.isnull().any()          # which columns have any null

# Drop rows with any null
df_clean = df.dropna()

# Drop rows where specific column is null
df_clean = df.dropna(subset=["salary"])

# Fill nulls with a value
df["salary"] = df["salary"].fillna(0)
df["city"] = df["city"].fillna("Unknown")

# Fill nulls with the column mean
df["salary"] = df["salary"].fillna(df["salary"].mean())

# Forward fill — use the previous row's value (common in time series)
df["salary"] = df["salary"].ffill()
```

---

### 2.7 Sorting and Ranking (Day 8)

```python
# Sort by one column
df_sorted = df.sort_values("salary", ascending=False)

# Sort by multiple columns
df_sorted = df.sort_values(["city", "salary"], ascending=[True, False])

# Reset index after sorting
df_sorted = df_sorted.reset_index(drop=True)

# Rank
df["salary_rank"] = df["salary"].rank(ascending=False)
```

---

### 2.8 GroupBy — Aggregation (Days 9–10)

This is one of the most important pandas features. It works exactly like `GROUP BY` in SQL.

```python
# Average salary per city
df.groupby("city")["salary"].mean()

# Multiple aggregations at once
df.groupby("city")["salary"].agg(["mean", "min", "max", "count"])

# GroupBy multiple columns
df.groupby(["city", "level"])["salary"].mean()

# Reset index to get a flat DataFrame back
summary = df.groupby("city")["salary"].mean().reset_index()
summary.columns = ["city", "avg_salary"]

# Apply multiple aggregations to multiple columns
df.groupby("city").agg(
    avg_salary=("salary", "mean"),
    total_employees=("name", "count")
).reset_index()
```

---

### 2.9 Merging and Joining DataFrames (Days 11–12)

This is the pandas equivalent of SQL JOINs.

```python
employees = pd.DataFrame({
    "emp_id": [1, 2, 3],
    "name": ["Reza", "Anna", "Tom"],
    "dept_id": [10, 20, 10]
})

departments = pd.DataFrame({
    "dept_id": [10, 20],
    "dept_name": ["Engineering", "Marketing"]
})

# INNER JOIN — only matching rows
merged = pd.merge(employees, departments, on="dept_id", how="inner")

# LEFT JOIN — all employees, even if no department match
merged = pd.merge(employees, departments, on="dept_id", how="left")

# Join on different column names
pd.merge(employees, departments, left_on="dept_id", right_on="id")

# Concatenate — stack DataFrames vertically (like UNION in SQL)
combined = pd.concat([df_2024, df_2025], ignore_index=True)
```

---

### 2.10 Working with Dates (Day 13)

Date handling is critical in data engineering — nearly every dataset has timestamps.

```python
# Parse dates when loading
df = pd.read_csv("sales.csv", parse_dates=["order_date"])

# Convert a column to datetime
df["order_date"] = pd.to_datetime(df["order_date"])

# Extract parts of a date
df["year"] = df["order_date"].dt.year
df["month"] = df["order_date"].dt.month
df["day"] = df["order_date"].dt.day
df["weekday"] = df["order_date"].dt.day_name()

# Date arithmetic
df["days_since_order"] = (pd.Timestamp.now() - df["order_date"]).dt.days

# Filter by date range
df_2025 = df[(df["order_date"] >= "2025-01-01") & (df["order_date"] < "2026-01-01")]

# Resample time series — sum sales per month
df.set_index("order_date").resample("ME")["sales"].sum()
```

---

### 2.11 Exporting Data (Day 14)

```python
# Save to CSV
df.to_csv("output.csv", index=False)    # index=False avoids saving row numbers

# Save to Excel
df.to_excel("report.xlsx", sheet_name="Results", index=False)

# Save to JSON
df.to_json("output.json", orient="records", indent=2)

# Save to Parquet — the standard format in data engineering and Azure
df.to_parquet("output.parquet", index=False)
```

**Parquet** is important: Azure Data Lake, Azure Databricks, and most modern data pipelines use Parquet instead of CSV because it is compressed, fast, and stores column types.

```bash
pip install pyarrow    # needed for parquet support
```

---

### 2.12 SQL Fundamentals (Days 15–20)

SQL is a separate language but you use it alongside pandas. In data engineering, SQL runs inside databases; pandas runs in Python memory. For large datasets, SQL is faster. For complex transformations in Python, pandas is more flexible.

**Install a local database for practice:**
```bash
pip install duckdb    # DuckDB runs SQL directly in Python, no server needed
```

#### Core SQL you must know

```sql
-- SELECT — choose columns
SELECT name, salary, city
FROM employees;

-- WHERE — filter rows
SELECT * FROM employees
WHERE salary > 60000 AND city = 'Hamburg';

-- ORDER BY — sort results
SELECT * FROM employees
ORDER BY salary DESC;

-- LIMIT — restrict number of rows
SELECT * FROM employees
ORDER BY salary DESC
LIMIT 10;

-- GROUP BY + aggregate functions
SELECT city, COUNT(*) AS employee_count, AVG(salary) AS avg_salary
FROM employees
GROUP BY city;

-- HAVING — filter after GROUP BY (WHERE filters before grouping)
SELECT city, AVG(salary) AS avg_salary
FROM employees
GROUP BY city
HAVING AVG(salary) > 60000;

-- INNER JOIN
SELECT e.name, d.dept_name, e.salary
FROM employees e
JOIN departments d ON e.dept_id = d.dept_id;

-- LEFT JOIN — keep all employees even without a department
SELECT e.name, d.dept_name
FROM employees e
LEFT JOIN departments d ON e.dept_id = d.dept_id;

-- Subquery
SELECT name, salary
FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);

-- CASE WHEN — like IF in Python
SELECT name, salary,
    CASE
        WHEN salary > 70000 THEN 'Senior'
        WHEN salary > 50000 THEN 'Mid'
        ELSE 'Junior'
    END AS level
FROM employees;

-- Window functions — critical for data engineering
SELECT name, salary, city,
    AVG(salary) OVER (PARTITION BY city) AS city_avg_salary,
    RANK() OVER (PARTITION BY city ORDER BY salary DESC) AS rank_in_city
FROM employees;
```

#### Running SQL inside Python with DuckDB

```python
import duckdb
import pandas as pd

df = pd.read_csv("employees.csv")

# Query a pandas DataFrame directly with SQL
result = duckdb.query("SELECT city, AVG(salary) FROM df GROUP BY city").df()

# Query a CSV file directly — no loading needed
result = duckdb.query("SELECT * FROM 'employees.csv' WHERE salary > 60000").df()

# Query a Parquet file — standard in Azure Data Lake
result = duckdb.query("SELECT * FROM 'data.parquet'").df()
```

This DuckDB pattern is used in real data engineering pipelines.

---

### 2.13 pandas + SQL Together — the Real Workflow

In practice, you combine both. Use SQL for the heavy lifting in the database, pull the result into Python, then use pandas for the final transformation.

```python
import duckdb
import pandas as pd

# Step 1 — pull aggregated data with SQL
raw = duckdb.query("""
    SELECT
        city,
        DATE_TRUNC('month', order_date) AS month,
        SUM(revenue) AS total_revenue
    FROM 'orders.parquet'
    WHERE order_date >= '2025-01-01'
    GROUP BY city, month
    ORDER BY month
""").df()

# Step 2 — further transform in pandas
raw["month"] = pd.to_datetime(raw["month"])
raw["revenue_millions"] = raw["total_revenue"] / 1_000_000

# Step 3 — save result
raw.to_parquet("monthly_revenue_by_city.parquet", index=False)
```

---

### Practice Projects for Step 2

Do at least two before moving to Step 3.

| Project | What you practice |
|---|---|
| Load a sales CSV, clean nulls, group by month and product, export to Parquet | pandas end-to-end |
| Analyze a public dataset (e.g. Berlin open data) — top 10 results, trend over time | GroupBy, sort, date handling |
| Join two datasets (e.g. orders + customers), calculate lifetime value per customer | Merge, GroupBy, aggregation |
| Rewrite a pandas transformation as a SQL query using DuckDB | SQL + pandas integration |
| Load a CSV with bad dates and mixed types, clean it fully, export to Excel | Data cleaning |

**Free public datasets for practice:**
- [Kaggle Datasets](https://www.kaggle.com/datasets) — search "sales", "employees", "ecommerce"
- [Berliner Open Data](https://daten.berlin.de) — German city data, good for context

---

### Resources for Step 2

| Resource | Type | Cost |
|---|---|---|
| [pandas official docs — 10 minutes to pandas](https://pandas.pydata.org/docs/user_guide/10min.html) | Docs | Free |
| [Kaggle pandas course](https://www.kaggle.com/learn/pandas) | Interactive | Free |
| [Mode SQL Tutorial](https://mode.com/sql-tutorial/) | Interactive | Free |
| [DuckDB docs](https://duckdb.org/docs/) | Docs | Free |
| [SQLBolt](https://sqlbolt.com) | Interactive exercises | Free |

---

✅ **You are ready for Step 3 when you can:**
- Load a CSV, clean nulls, filter, group, and export to Parquet
- Write SQL with JOIN, GROUP BY, HAVING, and a window function
- Run a SQL query on a pandas DataFrame using DuckDB
- Merge two DataFrames and calculate an aggregated metric

---

---

## Step 3 — FastAPI + APIs
**Estimated time:** 2–3 weeks (1–2 hours/day)

FastAPI is the standard Python framework for building APIs. In the context of AI and data engineering, you use it to expose your data pipelines, ML models, or RAG solutions as a web service that other systems or frontends can call. It is fast, modern, and used heavily in production AI applications.

---

### 3.1 What is an API and why does it matter?

An **API (Application Programming Interface)** is a way for two programs to talk to each other over the internet using HTTP.

- Your RAG solution is built in Python — an API lets a web app or mobile app call it
- A data pipeline result stored in Azure can be served via an API to a dashboard
- Companies expose their AI features as APIs internally

**HTTP basics you need to know:**

| Method | Purpose | Example |
|---|---|---|
| `GET` | Read data | Get a list of customers |
| `POST` | Send data / create something | Submit a question to your RAG system |
| `PUT` | Update something | Update a record |
| `DELETE` | Delete something | Remove a record |

A **response** always comes back with a **status code:**

| Code | Meaning |
|---|---|
| 200 | OK — success |
| 201 | Created — something was made |
| 400 | Bad Request — the input was wrong |
| 401 | Unauthorized — not logged in |
| 404 | Not Found |
| 500 | Internal Server Error — something crashed |

---

### 3.2 Setup (Day 1)

```bash
pip install fastapi uvicorn
```

- **FastAPI** — the framework
- **uvicorn** — the server that runs your FastAPI app

Create a file called `main.py`:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}
```

Run it:
```bash
uvicorn main:app --reload
```

Open your browser at `http://127.0.0.1:8000` — you will see your response.

FastAPI also auto-generates interactive documentation:
- `http://127.0.0.1:8000/docs` — Swagger UI, you can test endpoints here
- `http://127.0.0.1:8000/redoc` — alternative docs view

The `--reload` flag restarts the server automatically when you save a file.

---

### 3.3 Path Parameters and Query Parameters (Days 2–3)

```python
from fastapi import FastAPI

app = FastAPI()

# Path parameter — part of the URL
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    return {"employee_id": employee_id, "name": "Reza"}

# Query parameter — after the ? in the URL
# URL: /employees?city=Hamburg&min_salary=60000
@app.get("/employees")
def list_employees(city: str = None, min_salary: int = 0):
    return {
        "city": city,
        "min_salary": min_salary,
        "results": []   # would come from a database in real use
    }
```

**Path vs Query:**
- Path → `/employees/42` — identifies a specific resource
- Query → `/employees?city=Hamburg` — filters or options

---

### 3.4 Request Body with Pydantic (Days 4–5)

When a client sends data to your API (POST, PUT), it comes as JSON in the **request body**. FastAPI uses **Pydantic** to validate that data automatically.

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the shape of incoming data
class Employee(BaseModel):
    name: str
    city: str
    salary: float
    is_active: bool = True    # default value

@app.post("/employees")
def create_employee(employee: Employee):
    # FastAPI validates the incoming JSON automatically
    # If a required field is missing, it returns a 422 error automatically
    return {
        "message": "Employee created",
        "data": employee.model_dump()
    }
```

**Pydantic is powerful** — it also handles type coercion, optional fields, and validation:

```python
from pydantic import BaseModel, EmailStr, validator
from typing import Optional, List

class JobApplication(BaseModel):
    name: str
    email: str
    skills: List[str]
    years_experience: int
    linkedin_url: Optional[str] = None   # optional field

    @validator("years_experience")
    def experience_must_be_positive(cls, v):
        if v < 0:
            raise ValueError("Years of experience cannot be negative")
        return v
```

---

### 3.5 Calling External APIs with requests (Days 6–7)

In data engineering and AI work you often call external APIs to fetch data. The `requests` library is the standard tool.

```bash
pip install requests
```

```python
import requests

# GET request — fetch data
response = requests.get("https://restcountries.com/v3.1/name/germany")

# Always check the status code
if response.status_code == 200:
    data = response.json()          # parse JSON response
    country = data[0]
    print(country["name"]["common"])   # Germany
else:
    print(f"Error: {response.status_code}")

# POST request — send data
payload = {"question": "What is a data pipeline?"}
headers = {"Content-Type": "application/json", "Authorization": "Bearer YOUR_TOKEN"}

response = requests.post(
    "https://some-api.com/ask",
    json=payload,
    headers=headers
)

result = response.json()
```

**With error handling (always do this in pipelines):**

```python
import requests
from requests.exceptions import RequestException

def fetch_data(url: str) -> dict:
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()   # raises exception for 4xx/5xx
        return response.json()
    except RequestException as e:
        print(f"Request failed: {e}")
        return {}
```

---

### 3.6 Environment Variables — keeping secrets safe (Day 8)

Never put API keys, passwords, or connection strings directly in your code. Use environment variables.

```bash
pip install python-dotenv
```

Create a `.env` file (never commit this to git):
```
OPENAI_API_KEY=sk-abc123
DATABASE_URL=postgresql://user:pass@localhost/mydb
AZURE_STORAGE_KEY=abc456
```

Load it in Python:

```python
from dotenv import load_dotenv
import os

load_dotenv()   # reads .env file into environment

api_key = os.getenv("OPENAI_API_KEY")
db_url = os.getenv("DATABASE_URL")
```

In FastAPI, use this with Pydantic Settings:

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    azure_storage_key: str
    database_url: str
    debug: bool = False

    class Config:
        env_file = ".env"

settings = Settings()
```

```bash
pip install pydantic-settings
```

---

### 3.7 Structuring a Real FastAPI Project (Days 9–10)

A real project is not one big `main.py`. This is the standard structure:

```
my_api/
├── main.py            # entry point
├── routers/
│   ├── employees.py   # routes for /employees
│   └── analytics.py   # routes for /analytics
├── models/
│   └── schemas.py     # Pydantic models
├── services/
│   └── data_service.py   # business logic
├── .env               # secrets (never commit)
└── requirements.txt
```

**main.py:**
```python
from fastapi import FastAPI
from routers import employees, analytics

app = FastAPI(title="Data API", version="1.0")

app.include_router(employees.router, prefix="/employees", tags=["Employees"])
app.include_router(analytics.router, prefix="/analytics", tags=["Analytics"])
```

**routers/employees.py:**
```python
from fastapi import APIRouter
from models.schemas import Employee

router = APIRouter()

@router.get("/")
def list_employees():
    return []

@router.post("/")
def create_employee(employee: Employee):
    return employee
```

---

### 3.8 A Complete Mini Project — Data API (Days 11–14)

Build this: an API that reads a CSV of employees and exposes endpoints to query it.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import os

app = FastAPI(title="Employee Data API")

# Load data once at startup
DATA_PATH = "employees.csv"
df = pd.read_csv(DATA_PATH) if os.path.exists(DATA_PATH) else pd.DataFrame()

class Employee(BaseModel):
    name: str
    city: str
    salary: float

@app.get("/employees")
def get_employees(city: str = None, min_salary: float = 0):
    filtered = df.copy()
    if city:
        filtered = filtered[filtered["city"].str.lower() == city.lower()]
    filtered = filtered[filtered["salary"] >= min_salary]
    return filtered.to_dict(orient="records")

@app.get("/employees/{name}")
def get_employee_by_name(name: str):
    result = df[df["name"].str.lower() == name.lower()]
    if result.empty:
        raise HTTPException(status_code=404, detail=f"Employee '{name}' not found")
    return result.to_dict(orient="records")[0]

@app.get("/analytics/salary-by-city")
def salary_by_city():
    summary = df.groupby("city")["salary"].agg(["mean", "min", "max", "count"])
    summary.columns = ["avg_salary", "min_salary", "max_salary", "count"]
    return summary.reset_index().to_dict(orient="records")

@app.post("/employees")
def add_employee(employee: Employee):
    global df
    new_row = pd.DataFrame([employee.model_dump()])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(DATA_PATH, index=False)
    return {"message": "Employee added", "data": employee.model_dump()}
```

This project combines **pandas** (Step 2) with **FastAPI** (Step 3) — exactly the pattern used in real data engineering APIs.

---

### 3.9 Async FastAPI — brief introduction (Day 15)

FastAPI supports `async` functions, which allow the API to handle many requests at once without waiting.

```python
import httpx   # async version of requests

@app.get("/external-data")
async def get_external_data():
    async with httpx.AsyncClient() as client:
        response = await client.get("https://restcountries.com/v3.1/name/germany")
        return response.json()
```

```bash
pip install httpx
```

**When to use async:**
- Calling external APIs inside your endpoint
- Querying a database inside your endpoint
- Any I/O-heavy operation

For CPU-heavy work (data transformation, ML inference), regular functions are fine.

---

### Practice Projects for Step 3

| Project | What you practice |
|---|---|
| Build an API on top of your pandas dataset from Step 2 | FastAPI + pandas integration |
| Build a "question logger" API — POST a question, store it in a JSON file, GET all questions | POST, GET, file I/O |
| Call a public API, transform the data with pandas, return a summary | requests + pandas + FastAPI |
| Add Pydantic validation to an endpoint and test that bad inputs return 422 | Pydantic, validation |

---

### Resources for Step 3

| Resource | Type | Cost |
|---|---|---|
| [FastAPI Official Docs](https://fastapi.tiangolo.com) | Docs | Free |
| [FastAPI full course — freeCodeCamp](https://www.youtube.com/watch?v=0sOvCWFmrtA) | Video | Free |
| [Pydantic docs](https://docs.pydantic.dev) | Docs | Free |
| [Real Python — FastAPI guide](https://realpython.com/fastapi-python-web-apis/) | Article | Free |

---

✅ **You are ready for Step 4 when you can:**
- Build a FastAPI app with GET and POST endpoints
- Validate incoming data with Pydantic models
- Use environment variables to store secrets
- Call an external API using `requests` and return the result from your own endpoint
- Structure a project across multiple files using routers

---

---

## Step 4 — RAG & AI Solutions with Azure OpenAI

> Full content is in the separate file: [Step4_RAG_AzureOpenAI.md](Step4_RAG_AzureOpenAI.md)

**Estimated time:** 3–4 weeks (1–2 hours/day)

This step is where everything comes together. You will learn to build **RAG (Retrieval-Augmented Generation)** systems — the most in-demand AI skill for companies right now. A RAG system lets an LLM answer questions based on your company's own documents, not just its training data. All examples here use **Azure OpenAI**, which is the enterprise-standard way to deploy OpenAI models inside the Azure ecosystem.

---

### 4.1 How a RAG System Works — the concept first

Before writing any code, understand the architecture:

```
User asks a question
        ↓
Your system searches your document collection
for the most relevant chunks of text
        ↓
Those chunks are injected into the prompt
sent to the LLM
        ↓
The LLM answers using both its training
AND the retrieved context
        ↓
Answer is returned to the user
```

**Why RAG and not just "ask ChatGPT"?**
- LLMs have a knowledge cutoff — they don't know your company's internal docs
- You control the data — nothing leaves your Azure environment
- Answers are grounded in real sources — reduces hallucination
- You can cite which document the answer came from

**The four components of every RAG system:**

| Component | What it does |
|---|---|
| **Document store** | Where your raw documents live (PDFs, Word, text files) |
| **Embedding model** | Converts text into vectors (numbers that capture meaning) |
| **Vector database** | Stores and searches those vectors by similarity |
| **LLM** | Generates the final answer from the retrieved context |

---

### 4.2 Setup — Azure OpenAI (Day 1)

You need an Azure account with Azure OpenAI access. Once you have it, note these values from the Azure portal:

- `AZURE_OPENAI_ENDPOINT` — e.g. `https://your-resource.openai.azure.com/`
- `AZURE_OPENAI_KEY` — your API key
- `AZURE_OPENAI_DEPLOYMENT` — the name you gave to your deployed model (e.g. `gpt-4o`)
- `AZURE_OPENAI_EMBEDDING_DEPLOYMENT` — your embedding model deployment (e.g. `text-embedding-3-small`)

```bash
pip install openai python-dotenv
```

`.env` file:
```
AZURE_OPENAI_ENDPOINT=https://your-resource.openai.azure.com/
AZURE_OPENAI_KEY=your-key-here
AZURE_OPENAI_DEPLOYMENT=gpt-4o
AZURE_OPENAI_EMBEDDING_DEPLOYMENT=text-embedding-3-small
```

**First call to Azure OpenAI:**

```python
from openai import AzureOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-01"
)

response = client.chat.completions.create(
    model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
    messages=[
        {"role": "system", "content": "You are a helpful data engineering assistant."},
        {"role": "user", "content": "What is a data pipeline?"}
    ]
)

print(response.choices[0].message.content)
```

---

### 4.3 Embeddings — turning text into vectors (Days 2–3)

An **embedding** is a list of numbers (a vector) that represents the meaning of a piece of text. Two sentences with similar meaning will have vectors that are close to each other in space. This is how the search in RAG works.

```python
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-01"
)

def get_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        input=text,
        model=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    )
    return response.data[0].embedding

# Example
vector = get_embedding("What is Azure Data Factory?")
print(f"Vector length: {len(vector)}")   # e.g. 1536 dimensions
```

**Similarity between two vectors:**

```python
import numpy as np

def cosine_similarity(vec1: list, vec2: list) -> float:
    a = np.array(vec1)
    b = np.array(vec2)
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))

# Closer to 1.0 = more similar meaning
sim = cosine_similarity(
    get_embedding("data pipeline"),
    get_embedding("ETL process")
)
print(sim)   # e.g. 0.91 — very similar
```

---

### 4.4 Chunking Documents (Day 4)

LLMs have a context limit — you cannot send an entire 100-page PDF. You split documents into smaller **chunks**, embed each chunk, and store them. At query time you retrieve only the most relevant chunks.

```python
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    words = text.split()
    chunks = []
    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk = " ".join(words[start:end])
        chunks.append(chunk)
        start += chunk_size - overlap   # overlap keeps context at boundaries
    return chunks

# Example
with open("company_handbook.txt", "r") as f:
    text = f.read()

chunks = chunk_text(text, chunk_size=300, overlap=50)
print(f"Created {len(chunks)} chunks")
```

**Rule of thumb for chunk size:**
- Too small → chunks lose context
- Too large → you include irrelevant content in the prompt
- 300–500 words is a good starting point

---

### 4.5 Vector Database with ChromaDB (Days 5–7)

A **vector database** stores your embedded chunks and lets you search them by semantic similarity. ChromaDB runs locally — no server needed, perfect for learning and prototyping.

```bash
pip install chromadb
```

```python
import chromadb
from openai import AzureOpenAI
import os

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-01"
)

# Create a local ChromaDB instance
chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("company_docs")

def get_embedding(text: str) -> list[float]:
    response = client.embeddings.create(
        input=text,
        model=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    )
    return response.data[0].embedding

# Index documents — embed and store chunks
def index_documents(chunks: list[str], source: str):
    embeddings = [get_embedding(chunk) for chunk in chunks]
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=[f"{source}_chunk_{i}" for i in range(len(chunks))],
        metadatas=[{"source": source, "chunk": i} for i in range(len(chunks))]
    )
    print(f"Indexed {len(chunks)} chunks from {source}")

# Search — find the most relevant chunks for a question
def search(question: str, n_results: int = 3) -> list[dict]:
    query_embedding = get_embedding(question)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    return [
        {"text": doc, "source": meta["source"]}
        for doc, meta in zip(results["documents"][0], results["metadatas"][0])
    ]
```

---

### 4.6 Building a Complete RAG Pipeline (Days 8–10)

This is the full RAG system — combining everything above.

```python
from openai import AzureOpenAI
import chromadb
import os
from dotenv import load_dotenv

load_dotenv()

openai_client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-01"
)

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("company_docs")

def get_embedding(text: str) -> list[float]:
    response = openai_client.embeddings.create(
        input=text,
        model=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    )
    return response.data[0].embedding

def retrieve_context(question: str, n_results: int = 3) -> str:
    query_embedding = get_embedding(question)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )
    chunks = results["documents"][0]
    sources = [m["source"] for m in results["metadatas"][0]]
    context = "\n\n".join([f"[Source: {s}]\n{c}" for c, s in zip(chunks, sources)])
    return context

def ask(question: str) -> dict:
    # Step 1 — retrieve relevant context
    context = retrieve_context(question)

    # Step 2 — build the prompt
    system_prompt = """You are a helpful assistant. Answer the user's question
using ONLY the context provided below. If the answer is not in the context,
say 'I don't have information about that in the available documents.'

Context:
{context}""".format(context=context)

    # Step 3 — call the LLM
    response = openai_client.chat.completions.create(
        model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ],
        temperature=0.2   # lower = more factual, less creative
    )

    return {
        "question": question,
        "answer": response.choices[0].message.content,
        "context_used": context
    }

# Use it
result = ask("What is our company's vacation policy?")
print(result["answer"])
```

---

### 4.7 Expose the RAG System as a FastAPI API (Days 11–12)

This combines Step 3 and Step 4 — the real production pattern.

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import AzureOpenAI
import chromadb
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="RAG API")

openai_client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_KEY"),
    api_version="2024-02-01"
)

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_or_create_collection("company_docs")

class Question(BaseModel):
    text: str
    n_results: int = 3

class Answer(BaseModel):
    question: str
    answer: str
    sources: list[str]

def get_embedding(text: str) -> list[float]:
    response = openai_client.embeddings.create(
        input=text,
        model=os.getenv("AZURE_OPENAI_EMBEDDING_DEPLOYMENT")
    )
    return response.data[0].embedding

@app.post("/ask", response_model=Answer)
def ask_question(question: Question):
    try:
        # Retrieve
        query_embedding = get_embedding(question.text)
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=question.n_results
        )
        chunks = results["documents"][0]
        sources = list(set(m["source"] for m in results["metadatas"][0]))
        context = "\n\n".join(chunks)

        # Generate
        response = openai_client.chat.completions.create(
            model=os.getenv("AZURE_OPENAI_DEPLOYMENT"),
            messages=[
                {"role": "system", "content": f"Answer using only this context:\n{context}"},
                {"role": "user", "content": question.text}
            ],
            temperature=0.2
        )

        return Answer(
            question=question.text,
            answer=response.choices[0].message.content,
            sources=sources
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
def health():
    return {"status": "ok", "documents_indexed": collection.count()}
```

---

### 4.8 Loading Different Document Types (Day 13)

Real RAG systems need to handle PDFs, Word docs, and web pages — not just plain text.

```bash
pip install pypdf python-docx beautifulsoup4 requests
```

```python
from pypdf import PdfReader
from docx import Document
import requests
from bs4 import BeautifulSoup

def load_pdf(path: str) -> str:
    reader = PdfReader(path)
    return "\n".join(page.extract_text() for page in reader.pages)

def load_word(path: str) -> str:
    doc = Document(path)
    return "\n".join(para.text for para in doc.paragraphs)

def load_webpage(url: str) -> str:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    # Remove scripts and styles
    for tag in soup(["script", "style"]):
        tag.decompose()
    return soup.get_text(separator="\n", strip=True)

# Use any loader, then chunk and index
text = load_pdf("annual_report.pdf")
chunks = chunk_text(text)
index_documents(chunks, source="annual_report.pdf")
```

---

### 4.9 Azure AI Search — the production vector database (Days 14–16)

ChromaDB is for local development. In production on Azure, you use **Azure AI Search** (formerly Cognitive Search) as your vector database — it integrates natively with Azure OpenAI and Azure Blob Storage.

```bash
pip install azure-search-documents azure-identity
```

```python
from azure.search.documents import SearchClient
from azure.search.documents.indexes import SearchIndexClient
from azure.search.documents.indexes.models import (
    SearchIndex, SimpleField, SearchFieldDataType,
    SearchableField, VectorSearch, HnswAlgorithmConfiguration,
    VectorSearchProfile, SearchField
)
from azure.core.credentials import AzureKeyCredential
import os

endpoint = os.getenv("AZURE_SEARCH_ENDPOINT")
key = os.getenv("AZURE_SEARCH_KEY")
index_name = "company-docs"

# Create index with vector field
index_client = SearchIndexClient(endpoint, AzureKeyCredential(key))

fields = [
    SimpleField(name="id", type=SearchFieldDataType.String, key=True),
    SearchableField(name="content", type=SearchFieldDataType.String),
    SimpleField(name="source", type=SearchFieldDataType.String, filterable=True),
    SearchField(
        name="embedding",
        type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
        searchable=True,
        vector_search_dimensions=1536,
        vector_search_profile_name="my-profile"
    )
]

vector_search = VectorSearch(
    algorithms=[HnswAlgorithmConfiguration(name="my-hnsw")],
    profiles=[VectorSearchProfile(name="my-profile", algorithm_configuration_name="my-hnsw")]
)

index = SearchIndex(name=index_name, fields=fields, vector_search=vector_search)
index_client.create_or_update_index(index)

# Upload documents
search_client = SearchClient(endpoint, index_name, AzureKeyCredential(key))

def index_to_azure_search(chunks: list[str], source: str):
    documents = []
    for i, chunk in enumerate(chunks):
        embedding = get_embedding(chunk)
        documents.append({
            "id": f"{source}_{i}",
            "content": chunk,
            "source": source,
            "embedding": embedding
        })
    search_client.upload_documents(documents)
    print(f"Uploaded {len(documents)} chunks to Azure AI Search")

# Vector search
from azure.search.documents.models import VectorizedQuery

def search_azure(question: str, n_results: int = 3):
    query_embedding = get_embedding(question)
    vector_query = VectorizedQuery(
        vector=query_embedding,
        k_nearest_neighbors=n_results,
        fields="embedding"
    )
    results = search_client.search(
        search_text=None,
        vector_queries=[vector_query],
        select=["content", "source"]
    )
    return [{"text": r["content"], "source": r["source"]} for r in results]
```

---

### 4.10 Prompt Engineering — getting better answers (Day 17)

The quality of your RAG output depends heavily on how you write your prompts.

```python
# Basic prompt — works but generic
system = f"Answer using this context:\n{context}"

# Better — gives the model a clear role and rules
system = """You are a data engineering expert assistant for Reza's company.

Your rules:
- Answer ONLY from the provided context
- If the answer is not in the context, say exactly: "This information is not available in the documents."
- Be concise — 2-3 sentences max unless detail is specifically requested
- Always cite the source document at the end of your answer

Context:
{context}""".format(context=context)

# Add conversation history for multi-turn chat
messages = [
    {"role": "system", "content": system},
    {"role": "user", "content": "What is our data retention policy?"},
    {"role": "assistant", "content": "According to the IT policy document, data is retained for 7 years..."},
    {"role": "user", "content": "What about customer data specifically?"}   # follow-up
]
```

**Key parameters to understand:**

| Parameter | Effect | When to adjust |
|---|---|---|
| `temperature` | 0 = deterministic, 1 = creative | Use 0–0.3 for factual RAG |
| `max_tokens` | Max length of response | Set to avoid very long answers |
| `top_p` | Controls diversity of word choice | Usually leave at default |

---

### Practice Projects for Step 4

| Project | What you practice |
|---|---|
| Build a RAG system over your own CV/resume | Full pipeline: load, chunk, embed, retrieve, generate |
| Build a Q&A bot over a company handbook PDF | PDF loading + ChromaDB + Azure OpenAI |
| Expose a RAG system via FastAPI with `/ask` and `/upload` endpoints | Steps 3 + 4 combined |
| Build a multi-document RAG that cites which document answered | Metadata, source tracking |
| Compare answers with and without RAG — document the difference | Understand hallucination vs grounding |

---

### Resources for Step 4

| Resource | Type | Cost |
|---|---|---|
| [Azure OpenAI docs](https://learn.microsoft.com/en-us/azure/ai-services/openai/) | Docs | Free |
| [Azure AI Search vector search docs](https://learn.microsoft.com/en-us/azure/search/vector-search-overview) | Docs | Free |
| [ChromaDB docs](https://docs.trychroma.com) | Docs | Free |
| [Microsoft RAG tutorial](https://learn.microsoft.com/en-us/azure/search/retrieval-augmented-generation-overview) | Tutorial | Free |
| [LlamaIndex docs](https://docs.llamaindex.ai) | Docs | Free — alternative to building manually |

---

✅ **You are ready for Step 5 when you can:**
- Call Azure OpenAI to get a chat completion and an embedding
- Chunk a document, embed the chunks, and store them in ChromaDB
- Search ChromaDB by semantic similarity and inject the results into a prompt
- Build a FastAPI `/ask` endpoint that runs the full RAG pipeline
- Understand what Azure AI Search is and how it replaces ChromaDB in production

---

---

## Step 5 — Azure Cloud for Data & AI

> Full content is in the separate file: [Step5_Azure_Cloud.md](Step5_Azure_Cloud.md)

**Estimated time:** 4–6 weeks (1–2 hours/day)

Covers the core Azure services for data engineering and AI: Azure Data Lake Storage (ADLS), Azure Data Factory (ADF), Azure Databricks + PySpark, Azure SQL Database, Azure Functions, Azure Key Vault, and the full end-to-end pipeline architecture. Also includes the Azure certifications to target: AZ-900, DP-900, DP-203, and AI-102.
