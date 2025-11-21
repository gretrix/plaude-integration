# Plaud Integration Project Overview

## Project Purpose
Automated voice transcript processing system that extracts structured data from Plaud voice recordings and stores it in a MySQL database with a web dashboard interface.

## Architecture
```
Plaud App → Zapier → AI Extraction → Python Flask Server → MySQL Database → Web Dashboard
```

## Technology Stack
- **Backend**: Python 3.8+ with Flask
- **Database**: MySQL 8.x (hosted on AWS RDS)
- **Automation**: Zapier with AI by Zapier
- **Frontend**: HTML/CSS/JavaScript (Jinja2 templates)
- **Deployment**: AWS EC2 (Ubuntu)
- **Development**: ngrok for local webhook testing

## Core Features
1. **Diet Tracking**: Food items, calories, meal types, timestamps
2. **Task Management**: Tasks with priorities, due dates, status tracking, checkboxes
3. **CRM System**: Contact management with company, email, phone, notes
4. **Dashboard**: Mobile-responsive web interface with statistics and filtering

## Database Schema

### Tables
- `diet`: food, food_type, estimated_calories (INT), time_of_day, date
- `tasks`: task_name, task_type, responsible_party, status, best_start_date, best_due_date, time_interval, notes, dependency
- `crm_records`: contact_name, company, email, phone, notes, status
- `plaud_transcripts`: transcript_id, title, transcript_text, summary_text, create_time

## API Endpoints
- `GET /` - Web dashboard homepage
- `GET /diet` - Diet tracking page
- `GET /tasks` - Tasks management page
- `GET /crm` - CRM contacts page
- `POST /api/diet` - Receive diet data from Zapier
- `POST /api/tasks` - Receive task data from Zapier
- `POST /api/crm` - Receive CRM data from Zapier
- `POST /api/plaud` - Receive complete transcript data
- `PATCH /api/tasks/<id>/status` - Update task status
- `GET /api/stats` - Dashboard statistics
- `GET /health` - Health check endpoint

## Key Files
- `app.py` - Main Flask application with all routes and database logic
- `requirements.txt` - Python dependencies
- `create_tables.sql` - Database schema creation
- `templates/*.html` - Web dashboard templates
- `COMPLETE_SETUP_GUIDE.md` - Full setup documentation
- `zapier_prompts.md` - AI extraction prompts for Zapier

## Development Workflow
1. Make code changes locally
2. Test with ngrok webhook
3. Push to GitHub
4. SSH to EC2 and pull changes
5. Restart Flask server

## Deployment Details
- **EC2 IP**: 98.82.115.184
- **MySQL Host**: 52.2.41.189
- **Database**: slack
- **Port**: 5000
- **Process Management**: screen or nohup
