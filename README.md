
# TS-OSINT (TLER AL-SHAHRANI-OSINT)
## أداة (استخبارات المصادر المفتوحة-OSINT (Open-Source Intelligence 

<img src="https://github.com/tlersa/DAK-TS/assets/111729973/fe136b75-1fb9-4103-8832-0a03cc5ba609" width="1000">

### (KALI Linux) أوامر التثبيت
```
sudo git clone https://github.com/tlersa/DAK-TS.git
cd DAK-TS/
python3 DAK-TS.py
```

### (Termux) أوامر التثبيت
```
pkg install python git
git clone https://github.com/tlersa/DAK-TS.git
cd DAK-TS/
pip install -r requirements.txt
python DAK-TS.py
```

### المميزات
- مجانية ومفتوحة المصدر ✔️
- إذا لم تكن مثبت المكاتب المطلوبة (socket, random, threading, os) سيتم تثبيتها تلقائياً ✔️
- اختيار عدد الطلبات المرسلة على الخادم المستهدف ✔️
- تعمل على كل الأنظمة ✔️
 
### ملاحظات ⚠️
- أي استخدام خاطئ للأداة فنحن غير مسؤولين
- إذا كنت تريد الهجوم فعليا فستخدم الأداة وأنت متخفي على الانترنت، مثل Proxychains + TOR, VPN, anonsurf, torghost

### تثبيت المكاتب (إذا كنت تستخدم KALI Linux فلا تحتاج لتثبيتها)

```
pip install socket random threading os
```
