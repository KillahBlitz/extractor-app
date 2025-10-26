# 📊 EXTRACTOR-APP

Una aplicación de escritorio para la extracción, validación y almacenamiento de datos médicos desde archivos Excel y JSON. Desarrollada con PySide6, incluye validación con Pydantic y persistencia en SQLite.

## 🎯 Características

- ✅ **Interfaz gráfica moderna** con Qt Designer
- ✅ **Soporte para archivos Excel** (.xlsx, .xls) con hojas múltiples
- ✅ **Soporte para archivos JSON**
- ✅ **Extracción de datos** de pacientes, consultas y antecedentes
- ✅ **Validación de datos** con modelos Pydantic
- ✅ **Base de datos SQLite** para almacenamiento persistente
- ✅ **Arquitectura modular** y escalable
- ✅ **Manejo robusto de fechas** (YYYY-MM-DD)
- ✅ **Contadores de registros** procesados y validados

## 📋 Requisitos del Sistema

- **Python**: 3.13.0+
- **Sistema Operativo**: Windows 10/11
- **Memoria**: 4GB RAM mínimo
- **Espacio**: 500MB disponibles

## 🏥 Estructura de Datos

### **Modelo de Paciente**
```python
- name: str              # Nombre del paciente
- age: int               # Edad
- type_patient: str      # Tipo de paciente
- weight: float          # Peso en kg
- height: float          # Altura en cm
- total_consulation: int # Total de consultas
```

### **Modelo de Consulta**
```python
- name: str              # Nombre del paciente
- date: date             # Fecha (YYYY-MM-DD)
- weight: float          # Peso en kg
- height: float          # Altura en cm
- observations: str      # Observaciones médicas
- medications: str       # Medicamentos
```

### **Modelo de Antecedente**
```python
- name: str              # Nombre del paciente
- history: str           # Descripción del antecedente
- type_history: str      # Tipo de antecedente
```

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

### 📁 Formato de Archivos Excel

Para que la aplicación procese correctamente tu archivo Excel, debe contener **3 hojas** con los siguientes nombres:

#### **Hoja: "pacientes"**
| Columna | Tipo | Descripción |
|---------|------|-------------|
| Nombre del paciente | Texto | Nombre completo |
| Edad | Número | Edad en años |
| Tipo de paciente | Texto | Categoría del paciente |
| Peso | Decimal | Peso en kilogramos |
| Altura | Decimal | Altura en centímetros |
| Numero totales de registros | Número | Total de consultas |

#### **Hoja: "consultas"**
| Columna | Tipo | Descripción |
|---------|------|-------------|
| Nombre del paciente | Texto | Nombre completo |
| Fecha | Fecha | Formato YYYY-MM-DD |
| Peso | Decimal | Peso en kg |
| Altura | Decimal | Altura en cm |
| Observaciones | Texto | Notas médicas |
| Medicamentos | Texto | Medicamentos recetados |

#### **Hoja: "antecedentes"**
| Columna | Tipo | Descripción |
|---------|------|-------------|
| Nombre del paciente | Texto | Nombre completo |
| Antecedente | Texto | Descripción del antecedente |
| Tipo de antecedente | Texto | Categoría del antecedente |

### 💾 Base de Datos

Los datos procesados se guardan automáticamente en:
- **Ubicación**: `data/extractor_app.db` (SQLite)
- **Tablas**: `patients`, `consulations`, `histories`
- **Autoincremental**: IDs únicos para cada registro

#### **Extensiones Recomendadas para Ver la DB**
- **SQLite Viewer**: `qwtel.sqlite-viewer`
- **SQLite**: `alexcvzz.vscode-sqlite`

## 📁 Estructura del Proyecto

```
extractor-app/
├── 📄 README.md                 # Este archivo
├── 📄 widget.py                 # Aplicación principal
├── 📄 .env                      # Variables de entorno
├── 📁 config/                   # Configuración del proyecto
│   ├── 📄 config.py             # Configuración central
│   ├── 📄 setup_env.ps1         # Script de configuración (PowerShell)
│   └── 📄 setup_env.bat         # Script de configuración (Batch)
├── 📁 src/                      # Código fuente principal
│   ├── 📁 models/               # Modelos de datos Pydantic
│   │   ├── 📄 class_patient.py      # Modelo de paciente
│   │   ├── 📄 class_history.py      # Modelo de antecedentes
│   │   └── 📄 class_consulation.py  # Modelo de consultas
│   └── 📁 Scripts/
│       ├── 📁 extraction_data/      # Extracción desde Excel/JSON
│       │   ├── 📄 class_extraction.py
│       │   └── 📄 extraction_handler.py
│       ├── 📁 validation_data/      # Validación con Pydantic
│       │   └── 📄 class_validator.py
│       └── 📁 injection_data/       # Persistencia en SQLite
│           ├── 📄 class_injector.py
│           └── 📄 injector_handler.py
├── 📁 UI/                       # Archivos de interfaz Qt
│   ├── 📄 ui_MainUi.py             # Interfaz principal
│   ├── 📄 ui_Xlsx.py               # Interfaz Excel
│   └── 📄 ui_Json.py               # Interfaz JSON
├── 📁 data/                     # 🆕 Base de datos (generada automáticamente)
│   └── 📄 extractor_app.db         # Base de datos SQLite
└── 📁 assets/                   # Recursos estáticos
    └── 📄 requirements.txt         # Dependencias de Python
```

## 🔄 Flujo de Trabajo

1. **📂 Selección de Archivo**: Usuario selecciona archivo Excel o JSON
2. **📊 Extracción**: Se leen las hojas del Excel (pacientes, consultas, antecedentes)
3. **✅ Validación**: Cada registro se valida con modelos Pydantic
4. **💾 Almacenamiento**: Datos válidos se guardan en SQLite
5. **📈 Reporte**: Se muestran contadores de registros procesados
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
| `pandas` | ≥2.0.0 | Manipulación de datos y lectura Excel |
| `openpyxl` | ≥3.0.0 | Lectura de archivos Excel (.xlsx) |
| `pydantic` | ≥2.0.0 | Validación de modelos de datos |
| `sqlite3` | Built-in | Base de datos integrada en Python |

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

### Error de validación de fechas

**Problema**: `invalid literal for int() with base 10: '29 00:00:00'`

**Solución**: El validador ahora maneja automáticamente fechas en formato datetime y las convierte a date

### Error: "cannot import name 'Injector'"

**Causa:** Inconsistencia en nombres de clases

**Solución**: Verificar que los imports coincidan con los nombres de clase reales

### Error de permisos en PowerShell

**Solución:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Base de datos no se crea

**Verificar:**
1. Permisos de escritura en el directorio
2. Que la carpeta `data/` se cree automáticamente
3. Revisar logs de error en la consola

### Scripts de configuración no encontrados

**Nota importante:** Los scripts de configuración ahora se encuentran en la carpeta `config/`. Ejecuta:
```powershell
config\setup_env.ps1
```
En lugar de `.\setup_env.ps1`

### Aplicación no muestra interfaz

**Verificar:**
1. PySide6 instalado correctamente
2. Archivos UI generados en la carpeta `UI/`
3. Imports de UI correctos
4. Variables de entorno configuradas

### Datos no se procesan correctamente

**Verificar:**
1. Formato del archivo Excel con las 3 hojas requeridas
2. Nombres de columnas exactos según la documentación
3. Tipos de datos correctos (fechas en YYYY-MM-DD)
4. Revisar mensajes de validación en consola

## 🔧 Desarrollo

### Modificar la Interfaz

1. **Abrir Qt Designer:**
   ```bash
   pyside6-designer
   ```

2. **Editar archivos .ui** en la carpeta UI/

3. **Regenerar archivos Python:**
   ```bash
   pyside6-uic archivo.ui -o ui_archivo.py
   ```

### Agregar Nuevos Modelos

1. Crear modelo en `src/models/`
2. Actualizar validador en `src/Scripts/validation_data/`
3. Modificar extractor en `src/Scripts/extraction_data/`
4. Actualizar injector para nueva tabla

## 📊 Características Técnicas

- **Patrón MVC**: Separación clara entre modelo, vista y controlador
- **Validación robusta**: Pydantic para verificar tipos y constraints
- **Manejo de errores**: Try/catch en todos los puntos críticos
- **Logging**: Mensajes informativos para debugging
- **Modularidad**: Componentes independientes y reutilizables
- **Configuración centralizada**: Scripts y paths organizados

## 📈 Roadmap

- [ ] Soporte para más formatos de archivo (CSV, XML)
- [ ] Interfaz web complementaria
- [ ] Exportación de reportes en PDF
- [ ] Backup automático de base de datos
- [ ] Configuración de validaciones personalizadas
- [ ] API REST para integración externa

---

**Desarrollado por**: KillahBlitz  
**Licencia**: MIT  
**Versión**: 1.0.0

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