# Quick Answers to Your Questions

## ❓ Question 1: Do I need separate Zaps for diet, tasks, and CRM?

**Answer: NO!** ✅

You can use **ONE Zap** with multiple steps:

```
ONE ZAP:
├── Trigger: Plaud transcript ready
├── AI Step 1: Extract diet → Loop → Webhook to /api/diet
├── AI Step 2: Extract tasks → Loop → Webhook to /api/tasks
└── AI Step 3: Extract CRM → Loop → Webhook to /api/crm
```

**Benefits:**
- Single trigger per transcript
- All data processed automatically
- Easier to maintain
- More efficient

---

## ❓ Question 2: How to fix calories to be a number (not string)?

**Answer: Already done!** ✅

### What I Changed:

1. **Python Code**: Now extracts just the number from "~500 cal" → `500`
2. **Database**: Need to update column type from `VARCHAR` to `INT`

### SQL to Run:

```sql
USE slack;

-- Change column to INT
ALTER TABLE diet 
MODIFY COLUMN estimated_calories INT;

-- Clean existing data (optional)
UPDATE diet 
SET estimated_calories = CAST(REPLACE(REPLACE(estimated_calories, '~', ''), ' cal', '') AS UNSIGNED)
WHERE estimated_calories IS NOT NULL;
```

### Update Your Zapier AI Prompt:

Change this line:
```
- estimated_calories (string, e.g. "~500 cal")  ❌ OLD
```

To:
```
- estimated_calories (number only, e.g. 500)  ✅ NEW
```

Now AI will return `500` instead of `"~500 cal"`, and Python will store it as an integer!

---

## ❓ Question 3: How to configure Zapier for tasks and CRM?

**Answer: Copy your diet flow!** ✅

### For Tasks:

1. **Add AI by Zapier step** with the Tasks prompt (see `zapier_prompts.md`)
2. **Add Loop by Zapier** to split multiple tasks
3. **Add Webhook POST** to `https://your-ngrok-url/api/tasks`
4. **Map fields**:
   - `task_description` → Loop result
   - `priority` → Loop result
   - `status` → Loop result
   - `due_date` → Loop result

### For CRM:

1. **Add AI by Zapier step** with the CRM prompt
2. **Add Loop by Zapier** to split multiple contacts
3. **Add Webhook POST** to `https://your-ngrok-url/api/crm`
4. **Map fields**:
   - `contact_name` → Loop result
   - `company` → Loop result
   - `email` → Loop result
   - `phone` → Loop result
   - `notes` → Loop result
   - `status` → Loop result

---

## 📋 What Tables Do You Need?

### Already Have:
✅ `diet` - Just needs calories column updated to INT

### Need to Create:
❌ `tasks` - Run SQL from `create_tables.sql`
❌ `crm_records` - Run SQL from `create_tables.sql`

---

## 🚀 Your Complete Flow

```
1. Record transcript on Plaud
   ↓
2. Zapier triggers
   ↓
3. AI extracts:
   - Diet items → /api/diet endpoint
   - Tasks → /api/tasks endpoint
   - Contacts → /api/crm endpoint
   ↓
4. Python validates & processes
   ↓
5. MySQL stores permanently
   ↓
6. Done! ✅
```

---

## 📊 Endpoints Available

Your Python server now has:

| Endpoint | Purpose | Status |
|----------|---------|--------|
| `/api/diet` | Diet records | ✅ Working |
| `/api/tasks` | Task management | ✅ Ready (need table) |
| `/api/crm` | Contact management | ✅ Ready (need table) |
| `/health` | Server health check | ✅ Working |

---

## ⚡ Next 3 Steps:

1. **Run SQL** to update calories and create tasks/crm tables
2. **Update Zapier AI prompt** for diet (return numbers only)
3. **Add 2 more AI steps** in Zapier for tasks and CRM

That's it! 🎉

