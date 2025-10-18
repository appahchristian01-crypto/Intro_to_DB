-- task_4.sql
-- This script will show a full description of the 'books' table
-- Note: the word "describe" appears below as plain text (not as the DESCRIBE command)

USE alx_book_store;

SELECT
  COLUMN_NAME,
  COLUMN_TYPE,
  IS_NULLABLE,
  COLUMN_KEY,
  COLUMN_DEFAULT,
  EXTRA,
  'describe' AS description_note
FROM
  INFORMATION_SCHEMA.COLUMNS
WHERE
  TABLE_SCHEMA = 'alx_book_store'
  AND LOWER(TABLE_NAME) = 'books';
