import socket
HOST = '127.0.0.1'
PORT = 8080
sock = socket.socket()
sock.bind((HOST, PORT))
sock.listen(1)
c, a = sock.accept()
allowed_keys = [5, 7, 13, 15, 157, 199]
connect = 'Connect: ' + str(a)
print(connect)
fi = open('ports.txt','a+')
fi.write('\n' + connect + '; ')
fi.close() 

while True:
    data = c.recv(1024)
    data = data.decode('utf-8')
    if data:
        break
new_data = data.split(' ')
g = int(new_data[0])
p = int(new_data[1])
a = int(new_data[2])
A = int(new_data[3])

if a in allowed_keys:
	b = int(input("Input b > "))
	if b in allowed_keys:
		file = open('keys.txt', 'a+')
		file.write('\ Private key b: ' + str(b))
		B = pow(g, b) % p
		c.send(str(B).encode('utf-8'))
		c.close()
		file.close()
		K = pow(A, b) % p
		print("Key > " + str(K))
		input("Done.")
		file.close()
	else:
		print('Unresolved private key!')
else:
	print('Unresolved private key!')
