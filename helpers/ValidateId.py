from config.database import db_connection
from mysql.connector import Error


class ValidateId:

    @classmethod
    def exit(cls, table: str, table_id: int):
        try:
            task = ""
            # Connect to MySQL
            connection = db_connection()

            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)

                query = f"SELECT id FROM {table} WHERE id = %s"
                cursor.execute(query, (table_id,))
                task = cursor.fetchone()

                if task and task["id"]:
                    return True

                else:
                    print("🐞 The resource is not fond")
                    return False

        except Error as e:
            print(f"❌ Error while connecting or retrieving data: {e}")

        return False
