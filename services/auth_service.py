from database import get_db_connection
def register_user(name, email, password):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        INSERT INTO users (full_name, email, password, role)
        VALUES (%s, %s, %s, %s)
    """
    values = (
        name,
        email,
        password,
        "customer"
    )
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return True
def login_user(email, password):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT *
        FROM users
        WHERE email = %s AND password = %s
    """
    values = (
        email,
        password
    )
    cursor.execute(query, values)
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user