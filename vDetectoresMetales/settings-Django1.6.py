# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/opt/DetectoresMetales/my.cnf',
			'init_command': 'SET storage_engine=INNODB',
        },
    }
}

