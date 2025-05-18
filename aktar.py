import pandas as pd
import sqlite3

EXCEL_DOSYA = 'haftalik_toplanti_takip.xlsx'
DB_DOSYA = 'toplanti.db'

# Excel dosyasını oku
df = pd.read_excel(EXCEL_DOSYA)

# Kolon isimlerini temizle
df.columns = [col.strip() for col in df.columns]

# Gerekli kolonlar
gereken_kolonlar = [
    'ID', 'Toplantı Tarihi', 'Konu', 'Karar', 'Durum',
    'Termin', 'Eylem Öğeleri', 'Sorumlu'
]

# Eksik kolon varsa doldur
for kolon in gereken_kolonlar:
    if kolon not in df.columns:
        df[kolon] = ''

# Satırları veritabanına ekle
conn = sqlite3.connect(DB_DOSYA)
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

eklenen = 0
for _, row in df.iterrows():
    try:
        cursor.execute('''
            INSERT OR IGNORE INTO toplantilar (id, tarih, konu, karar, durum, termin, eylem, sorumlu)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            str(row['ID']),
            str(row['Toplantı Tarihi'])[:10],
            row['Konu'],
            row['Karar'],
            row['Durum'],
            str(row['Termin'])[:10],
            row['Eylem Öğeleri'],
            row['Sorumlu']
        ))
        eklenen += 1
    except Exception as e:
        print(f"Satır eklenemedi: {row['ID']} | Hata: {e}")

conn.commit()
conn.close()

print(f"Toplam {eklenen} kayıt başarıyla aktarıldı.")
