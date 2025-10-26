# 🚀 GUÍA RÁPIDA - EXTRACTOR-APP

## ⚡ Configuración Rápida (5 minutos)

### 1. Preparación Inicial
```powershell
# Clonar proyecto
git clone https://github.com/KillahBlitz/extractor-app.git
cd extractor-app

# Crear entorno virtual
python -m venv .venv

# Activar entorno virtual
.\.venv\Scripts\Activate.ps1
```

### 2. Instalación
```powershell
# Instalar dependencias
pip install -r requirements.txt

# Configurar entorno (IMPORTANTE)
.\setup_env.ps1
```

### 3. Ejecutar
```powershell
# Ejecutar aplicación principal
python widget.py
```

## 📋 Comandos Más Usados

### Configuración de Entorno
```powershell
# Configuración automática (recomendado)
.\setup_env.ps1

# Configuración manual
$env:PYTHONPATH = "$(Get-Location)\src"
.\.venv\Scripts\Activate.ps1
```

### Ejecutar Aplicación
```powershell
# Aplicación principal
python widget.py

# Módulo de extracción
python src\Scripts\extraction_data\class_extraction.py
```

### Qt Designer
```powershell
# Abrir diseñador
pyside6-designer

# Generar código desde .ui
pyside6-uic archivo.ui -o UI/ui_archivo.py
```

## 🔧 Variables de Entorno Importantes

| Variable | Valor | Propósito |
|----------|-------|-----------|
| `PYTHONPATH` | `./src` | Ruta base para imports |
| `PROJECT_ROOT` | `./` | Directorio raíz del proyecto |

## 🐛 Errores Comunes y Soluciones

### ❌ ModuleNotFoundError: No module named 'src'
```powershell
# Solución:
$env:PYTHONPATH = "$(Get-Location)\src"
```

### ❌ ImportError: cannot import name 'Patient'
```powershell
# Verificar que el entorno esté activado
.\setup_env.ps1
```

### ❌ Error de permisos en PowerShell
```powershell
# Habilitar ejecución de scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## 📁 Archivos Clave

- `widget.py` - Aplicación principal
- `setup_env.ps1` - Configuración automática
- `requirements.txt` - Dependencias
- `src/` - Código fuente principal

## 🎯 Flujo de Trabajo Típico

1. **Activar entorno:** `.\setup_env.ps1`
2. **Ejecutar app:** `python widget.py`
3. **Cargar archivo Excel/JSON**
4. **Procesar datos**
5. **Ver resultados**

---
💡 **Tip:** Siempre ejecuta `.\setup_env.ps1` antes de trabajar con el proyecto