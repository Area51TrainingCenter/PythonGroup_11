# Ejercicio #

## Modelos ##

Ya es hora de agregar modelos a tu proyecto django. Cuando Recuerda los comandos:

    # Revisamos si no hay errores con los cambios en los modelos de nuestra app1.
    python manage.py check app1

    # Aplicamos las migraciones a los modelos (necesario).
    python manage.py makemigrations

    # Podemos revisar el código sql de cada migración.
    python manage.py sqlmigrate app1 0001

    # Sincronizamos los modelos con la base de datos (necesario).
    python manage.py migrate

    # Creamos superusuario para el admin
    python manage.py createsuperuser
 
