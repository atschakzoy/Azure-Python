# Git & GitHub Complete Reference

---

## What are they?

| Tool | What it is |
|---|---|
| **Git** | A program on your computer that tracks changes to your files (like a time machine for code) |
| **GitHub** | A website where you store and share your Git projects online |

**Analogy:** Git = Track Changes in Word (lives on your Mac). GitHub = Google Drive (stores it online).

---

## First-time setup (do once ever)

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

---

## How to start a project — 3 scenarios

### Scenario A — You start on your computer, then push to GitHub
**When to use:** You already have a folder on your Mac and want to upload it to GitHub.

```bash
# 1. Go into your project folder
cd "/Users/rezanazari/Desktop/Learning Materials/Python exercise"

# 2. Start Git
git init

# 3. Rename branch to main
git branch -M main

# 4. Create a repo on github.com first, then paste your URL here
git remote add origin https://github.com/YOUR-USERNAME/your-repo-name.git

# 5. Ignore the venv folder
echo "venv/" > .gitignore

# 6. Stage all files
git add .

# 7. Check what's staged (venv should NOT appear)
git status

# 8. Save a snapshot
git commit -m "first commit"

# 9. Upload to GitHub
git push -u origin main
```

---

### Scenario B — Repo already exists on GitHub, you download it
**When to use:** A repo already exists on GitHub (yours or someone else's) and you want to download it to your Mac.

```bash
# 1. Go where you want the folder saved
cd "/Users/rezanazari/Desktop"

# 2. Clone (download) the repo — paste the URL from the GitHub page
git clone https://github.com/USERNAME/repo-name.git

# 3. Move into the newly created folder
cd repo-name

# Git is already set up — you're ready to work
```

---

### Scenario C — Create the repo from Terminal (no website needed)
**When to use:** You want to skip the GitHub website entirely and do everything in Terminal.

> **Note:** Requires the GitHub CLI tool (`gh`). Not set up yet — come back to this when ready.

```bash
# 1. Check if you have GitHub CLI installed
gh --version

# 2. If not installed, install it
brew install gh

# 3. Login to GitHub from Terminal (do once)
gh auth login

# 4. Then set up and push your project
cd "/Users/rezanazari/Desktop/Learning Materials/Python exercise"
git init
git branch -M main
echo "venv/" > .gitignore
git add .
git commit -m "first commit"
gh repo create python-exercise --public --source=. --push
# This last line creates the repo on GitHub AND pushes in one shot
```

---

## Scenario comparison

| | Scenario A | Scenario B | Scenario C |
|---|---|---|---|
| Where you start | Your Mac | GitHub website | Your Mac |
| First command | `git init` | `git clone URL` | `git init` |
| Create repo | On github.com manually | Already exists | `gh repo create` in Terminal |
| Remote linked automatically? | No — you add it manually | Yes | Yes |

---

## What each command does — explained

---

### `git config --global user.name` and `user.email`
```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```
Tells Git who you are. Every commit you make gets stamped with this name and email — like signing your work. `--global` means it applies to every Git project on your Mac, not just one.

---

### `git init`
```bash
git init
```
Turns your current folder into a Git project. It creates a hidden folder called `.git` inside — that's where Git stores all the history and tracking information. You only run this once per project.

> Think of it as: "Start tracking this folder."

---

### `git branch -M main`
```bash
git branch -M main
```
Renames your current branch to `main`. When Git starts, it may name the branch `master` (older default). GitHub expects `main`, so this makes sure they match. `-M` means force rename — it works even if `main` already exists.

> Think of it as: "Name this timeline 'main'."

---

### `git remote add origin URL`
```bash
git remote add origin https://github.com/YOUR-USERNAME/your-repo-name.git
```
Links your local folder on your Mac to your repo on GitHub. Without this, Git doesn't know where to send your files when you push.
- `origin` is just a nickname — you could call it anything, but `origin` is the standard
- The URL is the address of your GitHub repo

> Think of it as: "Here's the address to ship my work to."

---

### `git clone URL`
```bash
git clone https://github.com/USERNAME/repo-name.git
```
Downloads a full copy of a GitHub repo to your Mac — including all files and the entire history of commits. It also automatically sets up the remote link, so you don't need to run `git remote add` separately.

> Think of it as: "Download this project and set everything up for me."

---

### `.gitignore` and `echo "venv/" > .gitignore`
```bash
echo "venv/" > .gitignore
```
Creates a file called `.gitignore` with the text `venv/` inside it. Git reads this file and skips anything listed in it — those files will never be staged or uploaded.

The `venv` folder can be thousands of files and is specific to your Mac — other people don't need it, they create their own. So you always ignore it.

> Think of it as: "Here's a list of things Git should never touch."

---

### `git add` — staging your files

Git has 3 zones your files move through:

```
Working Area  →  Staging Area  →  Repository
(you edit)       (git add)        (git commit)
```

| Zone | What it is |
|---|---|
| **Working Area** | Your actual files — where you write and edit code |
| **Staging Area** | A holding area — files you've selected to include in the next save |
| **Repository** | The saved history — all your past commits |

**Why does staging exist?** It gives you control. Imagine you changed 5 files but only want to save 3 of them right now. You can stage just those 3 and commit only them.

```bash
git add .             # stage everything changed
git add exercise.py   # stage one specific file
```

> Think of it as: "Pack these items into the box — ready to ship."

---

### `git commit -m "message"`
```bash
git commit -m "add loop exercise"
```
Saves a permanent snapshot of everything in the staging area. The `-m` flag lets you write a short message describing what you did — this is your note to your future self.

Each commit is saved in history forever. You can always go back to any commit.

> Think of it as: "Seal the box and label it."

---

### `git push -u origin main`
```bash
git push -u origin main
```
Uploads your commits to GitHub for the **first time**.
- `origin` — the nickname for your GitHub repo
- `main` — the branch you're pushing
- `-u` — saves this destination so next time you just type `git push` with no extra words

> Think of it as: "Ship the box to GitHub — and remember this address for next time."

---

### `git push`
```bash
git push
```
Uploads your new commits to GitHub. Use this every time after the first push — no extra flags needed because `-u` already saved the destination.

> Think of it as: "Ship the box."

---

### `git pull`
```bash
git pull
```
Downloads the latest commits from GitHub to your Mac. Use this when someone else pushed changes, or when you made changes directly on GitHub and want to bring them down.

> Think of it as: "What's new on GitHub? Bring it to my Mac."

---

### `git status`
```bash
git status
```
Shows you the current state of your files:
- **Red** = changed but not staged yet
- **Green** = staged and ready to commit
- Nothing shown = everything is up to date

Run this often — it's your way of checking "where am I right now?"

---

### `git branch`
```bash
git branch
```
Lists all branches in your project. The one with `*` next to it is the branch you're currently on. Most of the time you'll just see `* main`.

---

### `git log`
```bash
git log
```
Shows the full history of all past commits — who made them, when, and the message. Most recent commit is at the top. Press `q` to exit.

---

### `git diff`
```bash
git diff
```
Shows exactly what changed in your files — line by line. Lines starting with `-` were removed, lines starting with `+` were added. Useful before committing to review what you actually changed.

---

## Scenario D — The daily developer workflow

**When to use:** Every single day when you sit down to work on a project that's already set up on GitHub.

This is the scenario you will use the most — more than any other.

---

### Step 1 — Start your session: pull first

Before touching any files, always get the latest version from GitHub:

```bash
git pull
```

**Why:** If you worked on another computer, or someone else pushed changes, your local files might be out of date. Always pull first so you're working on the latest version.

---

### Step 2 — Do your work

Open your files, write code, make changes. Git is just watching in the background — you don't need to do anything yet.

---

### Step 3 — Check what you changed

```bash
git status
```

Shows you which files you edited. Red = changed but not staged yet.

---

### Step 4 — Review your changes (optional but good habit)

```bash
git diff
```

Shows you exactly what lines you added or removed. Good to check before committing so you don't accidentally save something you didn't mean to.

---

### Step 5 — Stage your files

```bash
git add .
```

Stages everything. Or if you only want to save specific files:

```bash
git add exercise.py
```

---

### Step 6 — Commit (save a snapshot)

```bash
git commit -m "describe what you did"
```

Write a short message that explains what changed. Be specific — not just "update" but "fix loop in exercise 3" or "add functions chapter notes".

---

### Step 7 — Push to GitHub

```bash
git push
```

Uploads your commit to GitHub. Done.

---

### Full daily routine at a glance

```bash
git pull                              # 1. get latest from GitHub
# ... do your work ...
git status                            # 2. see what changed
git diff                              # 3. review changes (optional)
git add .                             # 4. stage everything
git commit -m "what you did"          # 5. save a snapshot
git push                              # 6. upload to GitHub
```

---

### Most used commands — ranked by how often developers use them

| Rank | Command | When |
|---|---|---|
| 1 | `git status` | Constantly — to check what's going on |
| 2 | `git add .` | Every time before committing |
| 3 | `git commit -m "..."` | Every time you finish a piece of work |
| 4 | `git push` | After committing |
| 5 | `git pull` | Start of every session |
| 6 | `git log` | When you want to see past history |
| 7 | `git diff` | Before committing to review changes |

> `git init` and `git remote add` are used rarely — only when starting a brand new project.

---

## Check commands

| Command | What it does |
|---|---|
| `git status` | Shows what files changed and what's staged |
| `git branch` | Shows your branches — `*` marks the one you're on |
| `git log` | Shows all past commits (press `q` to exit) |
| `git diff` | Shows exactly what lines changed in your files |

---

## Key terms

| Term | Meaning |
|---|---|
| **Repository (repo)** | A project folder tracked by Git |
| **Commit** | A saved snapshot of your code at a point in time |
| **Branch** | A separate copy of the code to experiment without breaking the main version |
| **main** | The default branch name |
| **origin** | A nickname for your GitHub repo URL |
| **Push** | Send commits from your Mac → GitHub |
| **Pull** | Bring commits from GitHub → your Mac |
| **Clone** | Download a full repo from GitHub to your Mac |
| **.gitignore** | A file that lists folders/files Git should never track |

---

## Common errors and fixes

| Error | What it means | Fix |
|---|---|---|
| `remote origin already exists` | You already linked to GitHub | Safe to ignore, keep going |
| `src refspec main does not match any` | You haven't committed anything yet | Run `git add .` then `git commit -m "..."` first |
| Asked for password | GitHub no longer uses your account password | Use a Personal Access Token instead |

---

## Scenario F — Pull Requests (PR)

**When to use:** When you want to merge a branch into `main` but with a review step in between — standard practice in teams, and a good habit even when working solo.

---

### What is a Pull Request?

A pull request is a way to **ask for your branch to be merged into another branch** on GitHub. Instead of merging directly in Terminal, you open a PR on GitHub so the changes can be reviewed, discussed, and approved before they touch `main`.

```
my-feature:   A --- B --- C   ← your changes
                            \
                             PR → review → merge
                            /
main:         A --- B --- C --- D   ← main gets updated
```

---

### Why use a PR instead of just merging?

| Direct merge | Pull Request |
|---|---|
| Instant, no review | Someone reviews before merging |
| Good for quick solo work | Standard in all teams |
| No record of discussion | Comments, feedback, history all saved on GitHub |

---

### Step 1 — Push your branch to GitHub (in Terminal)

```bash
git checkout -b my-feature      # create and switch to branch
# ... do your work ...
git add .
git commit -m "what you did"
git push -u origin my-feature   # push the branch to GitHub
```

---

### Step 2 — Open a Pull Request (on GitHub)

1. Go to your repo on **github.com**
2. GitHub shows a yellow banner: *"my-feature had recent pushes — Compare & pull request"*
3. Click **Compare & pull request**
4. Fill in:
   - **Title** — short description of what you did
   - **Description** — more detail if needed
5. Check the **base branch** (where you're merging INTO — usually `main`) and **compare branch** (your branch)
6. Click **Create pull request**

---

### Step 3 — Review the changes

On the **Files changed** tab you'll see:
- **Green lines (+)** = lines you added
- **Red lines (−)** = lines you removed

Review to make sure everything looks right before merging.

---

### Step 4 — Merge the Pull Request

1. Click **Merge pull request**
2. Click **Confirm merge**
3. Optionally click **Delete branch** to clean up the branch on GitHub

Your changes are now in `main` on GitHub.

---

### Step 5 — Update your local main (in Terminal)

After merging on GitHub, bring the update down to your Mac:

```bash
git checkout main
git pull
```

---

### Full PR workflow at a glance

```bash
# --- Terminal ---
git checkout -b my-feature          # 1. create branch
# ... do your work ...
git add .
git commit -m "what you did"        # 2. commit
git push -u origin my-feature       # 3. push branch to GitHub

# --- GitHub (website) ---
# 4. Click "Compare & pull request"
# 5. Write title and description
# 6. Click "Create pull request"
# 7. Review changes on "Files changed" tab
# 8. Click "Merge pull request" → "Confirm merge"
# 9. Click "Delete branch" (optional)

# --- Terminal ---
git checkout main                   # 10. switch back to main
git pull                            # 11. get the merged changes
git branch -d my-feature            # 12. delete branch locally (optional)
```

---

### Key PR terms

| Term | Meaning |
|---|---|
| **Pull Request (PR)** | A request to merge your branch into another branch |
| **Base branch** | The branch you want to merge INTO (usually `main`) |
| **Compare branch** | Your branch with the new changes |
| **Reviewer** | Someone who reads and approves your code before merging |
| **Merge** | When the PR is approved and changes are added to `main` |
| **Files changed** | The tab on GitHub showing exactly what lines you added/removed |
| **Conversation** | The comments and discussion thread on the PR |

---

## Tips

- Always write a clear commit message — future you will thank you
- Run `git status` often to see what's going on
- Commit small and often, not one big chunk at the end
- Never upload your `venv` folder — always add it to `.gitignore`
