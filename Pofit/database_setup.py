import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('finance.db')
c = conn.cursor()

# Create a table for transactions
c.execute('''
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    type TEXT NOT NULL,
    amount REAL NOT NULL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
)
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
