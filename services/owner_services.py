from database import get_db_connection


def get_today_sales():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT IFNULL(SUM(total_amount), 0)
        FROM orders
        WHERE DATE(order_date) = CURDATE()
        AND status = 'Completed'
    """)
    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result


def get_yesterday_sales():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT IFNULL(SUM(total_amount), 0)
        FROM orders
        WHERE DATE(order_date) = CURDATE() - INTERVAL 1 DAY
        AND status = 'Completed'
    """)
    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result


def get_total_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM orders")
    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result


def get_pending_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM orders WHERE status='Pending'")
    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result


def get_completed_orders():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM orders WHERE status='Completed'")
    result = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return result


def get_today_orders():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT * FROM orders
        WHERE DATE(order_date) = CURDATE()
        ORDER BY order_date DESC
    """)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result


def get_food_order_details():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT o.order_id, m.item_name, oi.quantity,
               oi.price, oi.total, o.status, o.order_date
        FROM orders o
        JOIN order_items oi ON o.order_id = oi.order_id
        JOIN menu m ON oi.menu_id = m.menu_id
        ORDER BY o.order_date DESC
    """)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result