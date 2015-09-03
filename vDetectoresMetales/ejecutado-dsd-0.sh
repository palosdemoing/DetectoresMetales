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
# creado estructura vacia para la app BBDD... templates, static, model de Expedientes, formulario



# Modificado el modelo Expedientes
# Añadido el manager por defecto de este modelo al admin site, editando BBDD/admin.py



Actualizado todo el proyecto en función al de ejemplo realizado en el curso, con todos
los elementos adaptados en nombres de variables y demás... a falta de ver si serán todos 
necesarios o que uso se puede hacer en nuestro escenario.

Falta: 
- las vistas de Solicitantes
- las templates de expedientes_··· por lo del delete, ver videos por lo del json y el
  ajax, aunque lo mismo lo tengo en la clase q sea
- hacer el syncdb de este modelo
- vincular en las plantillas estas vistas y los formularios y demás
- ver que tal el comando
- eliminar acentos de vocales y ñ
- realizar estructura de BBDD de los detectores
