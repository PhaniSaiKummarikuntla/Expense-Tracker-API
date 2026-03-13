from .database import get_connection


def add_expense(amount, category, date):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO expenses (amount, category, date) VALUES (?, ?, ?)",
        (amount, category, date)
    )

    conn.commit()
    conn.close()


def get_all_expenses():

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM expenses")

    rows = cursor.fetchall()

    conn.close()

    return rows


def delete_expense(expense_id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM expenses WHERE id=?", (expense_id,))

    conn.commit()
    conn.close()