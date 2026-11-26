from database import get_db_connection
def get_all_menu_items():

    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT *
        FROM menu
        WHERE available = 1
    """
    cursor.execute(query)
    menu_items = cursor.fetchall()
    cursor.close()
    connection.close()
    return menu_items
def get_menu_item(menu_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT *
        FROM menu
        WHERE menu_id = %s
    """
    cursor.execute(query, (menu_id,))
    menu_item = cursor.fetchone()
    cursor.close()
    connection.close()
    return menu_item