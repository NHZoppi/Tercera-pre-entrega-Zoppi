Django

instalación

Los requerimientos del proyecto, se encuentran dentro del archivo requirements.
Para instalar los paquetes de requirements el comando para la CMD es:
    pip install -r requirements.txt
    Solamente aplicamos este comando, cuando el entornos virtual este activado. Mas abajo esta explicado.

INSTALLED_APPS=[
...
'Django_filters',
...
]


Como iniciar el proyecto:
Debes tener un entorno virtual, que es donde van a ser instalados los paquetes de django y django_filter.

    Esto se hace en la consola de CMD.
    Crear entorno:

    python -m venv tutorial-env.

    Activar entorno:
    tutorial-env\Scripts\activate.bat

Si queres usar mi proyecto:

    git clone LinkRepositorio

Una vez clonado, nos tenemos que posicionar en la carpeta del proyecto. Te tiene que mostrar estas carpetas/archivos:

    -mipryoecto
        -manage.py
        -miproyecto
        -readme.txt
        -.gitignore
        -requirements.txt

una vez que nos posicionamos en la carpeta miproyecto, tipeamos en el CMD:

    python manage.py migrate

Esto nos creara la base de datos, con las tablas principales de django.

Ahora para actualizar los modelos personalizados. Debemos ejecutar este comando:

    python manage.py makemigrations

Y una vez mas para confirmar las migraciones de la App. Hacemos:

    python manage.py migrate
