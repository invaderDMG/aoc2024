
# Advent of Code 2024

Este proyecto contiene las soluciones para el Advent of Code 2024 usando Python 3.10.15.

## Requisitos
- Python 3.10.15
- Make (opcional)

## Configuración
1. Crear el entorno virtual:
   ```bash
   python3.10 -m venv venv
   source venv/bin/activate  # O en Windows: .\venv\Scripts\activate
   ```
2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Estructura del proyecto
```
AdventOfCode/
├── day01/
│   ├── input.txt
│   └── main.py
├── shared/
│   └── utils.py
├── venv/
├── Makefile
└── README.md
```

## Uso
### Objetivos del Makefile

- **Crear un nuevo día (`create_day`)**
  Crea una nueva carpeta para un día específico con un archivo `main.py` y `input.txt`. Además, crea una nueva rama en el repositorio asociada al día y hace un commit inicial.
  ```bash
  make create_day DAY=01
  ```

- **Ejecutar un día específico (`run`)**
  Ejecuta el script de solución para el día indicado.
  ```bash
  make run DAY=01
  ```

- **Integrar cambios en la rama `main` (`merge_to_main`)**
  Integra los cambios de la rama del día actual (`dayXX`) en la rama `main`. También elimina la rama del día tanto local como remotamente.
  ```bash
  make merge_to_main DAY=01
  ```

## Estrategia de branching

1. Inicio de un nuevo día

Crear una nueva rama para el día específico desde la rama main:

```bash
git checkout dev
git pull origin dev
git checkout -b dayXX
```

2. Desarrollo
Trabajar en la rama del día (dayXX), asegurándote de mantener los cambios específicos para ese día. Añadir los archivos y realizar commits regularmente:

```bash
git add .
git commit -m "Add solution for day XX"
```

3. Integración a main

Una vez que la solución esté terminada y probada, hacer merge de dayXX a main:

```bash
git checkout main
git merge dayXX
```

### Visualización del flujo

```
main
  |
  |--- day01
  |--- day02
  |--- day03
```