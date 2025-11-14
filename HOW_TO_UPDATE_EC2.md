# 🚀 Quick Guide: Update EC2 Server with New Changes

## ⚡ Fast Update (Copy & Paste)

Connect to EC2 and run these commands:

```bash
# 1. SSH into EC2
ssh ubuntu@98.82.115.184

# 2. Navigate to project
cd ~/plaude-integration

# 3. Pull latest changes
git pull origin main

# 4. Find running Python process
ps aux | grep "python app.py"

# 5. Kill the old process (replace <PID> with the actual process ID)
kill <PID>

# 6. Activate virtual environment
source venv/bin/activate

# 7. Start Flask server in background
nohup python app.py > app.log 2>&1 &

# 8. Verify it's running
ps aux | grep "python app.py"

# 9. Exit SSH
exit
```

---

## 📋 Step-by-Step Instructions

### Step 1: Connect to EC2
```bash
ssh ubuntu@98.82.115.184
```

### Step 2: Go to Project Directory
```bash
cd ~/plaude-integration
```

### Step 3: Pull Latest Code from GitHub
```bash
git pull origin main
```
You should see:
```
Updating 6353c56..667d8a1
Fast-forward
 TASKS_FEATURES_UPDATE.md | 245 +++++++++++++++++++++++
 app.py                   |  86 +++++++-
 templates/tasks.html     | 414 ++++++++++++++++++++++++++++++++++----
 4 files changed, 718 insertions(+), 27 deletions(-)
```

### Step 4: Find Running Process
```bash
ps aux | grep "python app.py"
```
Look for a line like:
```
ubuntu    1234  0.5  2.3  123456  45678 ?  S  10:30  0:05 python app.py
```
The number after `ubuntu` (e.g., `1234`) is the **Process ID (PID)**.

### Step 5: Stop Old Server
```bash
kill 1234
```
(Replace `1234` with your actual PID)

### Step 6: Activate Virtual Environment
```bash
source venv/bin/activate
```
Your prompt should change to show `(venv)`.

### Step 7: Start New Server
```bash
nohup python app.py > app.log 2>&1 &
```
This runs the server in the background and logs output to `app.log`.

### Step 8: Verify It's Running
```bash
ps aux | grep "python app.py"
```
You should see a new process running.

### Step 9: Test the Website
Open your browser and go to your dashboard URL. Test:
- ✅ Checkboxes on tasks
- ✅ Filters (Status, Type, Responsible)
- ✅ Sorting by clicking column headers
- ✅ Refresh page - filters should be remembered

### Step 10: Exit SSH
```bash
exit
```

---

## 🔍 Troubleshooting

### Problem: "Address already in use"
**Solution:** The old process is still running. Find and kill it:
```bash
ps aux | grep "python app.py"
kill <PID>
```

### Problem: Can't connect to database
**Solution:** Make sure EC2's IP is whitelisted in MySQL security group:
- EC2 IP: `98.82.115.184`
- MySQL Server: `52.2.41.189:3306`

### Problem: Changes not showing up
**Solution:** Clear browser cache or do a hard refresh:
- **Windows/Linux:** `Ctrl + Shift + R`
- **Mac:** `Cmd + Shift + R`

### Problem: Want to see server logs
**Solution:** View the log file:
```bash
tail -f ~/plaude-integration/app.log
```
Press `Ctrl + C` to stop viewing.

---

## 📝 What Changed in This Update

### New Features:
1. **Checkboxes** - Mark tasks complete/incomplete
2. **Advanced Filters** - Filter by Status, Type, Responsible Party
3. **localStorage** - Browser remembers your filter preferences
4. **Column Sorting** - Click headers to sort tasks
5. **New API Endpoint** - `PATCH /api/tasks/<id>/status`

### Files Modified:
- `templates/tasks.html` - Added UI and JavaScript
- `app.py` - Added status update endpoint
- `TASKS_FEATURES_UPDATE.md` - Full documentation

---

## ✅ Quick Verification Checklist

After updating, verify these work:

- [ ] Tasks page loads
- [ ] Checkboxes appear next to each task
- [ ] Clicking checkbox marks task complete
- [ ] Status badge changes to green "Completed"
- [ ] Filter dropdowns work
- [ ] Filters persist after page refresh
- [ ] Clicking column headers sorts tasks
- [ ] Sort direction toggles (▲ ▼)

---

## 🆘 Need Help?

If something doesn't work:

1. **Check server is running:**
   ```bash
   ssh ubuntu@98.82.115.184
   ps aux | grep python
   ```

2. **Check logs:**
   ```bash
   tail -50 ~/plaude-integration/app.log
   ```

3. **Restart server:**
   ```bash
   cd ~/plaude-integration
   source venv/bin/activate
   pkill -f "python app.py"
   nohup python app.py > app.log 2>&1 &
   ```

---

## 🎉 You're Done!

Your EC2 server now has all the new task management features! 🚀

Test it out and enjoy the improved workflow! ✨

