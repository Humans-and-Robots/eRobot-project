import socket
import Queue

UDP_IP = "127.0.0.1"
UDP_PORT = 30000

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

q = Queue.Queue(10)

def emotion_detect(q):
    smile_count = 0
    clench_count = 0
    neutral_count = 0
    smile = 'S'
    clench = 'G'
    neutral = 'neutral'
    window = []
    for i in range(q.qsize()):
	data = q.get()
	window.append(data)
	q.put(data)

    for data in window:
        if data.find(smile) == 0:
            data_copy = data[1:]
            if data_copy.isdigit():
                if int(data_copy) > 70:
                    smile_count += 1
        elif data.find(clench) == 0:
            data_copy = data[1:]
            if data_copy.isdigit():
                if int(data_copy) > 70:
                    clench_count += 1
        elif data == neutral:
            neutral_count += 1
    if smile_count > 5:
        return 'smile'
    elif clench_count > 4:
        return 'clench'
    else:
        return 'neutral'

while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    if q.full():
	q.get()
        q.put(data)
    else:
	q.put(data)
    print emotion_detect(q)
   # print q.qsize()
    # print "received message:", data
