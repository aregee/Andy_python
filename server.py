#
#!/usr/bin/env python2.7
# -*- coding: utf-8 -*- 
#_author_:Aregee:rahul.nbg@gmail.com
"""A Simple HTTP server on Android :)"""

import sys
import BaseHTTPServer
import android
from os import chdir
chdir("/sdcard/")
from SimpleHTTPServer import SimpleHTTPRequestHandler

droid=android.Android()

HandlerClass = SimpleHTTPRequestHandler
ServerClass  = BaseHTTPServer.HTTPServer
Protocol     = "HTTP/1.0"

if sys.argv[1:]:
    port = int(sys.argv[1])
else:
    port = 8000
server_address = ('127.8.0.1', port)

HandlerClass.protocol_version = Protocol
httpd = ServerClass(server_address, HandlerClass)

sa = httpd.socket.getsockname()
print "Serving HTTP on", sa[0], "port", sa[1], "..."

a = sa[0]
b=  sa[1]
list =['Http:%s , Port :%s ' % (sa[0],sa[1])]
droid.makeToast("server bitching ")
 
droid.makeToast( 'Http:%s, Port :%s' % (sa[0],sa[1]) )
url = 'http://127.8.0.1:8000'
droid.startActivity('android.intent.action.VIEW',url) 
 
droid.dialogCreateAlert("Serving http on") 
droid.dialogSetItems(list)
droid.dialogShow() 

httpd.serve_forever()


