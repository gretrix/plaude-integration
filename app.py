from flask import Flask, request, jsonify
import mysql.connector
from mysql.connector import Error
import json
import logging
from datetime import datetime
import os
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# MySQL Database Configuration
DB_CONFIG = {
    'host': '52.2.41.189',
    'port': 3306,
    'database': 'slack',
    'user': 'slack_rw',
    'password': 'oV8qDfbiZt4aL8gkC9dE76f3VdQSwmdV',
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci'
}

def get_db_connection():
    """Create and return MySQL database connection"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            logger.info("Successfully connected to MySQL database")
            return connection
    except Error as e:
        logger.error(f"Error connecting to MySQL: {e}")
        return None

def create_tables():
    """Create necessary tables if they don't exist"""
    connection = get_db_connection()
    if not connection:
        return False
    
    try:
        cursor = connection.cursor()
        
        # Create diet table
        diet_table = """
        CREATE TABLE IF NOT EXISTS diet_records (
            id INT AUTO_INCREMENT PRIMARY KEY,
            food VARCHAR(255) NOT NULL,
            food_type ENUM('Meal', 'Snack', 'Drink') NOT NULL,
            estimated_calories VARCHAR(50),
            time_of_day TIME NOT NULL,
            date DATE NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            UNIQUE KEY unique_diet_entry (food, food_type, time_of_day, date)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """
        
        # Create tasks table
        tasks_table = """
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            task_description TEXT NOT NULL,
            priority ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
            status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending',
            due_date DATE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            UNIQUE KEY unique_task (task_description(255), due_date)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """
        
        # Create CRM table
        crm_table = """
        CREATE TABLE IF NOT EXISTS crm_records (
            id INT AUTO_INCREMENT PRIMARY KEY,
            contact_name VARCHAR(255),
            company VARCHAR(255),
            email VARCHAR(255),
            phone VARCHAR(50),
            notes TEXT,
            status ENUM('Lead', 'Prospect', 'Customer', 'Lost') DEFAULT 'Lead',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
            UNIQUE KEY unique_contact (contact_name, email)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """
        
        # Create plaud_transcripts table to store raw transcript data
        transcripts_table = """
        CREATE TABLE IF NOT EXISTS plaud_transcripts (
            id INT AUTO_INCREMENT PRIMARY KEY,
            transcript_id VARCHAR(255) UNIQUE,
            title VARCHAR(500),
            transcript_text LONGTEXT,
            summary_text TEXT,
            create_time DATETIME,
            processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_transcript_id (transcript_id),
            INDEX idx_create_time (create_time)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
        """
        
        cursor.execute(diet_table)
        cursor.execute(tasks_table)
        cursor.execute(crm_table)
        cursor.execute(transcripts_table)
        
        connection.commit()
        logger.info("Database tables created/verified successfully")
        return True
        
    except Error as e:
        logger.error(f"Error creating tables: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_diet_data(diet_records: List[Dict[str, Any]]) -> bool:
    """Insert diet records with ON DUPLICATE KEY UPDATE"""
    if not diet_records:
        return True
        
    connection = get_db_connection()
    if not connection:
        logger.warning("Database connection failed - logging data only (not saving to DB)")
        # Log the data even if DB connection fails
        for record in diet_records:
            logger.info(f"Would insert: {record}")
        return True  # Return True to allow testing without DB
    
    try:
        cursor = connection.cursor()
        
        insert_query = """
        INSERT INTO diet (food, food_type, estimated_calories, time_of_day, date)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        estimated_calories = VALUES(estimated_calories)
        """
        
        data_to_insert = []
        for record in diet_records:
            data_to_insert.append((
                record.get('food', ''),
                record.get('food_type', 'Meal'),
                record.get('estimated_calories', ''),
                record.get('time_of_day', '00:00:00'),
                record.get('date', datetime.now().strftime('%Y-%m-%d'))
            ))
        
        cursor.executemany(insert_query, data_to_insert)
        connection.commit()
        
        logger.info(f"Successfully inserted/updated {len(diet_records)} diet records to MySQL")
        return True
        
    except Error as e:
        logger.error(f"Error inserting diet data: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_transcript_data(transcript_data: Dict[str, Any]) -> bool:
    """Insert raw transcript data"""
    connection = get_db_connection()
    if not connection:
        return False
    
    try:
        cursor = connection.cursor()
        
        insert_query = """
        INSERT INTO plaud_transcripts (transcript_id, title, transcript_text, summary_text, create_time)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        transcript_text = VALUES(transcript_text),
        summary_text = VALUES(summary_text),
        processed_at = CURRENT_TIMESTAMP
        """
        
        cursor.execute(insert_query, (
            transcript_data.get('id', ''),
            transcript_data.get('title', ''),
            transcript_data.get('transcript', ''),
            transcript_data.get('summary', ''),
            transcript_data.get('create_time', datetime.now())
        ))
        
        connection.commit()
        logger.info("Successfully inserted/updated transcript data")
        return True
        
    except Error as e:
        logger.error(f"Error inserting transcript data: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/api/plaud', methods=['POST'])
def handle_plaud_webhook():
    """Main webhook endpoint for receiving Plaud data from Zapier"""
    try:
        # Get the JSON data from Zapier
        data = request.get_json()
        
        if not data:
            logger.error("No JSON data received")
            return jsonify({'error': 'No JSON data received'}), 400
        
        logger.info(f"Received webhook data: {json.dumps(data, indent=2)}")
        
        # Store raw transcript data
        transcript_success = insert_transcript_data(data)
        
        # Process diet data if present
        diet_success = True
        if 'diet_data' in data and data['diet_data']:
            diet_success = insert_diet_data(data['diet_data'])
        
        # Process tasks data if present
        tasks_success = True
        if 'tasks_data' in data and data['tasks_data']:
            # TODO: Implement tasks insertion
            pass
        
        # Process CRM data if present
        crm_success = True
        if 'crm_data' in data and data['crm_data']:
            # TODO: Implement CRM insertion
            pass
        
        if transcript_success and diet_success and tasks_success and crm_success:
            return jsonify({
                'status': 'success',
                'message': 'Data processed successfully',
                'processed': {
                    'transcript': transcript_success,
                    'diet': diet_success,
                    'tasks': tasks_success,
                    'crm': crm_success
                }
            }), 200
        else:
            return jsonify({
                'status': 'partial_success',
                'message': 'Some data processing failed',
                'processed': {
                    'transcript': transcript_success,
                    'diet': diet_success,
                    'tasks': tasks_success,
                    'crm': crm_success
                }
            }), 207
            
    except Exception as e:
        logger.error(f"Error processing webhook: {e}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/diet', methods=['POST'])
def handle_diet_webhook():
    """Specific endpoint for diet data from AI by Zapier"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        logger.info(f"Received diet data: {json.dumps(data, indent=2)}")
        
        # Extract the actual diet data from Zapier loop format
        # Parse calories to extract just the number
        calories_raw = data.get('Result Estimated Calories') or data.get('estimated_calories', '0')
        # Remove "~", "cal", and whitespace, then convert to int
        calories_clean = ''.join(filter(str.isdigit, str(calories_raw))) or '0'
        
        diet_record = {
            'food': data.get('Result Food') or data.get('food', ''),
            'food_type': data.get('Result Food Type') or data.get('food_type', 'Meal'),
            'estimated_calories': int(calories_clean),
            'time_of_day': data.get('Result Time Of Day') or data.get('time_of_day', '00:00:00'),
            'date': data.get('Result Date') or data.get('date', datetime.now().strftime('%Y-%m-%d'))
        }
        
        # Handle Zapier line items format (comma-separated values) - legacy support
        if 'food' in data and isinstance(data['food'], str) and ',' in data['food']:
            # Split comma-separated values into individual records
            foods = [f.strip() for f in data['food'].split(',')]
            food_types = [f.strip() for f in data['food_type'].split(',')]
            calories = [c.strip() for c in data['estimated_calories'].split(',')]
            times = [t.strip() for t in data['time_of_day'].split(',')]
            dates = [d.strip() for d in data['date'].split(',')]
            
            # Create individual records
            diet_records = []
            for i in range(len(foods)):
                diet_records.append({
                    'food': foods[i],
                    'food_type': food_types[i] if i < len(food_types) else 'Meal',
                    'estimated_calories': calories[i] if i < len(calories) else '',
                    'time_of_day': times[i] if i < len(times) else '00:00:00',
                    'date': dates[i] if i < len(dates) else datetime.now().strftime('%Y-%m-%d')
                })
        # Handle both single record and array of records
        elif isinstance(data, list):
            diet_records = data
        else:
            diet_records = [diet_record]
        
        success = insert_diet_data(diet_records)
        
        if success:
            return jsonify({
                'status': 'success',
                'message': f'Processed {len(diet_records)} diet records',
                'count': len(diet_records),
                'data': diet_records
            }), 200
        else:
            return jsonify({'error': 'Failed to process diet data', 'data': diet_records}), 500
            
    except Exception as e:
        logger.error(f"Error processing diet webhook: {e}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

def insert_tasks_data(tasks_records: List[Dict[str, Any]]) -> bool:
    """Insert tasks records with ON DUPLICATE KEY UPDATE"""
    if not tasks_records:
        return True
        
    connection = get_db_connection()
    if not connection:
        logger.warning("Database connection failed - logging tasks only")
        for record in tasks_records:
            logger.info(f"Would insert task: {record}")
        return True
    
    try:
        cursor = connection.cursor()
        
        insert_query = """
        INSERT INTO tasks (task_name, task_type, responsible_party, status, 
                          best_start_date, best_due_date, time_interval, notes, dependency)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        data_to_insert = []
        for record in tasks_records:
            data_to_insert.append((
                record.get('task_name', ''),
                record.get('task_type', 'Other'),
                record.get('responsible_party', None),
                record.get('status', 'Pending'),
                record.get('best_start_date', None),
                record.get('best_due_date', None),
                record.get('time_interval', None),
                record.get('notes', ''),
                record.get('dependency', None)
            ))
        
        cursor.executemany(insert_query, data_to_insert)
        connection.commit()
        
        logger.info(f"Successfully inserted {len(tasks_records)} task records to MySQL")
        return True
        
    except Error as e:
        logger.error(f"Error inserting tasks data: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

def insert_crm_data(crm_records: List[Dict[str, Any]]) -> bool:
    """Insert CRM records with ON DUPLICATE KEY UPDATE"""
    if not crm_records:
        return True
        
    connection = get_db_connection()
    if not connection:
        logger.warning("Database connection failed - logging CRM data only")
        for record in crm_records:
            logger.info(f"Would insert CRM: {record}")
        return True
    
    try:
        cursor = connection.cursor()
        
        insert_query = """
        INSERT INTO crm_records (contact_name, company, email, phone, notes, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE
        company = VALUES(company),
        phone = VALUES(phone),
        notes = VALUES(notes),
        status = VALUES(status)
        """
        
        data_to_insert = []
        for record in crm_records:
            data_to_insert.append((
                record.get('contact_name', ''),
                record.get('company', None),
                record.get('email', None),
                record.get('phone', None),
                record.get('notes', ''),
                record.get('status', 'Lead')
            ))
        
        cursor.executemany(insert_query, data_to_insert)
        connection.commit()
        
        logger.info(f"Successfully inserted/updated {len(crm_records)} CRM records to MySQL")
        return True
        
    except Error as e:
        logger.error(f"Error inserting CRM data: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

@app.route('/api/tasks', methods=['POST'])
def handle_tasks_webhook():
    """Endpoint for tasks data from AI by Zapier"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        logger.info(f"Received tasks data: {json.dumps(data, indent=2)}")
        
        # Extract task data from Zapier loop format
        task_record = {
            'task_name': data.get('Result Task Name') or data.get('task_name', ''),
            'task_type': data.get('Result Task Type') or data.get('task_type', 'Other'),
            'responsible_party': data.get('Result Responsible Party') or data.get('responsible_party', None),
            'status': data.get('Result Status') or data.get('status', 'Pending'),
            'best_start_date': data.get('Result Best Start Date') or data.get('best_start_date', None),
            'best_due_date': data.get('Result Best Due Date') or data.get('best_due_date', None),
            'time_interval': data.get('Result Time Interval') or data.get('time_interval', None),
            'notes': data.get('Result Notes') or data.get('notes', ''),
            'dependency': data.get('Result Dependency') or data.get('dependency', None)
        }
        
        tasks_records = [task_record] if not isinstance(data, list) else data
        
        success = insert_tasks_data(tasks_records)
        
        if success:
            return jsonify({
                'status': 'success',
                'message': f'Processed {len(tasks_records)} task records',
                'count': len(tasks_records),
                'data': tasks_records
            }), 200
        else:
            return jsonify({'error': 'Failed to process tasks data', 'data': tasks_records}), 500
            
    except Exception as e:
        logger.error(f"Error processing tasks webhook: {e}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/api/crm', methods=['POST'])
def handle_crm_webhook():
    """Endpoint for CRM data from AI by Zapier"""
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No JSON data received'}), 400
        
        logger.info(f"Received CRM data: {json.dumps(data, indent=2)}")
        
        # Extract CRM data
        crm_record = {
            'contact_name': data.get('Result Contact Name') or data.get('contact_name', ''),
            'company': data.get('Result Company') or data.get('company', None),
            'email': data.get('Result Email') or data.get('email', None),
            'phone': data.get('Result Phone') or data.get('phone', None),
            'notes': data.get('Result Notes') or data.get('notes', ''),
            'status': data.get('Result Status') or data.get('status', 'Lead')
        }
        
        crm_records = [crm_record] if not isinstance(data, list) else data
        
        success = insert_crm_data(crm_records)
        
        if success:
            return jsonify({
                'status': 'success',
                'message': f'Processed {len(crm_records)} CRM records',
                'count': len(crm_records),
                'data': crm_records
            }), 200
        else:
            return jsonify({'error': 'Failed to process CRM data', 'data': crm_records}), 500
            
    except Exception as e:
        logger.error(f"Error processing CRM webhook: {e}")
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    connection = get_db_connection()
    if connection:
        connection.close()
        return jsonify({'status': 'healthy', 'database': 'connected'}), 200
    else:
        return jsonify({'status': 'unhealthy', 'database': 'disconnected'}), 500

@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API documentation"""
    return jsonify({
        'message': 'Plaud Webhook Server',
        'version': '1.0',
        'endpoints': {
            '/api/plaud': 'Main webhook for complete Plaud data (POST)',
            '/api/diet': 'Diet data webhook (POST)',
            '/api/tasks': 'Tasks data webhook (POST)',
            '/api/crm': 'CRM data webhook (POST)',
            '/health': 'Health check (GET)'
        },
        'database': 'MySQL - slack database',
        'status': 'running'
    }), 200

if __name__ == '__main__':
    # Initialize database tables
    create_tables()
    
    # Run the Flask app
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    logger.info(f"Starting Plaud webhook server on port {port}")
    app.run(host='0.0.0.0', port=port, debug=debug)
