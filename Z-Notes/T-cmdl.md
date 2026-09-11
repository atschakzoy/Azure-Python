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

## Files & Folders

### Create

| Command | What it does |
|---|---|
| `mkdir folder-name` | Create a new folder |
| `mkdir -p parent/child` | Create nested folders in one go |
| `touch filename.py` | Create a new empty file |

### Delete

| Command | What it does |
|---|---|
| `rm filename.py` | Delete a file |
| `rm -r folder-name` | Delete a folder and everything inside it |

> `rm` is permanent — no trash bin, no undo. Double-check before running.

### Copy & Move / Rename

| Command | What it does |
|---|---|
| `cp file.py copy.py` | Copy a file |
| `cp -r folder new-folder` | Copy a folder |
| `mv file.py new-name.py` | Rename a file |
| `mv file.py folder/` | Move a file into a folder |
| `mv folder/ new-location/` | Move a folder |

> `mv` is also how you rename — just give it a new name instead of a new path.

### Common workflow
```bash
mkdir my-project          # create project folder
cd my-project             # move into it
touch main.py             # create a file
mv main.py app.py         # rename it
cp app.py backup.py       # make a copy
rm backup.py              # delete the copy
```

---

## Tips

- Press **Up arrow** to repeat the last command
- Press **Tab** to auto-complete folder/file names
- Commands are case-sensitive (`ls` works, `LS` does not)
- If a path has spaces, wrap it in quotes: `cd "my folder"`
