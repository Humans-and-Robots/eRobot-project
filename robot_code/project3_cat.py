#!/usr/bin/env python

import socket
import os
import sys
import sound
import api
import time
TCP_IP = '192.168.86.130'
#TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response


if api.Initialize():
    print("Initialized")
#    api.PlayAction(3)
    time.sleep(3)
else:
    print("Initialization failed")
    sys.exit(1)



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
        	os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a cat_smile.jpg")
		sound.sound_activate ("cat_happy")
		api.PlayAction(66)
    	if data == 'blink':
        	os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a blink.png")
    	if data == 'leftwink':  
        	os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a leftwink.png")
    	if data == 'rightwink':  
        	os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a rightwink.png")
    	if data == 'frown':  
        	os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a cat_angry.jpg")
		sound.sound_activate ("cat_angry")
                api.PlayAction(29)
    	if data == 'clench':  
                os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a cat_angry.jpg")
                sound.sound_activate ("cat_angry")
                api.PlayAction(29)    	
	if data == 'surprise':  
        	os.system("sudo fbi -T 2 -d /dev/fb1 -noverbose -a cat_surprise.jpg")
		sound.sound_activate ("cat_surprise")
                api.PlayAction(45)
    except:
        api.ServoShutdown()
        conn.close()

api.ServoShutdown()
conn.close() 
