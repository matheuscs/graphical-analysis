import sqlite3


def _create_table():
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


def _drop_table():
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE stocks')
    conn.close()


def _create(symbol, date, open_, high, low, close, volume):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute("""
    INSERT OR IGNORE INTO stocks (symbol, date, open, high, low, close, volume)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (symbol, date, open_, high, low, close, volume))
    conn.commit()
    conn.close()


def _read():
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM stocks;
    """)
    for row in cursor.fetchall():
        print(row)
    conn.close()


def _update(symbol, date, open_, high, low, close, volume):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE stocks
    SET open=?, high=?, low=?, close=?, volume=?
    WHERE symbol=? AND date=?
    """, (open_, high, low, close, volume, symbol, date))
    conn.commit()
    conn.close()


def _delete(symbol, date):
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM stocks
    WHERE symbol=? AND date=?
    """, (symbol, date))
    conn.commit()
    conn.close()


def _delete_all():
    conn = sqlite3.connect('stocks.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM stocks')
    conn.commit()
    conn.close()
