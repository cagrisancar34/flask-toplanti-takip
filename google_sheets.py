import gspread
from oauth2client.service_account import ServiceAccountCredentials

def google_sheets_veri_ekle(veri_listesi):
    """
    Google Sheets'e bir satır veri ekler.
    Render'da GOOGLE_CREDS_JSON isimli secret dosyasını kullanarak kimlik doğrulaması yapar.
    
    :param veri_listesi: Liste halinde eklenecek satır verisi (örnek: [tarih, konu, karar, ...])
    """

    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]

    # Render'da tanımlanan gizli dosyanın yolu
    creds_path = "/etc/secrets/GOOGLE_CREDS_JSON"

    # Servis hesabı kimlik bilgilerini kullanarak yetkilendirme
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)

    try:
        # Google Sheets dosyasını ve sayfayı aç
        sheet = client.open("Toplanti Takip").worksheet("Sheet1")

        # Veriyi yeni satır olarak ekle
        sheet.append_row(veri_listesi, value_input_option="USER_ENTERED")

        print("✅ Google Sheets'e eklendi:", veri_listesi)

    except Exception as e:
        # Render loglarında görünmesi için hata mesajı yazdır
        print("❌ Sheets HATASI:", e)
        raise
