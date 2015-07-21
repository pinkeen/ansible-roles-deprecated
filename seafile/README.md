Seafile role
============

Sets up seafile with mysl and nginx as reverse-proxy.

HTTP sync is at `/seafhttp` and WebDAV is at `/seafdav`.

## Gotchas

You can change most of the config values and they should be updated, but:
 - Changing the data dir won't work due to how avatar dir is set up. Also existing data won't be moved (don't know how to do that idempotently.).
 - Version (`seafile_version`) bump as update may not work, because:
    - Config files may need new values.
    - There is no mysql migration, there's only schema init.

This role uses the mysql role, if you disable mysql networking or then seafile won't work.

## Required vars

- `seafile_db_pass` - mysql db pass - just invent something or use `password` lookup
- `seafile_server_domain` - the domain under which seahub will be accessible
- `seafile_secret_key` - generate your secret with sth like `python2 -c "import uuid ; print str(uuid.uuid4()) + str(uuid.uuid4())"`
- `seafile_admin_email` - admin's email (cannot be changed later via role)
- `seafile_admin_password` - admin's password (cannot be changed later via role)

## Interesting vars
- `seafile_max_upload_size` - max upload size (in MB)

### Customizations
- `seafile_css` - path to custom css
- `seafile_logo` - path to custom logo
- `seafile_logo_width`
- `seafile_logo_height`
- `seafile_site_title`
- `seafile_site_name`


## TODO
- memcached
- LDAP users
- some kind of upgrade role
- https