# Webfaction Node Install Script

A script to install [node.js][] on webfaction using [webfaction's][] api.

## How to Use

Simply follow this [link][] which will take you to the Apps Add page on the webfaction control panel..

Now to run the included 'Hello World' example log in and run
    node ~/webapps/<app_name>/server.js

Then create a website with the nodeapp mounted on a domain

## Uninstall Node

To uniinstall [node.js][] log in and navigate to ~/webapps/<app_name>/node-v0.1.98 and excute
    make uninstall

[node.js]: http://nodejs.org
[webfaction's]:  http://www.webfaction.com?affiliate=nateanderson
[link]: https://panel.webfaction.com/app/create?script_url=http%3A%2F%2Fgithub.com%2Fna%2FWebfaction-Node%2Fraw%2Fmaster%2Fwebfaction_node_js_install.py
