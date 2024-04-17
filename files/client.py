import socket
import ssl

context=ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("server.ca.cert")
client_socket=socket.socket()
clisocket=context.wrap_socket(client_socket,server_hostname="localhost")
client=clisocket.connect(('localhost',134))
while True: 
    try:
        msg_cli=input("Message for server= ")
        clisocket.send(bytes(msg_cli,"utf-8"))
        cli=clisocket.recv(1024)
        print("message",cli.decode("utf-8"))
    except KeyboardInterrupt: 
        break
clisocket.close() 


