import gspread
import os
import json
from google.oauth2.service_account import Credentials

def google_sheets_veri_ekle(veri_listesi):
    """
    Google Sheets'e bir satır veri ekler.
    Render'da GOOGLE_CREDS_JSON isimli environment değişkenini kullanarak kimlik doğrulama yapar.

    :param veri_listesi: Liste halinde eklenecek satır verisi (örnek: [tarih, konu, karar, ...])
    """

    try:
        # Ortam değişkeninden servis hesabı bilgilerini al ve düzelt
        raw_json = os.getenv("GOOGLE_CREDS_JSON")
        fixed_json = raw_json.replace('\\n', '\n')  # Satır sonu düzeltmesi
        service_account_info = json.loads(fixed_json)

        # Yetkilendirme işlemi
        creds = Credentials.from_service_account_info(service_account_info)
        client = gspread.authorize(creds)

        # Google Sheet dosyasını aç
        sheet = client.open("Toplanti Takip").worksheet("Sheet1")

        # Veriyi ekle
        sheet.append_row(veri_listesi, value_input_option="USER_ENTERED")

        print("✅ Google Sheets'e eklendi:", veri_listesi)

    except Exception as e:
        print("❌ Sheets HATASI:", e)
        raise
