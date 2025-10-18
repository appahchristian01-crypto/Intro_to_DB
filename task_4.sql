-- task_4.sql
-- Print the full description of the 'books' table in alx_book_store
-- WITHOUT using DESCRIBE, EXPLAIN, or ANALYZE

USE alx_book_store;

SELECT
  COLUMN_NAME,
  COLUMN_TYPE,
  IS_NULLABLE,
  COLUMN_KEY,
  COLUMN_DEFAULT,
  EXTRA
FROM
  INFORMATION_SCHEMA.COLUMNS
WHERE
  TABLE_SCHEMA = 'alx_book_store'
  AND LOWER(TABLE_NAME) = 'books';
