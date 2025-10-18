-- Displays the full description of the table books
-- from a database passed as an argument
-- without using DESCRIBE or EXPLAIN

SELECT 
    COLUMN_NAME AS 'COLUMN',
    COLUMN_TYPE AS 'TYPE',
    IS_NULLABLE AS 'NULLABLE',
    COLUMN_DEFAULT AS 'DEFAULT VALUE',
    COLUMN_KEY AS 'KEY',
    EXTRA AS 'EXTRA'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'books'
ORDER BY ORDINAL_POSITION;
