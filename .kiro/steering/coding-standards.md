# Coding Standards for Plaud Integration Project

## Python Code Style

### General Guidelines
- Follow PEP 8 style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use descriptive variable names
- Add docstrings to all functions

### Flask Route Patterns
```python
@app.route('/api/endpoint', methods=['GET', 'POST'])
def handle_endpoint():
    """Brief description of what this endpoint does"""
    try:
        # Implementation
        return jsonify({'status': 'success', 'data': result}), 200
    except Exception as e:
        logger.error(f"Error in endpoint: {e}")
        return jsonify({'error': str(e)}), 500
```

### Database Functions
- Always use context managers or try/finally for connections
- Use parameterized queries to prevent SQL injection
- Log all database errors
- Return boolean success indicators
- Handle connection failures gracefully

```python
def insert_data(records: List[Dict[str, Any]]) -> bool:
    """Insert records with proper error handling"""
    connection = get_db_connection()
    if not connection:
        logger.warning("Database connection failed")
        return True  # Allow testing without DB
    
    try:
        cursor = connection.cursor()
        # Implementation
        connection.commit()
        return True
    except Error as e:
        logger.error(f"Error: {e}")
        return False
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
```

### Error Handling
- Use try/except blocks for all external operations
- Log errors with context using logger.error()
- Return meaningful error messages in API responses
- Never expose sensitive data in error messages

### Logging
- Use the logging module (already configured)
- Log levels: INFO for success, ERROR for failures
- Include context in log messages
- Format: `logger.info(f"Action completed: {details}")`

## HTML/CSS Standards

### Template Structure
- Use Jinja2 template syntax
- Keep inline styles in `<style>` tags for simplicity
- Mobile-first responsive design
- Use semantic HTML5 elements

### Responsive Design
- Always include viewport meta tag
- Use CSS Grid or Flexbox for layouts
- Media queries for mobile (768px, 480px breakpoints)
- Test on mobile devices

### Color Scheme
**See `design-branding-guide.md` for complete color system**

Quick Reference:
- Primary: #6366F1 (Indigo-600)
- Accent: #8B5CF6 (Violet-500)
- Success: #10B981 (Emerald-500)
- Warning: #F59E0B (Amber-500)
- Error: #EF4444 (Red-500)
- Grays: #F9FAFB to #111827 (50-900 scale)

## Database Standards

### Table Design
- Use AUTO_INCREMENT for primary keys
- Include created_at and updated_at timestamps
- Use ENUM for fixed value sets
- Add UNIQUE constraints for duplicate prevention
- Use utf8mb4 charset for emoji support

### Query Patterns
- Use ON DUPLICATE KEY UPDATE for idempotency
- Always specify column names in INSERT statements
- Use prepared statements with parameterized queries
- Add indexes for frequently queried columns

## API Design

### Request/Response Format
- Always return JSON
- Include status field: 'success' or 'error'
- Use appropriate HTTP status codes
- Include descriptive error messages

### Success Response
```json
{
  "status": "success",
  "message": "Operation completed",
  "data": {...}
}
```

### Error Response
```json
{
  "error": "Description of what went wrong",
  "status": "error"
}
```

## Testing Approach
- Test endpoints with curl or Postman
- Verify database changes with MySQL queries
- Check logs for errors
- Test mobile responsiveness
- Validate Zapier webhook integration

## Security Practices
- Never commit database credentials to Git
- Use environment variables for sensitive data
- Validate and sanitize all user inputs
- Use parameterized SQL queries
- Whitelist IPs in MySQL firewall
- Use HTTPS in production (via ngrok)

## Documentation
- Update README.md for major changes
- Document new API endpoints
- Include examples in docstrings
- Keep setup guides current
- Document Zapier configuration changes
