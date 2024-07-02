import sqlite3

def clear_transactions_table():
    conn = sqlite3.connect('finance.db')
    c = conn.cursor()
    
    # Clear the transactions table
    c.execute('DELETE FROM transactions')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

if __name__ == '__main__':
    clear_transactions_table()
    print("All records in the 'transactions' table have been cleared.")
