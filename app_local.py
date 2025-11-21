from flask import Flask, request, jsonify, render_template
import json
import logging
from datetime import datetime
import os
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# Mock data for local testing
MOCK_STATS = {
    'calories_today': 1850,
    'pending_tasks': 5,
    'total_contacts': 12,
    'total_diet_entries': 45,
    'total_tasks': 15
}

MOCK_DIET = [
    {'id': 1, 'food': 'Chicken Salad', 'food_type': 'Meal', 'estimated_calories': 450, 'time_of_day': '12:30:00', 'date': '2025-11-20', 'created_at': datetime.now()},
    {'id': 2, 'food': 'Apple', 'food_type': 'Snack', 'estimated_calories': 95, 'time_of_day': '15:00:00', 'date': '2025-11-20', 'created_at': datetime.now()},
    {'id': 3, 'food': 'Coffee', 'food_type': 'Drink', 'estimated_calories': 5, 'time_of_day': '08:00:00', 'date': '2025-11-20', 'created_at': datetime.now()},
    {'id': 4, 'food': 'Grilled Salmon', 'food_type': 'Meal', 'estimated_calories': 550, 'time_of_day': '19:00:00', 'date': '2025-11-20', 'created_at': datetime.now()},
    {'id': 5, 'food': 'Protein Shake', 'food_type': 'Drink', 'estimated_calories': 200, 'time_of_day': '10:00:00', 'date': '2025-11-20', 'created_at': datetime.now()},
]

MOCK_TASKS = [
    {'id': 1, 'task_name': 'Review Q4 budget proposal', 'task_type': 'Meeting', 'status': 'Pending', 'responsible_party': 'John', 'priority': 1, 'best_due_date': '2025-11-25', 'best_start_date': '2025-11-22', 'notes': 'Prepare slides', 'dependency': None, 'created_at': datetime.now()},
    {'id': 2, 'task_name': 'Call vendor about pricing', 'task_type': 'Call', 'status': 'In Progress', 'responsible_party': 'Sarah', 'priority': 2, 'best_due_date': '2025-11-21', 'best_start_date': '2025-11-20', 'notes': 'Negotiate better rates', 'dependency': None, 'created_at': datetime.now()},
    {'id': 3, 'task_name': 'Send follow-up email to client', 'task_type': 'Email', 'status': 'Completed', 'responsible_party': 'Mike', 'priority': 5, 'best_due_date': '2025-11-19', 'best_start_date': '2025-11-18', 'notes': 'Include proposal', 'dependency': None, 'created_at': datetime.now()},
    {'id': 4, 'task_name': 'Update project documentation', 'task_type': 'Other', 'status': 'Pending', 'responsible_party': 'Lisa', 'priority': 3, 'best_due_date': '2025-11-30', 'best_start_date': '2025-11-25', 'notes': 'Add API specs', 'dependency': None, 'created_at': datetime.now()},
    {'id': 5, 'task_name': 'Schedule team meeting', 'task_type': 'Meeting', 'status': 'Pending', 'responsible_party': 'John', 'priority': 1, 'best_due_date': '2025-11-22', 'best_start_date': '2025-11-21', 'notes': 'Discuss roadmap', 'dependency': None, 'created_at': datetime.now()},
]

MOCK_CONTACTS = [
    {'id': 1, 'contact_name': 'Alice Johnson', 'company': 'Tech Corp', 'email': 'alice@techcorp.com', 'phone': '555-0101', 'status': 'Customer', 'notes': 'Key decision maker', 'created_at': datetime.now()},
    {'id': 2, 'contact_name': 'Bob Smith', 'company': 'StartupXYZ', 'email': 'bob@startupxyz.com', 'phone': '555-0102', 'status': 'Prospect', 'notes': 'Interested in enterprise plan', 'created_at': datetime.now()},
    {'id': 3, 'contact_name': 'Carol White', 'company': 'Design Studio', 'email': 'carol@designstudio.com', 'phone': '555-0103', 'status': 'Lead', 'notes': 'Met at conference', 'created_at': datetime.now()},
    {'id': 4, 'contact_name': 'David Brown', 'company': 'Consulting Inc', 'email': 'david@consulting.com', 'phone': '555-0104', 'status': 'Customer', 'notes': 'Long-term client', 'created_at': datetime.now()},
    {'id': 5, 'contact_name': 'Emma Davis', 'company': 'Marketing Pro', 'email': 'emma@marketingpro.com', 'phone': '555-0105', 'status': 'Prospect', 'notes': 'Needs demo', 'created_at': datetime.now()},
]

@app.route('/')
def dashboard():
    """Web dashboard homepage"""
    return render_template('dashboard.html', 
                         stats=MOCK_STATS,
                         recent_diet=MOCK_DIET[:5],
                         recent_tasks=MOCK_TASKS[:5],
                         recent_contacts=MOCK_CONTACTS[:5])

@app.route('/diet')
def diet_page():
    """Diet tracking page"""
    date_filter = request.args.get('date')
    return render_template('diet.html', records=MOCK_DIET, date_filter=date_filter)

@app.route('/tasks')
def tasks_page():
    """Tasks management page"""
    status_filter = request.args.get('status')
    return render_template('tasks.html', tasks=MOCK_TASKS, status_filter=status_filter)

@app.route('/crm')
def crm_page():
    """CRM contacts page"""
    search_query = request.args.get('search')
    return render_template('crm.html', contacts=MOCK_CONTACTS, search_query=search_query)

@app.route('/api')
def api_home():
    """API documentation page"""
    return render_template('api.html')

@app.route('/health')
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'mode': 'local_development',
        'database': 'mock_data'
    }), 200

@app.route('/api/tasks/<int:task_id>/status', methods=['PATCH'])
def update_task_status(task_id):
    """Update task status (for checkbox toggle)"""
    try:
        data = request.get_json()
        
        if not data or 'status' not in data:
            return jsonify({'error': 'Status is required'}), 400
        
        new_status = data['status']
        
        # Find and update mock task
        for task in MOCK_TASKS:
            if task['id'] == task_id:
                task['status'] = new_status
                logger.info(f"Updated task {task_id} status to {new_status}")
                return jsonify({
                    'status': 'success',
                    'message': f'Task status updated to {new_status}',
                    'task_id': task_id,
                    'new_status': new_status
                }), 200
        
        return jsonify({'error': 'Task not found'}), 404
    
    except Exception as e:
        logger.error(f"Error in update_task_status: {e}")
        return jsonify({'error': 'Internal server error'}), 500

@app.route('/api/tasks/<int:task_id>/priority', methods=['PATCH'])
def update_task_priority(task_id):
    """Update task priority"""
    try:
        data = request.get_json()
        
        if not data or 'priority' not in data:
            return jsonify({'error': 'Priority is required'}), 400
        
        new_priority = data['priority']
        
        # Validate priority
        if new_priority is not None and (new_priority < 1 or new_priority > 99):
            return jsonify({'error': 'Priority must be between 1 and 99'}), 400
        
        # Find and update mock task
        for task in MOCK_TASKS:
            if task['id'] == task_id:
                task['priority'] = new_priority
                logger.info(f"Updated task {task_id} priority to {new_priority}")
                return jsonify({
                    'status': 'success',
                    'message': f'Task priority updated to {new_priority}',
                    'task_id': task_id,
                    'new_priority': new_priority
                }), 200
        
        return jsonify({'error': 'Task not found'}), 404
    
    except Exception as e:
        logger.error(f"Error in update_task_priority: {e}")
        return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    
    logger.info("=" * 60)
    logger.info("🚀 Starting Plaud Integration - LOCAL DEV MODE")
    logger.info("=" * 60)
    logger.info(f"📍 Server running on: http://localhost:{port}")
    logger.info("📊 Using mock data (no database connection)")
    logger.info("🎨 New modern design implemented!")
    logger.info("=" * 60)
    
    app.run(host='127.0.0.1', port=port, debug=True)
