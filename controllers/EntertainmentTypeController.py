from config.database import db_connection
from mysql.connector import Error


class EntertainmentTypeController:

    @classmethod
    def index(cls, keyword:str):
        try:
            # Connect to MySQL
            connection = db_connection()

            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                query = "SELECT id, name FROM entertainment_types"

                if keyword:
                    query += " WHERE name LIKE %s OR description LIKE %s"
                    cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
                else:
                    cursor.execute(query)

                rows = cursor.fetchall()

                return rows

        except Error as e:
            print(f"❌ Error while connecting or retrieving data: {e}")

        # Store the entertainment type data
        return query

    @classmethod
    def store(cls, data: dict[str]):

        try:
            # Connect to MySQL
            connection = db_connection()

            if connection.is_connected():
                cursor = connection.cursor()

                insert_statement = "INSERT INTO entertainment_types (name, description) VALUES (%s, %s)"
                val = [
                    (data["name"], data["description"])
                ]

                cursor.executemany(insert_statement, val)

                connection.commit()

        except Error as e:
            print(f"❌ Error while connecting or storing data: {e}")

        print(data)
        # Store the entertainment type data
        return True
