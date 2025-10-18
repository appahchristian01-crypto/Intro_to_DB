"""
MySQLServer.py
Simple script to create the alx_book_store database in MySQL.
Replace the connection values (HOST, USER, PASSWORD) with yours.
"""

import mysql.connector
from mysql.connector import Error

# --- CONFIG: change these to match your MySQL server ---
HOST = "localhost"      # usually "localhost" for local installs
USER = "root"           # your MySQL username
PASSWORD = "your_pass"  # your MySQL password
# ------------------------------------------------------

def create_database():
    conn = None
    cursor = None
    try:
        # 1) Connect to MySQL server (no specific database required)
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="papaboaz2020"
        )

        if conn.is_connected():
            # 2) Create a cursor to run SQL statements
            cursor = conn.cursor()

            # 3) Execute CREATE DATABASE with IF NOT EXISTS so it won't fail if the DB exists
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            # 4) (Optional) commit changes (DDL is auto-committed but safe to call)
            conn.commit()

            # 5) Print success message
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        # Print errors related to connection or SQL execution
        print("Error: Could not connect to MySQL server or execute statement.")
        print("MySQL Error message:", e)

    finally:
        # 6) Close cursor and connection if they were opened
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database()
