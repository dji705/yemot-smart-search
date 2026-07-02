# yemot-smart-search

Yemot Search API

פרויקט זה מאפשר לבצע חיפוש חכם במגוון אתרי תוכן איכותיים (ישראליים ובינלאומיים) מתוך מערכת הטלפוניה "ימות המשיח", באמצעות שרת Flask ו-Google Custom Search API.

🚀 תכונות עיקריות

אינטגרציה מלאה עם ימות המשיח: קבלת קלט מהטלפון והחזרת תוצאות חיפוש ישירות להקראה.

סינון אתרים איכותי: החיפוש מוגבל לרשימת אתרים מהימנים ומקצועיים.

מוכן לענן: הקוד מותאם להעלאה קלה ל-Vercel או לשרתים מרוחקים, כדי לעקוף חסימות רשת מקומיות.

🛠️ טכנולוגיות בשימוש

Flask: שרת ה-API.

Google Custom Search API: מנוע החיפוש החכם.

Python-dotenv: לניהול מאובטח של מפתחות ה-API.

ngrok: לחשיפת השרת המקומי במהלך פיתוח ובדיקות.

⚙️ התקנה והגדרה

שכפול המאגר:

git clone https://github.com/your-username/yemot-search-api.git
cd yemot-search-api


התקנת ספריות:

pip install -r requirements.txt


הגדרת משתני סביבה:
צור קובץ בשם .env בתיקייה הראשית והוסף בו:

SEARCH_API_KEY=YOUR_GOOGLE_API_KEY
SEARCH_ENGINE_ID=d5a3158fa24db4e1c


הרצה מקומית:

python app.py


🌐 העלאה ל-Vercel (מומלץ)

הפרויקט מכיל קובץ vercel.json המאפשר העלאה מהירה ל-Vercel.

בלוח הבקרה של Vercel, הגדר תחת Environment Variables את המפתחות SEARCH_API_KEY ו-SEARCH_ENGINE_ID.

📞 חיבור לימות המשיח

הפעל את השרת (מקומי עם ngrok או בענן).

בהגדרות השלוחה בימות המשיח, בחר סוג שלוחה API.

הזן את הכתובת של השרת בצירוף הנתיב: https://your-domain.app/yemot_webhook

📝 רישיון

הפרויקט מופץ כקוד פתוח. תרגישו חופשי לתרום ולשפר!
