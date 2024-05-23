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
    