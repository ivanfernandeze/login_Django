# Proyecto de Login con Django

Este proyecto es una aplicación de login construida con Django. A continuación, se proporciona una guía para instalar las dependencias necesarias y una descripción de las tecnologías utilizadas para implementar el sistema de autenticación.

## Requisitos

- Python 3.x
- Django 3.x o superior
- pip (gestor de paquetes de Python)

## Instalación

1. Clona el repositorio en tu máquina local:
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd login_django
    ```

2. Instala las dependencias del proyecto:
    ```bash
    pip install -r requirements.txt
    ```

3. Realiza las migraciones de la base de datos:
    ```bash
    python manage.py migrate
    ```

4. Ejecuta el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```

## Tecnologías Utilizadas

- **Django**: Framework web de alto nivel que permite el desarrollo rápido de aplicaciones web seguras y mantenibles.
- **Django Authentication**: Sistema de autenticación integrado en Django que proporciona funcionalidades como el inicio de sesión, cierre de sesión, y gestión de usuarios.

## Funcionalidades del Login

- **Registro de Usuarios**: Permite a los nuevos usuarios crear una cuenta.
- **Inicio de Sesión**: Permite a los usuarios registrados iniciar sesión en la aplicación.
- **Cierre de Sesión**: Permite a los usuarios cerrar sesión de manera segura.
- **Recuperación de Contraseña**: Permite a los usuarios recuperar su contraseña en caso de olvido.

## Estructura del Proyecto

- `login_django/`: Directorio principal del proyecto.
- `login_django/settings.py`: Configuración del proyecto.
- `login_django/urls.py`: Definición de las rutas del proyecto.
- `login_django/views.py`: Vistas del proyecto.
- `templates/`: Directorio que contiene las plantillas HTML.

## Contribuir

Si deseas contribuir a este proyecto, por favor sigue los siguientes pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -am 'Añadir nueva funcionalidad'`).
4. Sube tus cambios a tu fork (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.

## Creación del Superusuario

Para acceder al panel de administración de Django y gestionar usuarios y otros modelos, sigue estos pasos:

1. Ejecuta el comando:
    ```bash
    python manage.py createsuperuser
    ```
2. Ingresa el nombre de usuario, correo electrónico y contraseña cuando se te solicite.
3. Accede al panel de administración en `http://127.0.0.1:8000/admin/` con las credenciales del superusuario.
