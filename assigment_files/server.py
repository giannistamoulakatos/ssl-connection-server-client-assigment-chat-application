import socket
import ssl

context=ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
context.load_cert_chain(certfile="server.ca.cert",keyfile="server.ca.key")
server_socket=socket.socket()

server_socket.bind(('localhost',134))

server_socket.listen(2)

while True:
    ser_socket,server_addr=server_socket.accept()
    server_connections=context.wrap_socket(ser_socket,server_side=True)
    server_connections.send(bytes("client hello","utf-8"))
    ser=server_connections.recv(1024)
    print(ser.decode("utf-8"))
    server_connections.close()
    
    
    


