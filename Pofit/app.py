from flask import Flask, request, render_template, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('finance.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    transactions = conn.execute('SELECT * FROM transactions').fetchall()
    conn.close()

    total_deposit = sum([tx['amount'] for tx in transactions if tx['type'] == 'deposit'])
    total_withdrawal = sum([tx['amount'] for tx in transactions if tx['type'] == 'withdrawal'])
    profit = total_withdrawal - total_deposit

    return render_template('index.html', transactions=transactions, profit=profit)

@app.route('/transaction', methods=['POST'])
def transaction():
    type = request.form['type']
    amount = float(request.form['amount'])

    conn = get_db_connection()
    conn.execute('INSERT INTO transactions (type, amount) VALUES (?, ?)', (type, amount))
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

@app.route('/clear', methods=['POST'])
def clear_transactions():
    conn = get_db_connection()
    conn.execute('DELETE FROM transactions')
    conn.execute('DELETE FROM sqlite_sequence WHERE name="transactions"')  # Reset the auto-increment counter
    conn.commit()
    conn.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
