# veritabani.py
import sqlite3

def baglanti_kur():
    return sqlite3.connect('toplanti.db')

def tablo_olustur():
    conn = baglanti_kur()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS toplantilar (
            id TEXT PRIMARY KEY,
            tarih TEXT,
            konu TEXT,
            karar TEXT,
            durum TEXT,
            termin TEXT,
            eylem TEXT,
            sorumlu TEXT
        )
    ''')
    conn.commit()
    conn.close()
