
import os
import mysql.connector


def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME", "smart_canteen"),
            port=int(os.getenv("DB_PORT", "4000")),
            ssl_ca=os.getenv("SSL_CA"),
            ssl_verify_cert=True,
            ssl_verify_identity=True
        )

        print("Database connected successfully!")
        return connection

    except mysql.connector.Error as error:
        print("Database connection failed:", error)
        return None
