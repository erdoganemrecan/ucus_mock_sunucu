
# Mock Uçuş API Sunucusu

Bu sunucu, Skyscanner API erişimi olmadan sahte (mock) verilerle uçuş bilgisi sağlayan bir demo sunucudur.

## Başlatmak için:

1. Python 3.10+ yüklü olmalı.
2. Gerekli kütüphaneleri kurun:

```
pip install -r requirements.txt
```

3. Sunucuyu çalıştırın:

```
python app.py
```

4. Tarayıcıdan veya GPT'den şu formatta çağırın:

```
http://localhost:5000/ucus-bilgisi?from=DXB&to=IST&date=15/05/2025
```
