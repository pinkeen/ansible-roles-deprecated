SECRET_KEY = "{{ seafile_secret_key }}"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ seafile_seahub_db_name }}',
        'USER': '{{ seafile_user }}',
        'PASSWORD': '{{ seafile_db_pass }}',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        }
    }
}

