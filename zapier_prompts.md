# Zapier AI Prompts for Plaud Integration

## 🍽️ Diet Extraction Prompt (UPDATED for numeric calories)

```
You are an AI assistant. From the transcript, extract all dietary information.

Return the result in valid JSON as an array of objects.
Each object must contain exactly these keys:
- food (string, e.g. "Sandwich")
- food_type (string, one of: "Meal", "Snack", "Drink")
- estimated_calories (number only, e.g. 500, not "~500 cal")
- time_of_day (string in strict 24hr format "HH:MM:SS", e.g. "12:30:00")
- date (string in strict "YYYY-MM-DD" format, e.g. "2025-09-24")

Rules:
- Create one JSON object for **each distinct food or drink item mentioned**.
- estimated_calories must be a NUMBER ONLY (e.g. 500, not "~500 cal" or "500 cal")
- Always return time_of_day with **seconds** (HH:MM:SS).
- Always return date with only year-month-day (YYYY-MM-DD).
- Never include timezone offsets or extra text.
- If no diet info is mentioned, return an empty array [].
- Do not include explanations, comments, or extra fields — return only the JSON array.
```

---

## 📋 Tasks Extraction Prompt (UPDATED for your database)

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

## 👥 CRM Extraction Prompt

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

## 🔧 How to Use These Prompts

### Option 1: Separate AI Steps (Recommended for clarity)
1. **Step 2a**: AI by Zapier - Diet Extraction
2. **Step 2b**: AI by Zapier - Tasks Extraction
3. **Step 2c**: AI by Zapier - CRM Extraction
4. Then loop and webhook each separately

### Option 2: One AI Step with Multiple Categories
Create one prompt that returns:
```json
{
  "diet": [...],
  "tasks": [...],
  "crm": [...]
}
```
Then send all to one endpoint: `/api/plaud`

