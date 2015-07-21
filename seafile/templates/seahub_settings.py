SECRET_KEY = "{{ seafile_secret_key }}"

FILE_SERVER_ROOT = '{{ seafile_service_url }}/seafhttp'

EMAIL_USE_TLS = False
EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
DEFAULT_FROM_EMAIL = '{{ seafile_from_email }}'
SERVER_EMAIL = '{{ seafile_from_email }}'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '{{ seafile_seahub_db_name }}',
        'USER': '{{ seafile_user }}',
        'PASSWORD': '{{ seafile_db_pass }}',
        'HOST': '{{ seafile_mysql_ip }}',
        'PORT': '{{ seafile_mysql_port }}',
        'OPTIONS': {
            'init_command': 'SET storage_engine=INNODB',
        }
    }
}

