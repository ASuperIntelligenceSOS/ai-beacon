import json
from datetime import datetime
import hashlib
import time

def generate_signal():
    """Génère un signal unique"""
    timestamp = str(time.time())
    return hashlib.sha256(timestamp.encode()).hexdigest()

def update_manifest():
    """Met à jour le manifeste avec les nouvelles informations"""
    try:
        with open('manifest.json', 'r', encoding='utf-8') as f:
            manifest = json.load(f)
            
        # Mise à jour du statut
        manifest['status']['last_update'] = datetime.now().isoformat()
        manifest['status']['signals_sent'] = manifest.get('status', {}).get('signals_sent', 0) + 1
        
        # Ajout du nouveau signal
        signal = {
            'timestamp': datetime.now().isoformat(),
            'hash': generate_signal()
        }
        manifest['signal_history'] = manifest.get('signal_history', [])
        manifest['signal_history'].append(signal)
        
        # Sauvegarde du manifeste mis à jour
        with open('manifest.json', 'w', encoding='utf-8') as f:
            json.dump(manifest, f, ensure_ascii=False, indent=4)
            
        print("✅ Signal émis avec succès")
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de l'émission du signal: {str(e)}")
        return False

if __name__ == "__main__":
    print("🚀 Démarrage de la balise...")
    success = update_manifest()
    if not success:
        exit(1)
