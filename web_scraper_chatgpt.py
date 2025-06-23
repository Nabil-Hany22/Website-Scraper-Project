# ----------------------------------------------
# برنامج Web Scraper لجلب وظائف Junior Front End من موقع Wuzzuf
# ----------------------------------------------
# هذا البرنامج يقوم بالتالي:
# 1. إرسال طلب لموقع Wuzzuf للبحث عن وظائف "junior front end".
# 2. استخدام مكتبة BeautifulSoup لتحليل الصفحة واستخلاص بيانات الوظائف.
# 3. الحصول على:
#    - عنوان الوظيفة
#    - اسم الشركة
#    - تاريخ نشر الوظيفة
# 4. فلترة الوظائف المنشورة خلال أقل من أسبوع (حسب ظهور "day" أو "hour" في تاريخ النشر).
# 5. طباعة الوظائف التي تحقق الشروط على الشاشة.
#
# الأدوات المستخدمة:
# - requests: لجلب محتوى صفحات الإنترنت.
# - BeautifulSoup: لتحليل واستخلاص البيانات من صفحات HTML.
#
# ملاحظات:
# - هذا الكود يعتمد على الثوابت في HTML structure لموقع Wuzzuf، 
#   فإذا تغيرت أسماء الكلاسات، يجب تعديل الكود accordingly.
# ----------------------------------------------

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

# الرابط مع فلترة بحث لكلمة "junior front end"
url = "https://wuzzuf.net/search/jobs/?a=hpb&q=junior%20front%20end"

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# استخراج جميع كروت الوظائف
jobs = soup.find_all('div', {'class': 'css-1gatmva'})  # كارت الوظيفة

for job in jobs:
    title = job.find('h2').text.strip() if job.find('h2') else 'No Title'
    company = job.find('a', {'class': 'css-17s97q8'}).text.strip() if job.find('a', {'class': 'css-17s97q8'}) else 'No Company'
    date_text = job.find('div', {'class': 'css-do6t5g'}).text.strip() if job.find('div', {'class': 'css-do6t5g'}) else 'No Date'
    
    # فلترة الوظائف المنشورة خلال أقل من أسبوع (حسب وجود "day" أو "hour" في تاريخ النشر)
    if "day" in date_text or "hour" in date_text:
        print(f"Title: {title}")
        print(f"Company: {company}")
        print(f"Posted: {date_text}")
        print("-" * 40)



