import sqlite3

def init_db():
    conn = sqlite3.connect('sales.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            branch TEXT NOT NULL,
            item TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            price_per_unit REAL NOT NULL,
            total_price REAL NOT NULL,
            order_date DATE DEFAULT CURRENT_DATE
        )
    ''')
    # Sample data for Pune branch comparison
    sample_sales = [
        ('Hinjewadi', 'Classic Burger', 30, 250.0, 7500.0),
        ('Magarpatta', 'Classic Burger', 20, 250.0, 5000.0),
        ('Baner', 'Classic Burger', 15, 250.0, 3750.0)
    ]
    cursor.executemany('INSERT INTO sales (branch, item, quantity, price_per_unit, total_price) VALUES (?, ?, ?, ?, ?)', sample_sales)
    conn.commit()
    conn.close()
    print("✅ Sales database ready.")

if __name__ == "__main__":
    init_db()