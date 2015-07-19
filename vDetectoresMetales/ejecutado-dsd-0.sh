sudo pip install virtualenv
sudo pip install Django
sudo pip install Pillow
sudo pip install Pillow
sudo pip install django-bootstrap3

virtualenv DetectoresMetales
cd DetectoresMetales
django-admin.py startproject DetectoresMetales



    #~ en consola mysql
        
        CREATE DATABASE DetectoresMetales CHARACTER SET utf8;
        create user el_usuario identified by 'la_contrasenia';
        grant all privileges on DetectoresMetales.* to el_usuario@localhost;
        UPDATE mysql.user SET Password=PASSWORD('la_contrasenia') WHERE User='el_usuario';



    #~ editado settins.py para MySQL, aplicaciones y templates

python manage.py migrate                  (lo solicita python manage.py runserver)
python manage.py startapp BBDD


# metido documentación del curso, en scripts iniciales y dado la estructura que indica

# colocado ficheros de tema bootstrap
# creado estructura vacía para la app BBDD... templates, static, model de Expedientes, formulario
