import socket
host ="127.0.0.1" #buraya server ip adresi tanımlanır ben localhostta çalıştırdım bu yüzden
port =80
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #Af_inet dağılımı ve sock stream protokolünü kullandım

s.bind((host,port)) #client in bağlanması için bağlantı noktası oluşturdum
s.listen() #dinlemeye başlanan satır parantez içine kaç client ile sınırlanabileceği yazılabilir

conn,addr = s.accept()

if conn:
    print(f"Yeni bir bağlantı var:{addr}")
    while True:
        ldata = conn.recv(1024) #dinlenilen veri 1024lük veri haline getiriliyor
        print(ldata.decode("utf-8").upper()) #gelen veri büyük harfe çevrilip ekrana yazıldı
        conn.sendall(ldata.upper()) #aynı veri büyük harfe çevrilip tekrar client e yollandı


