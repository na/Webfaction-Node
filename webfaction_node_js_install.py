-----BEGIN WEBFACTION INSTALL SCRIPT-----
#!/bin/env python

"""
node.js install/uninstall script for WebFaction.  Will install
code from hhttp://nodejs.org/dist/node-v0.1.98.tar.gz. This installs
node.js along with V8 engine. The node.js files
are found in ~/webapps/<app_name>/node-v0.1.98

autostart: Not Applicable
extra info: Number of jobs as integer

"""

from sys import argv, exit
from xmlrpclib import Server

def create(app_name, server, session_id):
    app = server.create_app(session_id, app_name, 'custom_app_with_port', False, '')

    cmd = """\
wget -q http://nodejs.org/dist/node-v0.1.98.tar.gz
tar fxz node-v0.1.98.tar.gz
rm node-v0.1.98.tar.gz
cd node-v0.1.98
./configure --jobs=%s --prefix=$HOME > configure-log 2>&1
make >> make-log 2>&1
make install >> install-log 2>&1
""" % str(extra_info)

    server.system(session_id, cmd)

    _file = """\
    var sys = require('sys'),
        http = require('http');
    http.createServer(function (req, res) {
        res.writeHead(200, {'Content-Type': 'text/plain'});
        res.end('Hello World');
    }).listen(%s, "127.0.0.1");
    sys.puts('Server listening on port %s');
    """ % (app['port'], app['port'])

    server.write_file(session_id, "server.js", _file)

    print "node app: %s created listening on port: %s " % (app['id'], app['port'])

def delete(app_name, server, session_id):
    server.delete_app(session_id, app_name)

if __name__ == '__main__':
    action, username, password, machine, app_name, autostart, extra_info = argv[1:]
    server = Server('https://api.webfaction.com/')
    session_id, account = server.login(username, password, machine)

    try:
        int(extra_info)
    except:
        print 'Extra information must be an integer.'
        exit()

    locals()[action](app_name, server, session_id)
-----END WEBFACTION INSTALL SCRIPT-----
