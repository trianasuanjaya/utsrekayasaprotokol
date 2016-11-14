import socket
import time;
import datetime

s=socket.socket()
host = socket.gethostname()
port = 12345
s.bind ((host,port))
s.listen(5)
while True:
    c,addr = s.accept()
    print ('daftar Printah') ,c.recv(1024)
    print ('dari'), addr
    localtime = time.localtime(time.time())
    dt = datetime.datetime(*localtime[:6])
    print "Local current time :", localtime
    c.send(dt.strftime('Waktu : pukul %H : %M'))
    
    c.close()
