import sqlite3
import pandas as pd

from datetime import date, timedelta

DB = './data/stocks.db'


def create_table():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE stocks (
            symbol VARCHAR(6) NOT NULL,
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
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE stocks')
    conn.close()


def create(symbol, date_, open_, high, low, close, volume):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT OR IGNORE INTO stocks (symbol, date, open, high, low, close, volume)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (symbol, date_, open_, high, low, close, volume))
    conn.commit()
    conn.close()


def bulk_create(data):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.executemany("""
    INSERT OR IGNORE INTO stocks (symbol, date, open, high, low, close, volume)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, data)
    conn.commit()
    conn.close()


def read(symbol, days_delta=9999):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM stocks
    WHERE symbol=? AND date>?
    """, (symbol, date.today() + timedelta(-days_delta)))
    index = []
    data = []
    for row in cursor.fetchall():
        index.append(row[1])
        data.append([row[2], row[3], row[4], row[5], row[6]])
    conn.close()

    return pd.DataFrame(data, index=index,
                        columns=['Open', 'High', 'Low', 'Close', 'Volume'])


def update(symbol, date_, open_, high, low, close, volume):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE stocks
    SET open=?, high=?, low=?, close=?, volume=?
    WHERE symbol=? AND date=?
    """, (open_, high, low, close, volume, symbol, date_))
    conn.commit()
    conn.close()


def delete(symbol, date_):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
    DELETE FROM stocks
    WHERE symbol=? AND date=?
    """, (symbol, date_))
    conn.commit()
    conn.close()


def delete_all():
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM stocks')
    conn.commit()
    conn.close()
