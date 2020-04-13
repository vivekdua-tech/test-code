import socket

host = b'www.jython.org'
port = 80
resource = b'/'

request =  b'GET %s HTTP/1.1\r\n' % resource
request += b'Host: %s\r\n' % host
request += b'Connection: close\r\n'
request += b'\r\n' 

s = socket.socket()
try:
    s.connect((host, port))
    s.send(request)

    blocks = []
    while True:
        block = s.recv(4096)
        if not block:
            break
        blocks.append(block)
    page = b''.join(blocks)
    print(page.replace(b'\r\n', b'\n').decode())
finally:
    s.close()

