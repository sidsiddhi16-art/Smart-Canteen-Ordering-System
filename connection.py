import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="1234",
            database="smart_canteen"
        )

        print("Database connected successfully!")
        return connection

    except mysql.connector.Error as error:
        print("Database connection failed:", error)
        return None