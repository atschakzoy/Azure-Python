# Terminal Commands Reference

## Navigation

| Command | What it does |
|---|---|
| `cd path` | Move into a folder |
| `cd ..` | Go up one folder level |
| `ls` | List files in current folder |
| `pwd` | Show your current location |
| `cat filename` | Print file contents in the terminal |

**Example:**
```bash
cd "/Users/rezanazari/Desktop/Learning Materials/Python exercise"
ls
```

---

## Python

| Command | What it does |
|---|---|
| `python3 --version` | Check Python version |
| `python3 exercise.py` | Run your Python file |

---

## Virtual Environment

| Command | What it does |
|---|---|
| `python3 -m venv venv` | Create a virtual environment |
| `source venv/bin/activate` | Activate it (Mac/Linux) |
| `deactivate` | Turn it off |

**When active:** your prompt starts with `(venv)`  
**Rule:** Always activate before running your Python files.

**Every session:**
```bash
cd "/Users/rezanazari/Desktop/Learning Materials/Python exercise"
source venv/bin/activate
# ... do your work ...
deactivate
```

---

## Tips

- Press **Up arrow** to repeat the last command
- Press **Tab** to auto-complete folder/file names
- Commands are case-sensitive (`ls` works, `LS` does not)
- If a path has spaces, wrap it in quotes: `cd "my folder"`
