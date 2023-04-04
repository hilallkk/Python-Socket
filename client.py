import socket
host="127.0.0.1"
port =80

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while True:
    data = input("Mesaj:") #sunucuya gönderilecek mesaj 
    s.sendall(data.encode("utf-8"))
    ldata = s.recv(1024)
    print("Gelen Mesaj:" + ldata.decode("utf-8"))


   

      