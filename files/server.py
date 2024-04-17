import socket
import ssl

context=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.ca.cert",keyfile="server.ca.key")
server_socket=socket.socket()

server_socket.bind(('localhost',134))

server_socket.listen(2)

ser_socket,server_addr=server_socket.accept()
server_connections=context.wrap_socket(ser_socket,server_side=True)
while True:
    try:
        ser1=server_connections.recv(1024)
        print("Message",ser1.decode("utf-8"))
        msg_ser=input("Message for client= ")
        server_connections.send(bytes(msg_ser,"utf-8"))
    except KeyboardInterrupt:
        break;
        
      
server_connections.close()
server_socket.close()
    
    


