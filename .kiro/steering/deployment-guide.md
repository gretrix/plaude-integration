# Deployment and Update Guide

## Local Development Setup

### Prerequisites
```bash
# Install Python 3.8+
python --version

# Install dependencies
pip install -r requirements.txt

# Configure database credentials in app.py
# Update DB_CONFIG dictionary
```

### Running Locally
```bash
# Start Flask server
python app.py

# In another terminal, start ngrok
ngrok http 5000

# Use ngrok URL in Zapier webhooks
```

## EC2 Deployment

### Server Details
- **IP**: 98.82.115.184
- **User**: ubuntu
- **Project Path**: ~/plaude-integration
- **Python**: Python 3.x with venv

### SSH Access
```bash
ssh ubuntu@98.82.115.184
```

### Standard Update Workflow

Every time you push new code to GitHub, run these commands on EC2:

```bash
# 1. Stop the old server
pkill -f app.py

# 2. Navigate to project folder
cd ~/plaude-integration

# 3. Pull latest code from GitHub
git pull origin main

# 4. Activate virtual environment
source venv/bin/activate

# 5. Start server in background
screen -dmS flask python app.py
```

### Verify Deployment
```bash
# Check if Flask is running
ps aux | grep app.py

# View Flask logs (if using screen)
screen -r flask
# Press Ctrl+A then D to exit without stopping

# Test health endpoint
curl http://localhost:5000/health
```

### Troubleshooting

#### Server Not Starting
```bash
# Check for port conflicts
lsof -i :5000

# View recent logs
tail -f ~/plaude-integration/flask.log

# Check Python errors
python app.py  # Run in foreground to see errors
```

#### Database Connection Issues
```bash
# Test MySQL connection
mysql -h 52.2.41.189 -u slack_rw -p slack

# Check firewall rules
# Verify IP 115.98.213.83 is whitelisted

# Test from Python
python -c "import mysql.connector; print('OK')"
```

#### Git Pull Conflicts
```bash
# Stash local changes
git stash

# Pull latest
git pull origin main

# Reapply changes if needed
git stash pop
```

## Process Management

### Using screen (Recommended)
```bash
# Start new screen session
screen -S flask
python app.py
# Press Ctrl+A then D to detach

# List sessions
screen -ls

# Reattach to session
screen -r flask

# Kill session
screen -X -S flask quit
```

### Using nohup (Alternative)
```bash
# Start in background
nohup python app.py > flask.log 2>&1 &

# View logs
tail -f flask.log

# Stop process
pkill -f app.py
```

## Database Updates

### Running SQL Scripts
```bash
# Connect to MySQL
mysql -h 52.2.41.189 -u slack_rw -p slack

# Run SQL file
mysql -h 52.2.41.189 -u slack_rw -p slack < create_tables.sql

# Or run inline
mysql -h 52.2.41.189 -u slack_rw -p slack -e "SHOW TABLES;"
```

### Schema Changes
1. Test SQL locally first
2. Backup data if modifying existing tables
3. Run ALTER TABLE statements
4. Update app.py if column names change
5. Restart Flask server

## Monitoring

### Health Checks
```bash
# Check server health
curl http://98.82.115.184:5000/health

# Check API endpoints
curl http://98.82.115.184:5000/api

# View recent diet entries
curl http://98.82.115.184:5000/api/diet?limit=5
```

### Log Monitoring
```bash
# Watch logs in real-time
tail -f flask.log

# Search for errors
grep ERROR flask.log

# View last 50 lines
tail -50 flask.log
```

## Rollback Procedure

If deployment fails:

```bash
# 1. Stop current server
pkill -f app.py

# 2. Revert to previous commit
git log --oneline -5  # Find previous commit
git checkout <commit-hash>

# 3. Restart server
source venv/bin/activate
screen -dmS flask python app.py

# 4. Verify
curl http://localhost:5000/health
```

## Zapier Configuration

### Updating Webhook URLs
1. Get ngrok URL (for testing) or EC2 IP (for production)
2. Update webhook URLs in Zapier:
   - Diet: `http://your-url/api/diet`
   - Tasks: `http://your-url/api/tasks`
   - CRM: `http://your-url/api/crm`
3. Test with Zapier's "Test" button
4. Check Flask logs for incoming requests

### Testing Zapier Integration
1. Record a test transcript in Plaud
2. Check Zapier task history
3. Verify data in MySQL
4. Check Flask logs for webhook calls

## Security Checklist

- [ ] Database credentials not in Git
- [ ] IP whitelisted in MySQL
- [ ] Flask running on correct port
- [ ] ngrok HTTPS for webhooks
- [ ] Logs don't contain sensitive data
- [ ] Error messages don't expose internals

## Performance Optimization

### Database
- Use connection pooling for high traffic
- Add indexes on frequently queried columns
- Use LIMIT in queries to prevent large result sets

### Flask
- Enable production mode (debug=False)
- Use gunicorn for production WSGI server
- Consider caching for dashboard stats

## Backup Strategy

### Database Backups
```bash
# Backup entire database
mysqldump -h 52.2.41.189 -u slack_rw -p slack > backup_$(date +%Y%m%d).sql

# Backup specific table
mysqldump -h 52.2.41.189 -u slack_rw -p slack diet > diet_backup.sql

# Restore from backup
mysql -h 52.2.41.189 -u slack_rw -p slack < backup.sql
```

### Code Backups
- All code is in GitHub (primary backup)
- EC2 has local copy
- Keep local development copy synced
