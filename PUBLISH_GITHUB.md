# Publish DDOS INFINITY X on GitHub

Repository URL (update username if yours is different):

**https://github.com/adilf/DDOS-INFINITY-X**

---

## Step 1 — Install Git

Download: https://git-scm.com/download/win  
Restart PowerShell after install.

Optional GitHub CLI: https://cli.github.com/

---

## Step 2 — Create repo on GitHub

1. Open https://github.com/new  
2. Repository name: `DDOS-INFINITY-X`  
3. Description: `DDOS INFINITY X — educational stress-testing framework by adil fayyaz`  
4. Public (or Private)  
5. **Do not** add README / .gitignore (already in project)  
6. Click **Create repository**

If your username is not `adilf`, replace `adilf` in README, banner.py, and this file with your GitHub username.

---

## Step 3 — Push from PowerShell

```powershell
cd "c:\Users\adilf\Downloads\MHDDoS-main\MHDDoS-main"

git init
git add .
git commit -m "Initial release: DDOS INFINITY X by adil fayyaz"
git branch -M main
git remote add origin https://github.com/TUO_USERNAME/DDOS-INFINITY-X.git
git push -u origin main
```

Replace `TUO_USERNAME` with your GitHub username.

---

## Step 4 — With GitHub CLI (optional)

```powershell
gh auth login
gh repo create DDOS-INFINITY-X --public --source=. --remote=origin --push
```

---

## Step 5 — Enable Actions

After push, open **Actions** on GitHub and enable workflows for Docker builds.

---

## Rename folder (optional)

Rename `MHDDoS-main` to `DDOS-INFINITY-X` on disk so the folder matches the repo name.
