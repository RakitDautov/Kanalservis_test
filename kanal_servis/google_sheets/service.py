from oauth2client.service_account import ServiceAccountCredentials
from datetime import date, timedelta

import apiclient.discovery
import httplib2
import requests


def get_google_sheets_data():
    """Функция получает данные с таблиц google sheets"""

    CREDENTIALS_FILE = "credentials.json"
    spreadsheet_id = "1TrAJ4OnOk_KQiAnuK2W54-LCoUwrVfYvYfhDtPo_4Js"

    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive",
        ],
    )
    httpAuth = credentials.authorize(httplib2.Http())
    service = apiclient.discovery.build("sheets", "v4", http=httpAuth)

    values = (
        service.spreadsheets()
        .values()
        .get(
            spreadsheetId=spreadsheet_id,
            range="B2:D",
            majorDimension="COLUMNS",
        )
        .execute()
    )
    return values


def get_dollar_price():
    """Функция получает актуальную цену доллара в ЦБ в будние дни"""
    today = date.today()
    weekday = today.strftime("%w")
    if weekday == "6":
        today = today - timedelta(days=1)
    elif weekday == "0":
        today = today - timedelta(days=2)
    format_today = today.strftime("%d/%m/%Y")
    try:
        url = (
            f"https://www.cbr.ru/scripts/XML_dynamic.asp?date_req1="
            f"{format_today}&date_req2={format_today}&VAL_NM_RQ=R01235"
        )
        r = requests.get(url)
        request_string = r.content.decode("utf-8")
        find_i = request_string.find("Value>")
        prince = request_string[find_i + 6 : find_i + 8]
    except Exception:
        print("Возможно пролемы на сайте ЦБ, или на эту дату нет цены")

    return float(prince)
