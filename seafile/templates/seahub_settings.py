SECRET_KEY = "{{ seafile_secret_key }}"

FILE_SERVER_ROOT = '{{ seafile_service_url }}/seafhttp'

EMAIL_USE_TLS = False
EMAIL_HOST = 'localhost'
EMAIL_PORT = '25'
DEFAULT_FROM_EMAIL = '{{ seafile_from_email }}'
SERVER_EMAIL = '{{ seafile_from_email }}'

SITE_NAME = '{{ seafile_site_name }}'
SITE_TITLE = '{{ seafile_site_title }}'

{% if seafile_logo is defined %}
LOGO_PATH = 'custom/logo.png'
LOGO_WIDTH = {{ seafile_logo_width }}
LOGO_HEIGHT = {{ seafile_logo_height }}
{% endif %}

{% if seafile_css is defined %}
BRANDING_CSS = 'custom/styles.css'
{% endif %}

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

