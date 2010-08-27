-----BEGIN WEBFACTION INSTALL SCRIPT-----
#!/bin/env python

"""
Node v0.2.0

node.js install/uninstall script for WebFaction.  Will install
code from http://nodejs.org/dist/node-v0.2.0.tar.gz. This installs
node.js along with V8 engine.

To test if node is working log into your account and run the server.js script.  Then create a website with with the app mounted at '/'.  Then open
your browser and go to the website you just created and you should see "Hello World".

autostart: Not Applicable
extra info: Not Applicable

"""

from sys import argv, exit
from xmlrpclib import Server

def create(app_name, server, session_id):

    #define node version
    node_version = 'node-v0.2.0'

    # initial config
    home_dir = '%s/%s' % (account['home'], username)
    app_dir = '%s/webapps/%s' % (home_dir, app_name)
    bin_dir = '%s/bin' % app_dir
    src_dir = '%s/src' % app_dir

    # Create new "Custom App Listening on Port"
    app = server.create_app(session_id, app_name, 'custom_app_with_port', False, '')

    # download and install app
    cmd = 'cd;'
    cmd += 'mkdir -p %s;' % bin_dir
    cmd += 'mkdir -p %s;' % src_dir
    cmd += 'cd %s;' % src_dir
    cmd += 'wget -q http://nodejs.org/dist/%s.tar.gz > /dev/null 2>&1;' % node_version
    cmd += 'tar fxz %s.tar.gz > /dev/null 2>&1;' % node_version
    cmd += 'rm %s.tar.gz;' % node_version
    cmd += 'cd %s/%s;' % (src_dir, node_version)
    cmd += './configure --jobs=1 --prefix=%s > /dev/null 2>&1;' % app_dir
    cmd += 'make > /dev/null 2>&1;'
    cmd += 'make install > /dev/null 2>&1;'
    cmd += 'cd;'
    cmd += 'rm -rf %s;' % src_dir
    server.system(session_id, cmd)

    # create a "hello world" file to use with node
    filename = '%s/server.js' % app_dir
    _file = """\
#!%s/node
var sys = require('sys'),
    http = require('http');

http.createServer(function (req, res) {
    res.writeHead(200, {'Content-Type': 'text/plain'});
    res.end('Hello World');
}).listen(%s, "127.0.0.1");

sys.puts('Server listening on port %s');
    """ % (bin_dir, app['port'], app['port'])
    server.write_file(session_id, filename, _file)

    # change script to executable
    cmd = 'chmod 711 %s' % filename
    server.system(session_id, cmd)

    print "node app: %s created listening on port: %s " % (app['id'], app['port'])

def delete(app_name, server, session_id):
    server.delete_app(session_id, app_name)

if __name__ == '__main__':
    action, username, password, machine, app_name, autostart, extra_info = argv[1:]
    server = Server('https://api.webfaction.com/')
    session_id, account = server.login(username, password, machine)

    locals()[action](app_name, server, session_id)
-----END WEBFACTION INSTALL SCRIPT-----
