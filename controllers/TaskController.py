from config.database import db_connection
from mysql.connector import Error


class TaskController:

    @classmethod
    def index(cls, keyword: str):
        query = ""

        try:
            # Connect to MySQL
            connection = db_connection()

            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                query = "SELECT id, name, status FROM tasks"

                if keyword:
                    query += " WHERE name LIKE %s OR description LIKE %s ORDER BY id desc"
                    cursor.execute(query, (f"%{keyword}%", f"%{keyword}%"))
                else:
                    cursor.execute(query + " ORDER BY id desc")

                rows = cursor.fetchall()

                return rows

        except Error as e:
            print(f"❌ Error while connecting or retrieving data: {e}")

        return query

    @classmethod
    def store(cls, data: dict[str]):

        try:
            # Connect to MySQL
            connection = db_connection()

            if connection.is_connected():
                cursor = connection.cursor()

                insert_statement = "INSERT INTO tasks (name, description) VALUES (%s, %s)"
                val = [
                    (data["name"], data["description"])
                ]

                cursor.executemany(insert_statement, val)

                connection.commit()

        except Error as e:
            print(f"❌ Error while connecting or storing data: {e}")

        print(data)

        return True

    @classmethod
    def show(cls, task_id: int) -> object:
        try:
            # Connect to MySQL
            connection = db_connection()

            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                query = "SELECT id, name, status, description FROM tasks WHERE id = %s"
                cursor.execute(query, (task_id,))

                task = cursor.fetchone()

                return task

        except Error as e:
            print(f"❌ Error while connecting or retrieving data: {e}")

        return task

    @classmethod
    def update(cls, task_id: int, data: dict) -> bool:
        task = ""

        try:
            # Connect to MySQL
            connection = db_connection()

            if connection.is_connected():
                cursor = connection.cursor(dictionary=True)
                query = """
                    UPDATE tasks
                    SET name = %s,
                        description = %s,
                        status = %s,
                        updated_at = NOW()
                    WHERE id = %s
                """
                values = (data["name"], data["description"], data["status"], task_id)
                cursor.execute(query, values)
                connection.commit()

                return True

        except Error as e:
            print(f"❌ Error while connecting or updating task {task_id} data: {e}")

        return task
