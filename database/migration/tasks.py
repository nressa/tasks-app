from mysql.connector import Error
from config.database import db_connection

try:
    # Connect to MySQL
    connection = db_connection()

    if connection.is_connected():
        cursor = connection.cursor()

        create_table_query = """
        CREATE TABLE IF NOT EXISTS tasks (
            id BIGINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL UNIQUE,
            description VARCHAR(255),
            status ENUM('to do', 'in progress', 'for review', 'done', 'close') NOT NULL DEFAULT 'to do',
            created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
        );
        """

        cursor.execute(create_table_query)
        print("✅ Table 'tasks' created successfully.")

except Error as e:
    print(f"❌ Error while connecting or creating table: {e}")

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("🔌 MySQL connection closed.")
