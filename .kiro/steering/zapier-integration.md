# Zapier Integration Guide

## Overview
This project uses Zapier to automate the extraction and processing of voice transcripts from Plaud app. The workflow uses AI to extract structured data and sends it to the Flask webhook server.

## Zapier Workflow Architecture

```
Plaud Trigger (New Transcript)
    ↓
AI Step 1: Extract Diet Data
    ↓
Loop: Process Each Diet Item
    ↓
Webhook: POST to /api/diet
    ↓
AI Step 2: Extract Tasks
    ↓
Loop: Process Each Task
    ↓
Webhook: POST to /api/tasks
    ↓
AI Step 3: Extract CRM Data
    ↓
Loop: Process Each Contact
    ↓
Webhook: POST to /api/crm
```

## AI Extraction Prompts

### Diet Extraction
The AI must return numeric calories (not strings like "~500 cal").

**Output Fields**: food, food_type, estimated_calories, time_of_day, date

**Key Requirements**:
- estimated_calories must be a NUMBER (e.g., 500)
- time_of_day in 24hr format with seconds (HH:MM:SS)
- date in YYYY-MM-DD format
- food_type must be: "Meal", "Snack", or "Drink"

### Tasks Extraction
**Output Fields**: task_name, task_type, responsible_party, status, best_start_date, best_due_date, time_interval, notes, dependency

**Key Requirements**:
- status must be: "Pending", "In Progress", "Completed", or "Cancelled"
- task_type examples: "Meeting", "Call", "Email", "Follow-up", "Other"
- Dates in YYYY-MM-DD format
- Use null for optional fields if not mentioned

### CRM Extraction
**Output Fields**: contact_name, company, email, phone, notes, status

**Key Requirements**:
- status must be: "Lead", "Prospect", "Customer", or "Lost"
- Default status is "Lead" if not mentioned
- Use null for optional fields

## Webhook Configuration

### Diet Webhook
- **URL**: `https://your-ngrok-url/api/diet` or `http://98.82.115.184:5000/api/diet`
- **Method**: POST
- **Content-Type**: application/json
- **Payload Mapping**:
  - food → Loop Result: Food
  - food_type → Loop Result: Food Type
  - estimated_calories → Loop Result: Estimated Calories
  - time_of_day → Loop Result: Time Of Day
  - date → Loop Result: Date

### Tasks Webhook
- **URL**: `https://your-ngrok-url/api/tasks` or `http://98.82.115.184:5000/api/tasks`
- **Method**: POST
- **Content-Type**: application/json
- **Payload Mapping**:
  - task_name → Loop Result: Task Name
  - task_type → Loop Result: Task Type
  - responsible_party → Loop Result: Responsible Party
  - status → Loop Result: Status
  - best_start_date → Loop Result: Best Start Date
  - best_due_date → Loop Result: Best Due Date
  - time_interval → Loop Result: Time Interval
  - notes → Loop Result: Notes
  - dependency → Loop Result: Dependency

### CRM Webhook
- **URL**: `https://your-ngrok-url/api/crm` or `http://98.82.115.184:5000/api/crm`
- **Method**: POST
- **Content-Type**: application/json
- **Payload Mapping**:
  - contact_name → Loop Result: Contact Name
  - company → Loop Result: Company
  - email → Loop Result: Email
  - phone → Loop Result: Phone
  - notes → Loop Result: Notes
  - status → Loop Result: Status

## Testing Zapier Integration

### 1. Test AI Extraction
- Use Zapier's "Test" button on AI step
- Verify JSON output matches expected format
- Check that field names match exactly

### 2. Test Loop
- Verify loop creates separate items
- Check that all fields are accessible in loop results

### 3. Test Webhook
- Send test data to webhook
- Check Flask logs for incoming request
- Verify data appears in MySQL database
- Check for any error responses

### 4. End-to-End Test
- Record a real transcript in Plaud
- Wait for Zapier trigger
- Monitor Zapier task history
- Check Flask logs
- Verify data in database
- View in web dashboard

## Common Issues and Solutions

### Issue: Calories Stored as String
**Solution**: Update AI prompt to return numbers only, not "~500 cal"

### Issue: Date Format Errors
**Solution**: Ensure AI returns YYYY-MM-DD format, not other formats

### Issue: Webhook 404 Error
**Solution**: 
- Verify Flask server is running
- Check ngrok tunnel is active
- Confirm URL is correct in Zapier

### Issue: Data Not Saving
**Solution**:
- Check Flask logs for errors
- Verify MySQL connection via /health endpoint
- Check table structure matches code

### Issue: Duplicate Data
**Solution**: 
- UNIQUE constraints prevent duplicates
- ON DUPLICATE KEY UPDATE handles conflicts
- Check if constraint columns match your data

### Issue: Empty Arrays from AI
**Solution**:
- Verify transcript contains relevant data
- Check AI prompt is clear
- Test with more explicit transcript content

## Zapier Best Practices

### Single Zap vs Multiple Zaps
**Recommended**: Use ONE Zap with multiple AI steps
- More efficient (single trigger)
- Easier to maintain
- All data processed together
- Fewer Zap tasks consumed

### Error Handling
- Enable "Continue on Error" for non-critical steps
- Add filters to skip empty results
- Monitor Zapier task history regularly
- Set up email alerts for failures

### Performance
- Use loops for multiple items (don't create separate Zaps)
- Batch similar operations together
- Avoid unnecessary delays
- Test with realistic data volumes

### Maintenance
- Document all Zap configurations
- Keep AI prompts in version control (zapier_prompts.md)
- Test after any changes
- Keep webhook URLs updated

## Monitoring Zapier Integration

### Check Zapier Task History
- View recent runs
- Check for errors or warnings
- Verify data was sent correctly
- Monitor success rate

### Check Flask Logs
```bash
# View recent webhook calls
grep "Received.*data" flask.log

# Check for errors
grep ERROR flask.log

# Monitor in real-time
tail -f flask.log
```

### Check Database
```sql
-- Recent diet entries
SELECT * FROM diet ORDER BY created_at DESC LIMIT 10;

-- Recent tasks
SELECT * FROM tasks ORDER BY created_at DESC LIMIT 10;

-- Recent contacts
SELECT * FROM crm_records ORDER BY created_at DESC LIMIT 10;
```

## Updating Zapier Configuration

When making changes:
1. Test changes in a copy of the Zap first
2. Update AI prompts in zapier_prompts.md
3. Update webhook URLs if endpoints change
4. Test thoroughly before enabling
5. Monitor first few runs closely
6. Document changes in project docs

## Zapier Alternatives

If Zapier becomes limiting, consider:
- **Make.com**: More complex workflows
- **n8n**: Self-hosted automation
- **Direct API Integration**: Custom Python script
- **AWS Lambda**: Serverless processing

## Security Considerations

### Webhook Security
- Use HTTPS (ngrok provides this)
- Consider adding API key authentication
- Validate incoming data format
- Rate limit if needed

### Data Privacy
- Transcripts may contain sensitive information
- Ensure database is secured
- Don't log sensitive data
- Follow data retention policies
