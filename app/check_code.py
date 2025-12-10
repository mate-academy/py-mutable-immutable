#!/usr/bin/env python3
"""
Herramienta para verificar y corregir problemas de código Python.
Uso: python check_code.py [opciones]
"""

import os
import subprocess
import sys
from pathlib import Path

def run_flake8(directory="app"):
    """Ejecuta flake8 en el directorio especificado."""
    print(f"\n{'='*50}")
    print("EJECUTANDO FLAKE8")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(
            ["flake8", directory],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            print("✓ No se encontraron errores de estilo")
            return True
        else:
            print("✗ Se encontraron errores:")
            print(result.stdout)
            
            # Mostrar ayuda específica para errores comunes
            errors = result.stdout.split('\n')
            for error in errors:
                if "E265" in error:
                    print("\n💡 Ayuda para E265: Los comentarios deben empezar con '# '")
                    print("   Ejemplo incorrecto: '#esto es un comentario'")
                    print("   Ejemplo correcto:   '# esto es un comentario'")
                elif "E302" in error:
                    print("\n💡 Ayuda para E302: Se esperan 2 líneas en blanco antes de una función")
                elif "E501" in error:
                    print("\n💡 Ayuda para E501: Línea demasiado larga (>79 caracteres)")
            
            return False
    except FileNotFoundError:
        print("✗ Error: flake8 no está instalado")
        print("  Ejecuta: pip install flake8")
        return False

def run_pytest():
    """Ejecuta pytest para correr los tests."""
    print(f"\n{'='*50}")
    print("EJECUTANDO TESTS")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(
            ["pytest"],
            capture_output=True,
            text=True
        )
        
        print(result.stdout)
        
        if result.returncode == 0:
            print("✓ Todos los tests pasaron")
            return True
        else:
            print("✗ Algunos tests fallaron")
            if result.stderr:
                print("Errores:", result.stderr)
            return False
    except FileNotFoundError:
        print("✗ Error: pytest no está instalado")
        print("  Ejecuta: pip install pytest")
        return False

def check_requirements():
    """Verifica si las dependencias están instaladas."""
    print(f"\n{'='*50}")
    print("VERIFICANDO DEPENDENCIAS")
    print(f"{'='*50}")
    
    # Mapeo de nombres de paquetes a módulos de importación
    requirements_map = {
        "flake8": "flake8",
        "flake8-annotations": "flake8_annotations",
        "flake8-quotes": "flake8_quotes", 
        "flake8-variables-names": "flake8_variables_names",
        "pep8-naming": "pep8ext_naming",  # ¡Corregido!
        "pytest": "pytest"
    }
    
    missing = []
    
    for package_name, import_name in requirements_map.items():
        try:
            # Intentar importar el módulo
            subprocess.run(
                [sys.executable, "-c", f"import {import_name}"],
                check=True,
                capture_output=True,
                timeout=3
            )
            print(f"✓ {package_name}")
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Intentar método alternativo usando pip list
            try:
                result = subprocess.run(
                    [sys.executable, "-m", "pip", "list"],
                    capture_output=True,
                    text=True,
                    check=True
                )
                
                # Buscar el paquete en la lista de pip
                package_installed = False
                for line in result.stdout.split('\n'):
                    if package_name.lower() in line.lower():
                        package_installed = True
                        break
                
                if package_installed:
                    print(f"✓ {package_name} (instalado pero no importable como {import_name})")
                else:
                    print(f"✗ {package_name}")
                    missing.append(package_name)
                    
            except Exception:
                print(f"✗ {package_name}")
                missing.append(package_name)
    
    if missing:
        print(f"\n⚠ Faltan {len(missing)} dependencias:")
        for package in missing:
            print(f"  pip install {package}")
        
        # Verificación adicional para pep8-naming
        if "pep8-naming" in missing:
            print("\n💡 Nota sobre pep8-naming:")
            print("  Este paquete se instala como 'pep8-naming'")
            print("  pero se importa como 'pep8ext_naming'")
            print("  Prueba: pip install pep8-naming --force-reinstall")
        
        return False
    
    print("\n✅ Todas las dependencias están instaladas correctamente")
    return True

def fix_common_issues():
    """Sugiere correcciones para problemas comunes."""
    print(f"\n{'='*50}")
    print("SUGERENCIAS DE CORRECCIÓN")
    print(f"{'='*50}")
    
    suggestions = [
        "1. Comentarios: Asegúrate que empiezan con '# ' (espacio después del #)",
        "2. Indentación: Usa 4 espacios (no tabs)",
        "3. Longitud de línea: Máximo 79 caracteres",
        "4. Espacios en blanco:",
        "   - 2 líneas antes de funciones/clases",
        "   - 1 línea antes de métodos",
        "5. Nombres:",
        "   - Funciones: snake_case (mi_funcion)",
        "   - Clases: CamelCase (MiClase)",
        "   - Constantes: MAYÚSCULAS (MI_CONSTANTE)",
    ]
    
    for suggestion in suggestions:
        print(suggestion)

def create_git_hook():
    """Crea un git hook para verificar el código antes de commit."""
    print(f"\n{'='*50}")
    print("CREANDO GIT HOOK")
    print(f"{'='*50}")
    
    hook_content = """#!/bin/sh
# Pre-commit hook para verificar código Python

echo "🔍 Ejecutando flake8..."
flake8 app/

if [ $? -ne 0 ]; then
    echo "❌ Errores de estilo encontrados. Corrígelos antes de commit."
    exit 1
fi

echo "🧪 Ejecutando tests..."
pytest

if [ $? -ne 0 ]; then
    echo "❌ Tests fallaron. Corrígelos antes de commit."
    exit 1
fi

echo "✅ Todo correcto! Puedes hacer commit."
exit 0
"""
    
    hook_path = Path(".git/hooks/pre-commit")
    
    try:
        hook_path.parent.mkdir(parents=True, exist_ok=True)
        hook_path.write_text(hook_content)
        hook_path.chmod(0o755)  # Hacer ejecutable
        print("✓ Git hook creado en .git/hooks/pre-commit")
        print("  Se ejecutará automáticamente antes de cada commit")
    except Exception as e:
        print(f"✗ Error creando git hook: {e}")

def main():
    """Función principal."""
    print(f"{'#'*60}")
    print("# HERRAMIENTA DE VERIFICACIÓN DE CÓDIGO PYTHON")
    print(f"{'#'*60}")
    
    # Verificar que estamos en el directorio correcto
    if not Path("requirements.txt").exists():
        print("⚠ Advertencia: No se encontró requirements.txt en el directorio actual")
    
    # Menú de opciones
    if len(sys.argv) > 1:
        option = sys.argv[1].lower()
    else:
        print("\nOpciones disponibles:")
        print("  all     - Ejecutar todas las verificaciones")
        print("  flake8  - Solo verificar estilo con flake8")
        print("  test    - Solo ejecutar tests")
        print("  deps    - Solo verificar dependencias")
        print("  fix     - Mostrar sugerencias de corrección")
        print("  git     - Crear git hook")
        print("  help    - Mostrar este mensaje")
        
        option = input("\nSelecciona una opción (all): ").strip().lower() or "all"
    
    # Ejecutar opción seleccionada
    results = []
    
    if option in ["all", "flake8"]:
        results.append(run_flake8())
    
    if option in ["all", "test"]:
        results.append(run_pytest())
    
    if option in ["all", "deps"]:
        results.append(check_requirements())
    
    if option in ["fix"]:
        fix_common_issues()
    
    if option in ["git"]:
        create_git_hook()
    
    if option in ["help"]:
        print("\nUso: python check_code.py [opción]")
        print("\nOpciones: all, flake8, test, deps, fix, git, help")
    
    # Resumen final
    if option == "all":
        print(f"\n{'='*50}")
        print("RESUMEN FINAL")
        print(f"{'='*50}")
        
        if all(results):
            print("✅ ¡Todo correcto! Tu código pasa todas las verificaciones.")
        else:
            print("❌ Se encontraron problemas. Revisa los mensajes arriba.")
            print("\n💡 Consejo: Ejecuta 'python check_code.py fix' para ver sugerencias")

if __name__ == "__main__":
    main()