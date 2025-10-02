-- Update the calories column to be a number instead of string
-- Run this in your MySQL database

USE slack;

-- First, let's see the current structure
DESCRIBE diet;

-- Modify the estimated_calories column to be an integer
ALTER TABLE diet 
MODIFY COLUMN estimated_calories INT;

-- Verify the change
DESCRIBE diet;

-- Optional: Update any existing string values to numbers
-- This removes "~" and " cal" from existing data
UPDATE diet 
SET estimated_calories = 
    CAST(REPLACE(REPLACE(estimated_calories, '~', ''), ' cal', '') AS UNSIGNED)
WHERE estimated_calories IS NOT NULL;

