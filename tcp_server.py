import socket as sc
import threading  as th
#now we set ip and port for the server
ip = "127.0.0.1"
port = 9000
def main():
    #now we create object for the socket 
    server = sc.socket(sc.AF_INET,sc.SOCK_STREAM)
    