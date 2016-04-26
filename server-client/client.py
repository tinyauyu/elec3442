import socket

PORT = 12349

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# now connect to the web server on port 80 - the normal http port
s.connect(('192.168.1.103', PORT))

s.send('hihi'.encode())
reply = s.recv(1024)

while True:
	cmd = raw_input('Enter your command: ')
	s.send(cmd.encode())
