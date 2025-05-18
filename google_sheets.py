import gspread
from oauth2client.service_account import ServiceAccountCredentials

def google_sheets_veri_ekle(veri_listesi):
    scope = [
        "https://spreadsheets.google.com/feeds",
        "https://www.googleapis.com/auth/drive"
    ]
    creds_path = "/etc/secrets/GOOGLE_CREDS_JSON"  # Render.io path
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_path, scope)
    client = gspread.authorize(creds)

    try:
        sheet = client.open("Toplanti Takip").worksheet("Sheet1")
        sheet.append_row(veri_listesi, value_input_option="USER_ENTERED")
        print("✅ Google Sheets'e eklendi:", veri_listesi)
    except Exception as e:
        print("❌ Sheets HATASI:", e)
        raise
