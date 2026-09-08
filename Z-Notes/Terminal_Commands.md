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

## Git

### Setup (do once ever)

| Command | What it does |
|---|---|
| `git config --global user.name "Name"` | Set your name on all commits |
| `git config --global user.email "you@email.com"` | Set your email on all commits |

---

### Starting a project

| Command | What it does |
|---|---|
| `git init` | Turn current folder into a Git project |
| `git branch -M main` | Rename default branch to `main` |
| `git remote add origin URL` | Link your local folder to a GitHub repo |
| `git clone URL` | Download a full repo from GitHub to your Mac |

---

### Daily workflow

```bash
git pull                          # 1. get latest from GitHub
# ... do your work ...
git status                        # 2. see what changed
git add .                         # 3. stage everything
git commit -m "what you did"      # 4. save a snapshot
git push                          # 5. upload to GitHub
```

---

### Checking what's going on

| Command | What it does |
|---|---|
| `git status` | Shows changed files — red = not staged, green = staged |
| `git log` | Full history of all past commits (press `q` to exit) |
| `git log --oneline` | Same history but compact, one line per commit |
| `git diff` | Shows exactly what lines changed (before staging) |
| `git branch` | Lists all branches — `*` marks the one you're on |
| `git branch -a` | Lists local AND remote branches |

---

### Staging and committing

| Command | What it does |
|---|---|
| `git add .` | Stage all changed files |
| `git add filename` | Stage one specific file |
| `git commit -m "message"` | Save a snapshot of staged files |

---

### Pushing and pulling

| Command | What it does |
|---|---|
| `git push -u origin main` | Push to GitHub for the first time (saves the destination) |
| `git push` | Push after the first time |
| `git pull` | Download latest commits from GitHub to your Mac |

---

### Branches

| Command | What it does |
|---|---|
| `git checkout -b branch-name` | Create a new branch and switch to it |
| `git checkout branch-name` | Switch to an existing branch |
| `git merge branch-name` | Merge a branch into the current branch |
| `git branch -d branch-name` | Delete a branch locally (safe — only if already merged) |
| `git push -u origin branch-name` | Push a new branch to GitHub for the first time |
| `git push origin --delete branch-name` | Delete a branch on GitHub |

**Branch workflow at a glance:**
```bash
git checkout main                        # start from main
git pull                                 # get latest
git checkout -b my-feature               # create + switch to new branch
# ... do your work ...
git add .
git commit -m "what you did"
git push -u origin my-feature            # push branch to GitHub
git checkout main                        # switch back to main
git merge my-feature                     # merge work into main
git push                                 # push updated main to GitHub
git branch -d my-feature                 # clean up (optional)
```

---

### Key Git terms

| Term | Meaning |
|---|---|
| **Repository (repo)** | A project folder tracked by Git |
| **Commit** | A saved snapshot of your files at a point in time |
| **Branch** | An isolated copy of the project to work on safely |
| **main** | The default, stable branch |
| **origin** | Nickname for your GitHub repo URL |
| **Push** | Send commits from your Mac → GitHub |
| **Pull** | Bring commits from GitHub → your Mac |
| **Clone** | Download a full repo from GitHub to your Mac |
| **Merge** | Combine the changes from one branch into another |
| **Staging area** | A holding zone — files you've selected for the next commit |

---

### Common errors and fixes

| Error | What it means | Fix |
|---|---|---|
| `remote origin already exists` | Already linked to GitHub | Safe to ignore, keep going |
| `src refspec main does not match any` | No commits yet | Run `git add .` then `git commit -m "..."` first |
| Asked for password | GitHub no longer uses account passwords | Use a Personal Access Token instead |

---

## Tips

- Press **Up arrow** to repeat the last command
- Press **Tab** to auto-complete folder/file names
- Commands are case-sensitive (`ls` works, `LS` does not)
- If a path has spaces, wrap it in quotes: `cd "my folder"`
