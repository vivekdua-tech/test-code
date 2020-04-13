import socket, time

def server(handler, host, port):
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    print('Server up, running, and waiting for call')
    try:
        while True:
            c, a = s.accept()
            try:
                handler(c, a)
            finally:
                c.close()
    finally:
        s.close()

def time_handler(c, a):
    print("Received connection from", a)
    c.sendall(b"Hello %s\r\n" % a[0].encode())
    c.sendall(b"The time is %s\r\n" % time.ctime().encode())

def slow_time_handler(c, a):
    print("Received connection from", a)
    c.sendall(b"Hello %s\r\n" % a[0].encode())
    c.sendall(b"The time is %s\r\n" % time.ctime().encode())
    for i in range(10):
        c.sendall(b"The count is %d\r\n" % i)
        time.sleep(1)

if __name__ == '__main__':

    server(slow_time_handler, 'localhost', 9605)
