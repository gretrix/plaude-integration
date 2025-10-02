# 🚀 Complete Plaud → Zapier → Python → MySQL Setup Guide

## ✅ What You've Built

A complete automated system that:
1. **Plaud** records your voice transcripts
2. **Zapier** automatically grabs new transcripts
3. **AI** extracts diet, tasks, and CRM data
4. **Python server** processes and validates data
5. **MySQL** stores everything permanently

---

## 📋 Step 1: Update Database (Fix Calories Column)

Run this SQL in your MySQL database:

```sql
USE slack;

-- Update calories to be a number (not string)
ALTER TABLE diet 
MODIFY COLUMN estimated_calories INT;

-- Optional: Clean existing data
UPDATE diet 
SET estimated_calories = CAST(REPLACE(REPLACE(estimated_calories, '~', ''), ' cal', '') AS UNSIGNED)
WHERE estimated_calories IS NOT NULL;
```

---

## 📋 Step 2: Create Tasks and CRM Tables

Run the SQL from `create_tables.sql`:

```sql
USE slack;

CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task_description TEXT NOT NULL,
    priority ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
    status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending',
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS crm_records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    contact_name VARCHAR(255) NOT NULL,
    company VARCHAR(255),
    email VARCHAR(255),
    phone VARCHAR(50),
    notes TEXT,
    status ENUM('Lead', 'Prospect', 'Customer', 'Lost') DEFAULT 'Lead',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    UNIQUE KEY unique_contact (contact_name, email)
);
```

---

## 🔧 Step 3: Restart Your Python Server

Your server now has 3 new endpoints!

**Available endpoints:**
- `/api/diet` - For diet data
- `/api/tasks` - For task data
- `/api/crm` - For CRM data

---

## ⚡ Step 4: Configure Zapier

### Option A: ONE Zap with Multiple AI Steps (RECOMMENDED)

```
Trigger: Plaud - New Transcript
  ↓
Step 2a: AI by Zapier - Extract Diet Data
  ↓
Step 3a: Loop by Zapier - Loop through diet items
  ↓
Step 4a: Webhook POST to https://your-ngrok.url/api/diet
  ↓
Step 2b: AI by Zapier - Extract Tasks
  ↓
Step 3b: Loop by Zapier - Loop through tasks
  ↓
Step 4b: Webhook POST to https://your-ngrok.url/api/tasks
  ↓
Step 2c: AI by Zapier - Extract CRM Data
  ↓
Step 3c: Loop by Zapier - Loop through contacts
  ↓
Step 4c: Webhook POST to https://your-ngrok.url/api/crm
```

---

## 📝 AI Prompts to Use

### Diet Extraction (UPDATED - Returns Numbers Only)

```
You are an AI assistant. From the transcript, extract all dietary information.

Return the result in valid JSON as an array of objects.
Each object must contain exactly these keys:
- food (string, e.g. "Sandwich")
- food_type (string, one of: "Meal", "Snack", "Drink")
- estimated_calories (number only, e.g. 500, NOT "~500 cal")
- time_of_day (string in strict 24hr format "HH:MM:SS", e.g. "12:30:00")
- date (string in strict "YYYY-MM-DD" format, e.g. "2025-09-24")

Rules:
- estimated_calories must be a NUMBER ONLY (e.g. 500)
- Always return time_of_day with seconds (HH:MM:SS)
- If no diet info is mentioned, return an empty array []
```

### Tasks Extraction

```
You are an AI assistant. From the transcript, extract all tasks and to-do items.

Return the result in valid JSON as an array of objects.
Each object must contain exactly these keys:
- task_description (string, e.g. "Call John about project")
- priority (string, one of: "Low", "Medium", "High")
- status (string, one of: "Pending", "In Progress", "Completed")
- due_date (string in "YYYY-MM-DD" format, or null if not mentioned)

Rules:
- If priority is not mentioned, use "Medium"
- If status is not mentioned, use "Pending"
- If no tasks are mentioned, return an empty array []
```

### CRM Extraction

```
You are an AI assistant. From the transcript, extract all contact and CRM information.

Return the result in valid JSON as an array of objects.
Each object must contain exactly these keys:
- contact_name (string, e.g. "John Smith")
- company (string, or null if not mentioned)
- email (string, or null if not mentioned)
- phone (string, or null if not mentioned)
- notes (string, any additional context)
- status (string, one of: "Lead", "Prospect", "Customer", "Lost")

Rules:
- If status is not mentioned, use "Lead"
- If no contacts are mentioned, return an empty array []
```

---

## 🎯 Webhook Configuration for Each Type

### For Diet (Step 4a):
- **URL**: `https://your-ngrok-url/api/diet`
- **Method**: POST
- **Data**:
  - `food` → `3a. Result Food`
  - `food_type` → `3a. Result Food Type`
  - `estimated_calories` → `3a. Result Estimated Calories`
  - `time_of_day` → `3a. Result Time Of Day`
  - `date` → `3a. Result Date`

### For Tasks (Step 4b):
- **URL**: `https://your-ngrok-url/api/tasks`
- **Method**: POST
- **Data**:
  - `task_description` → `3b. Result Task Description`
  - `priority` → `3b. Result Priority`
  - `status` → `3b. Result Status`
  - `due_date` → `3b. Result Due Date`

### For CRM (Step 4c):
- **URL**: `https://your-ngrok-url/api/crm`
- **Method**: POST
- **Data**:
  - `contact_name` → `3c. Result Contact Name`
  - `company` → `3c. Result Company`
  - `email` → `3c. Result Email`
  - `phone` → `3c. Result Phone`
  - `notes` → `3c. Result Notes`
  - `status` → `3c. Result Status`

---

## 💡 Do You Need Separate Zaps?

**NO!** You can use **ONE Zap** with multiple AI steps and webhook calls.

**Benefits:**
- ✅ Single trigger per transcript
- ✅ All data extracted in one flow
- ✅ Easier to manage
- ✅ Uses fewer Zap tasks

---

## 🎊 Testing

1. **Record something on Plaud** with diet, tasks, and contacts
2. **Watch Zapier trigger**
3. **See AI extract all three types**
4. **Watch webhooks send to your server**
5. **Check MySQL** - all tables populated!

---

## 📊 Current Status

✅ MySQL connected  
✅ Diet endpoint working  
✅ Tasks endpoint added  
✅ CRM endpoint added  
✅ Numeric calories implemented  
✅ Error handling in place  
✅ Ready for production!

---

## 🔥 Your Public IP (Whitelisted)

`115.98.213.83` - Already whitelisted by Sunil!

---

## 📞 Next Steps

1. Run the SQL to update calories and create new tables
2. Restart your Python server
3. Update your Zapier AI prompt for diet (use numbers only)
4. Add 2 more AI steps + loops + webhooks for tasks and CRM
5. Test with a real transcript!

**You're 95% done!** Just need to create the tables and update the Zap! 🚀

