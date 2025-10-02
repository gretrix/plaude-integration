# 📋 Zapier AI Output Fields Configuration

## How to Configure the "Output fields" Section

When you see the **"Output fields"** section in AI by Zapier, you're telling Zapier what data to extract and structure from the AI response.

---

## 🍽️ DIET - Output Fields (Already Working)

```
✅ food
✅ food_type
✅ estimated_calories
✅ time_of_day
✅ date
```

---

## 📋 TASKS - Output Fields Configuration

### Your MySQL Table Structure:
`id, task_name, task_type, responsible_party, status, best_start_date, best_due_date, time_interval, notes, dependency, created_at`

### In Zapier AI by Zapier "Output fields" section:

Click **"+ Add field"** for each of these (in order):

1. **task_name** (type: text)
2. **task_type** (type: text)
3. **responsible_party** (type: text)
4. **status** (type: text)
5. **best_start_date** (type: text)
6. **best_due_date** (type: text)
7. **time_interval** (type: text)
8. **notes** (type: text)
9. **dependency** (type: text)

### Updated AI Prompt for Tasks:

```
You are an AI assistant. From the transcript, extract all tasks and to-do items.

Return the result in valid JSON as an array of objects.
Each object must contain exactly these keys:
- task_name (string, e.g. "Call John about project")
- task_type (string, e.g. "Meeting", "Call", "Email", "Other")
- responsible_party (string, name of person responsible, or null if not mentioned)
- status (string, one of: "Pending", "In Progress", "Completed", "Cancelled")
- best_start_date (string in "YYYY-MM-DD" format, or null if not mentioned)
- best_due_date (string in "YYYY-MM-DD" format, or null if not mentioned)
- time_interval (string, e.g. "1 hour", "2 days", or null if not mentioned)
- notes (string, any additional context about the task)
- dependency (string, what this task depends on, or null if no dependency)

Rules:
- Create one JSON object for **each distinct task mentioned**.
- If status is not mentioned, use "Pending"
- If task_type is not clear, use "Other"
- Always return dates with only year-month-day (YYYY-MM-DD)
- If no tasks are mentioned, return an empty array []
- Do not include explanations, comments, or extra fields — return only the JSON array
```

---

## 👥 CRM - Output Fields Configuration

### Your MySQL Table Structure:
`id, contact_name, company, email, phone, notes, status, created_at, updated_at`

### In Zapier AI by Zapier "Output fields" section:

Click **"+ Add field"** for each of these (in order):

1. **contact_name** (type: text)
2. **company** (type: text)
3. **email** (type: text)
4. **phone** (type: text)
5. **notes** (type: text)
6. **status** (type: text)

### AI Prompt for CRM (Already Correct):

```
You are an AI assistant. From the transcript, extract all contact and CRM information.

Return the result in valid JSON as an array of objects.
Each object must contain exactly these keys:
- contact_name (string, e.g. "John Smith")
- company (string, e.g. "Acme Corp", or null if not mentioned)
- email (string, or null if not mentioned)
- phone (string, or null if not mentioned)
- notes (string, any additional context about the contact)
- status (string, one of: "Lead", "Prospect", "Customer", "Lost")

Rules:
- Create one JSON object for **each distinct contact mentioned**.
- If status is not mentioned, use "Lead"
- Extract any relevant context into the notes field
- If no contacts are mentioned, return an empty array [].
- Do not include explanations, comments, or extra fields — return only the JSON array.
```

---

## 🔧 Visual Guide: What to Type in Zapier

### For Tasks AI Step:

```
Output fields section:
┌─────────────────────────┐
│ + Add field             │
├─────────────────────────┤
│ task_name          [x]  │  ← Click "+ Add field" and type "task_name"
│ task_type          [x]  │  ← Click "+ Add field" and type "task_type"
│ responsible_party  [x]  │  ← Click "+ Add field" and type "responsible_party"
│ status             [x]  │  ← Click "+ Add field" and type "status"
│ best_start_date    [x]  │  ← Click "+ Add field" and type "best_start_date"
│ best_due_date      [x]  │  ← Click "+ Add field" and type "best_due_date"
│ time_interval      [x]  │  ← Click "+ Add field" and type "time_interval"
│ notes              [x]  │  ← Click "+ Add field" and type "notes"
│ dependency         [x]  │  ← Click "+ Add field" and type "dependency"
└─────────────────────────┘
```

### For CRM AI Step:

```
Output fields section:
┌─────────────────────────┐
│ + Add field             │
├─────────────────────────┤
│ contact_name       [x]  │  ← Click "+ Add field" and type "contact_name"
│ company            [x]  │  ← Click "+ Add field" and type "company"
│ email              [x]  │  ← Click "+ Add field" and type "email"
│ phone              [x]  │  ← Click "+ Add field" and type "phone"
│ notes              [x]  │  ← Click "+ Add field" and type "notes"
│ status             [x]  │  ← Click "+ Add field" and type "status"
└─────────────────────────┘
```

---

## 🎯 Complete Zapier Flow

### Step-by-Step:

```
1. Plaud Trigger: Transcript Ready
   ↓
2. AI by Zapier: Extract Tasks
   - Paste the Tasks prompt
   - Add output fields: task_name, task_type, responsible_party, status, 
     best_start_date, best_due_date, time_interval, notes, dependency
   ↓
3. Loop by Zapier: Create Loop
   - Add all 9 values from Step 2
   ↓
4. Webhooks POST: https://your-ngrok-url/api/tasks
   - Map: task_name → 3. Result Task Name
   - Map: task_type → 3. Result Task Type
   - Map: responsible_party → 3. Result Responsible Party
   - Map: status → 3. Result Status
   - Map: best_start_date → 3. Result Best Start Date
   - Map: best_due_date → 3. Result Best Due Date
   - Map: time_interval → 3. Result Time Interval
   - Map: notes → 3. Result Notes
   - Map: dependency → 3. Result Dependency
```

**Then repeat the same for CRM!**

---

## ✅ Checklist

- [ ] Update Tasks AI prompt in Zapier
- [ ] Add 9 output fields for Tasks
- [ ] Update CRM prompt (already correct)
- [ ] Add 6 output fields for CRM
- [ ] Configure Loop steps
- [ ] Configure Webhook POST steps
- [ ] Test!

---

## 💡 Pro Tip

The output field names MUST match exactly what you put in the AI prompt. If the prompt says `task_name`, the output field should be `task_name` (not `Task Name` or `taskName`).

