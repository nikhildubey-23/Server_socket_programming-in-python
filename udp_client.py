import socket as sc
#adding target host and target port 
target_host = "127.0.0.1"
target_port = 9987
#creating the socket object
client = sc.socket(sc.AF_INET,sc.SOCK_DGRAM)