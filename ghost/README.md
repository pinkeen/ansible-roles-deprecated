Ghost role
==========

Sets up ghost blogging software with nginx as reverse-proxy, sqlite for storage and local postfix for email.

## Required vars
- `ghost_domain` - Hostname of your new shiny blog.

## Interesting vars
- `ghost_themes` - List of git repo URIs which contain ghost themes that will be installed.

## TODO
- MySQL
- Scalability? More processes?
- Use forever or some other node process manager
