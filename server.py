# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 18:09:59 2017

@author: Daniel
"""

import os
import http.server
import socketserver

PORT = int(os.getenv('VCAP_APP_PORT', '8000'))

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer(("", PORT), Handler)

print("serving at port", PORT)
httpd.serve_forever()