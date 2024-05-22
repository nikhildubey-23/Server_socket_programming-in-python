import socket as sc
#step number 1 first create target host and target port for to connect with
target_host = "127.0.0.1"
target_port = 9956
# now second step is to create a socket object
client = sc.socket()
#now we connect to the client 
client.connect((target_host,target_port)) 
#now we send some data to  the server
client.send(b"i am anonymous clinet tell me your ip address\n")
#after getting the message server will response back so for to receive to the message we have tp create method 
response = client.recv(4049)
#after getting the response we have to decode the response 
print(response.decode())
#after everything get over we will close the client server
