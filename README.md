
# Proyecto Flask MySQL

Este proyecto es una aplicación web básica desarrollada con el framework Flask y utilizando MySQL como base de datos. La estructura del proyecto está organizada para facilitar el desarrollo y mantenimiento de la aplicación.

## Estructura del Proyecto

```plaintext
Proyecto Flask MySQL/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   └── templates/
│       └── base.html
│   └── static/
│       ├── css/
│       ├── js/
│       └── img/
│
├── config/
│   └── config.py
│
├── scripts/
│   └── init_db.py
│
└── app.py
```

## Descripción de los Directorios y Archivos

- `app/`: Contiene la aplicación principal.
  - `__init__.py`: Inicializa la aplicación Flask.
  - `routes.py`: Define las rutas de la aplicación.
  - `models.py`: Define los modelos de la base de datos.
  - `templates/`: Contiene las plantillas HTML.
    - `base.html`: Plantilla base.
  - `static/`: Archivos estáticos (CSS, JS, imágenes).
    - `css/`: Archivos CSS.
    - `js/`: Archivos JavaScript.
    - `img/`: Imágenes.

- `config/`: Archivos de configuración.
  - `config.py`: Configuración de la aplicación.

- `scripts/`: Scripts de base de datos y otros scripts de utilidad.
  - `init_db.py`: Inicializa la base de datos.

- `app.py`: Archivo principal para ejecutar la aplicación Flask.

## Requisitos

- Python 3.x
- Flask
- MySQL

## Instalación

1. Clona el repositorio:
   ```sh
   git clone https://github.com/tu_usuario/proyecto-flask-mysql.git
   cd proyecto-flask-mysql
   ```

2. Crea y activa un entorno virtual (opcional pero recomendado):
   ```sh
   python -m venv venv
   venv\Scripts\activate  # En Windows
   source venv/bin/activate  # En Linux/MacOS
   ```

3. Instala las dependencias:
   ```sh
   pip install -r requirements.txt
   ```

4. Configura la base de datos en `config/config.py`.

5. Inicializa la base de datos:
   ```sh
   python scripts/init_db.py
   ```

6. Ejecuta la aplicación:
   ```sh
   python app.py
   ```

## Uso

Accede a la aplicación en tu navegador en `http://localhost:5000`.

## Contribución

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tu rama (`git push origin feature/nueva-funcionalidad`).
5. Crea un nuevo Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo `LICENSE` para más información.

---