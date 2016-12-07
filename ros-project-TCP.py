#!/usr/bin/env python

import socket
import os
import sys

#TCP_IP = '192.168.86.134'
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response



s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

print 'Connection address:', addr
while 1:
    try:
    	data = conn.recv(BUFFER_SIZE)
    	if not data: break
    	print "received data:", data
 
   	if data == 'smile':
    		print "simle"
	if data == 'blink':
    	if data == 'rightwink':  
    	if data == 'frown':  
    	if data == 'clench':  
    	if data == 'surprise':  

    except:
        conn.close()

conn.close() 
