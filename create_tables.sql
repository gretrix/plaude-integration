-- Create all necessary tables for Plaud integration
-- Run this in your MySQL database

USE slack;

-- =====================================================
-- DIET TABLE (Updated with numeric calories)
-- =====================================================
CREATE TABLE IF NOT EXISTS diet (
    id INT AUTO_INCREMENT PRIMARY KEY,
    food VARCHAR(255) NOT NULL,
    food_type ENUM('Meal', 'Snack', 'Drink') NOT NULL,
    estimated_calories INT,  -- Changed to INT for math operations
    time_of_day TIME NOT NULL,
    date DATE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    UNIQUE KEY unique_diet_entry (food, food_type, time_of_day, date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================
-- TASKS TABLE
-- =====================================================
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task_description TEXT NOT NULL,
    priority ENUM('Low', 'Medium', 'High') DEFAULT 'Medium',
    status ENUM('Pending', 'In Progress', 'Completed', 'Cancelled') DEFAULT 'Pending',
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_status (status),
    INDEX idx_due_date (due_date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================
-- CRM TABLE
-- =====================================================
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
    UNIQUE KEY unique_contact (contact_name, email),
    INDEX idx_status (status),
    INDEX idx_company (company)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================
-- PLAUD TRANSCRIPTS TABLE (for raw data backup)
-- =====================================================
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- =====================================================
-- If diet table already exists, update calories column
-- =====================================================
-- Uncomment these lines if you need to update existing table:
-- ALTER TABLE diet MODIFY COLUMN estimated_calories INT;
-- UPDATE diet SET estimated_calories = CAST(REPLACE(REPLACE(estimated_calories, '~', ''), ' cal', '') AS UNSIGNED) WHERE estimated_calories IS NOT NULL;

-- Show all tables
SHOW TABLES;

-- Show structure of each table
DESCRIBE diet;
DESCRIBE tasks;
DESCRIBE crm_records;
DESCRIBE plaud_transcripts;

