"""
Configuración automática de rutas para el proyecto Extractor App
Ejecutar este archivo antes de importar otros módulos del proyecto
"""
import sys
from pathlib import Path

# Obtener la ruta del directorio src
SRC_DIR = Path(__file__).parent.resolve()

# Agregar src al path si no está ya incluido
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

# También agregar el directorio raíz del proyecto
PROJECT_ROOT = SRC_DIR.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

print(f"✓ Configuración de rutas completada")
print(f"  - SRC_DIR: {SRC_DIR}")
print(f"  - PROJECT_ROOT: {PROJECT_ROOT}")