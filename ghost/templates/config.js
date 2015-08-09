var path = require('path'),
    config;

config = {
    production: {
        url: 'http://{{ ghost_domain }}',
        mail: {},
        database: {
            client: 'sqlite3',
            connection: {
                filename: path.join(__dirname, '/content/data/ghost.db')
            },
            debug: false
        },

        server: {
            host: '127.0.0.1',
            port: '{{ ghost_port }}'
        },
        mail: {
            transport: 'sendmail'
        }   
    }
};

module.exports = config;
