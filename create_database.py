import sqlite3
import pandas as pd
from datetime import datetime, timedelta
import random

# Connect to (or create) the database file
conn = sqlite3.connect('sales.db')
cursor = conn.cursor()

# 1. Create a table for Daily Sales
cursor.execute('''
    CREATE TABLE IF NOT EXISTS daily_sales (
        order_date DATE,
        store_location TEXT,
        product_name TEXT,
        category TEXT,
        units_sold INTEGER,
        revenue REAL,
        promotion_active BOOLEAN
    )
''')

# 2. Generate Realistic Sample Data (Last 30 days)
products = [
    ('Classic Burger', 'Main'), ('Cheeseburger', 'Main'), 
    ('French Fries', 'Side'), ('Soft Drink', 'Beverage'),
    ('Chicken Wrap', 'Main'), ('Ice Cream', 'Dessert')
]
locations = ['Pune-Baner', 'Pune-Hinjewadi', 'Mumbai-Andheri']

data = []
start_date = datetime.now() - timedelta(days=30)

for i in range(100):
    date = start_date + timedelta(days=random.randint(0, 30))
    prod = random.choice(products)
    loc = random.choice(locations)
    units = random.randint(10, 100)
    rev = units * random.uniform(5.0, 15.0)
    promo = random.choice([True, False])
    data.append((date.strftime('%Y-%m-%d'), loc, prod[0], prod[1], units, round(rev, 2), promo))

# 3. Load data into SQL
cursor.executemany('INSERT INTO daily_sales VALUES (?, ?, ?, ?, ?, ?, ?)', data)
conn.commit()

# Verify by printing total rows
cursor.execute("SELECT COUNT(*) FROM daily_sales")
print(f"Database created! Total sales records added: {cursor.fetchone()[0]}")

conn.close()