# ============================================================================
# 🚀 EXTRACTOR-APP - Script de Configuración del Entorno de Desarrollo
# ============================================================================
# Este script configura automáticamente el entorno de desarrollo para 
# Extractor-App, incluyendo PYTHONPATH y activación del entorno virtual.

Write-Host "🔧 Configurando entorno para EXTRACTOR-APP..." -ForegroundColor Cyan
Write-Host ("=" * 60) -ForegroundColor DarkGray

# El directorio del proyecto está un nivel arriba de config/
$ProjectRoot = Split-Path $PSScriptRoot -Parent
$SrcPath = Join-Path $ProjectRoot "src"

# Verificar que estamos en el directorio correcto
if (-not (Test-Path $SrcPath)) {
    Write-Host "❌ Error: No se encontró el directorio 'src'" -ForegroundColor Red
    Write-Host "   Asegúrate de ejecutar este script desde el directorio raíz del proyecto" -ForegroundColor Yellow
    Read-Host "Presiona Enter para continuar"
    exit 1
}

# Configurar PYTHONPATH
$env:PYTHONPATH = $SrcPath
Write-Host "✅ PYTHONPATH configurado:" -ForegroundColor Green
Write-Host "   $SrcPath" -ForegroundColor White

# Activar entorno virtual si existe
$VenvPath = Join-Path $ProjectRoot ".venv\Scripts\Activate.ps1"
if (Test-Path $VenvPath) {
    Write-Host "🔄 Activando entorno virtual..." -ForegroundColor Yellow
    & $VenvPath
    Write-Host "✅ Entorno virtual activado" -ForegroundColor Green
} else {
    Write-Host "⚠️  No se encontró entorno virtual en .venv" -ForegroundColor Yellow
    Write-Host "   Ejecuta: python -m venv .venv" -ForegroundColor White
}

# Verificar instalación de dependencias
$RequirementsPath = Join-Path $ProjectRoot "requirements.txt"
if (Test-Path $RequirementsPath) {
    Write-Host "📦 Verificando dependencias..." -ForegroundColor Yellow
    
    # Verificar si pip está disponible
    try {
        $pipVersion = & pip --version 2>$null
        if ($pipVersion) {
            Write-Host "✅ pip disponible: $($pipVersion.Split(' ')[1])" -ForegroundColor Green
        }
    } catch {
        Write-Host "❌ pip no está disponible" -ForegroundColor Red
    }
    
    # Sugerir instalación de dependencias si es necesario
    Write-Host "💡 Para instalar dependencias ejecuta:" -ForegroundColor Cyan
    Write-Host "   pip install -r requirements.txt" -ForegroundColor White
}

Write-Host ""
Write-Host ("=" * 60) -ForegroundColor DarkGray
Write-Host "🎉 ¡Configuración completada!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Comandos disponibles:" -ForegroundColor Cyan
Write-Host "   python widget.py                                    # Ejecutar aplicación principal" -ForegroundColor White
Write-Host "   python src\Scripts\extraction_data\class_extraction.py  # Ejecutar extractor" -ForegroundColor White
Write-Host "   pyside6-designer                                     # Abrir Qt Designer" -ForegroundColor White
Write-Host ""
Write-Host "📚 Documentación:" -ForegroundColor Cyan
Write-Host "   README.md        # Documentación completa" -ForegroundColor White
Write-Host "   QUICK_START.md   # Guía rápida" -ForegroundColor White
Write-Host ""
Write-Host "💡 Tip: Este script configuró tu sesión actual." -ForegroundColor Yellow
Write-Host "   Para nuevas sesiones, ejecuta este script nuevamente." -ForegroundColor Yellow