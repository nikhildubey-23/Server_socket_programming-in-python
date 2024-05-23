import socket as sc
import threading  as th
#now we set ip and port for the server
ip = "127.0.0.1"
port = 9000
def main():
    #now we create object for the socket 
    server = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
    #now we bind the ip and port 
    server.bind((ip,port))
    #now we listen the upcoming client ip address and port which is used by the client  
    server.listen(6)
    print(f"listening on {ip}:{port} \n ")
    while True:
        client , address =server.accept()
        print(f"accepted connection form {address[0]}:{address[1]}")
        client_handler = th.Thread(target=handle_client,args=(client,))
        client_handler.start()
def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f"Received:{request.decode()}")
        sock.send(b'ACK')
if __name__=='__main__':
    main()
    


