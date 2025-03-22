from config.database import db_connection
from mysql.connector import Error


class EntertainmentTypeController:

    def __init__(self, name):
        self.name = name

    @classmethod
    def store(cls, data):

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
        return True;
