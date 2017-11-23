import sqlite3


def create_table():
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE stocks (
            symbol VARCHAR(5) NOT NULL,
            date VARCHAR(10) NOT NULL,
            open NUMERIC NOT NULL,
            high NUMERIC NOT NULL,
            low NUMERIC NOT NULL,
            close NUMERIC NOT NULL,
            volume NUMERIC NOT NULL,
            PRIMARY KEY (symbol, date)
    );
    """)
    conn.close()


def drop_table():
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE stocks')
    conn.close()


def create(symbol, date, open_, high, low, close, volume):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute("""
    INSERT OR IGNORE INTO stocks (symbol, date, open, high, low, close, volume)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (symbol, date, open_, high, low, close, volume))
    conn.commit()
    conn.close()


def read():
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM stocks;
    """)
    for row in cursor.fetchall():
        print(row)
    conn.close()


def update(symbol, date, open_, high, low, close, volume):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE stocks
    SET open=?, high=?, low=?, close=?, volume=?
    WHERE symbol=? AND date=?
    """, (open_, high, low, close, volume, symbol, date))
    conn.commit()
    conn.close()


def delete(symbol, date):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM stocks
    WHERE symbol=? AND date=?
    """, (symbol, date))
    conn.commit()
    conn.close()


def delete_all():
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM stocks')
    conn.commit()
    conn.close()


create('CRFB3', '2017-10-16', 16.19, 16.37, 15.72, 15.78, 1823800)
create('CRFB3', '2017-10-17', 15.85, 15.99, 15.52, 15.57, 1353700)
update('CRFB3', '2017-10-18', 15.85, 15.99, 15.52, 15.57, 1353701)
# read()
# delete('CRFB3', '2017-10-16')
# delete_all()
read()
