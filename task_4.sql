-- Display full description of the 'books' table
-- from the current database without using DESCRIBE or EXPLAIN

SELECT 
    COLUMN_NAME AS 'Column',
    COLUMN_TYPE AS 'Type',
    IS_NULLABLE AS 'Nullable',
    COLUMN_DEFAULT AS 'Default Value',
    COLUMN_KEY AS 'Key',
    EXTRA AS 'Extra'
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE()
  AND TABLE_NAME = 'books'
ORDER BY ORDINAL_POSITION;
