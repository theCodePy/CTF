import socket 


host = "82e0d7457eedd925.247ctf.com"
port = 50424

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host, port))
    for i in range(500):
        data = s.recv(1024).decode()
        print(data)
        data = data.split("What is the answer to ")[1].strip().replace('?','')
        a , b = data.split(' + ')
        c = int(a) + int(b)
        print(c)
        message = f"{c}\r\n".encode()
        s.send(message)

    data = s.recv(1024).decode()
    print(data)
