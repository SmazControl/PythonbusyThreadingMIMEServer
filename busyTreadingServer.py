# -*- coding: utf-8 -*-
"""
busyThreading MIMEServer Example
Created on Sun May 19 06:59:10 2019

@author: Bunnavit Sawangpiriyakij
"""
import http.server
from http.server import HTTPServer, BaseHTTPRequestHandler
import time
import threading 

PORT = 8080
timeout= 1

class WebHTTPServer(HTTPServer):
    timeout = 2
    daemon_threads = True
    allow_reuse_address = True    
    def server_bind(self):
        HTTPServer.server_bind(self)
        self.socket.settimeout(timeout)
        
Handler = http.server.SimpleHTTPRequestHandler

Handler.extensions_map={
        '.manifest': 'text/cache-manifest',
	'.html': 'text/html',
        '.png': 'image/png',
	'.jpg': 'image/jpg',
	'.svg':	'image/svg+xml',
	'.css':	'text/css',
	'.js':	'application/x-javascript',
	'': 'application/octet-stream', # Default
    }

class MIMEServerThread(threading.Thread):
    
    def __init__(self):
        self.busy = False        
        threading.Thread.__init__(self)

    def run(self):
        self.busy = True
        # HTTP Server Section
        try:
            httpd = WebHTTPServer(("", PORT), Handler)
            print("serving at port", PORT)
        except:
            pass    
        try:
            httpd.handle_request()
        except:
            pass
        self.busy = False 
        
server = MIMEServerThread()        
# Loop until the user clicks the close button.
done = False
count = 0
while not done:
    
    if server.busy == False:
        server = MIMEServerThread()        
        server.start()
    else:
        # only print pass 1 time in 10 time
        if count>=9:
           print("pass")
           count=0
        else:
           count+=1
    time.sleep(0.1)
        
        
        
        
        
