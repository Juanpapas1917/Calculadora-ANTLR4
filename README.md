# Calculadora-ANTLR4
Ejecucion de antlr4 

1. Crear un Entorno Virtual (VENV)
    python3 -m venv .venv

Para activar el entorno virtual, ejecuta:

    source .venv/bin/activate
    
3. Instalar los Requisitos
Con el entorno virtual activado
    pip install -r requirements.txt

Esto instalará todos los paquetes listados en requirements.txt.

4. Generar los Archivos ANTLR
5. calculator.g4, ejecuta:

    antlr4 -visitor -Dlanguage=Python3 calculator.g4

Este comando generará el código fuente necesario en Python, incluyendo los archivos para el parser y el visitor.
6. Ejecutar 
  python calc.py
7. Hacer pruebas
  
