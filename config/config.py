"""
Configuración de rutas del proyecto Extractor App
"""
import os
from pathlib import Path

# Ruta absoluta del directorio raíz del proyecto
PROJECT_ROOT = Path(__file__).parent.resolve()

# Ruta absoluta del directorio src
SRC_PATH = PROJECT_ROOT / "src"

# Otras rutas importantes del proyecto
UI_PATH = PROJECT_ROOT / "UI"
ASSETS_PATH = PROJECT_ROOT / "assets"
SCRIPTS_PATH = SRC_PATH / "Scripts"
MODELS_PATH = SRC_PATH / "models"
EXTRACTION_PATH = SCRIPTS_PATH / "extraction_data"

# Función para configurar las rutas del proyecto
def setup_project_paths():
    """
    Configura sys.path para incluir las rutas necesarias del proyecto
    """
    import sys
    
    paths_to_add = [
        str(PROJECT_ROOT),
        str(SRC_PATH),
    ]
    
    for path in paths_to_add:
        if path not in sys.path:
            sys.path.insert(0, path)

# Información del proyecto
PROJECT_INFO = {
    "name": "Extractor App",
    "version": "1.0.0",
    "description": "Aplicación para extracción de datos de archivos Excel y JSON"
}