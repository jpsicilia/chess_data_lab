import gdown
import os

# Ruta donde se guarda
output_dir = os.path.join(os.path.dirname(__file__), '..', 'data')
os.makedirs(output_dir, exist_ok=True)

output = os.path.join(output_dir, 'dataset.csv')

# Enlace directo al archivo CSV
url = "https://drive.google.com/uc?id=1DLRxgae9klToBewBU4q20MGvDT7VOWCw"

print("⬇️ Descargando el dataset CSV...")
gdown.download(url, output, quiet=False)
print(f"✅ Descarga completada: '{output}'")
