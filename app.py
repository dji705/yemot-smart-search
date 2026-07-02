import os
import requests
from flask import Flask, request
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

app = Flask(__name__)

# ב-Vercel נגדיר את אלו ב-Environment Variables בלוח הבקרה
API_KEY = os.getenv("SEARCH_API_KEY")
CSE_ID = os.getenv("SEARCH_ENGINE_ID")

@app.route('/yemot_webhook', methods=['GET', 'POST'])
def yemot_webhook():
    user_input = request.values.get("data")
    if user_input == "3":
        query = "חדשות"
        search_url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={CSE_ID}&q={query}"
        headers = {'User-Agent': 'Mozilla/5.0'}
        try:
            response = requests.get(search_url, headers=headers, verify=False, timeout=10)
            response.raise_for_status()
            data = response.json()
            first_result = data.get("items", [{}])[0].get("title", "לא נמצאו תוצאות")
            return f"say=התוצאה הראשונה שמצאתי היא: {first_result}"
        except Exception as e:
            return f"say=שגיאה בחיבור למנוע החיפוש"
    return "say=אנא הקש 3"

# זהו החלק החשוב ל-Vercel:
if __name__ == '__main__':
    app.run()