# Git Commands Reference

## Setup (do once ever)

| Command | What it does |
|---|---|
| `git config --global user.name "Name"` | Set your name on all commits |
| `git config --global user.email "you@email.com"` | Set your email on all commits |

---

## Starting a project

| Command | What it does |
|---|---|
| `git init` | Turn current folder into a Git project |
| `git branch -M main` | Rename default branch to `main` |
| `git remote add origin URL` | Link your local folder to a GitHub repo |
| `git clone URL` | Download a full repo from GitHub to your Mac |

---

## Daily workflow

```bash
git pull                          # 1. get latest from GitHub
# ... do your work ...
git status                        # 2. see what changed
git add .                         # 3. stage everything
git commit -m "what you did"      # 4. save a snapshot
git push                          # 5. upload to GitHub
```

---

## Checking what's going on

| Command | What it does |
|---|---|
| `git status` | Shows changed files — red = not staged, green = staged |
| `git log` | Full history of all past commits (press `q` to exit) |
| `git log --oneline` | Same history but compact, one line per commit |
| `git diff` | Shows exactly what lines changed (before staging) |
| `git branch` | Lists all branches — `*` marks the one you're on |
| `git branch -a` | Lists local AND remote branches |

---

## Staging and committing

| Command | What it does |
|---|---|
| `git add .` | Stage all changed files |
| `git add filename` | Stage one specific file |
| `git commit -m "message"` | Save a snapshot of staged files |

---

## Pushing and pulling

| Command | What it does |
|---|---|
| `git push -u origin main` | Push to GitHub for the first time (saves the destination) |
| `git push` | Push after the first time |
| `git pull` | Pull from wherever current branch is tracking |
| `git pull origin main` | Pull main from GitHub — use on feature branch for morning sync |

---

## Branches

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

## Team workflow (5-person project)

**Step 1 — First day (once only)**
```bash
git clone https://github.com/your-org/your-repo.git
cd your-repo
git checkout -b feature/reza-azure-pipeline   # your own branch, never work on main
```

**Step 2 — Every morning**
```bash
git checkout main
git pull origin main                           # get teammates' latest changes
git checkout feature/reza-azure-pipeline
git merge main                                 # bring those changes into your branch
```

**Step 3 — While working**
```bash
git status
git add .
git commit -m "add: azure storage pipeline configuration"
git push origin feature/reza-azure-pipeline
```

**Step 4 — When your feature is done**
```
Push your branch → GitHub → "Compare & Pull Request"
→ describe what you did → assign a teammate to review → wait for approval → merge
```

**Step 5 — After PR is merged**
```bash
git checkout main
git pull origin main
git branch -d feature/reza-azure-pipeline     # delete old branch
git checkout -b feature/reza-next-task        # start fresh for next task
```

**Step 6 — End of project**
```bash
git checkout main
git pull origin main
git log --oneline --graph --all               # see full history
git tag -a v1.0.0 -m "Project final release"
git push origin v1.0.0
```

**Golden rules**
- Never push directly to `main`
- Never start working without pulling first in the morning
- Always work on your own branch
- Always write clear commit messages
- Always open a Pull Request — let a teammate review before merging

---

## Key Git terms

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

## Common errors and fixes

| Error | What it means | Fix |
|---|---|---|
| `remote origin already exists` | Already linked to GitHub | Safe to ignore, keep going |
| `src refspec main does not match any` | No commits yet | Run `git add .` then `git commit -m "..."` first |
| Asked for password | GitHub no longer uses account passwords | Use a Personal Access Token instead |
