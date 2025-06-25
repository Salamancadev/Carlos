# ⚙️ Proyecto Django + MySQL: Sistema STK

Este repositorio contiene la configuración base de un proyecto Django con conexión a una base de datos MySQL, organizado para facilitar su instalación y despliegue local.

---

## 📁 Requisitos previos

Antes de comenzar, asegúrate de tener instalado:

- Python 3.10 o superior
- MySQL Server
- Git
- Visual Studio Code (opcional pero recomendado)

---

## 🚀 Instrucciones para levantar el proyecto

Sigue estos pasos para clonar y ejecutar el proyecto en tu equipo.

---

### 1️⃣ Clona el repositorio

```bash
git clone git@github.com:Salamancadev/Carlos.git
cd Carlos
2️⃣ Crea y activa un entorno virtual
bash
Copiar
Editar
python -m venv env
# En Windows:
env\Scripts\activate
# En Linux/Mac:
source env/bin/activate
3️⃣ Instala las dependencias
bash
Copiar
Editar
pip install -r requirements.txt
4️⃣ Configura la base de datos MySQL
Crea una base de datos en tu servidor MySQL llamada, por ejemplo, stk_db.

Luego edita el archivo config/settings.py en la sección DATABASES con tus credenciales:

python
Copiar
Editar
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'stk_db',
        'USER': 'tu_usuario_mysql',
        'PASSWORD': 'tu_contraseña_mysql',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}
5️⃣ Aplica migraciones
bash
Copiar
Editar
python manage.py migrate
6️⃣ Ejecuta el servidor
bash
Copiar
Editar
python manage.py runserver
Abre tu navegador en http://127.0.0.1:8000 para ver el proyecto en ejecución.

🧾 Archivos importantes
Archivo	Descripción
requirements.txt	Lista de dependencias necesarias
.gitignore	Archivos que no se suben al repositorio (como el entorno virtual)
config/	Proyecto Django principal
manage.py	Comando principal de Django

🧑‍💻 Autor
Santiago Salamanca
Programa ADSO – SENA
6.º trimestre
Fecha: Junio de 2025

yaml
Copiar
Editar
