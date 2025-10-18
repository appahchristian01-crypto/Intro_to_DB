cat > task_4.sql <<'SQL'
-- task_4.sql
-- Print the full description of the table books from the alx_book_store database
-- Do NOT use DESCRIBE, EXPLAIN, or ANALYZE

SELECT
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_KEY,
    COLUMN_DEFAULT,
    EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = 'alx_book_store'
  AND TABLE_NAME = 'books';
SQL
