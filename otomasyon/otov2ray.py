import base64
import requests
import os
import binascii

# Base64 çözme fonksiyonu
def decode_base64(encoded):
    """Base64 kodunu çözüp string olarak döndürür."""
    try:
        decoded_bytes = base64.b64decode(encoded, validate=True)
        return decoded_bytes.decode('utf-8', errors='ignore')
    except (binascii.Error, UnicodeDecodeError):
        return None

# URL'lerden veriyi çekip base64'ü çözen fonksiyon
def fetch_and_decode_links(links):
    decoded_data = []

    for link in links:
        try:
            response = requests.get(link, timeout=10)  # 10 saniye bekleme süresi
            response.raise_for_status()  # HTTP hatalarını kontrol et

            content = response.content.strip()  # Boşlukları temizle
            decoded_text = decode_base64(content)

            if decoded_text:
                decoded_data.append(decoded_text)
            else:
                print(f"⚠ Uyarı: {link} base64 çözülemedi veya boş içerik döndürdü.")

        except requests.exceptions.RequestException as e:
            print(f"❌ Hata: {link} bağlantısı alınamadı! - {e}")

    return decoded_data

# Kullanılacak kaynaklar
links = [
    'https://raw.githubusercontent.com/MrPooyaX/VpnsFucking/main/Shenzo.txt',
    'https://raw.githubusercontent.com/MrPooyaX/SansorchiFucker/main/data.txt',
    'https://mrpooyax.camdvr.org/api/ramezan/lena.php?sub=1',
    'https://mrpooyax.camdvr.org/api/ramezan/run.php?sub=1',
    'https://raw.githubusercontent.com/yebekhe/TVC/main/subscriptions/xray/base64/mix',
    'https://mrpooyax.camdvr.org/api/ramezan/alpha.php?sub=1',
    'https://raw.githubusercontent.com/ALIILAPRO/v2rayNG-Config/main/sub.txt',
    'https://raw.githubusercontent.com/yebekhe/TelegramV2rayCollector/main/sub/base64/donated',
    'https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/reality',
    'https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vless',
    'https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/vmess',
    'https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/trojan',
    'https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/protocols/shadowsocks',
    'https://raw.githubusercontent.com/ts-sf/fly/main/v2',
    'https://raw.githubusercontent.com/Pawdroid/Free-servers/main/sub',
    'https://raw.githubusercontent.com/shabane/kamaji/master/hub/b64/merged.txt',
    'https://raw.githubusercontent.com/barry-far/V2ray-Configs/refs/heads/main/All_Configs_Sub.txt'
]

# Verileri al ve çözümlenmiş içeriği listeye kaydet
decoded_links = fetch_and_decode_links(links)

# Dosya yolu
file_path = os.path.join(os.getcwd(), "alexander.txt")

# Dosyaya yazma işlemi
with open(file_path, 'w', encoding='utf-8') as f:
    for config in decoded_links:
        if config.strip():  # Boş stringleri kaydetme
            f.write(config + '\n')

print(f"✅ Çözümlenen veriler {file_path} dosyasına kaydedildi.")

