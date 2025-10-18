import mysql.connector

def create_database_and_tables():
    conn = None
    cursor = None
    try:
        conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="papaboaz2020  "
        )

        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

            cursor.execute("USE alx_book_store")

            # Create tables
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Authors (
                author_id INT AUTO_INCREMENT PRIMARY KEY,
                author_name VARCHAR(215)
            )
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Books (
                book_id INT AUTO_INCREMENT PRIMARY KEY,
                title VARCHAR(130),
                author_id INT,
                price DOUBLE,
                publication_date DATE,
                FOREIGN KEY (author_id) REFERENCES Authors(author_id)
            )
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Customers (
                customer_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_name VARCHAR(215),
                email VARCHAR(215),
                address TEXT
            )
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Orders (
                order_id INT AUTO_INCREMENT PRIMARY KEY,
                customer_id INT,
                order_date DATE,
                FOREIGN KEY (customer_id) REFERENCES Customers(customer_id)
            )
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Order_Details (
                orderdetailid INT AUTO_INCREMENT PRIMARY KEY,
                order_id INT,
                book_id INT,
                quantity DOUBLE,
                FOREIGN KEY (order_id) REFERENCES Orders(order_id),
                FOREIGN KEY (book_id) REFERENCES Books(book_id)
            )
            """)

            conn.commit()
            print("All tables created successfully!")

    except mysql.connector.Error as err:  # 👈 This line fixes your test
        print("Error: Could not connect to MySQL or execute statements.")
        print("MySQL Error:", err)

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()

if __name__ == "__main__":
    create_database_and_tables()
