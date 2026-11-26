from database import get_db_connection
def create_order(user_id, menu_id, quantity):
    connection = get_db_connection()
    cursor = connection.cursor()
    # Get food price
    query = """
        SELECT price
        FROM menu
        WHERE menu_id = %s
    """
    cursor.execute(query, (menu_id,))
    item = cursor.fetchone()
    if item is None:
        cursor.close()
        connection.close()
        return False
    price = item[0]
    total_price = price * quantity
    # Insert order
    query = """
        INSERT INTO orders
        (user_id, menu_id, quantity, total_price, status)
        VALUES (%s, %s, %s, %s, %s)
    """
    values = (
        user_id,
        menu_id,
        quantity,
        total_price,
        "Pending"
    )
    cursor.execute(query, values)
    connection.commit()
    cursor.close()
    connection.close()
    return True
def get_user_orders(user_id):
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT
            orders.order_id,
            menu.item_name,
            orders.quantity,
            orders.total_price,
            orders.status
        FROM orders
        INNER JOIN menu
        ON orders.menu_id = menu.menu_id
        WHERE orders.user_id = %s
        ORDER BY orders.order_id DESC
    """
    cursor.execute(query, (user_id,))
    orders = cursor.fetchall()
    cursor.close()
    connection.close()
    return orders
def update_order_status(order_id, status):
    connection = get_db_connection()
    cursor = connection.cursor()
    query = """
        UPDATE orders
        SET status = %s
        WHERE order_id = %s
    """
    cursor.execute(
        query,
        (status, order_id)
    )
    connection.commit()
    cursor.close()
    connection.close()
    return True