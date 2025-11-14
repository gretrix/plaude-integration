# Plaud Integration - Automated Transcript Processing

Automated system that processes Plaud voice transcripts through Zapier, extracts structured data using AI, and stores it in MySQL.

## 🎯 Overview

This project automatically:
- 📝 Captures transcripts from Plaud app
- 🤖 Extracts diet, tasks, and CRM data using AI
- 🔄 Processes data through Python webhook server
- 💾 Stores structured data in MySQL database

## 🏗️ Architecture

```
Plaud App → Zapier → AI Extraction → Python Server → MySQL
```

## ✨ Features

- ✅ Automatic diet tracking with calorie counting
- ✅ Task management with priorities and due dates
- ✅ CRM contact management
- ✅ Bulk insert with duplicate handling
- ✅ Error handling and logging
- ✅ MySQL connection with fallback mode
- ✅ **Mobile-responsive web dashboard** 📱
- ✅ **Optimized for phones and tablets**

## 📋 Prerequisites

- Python 3.8+
- MySQL database
- Zapier account
- Plaud app account
- ngrok (for local development)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure Database

Update MySQL credentials in `app.py`:

```python
DB_CONFIG = {
    'host': 'your-mysql-host',
    'port': 3306,
    'database': 'your-database',
    'user': 'your-username',
    'password': 'your-password'
}
```

### 3. Create Database Tables

```bash
mysql -u username -p database_name < create_tables.sql
```

### 4. Run the Server

```bash
python app.py
```

Server will start on `http://localhost:5000`

### 5. Expose with ngrok (for Zapier)

```bash
ngrok http 5000
```

## 📡 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | API documentation |
| `/health` | GET | Health check |
| `/api/diet` | POST | Receive diet data |
| `/api/tasks` | POST | Receive task data |
| `/api/crm` | POST | Receive CRM data |
| `/api/plaud` | POST | Receive complete transcript |

## 🔧 Zapier Configuration

See `COMPLETE_SETUP_GUIDE.md` for detailed Zapier setup instructions.

### Quick Summary:

1. **Trigger**: Plaud - New Transcript
2. **AI Steps**: Extract diet/tasks/CRM data
3. **Loop Steps**: Process multiple items
4. **Webhook Steps**: POST to Python server

## 📊 Database Schema

### Diet Table
- food, food_type, estimated_calories (INT), time_of_day, date

### Tasks Table
- task_name, task_type, responsible_party, status, best_start_date, best_due_date, time_interval, notes, dependency

### CRM Table
- contact_name, company, email, phone, notes, status

## 📚 Documentation

- `COMPLETE_SETUP_GUIDE.md` - Full setup guide
- `ZAPIER_OUTPUT_FIELDS_GUIDE.md` - Zapier configuration
- `zapier_prompts.md` - AI prompts for data extraction
- `QUICK_ANSWERS.md` - FAQ and quick reference

## 🛠️ Development

### Project Structure

```
plaud-integration/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── create_tables.sql              # Database schema
├── zapier_prompts.md              # AI extraction prompts
├── COMPLETE_SETUP_GUIDE.md        # Setup documentation
├── ZAPIER_OUTPUT_FIELDS_GUIDE.md  # Zapier configuration
└── QUICK_ANSWERS.md               # FAQ
```

## 🔒 Security Notes

- **Never commit database credentials** to GitHub
- Use environment variables for sensitive data
- Whitelist IPs in MySQL firewall
- Use HTTPS in production (ngrok provides this)

## 🐛 Troubleshooting

### MySQL Connection Failed
- Check firewall/security group settings
- Verify IP is whitelisted
- Test connection: `mysql -h host -u user -p`

### 404 Error from Webhook
- Verify Flask server is running
- Check ngrok tunnel is active
- Ensure correct endpoint URL

### Data Not Saving
- Check MySQL connection status via `/health` endpoint
- Review server logs for errors
- Verify table structure matches code

## 📈 Performance

- Handles multiple concurrent requests
- Bulk insert operations for efficiency
- ON DUPLICATE KEY UPDATE for idempotency
- Connection pooling ready

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

MIT License - feel free to use this project for your own purposes!

## 👤 Author

Created by Kiran

## 🙏 Acknowledgments

- Plaud for voice recording
- Zapier for automation
- OpenAI for AI extraction
- Flask for web framework

## 📞 Support

For issues or questions:
1. Check the documentation files
2. Review terminal logs
3. Open a GitHub issue

---

**Status**: ✅ Production Ready

Last Updated: October 2025


# Check if Flask is running
ps aux | grep app.py

# View Flask logs
tail -f ~/plaude-integration/flask.log

# Stop Flask
pkill -f app.py

# Start Flask again
cd ~/plaude-integration
source venv/bin/activate
nohup python3 app.py > flask.log 2>&1 &


1. Stop the old Flask server:

pkill -f app.py

2. Verify it's stopped:

ps aux | grep app.py


3. Pull the latest code (you already did this, but let's be sure):

cd ~/plaude-integration
git pull origin main

4. Check what branch you're on:

git branch


5. Check if you have the latest changes:


git log --oneline -5

6. Activate virtual environment:

source venv/bin/activate

7. Start Flask with screen (better than nohup):

screen -S flask
python app.py

8. Detach from screen:
Press Ctrl+A then D
✅ Verify It's Running:

ps aux | grep app.py


🔄 Future Update Workflow
Every Time You Push New Code to GitHub:
Run this simple 5-command sequence on your EC2:

# 1. Stop the old server
pkill -f app.py

# 2. Go to project folder
cd ~/plaude-integration

# 3. Pull latest code from GitHub
git pull origin main

# 4. Activate virtual environment
source venv/bin/activate

# 5. Start server in background
screen -dmS flask python app.py



# Check if Flask is running
ps aux | grep app.py

# View Flask logs (if you used screen)
screen -r flask
# Press Ctrl+A then D to exit without stopping

# Stop Flask manually
pkill -f app.py

# View recent commits
cd ~/plaude-integration
git log --oneline -5

# Check current branch
git branch





