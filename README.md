# 📊 EXTRACTOR-APP

Una aplicación de escritorio para la extracción y procesamiento de datos de archivos Excel y JSON, desarrollada con PySide6 y diseño modular.

## 🎯 Características

- ✅ **Interfaz gráfica moderna** con Qt Designer
- ✅ **Soporte para archivos Excel** (.xlsx, .xls)
- ✅ **Soporte para archivos JSON**
- ✅ **Extracción de datos** estructurados
- ✅ **Modelos de datos** con Pydantic
- ✅ **Arquitectura modular** y escalable

## 📋 Requisitos del Sistema

- **Python**: 3.13.0
- **Sistema Operativo**: Windows 10/11
- **Memoria**: 4GB RAM mínimo
- **Espacio**: 500MB disponibles

## 🚀 Configuración e Instalación

### 1. Clonar el Repositorio

```bash
git clone https://github.com/KillahBlitz/extractor-app.git
cd extractor-app
```

### 2. Crear Entorno Virtual

Ejecuta el siguiente comando:

#### **Con Python**
```bash
python -m venv .venv
```

### 3. Activar Entorno Virtual

#### **En Windows (PowerShell) - RECOMENDADO**
```powershell
.\.venv\Scripts\Activate.ps1
```

#### **En Windows (CMD)**
```cmd
.venv\Scripts\activate.bat
```

#### **Verificar activación**
Deberías ver `(.venv)` al inicio de tu línea de comandos:
```
(.venv) PS C:\...\extractor-app>
```

### 4. Instalar Dependencias

```bash
pip install -r assets/requirements.txt
```

### 5. Configurar Variables de Entorno

El proyecto incluye scripts automáticos para configurar el entorno ubicados en la carpeta `config/`:

#### **PowerShell (Recomendado)**
```powershell
config\setup_env.ps1
```

#### **CMD/Batch**
```cmd
config\setup_env.bat
```

#### **Manual (si es necesario)**
```powershell
$env:PYTHONPATH = "$(Get-Location)\src"
```

## 🎮 Uso de la Aplicación

### Ejecutar la Aplicación Principal

#### **Método 1: Con configuración automática**
```powershell
# Ejecutar script de configuración desde config/
config\setup_env.ps1

# Ejecutar aplicación
python widget.py
```

#### **Método 2: Manual**
```powershell
# Configurar path
$env:PYTHONPATH = "$(Get-Location)\src"

# Ejecutar aplicación
python widget.py
```

### Ejecutar Módulos de Extracción

```powershell
# Configurar entorno
$env:PYTHONPATH = "$(Get-Location)\src"

# Ejecutar extractor
python src\Scripts\extraction_data\class_extraction.py
```

## 📁 Estructura del Proyecto

```
extractor-app/
├── 📄 README.md                 # Este archivo
├── 📄 widget.py                 # Aplicación principal
├── 📄 .env                      # Variables de entorno
├──  config/                   # Configuración del proyecto
│   ├── 📄 config.py             # Configuración central
│   ├── 📄 setup_env.ps1         # Script de configuración (PowerShell)
│   └── 📄 setup_env.bat         # Script de configuración (Batch)
├── 📁 src/                      # Código fuente principal
│   ├── 📁 models/               # Modelos de datos
│   │   ├── 📄 class_patient.py
│   │   ├── 📄 class_history.py
│   │   └── 📄 class_consulation.py
│   └── 📁 Scripts/
│       └── 📁 extraction_data/  # Lógica de extracción
│           ├── 📄 class_extraction.py
│           └── 📄 extraction_handler.py
├── 📁 UI/                       # Archivos de interfaz
│   ├── 📄 ui_MainUi.py
│   ├── 📄 ui_Xlsx.py
│   └── 📄 ui_Json.py
└── 📁 assets/                   # Recursos estáticos
    └── 📄 requirements.txt      # Dependencias de Python
```

## 🔧 Desarrollo

### Modificar la Interfaz

1. **Abrir Qt Designer:**
   ```bash
   pyside6-designer
   ```

2. **Editar archivos .ui** en la carpeta UI/

3. **Generar código Python:**
   ```bash
   pyside6-uic archivo.ui -o UI/ui_archivo.py
   ```

### Agregar Nuevos Modelos

1. Crear archivo en `src/models/`
2. Definir clase con Pydantic
3. Importar en `class_extraction.py`

## 📦 Dependencias Principales

| Dependencia | Versión | Propósito |
|-------------|---------|-----------|
| `PySide6` | ≥6.10.0 | Interfaz gráfica Qt |
| `pandas` | ≥2.0.0 | Manipulación de datos |
| `openpyxl` | ≥3.0.0 | Lectura de archivos Excel |
| `pydantic` | ≥2.0.0 | Validación de modelos |

## 🐛 Solución de Problemas

### Error: "No module named 'src'"

**Solución:**
```powershell
# Configurar PYTHONPATH manualmente
$env:PYTHONPATH = "$(Get-Location)\src"

# O usar el script de configuración
config\setup_env.ps1
```

### Error: "cannot import name 'Patient'"

**Causa:** Nombres de clases incorrectos en imports

**Solución:** Verificar nombres exactos en archivos de modelos

### Error de permisos en PowerShell

**Solución:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Scripts de configuración no encontrados

**Nota importante:** Los scripts de configuración ahora se encuentran en la carpeta `config/`. Ejecuta:
```powershell
config\setup_env.ps1
```
En lugar de `.\setup_env.ps1`

### Aplicación no muestra interfaz

**Verificar:**
1. PySide6 instalado correctamente
2. Archivos UI generados
3. Imports de UI correctos

## 📝 Changelog

### v1.0.0 (Actual)
- ✅ Interfaz gráfica básica
- ✅ Extracción de archivos Excel
- ✅ Modelos de datos con Pydantic
- ✅ Configuración automática de entorno

## 👥 Autores

- **KillahBlitz y KapauCastle**- *Desarrollo inicial* - [GitHub KillabBlitz](https://github.com/KillahBlitz) [GitHub KapauCastle](https://github.com/KapauCastle)

## 📄 Licencia

Este proyecto está bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para detalles.

---

⭐ **¡Dale una estrella al proyecto si te fue útil!** ⭐