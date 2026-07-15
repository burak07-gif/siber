# 1. Depoları güncelle
pkg update -y && pkg upgrade -y

# 2. Python kur
pkg install python -y

# 3. Kodu indir veya kaydet
# Dosyayı oluştur:
nano mrrobot_pentest.py
# (Yukarıdaki kodu yapıştır, Ctrl+X, Y, Enter ile kaydet)

# Veya direkt olarak:
curl -O https://pastebin.com/raw/XXXXX  # (Kodu bir yere upload edip buradan çekebiliriz)

# 4. Çalıştırılabilir yap
chmod +x mrrobot_pentest.py

# 5. Çalıştır
python mrrobot_pentest.py
