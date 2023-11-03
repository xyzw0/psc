# CLIENT
import socket
def client_program():
client_socket = socket.socket() # instantiate
client_socket.connect((socket.gethostname(), 5000)) # connect to the server
message = input(" -> ") # take input
while message.lower().strip() != 'bye':
client_socket.send(message.encode()) # send message
data = client_socket.recv(1024).decode() # receive response
print('User - 1 (Server-Side): ' + data) # show in terminal
message = input(" -> ") # again take input
client_socket.close() # close the connection
if __name__ == '__main__':
client_program()
# ------ OUPTUT----------
# CLIENT SIDE:
# Hi User 1
# User-1: How u doin ??
# SERVER
import socket
def server_program():
server_socket = socket.socket() # get instance
server_socket.bind((socket.gethostname(),5000)) # bind host address and port to
server_socket.listen(2) # No of clients
conn , address = server_socket.accept() # accept new connection
print("Server Started : ")
while True:
data = conn.recv(1024).decode()
if not data:
break
print("User - 2 (Client-Side): " + str(data))
data = input(' -> ')
conn.send(data.encode()) # send data to the client
conn.close() # close the connection
if __name__ == '__main__':
server_program()
# ------ OUPTUT----------
#SERVER SIDE:
# User-2: Hi User 1
# How u doin ??
