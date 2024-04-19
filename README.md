
# DAK-TS (DDOS attack-TLER AL-SHAHRANI)
## أداة هجمة DDOS

<img src="https://github.com/tlersa/DAK-TS/assets/111729973/fa14ed33-ff22-4c2a-8ac9-b9b1c6210c64" width="1000">

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
- اختيار عدد الطلبات المرسلة على الخادم المستهدف لهجمة DOS ✔️
- إرسال الطلبات على الخادم المستهدف بشكل سريع جدا لهجمة DDOS ✔️
- تعمل على كل الأنظمة ✔️
 
### ملاحظات ⚠️
- أي استخدام خاطئ للأداة فنحن غير مسؤولين
- إذا كنت تريد الهجوم فعليا فستخدم الأداة وأنت متخفي على الانترنت، مثل Proxychains + TOR, VPN, anonsurf, torghost [[شرح لطرق التخفي](https://t.me/tler_sa/138)]

### تثبيت المكاتب (إذا كنت تستخدم KALI Linux فلا تحتاج لتثبيتها)

```
pip install socket random threading os
```
