import socket
import struct
import pickle
import cv2
import numpy as np
import pickle_compat

def initialize_server(tcp_ip, tcp_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((tcp_ip, tcp_port))
    s.listen(True)
    sock, addr = s.accept()
    print("Connected with client {}:{}".format(tcp_ip, tcp_port))
    return sock, addr

def initialize_client(tcp_ip, tcp_port):
    sock = socket.socket()
    sock.connect((tcp_ip, tcp_port))
    print("Connected wtih server {}:{}".format(tcp_ip, tcp_port))
    return sock

def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf

def recvall_pickle(sock):
    pickle_compat.patch()
    packed_length = recvall(sock, 8) 
    length = struct.unpack("L", packed_length)[0]
    string_data = recvall(sock, int(length))
    try:
        # python 3 -> 2
        data = pickle.loads(string_data)
    except TypeError:
        # python 2 -> 3
        data = pickle.loads(string_data, encoding="bytes")
    pickle_compat.unpatch()
    return data

def sendall_pickle(sock, data):
    data = pickle.dumps(data, protocol=2)
    sock.send(struct.pack("L", len(data)))
    sock.send(data)

def recvall_image(sock):
    length = recvall(sock, 16) 
    string_data = recvall(sock, int(length))
    data = np.fromstring(string_data, dtype='uint8')
    return cv2.imdecode(data, 1)

def sendall_image(sock, image):
    encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
    result, imgencode = cv2.imencode('.jpg', image, encode_param)
    data = np.array(imgencode)
    string_data = data.tostring()
    try:
        # python 3 -> 2
        sock.send(str(len(string_data)).ljust(16))
    except TypeError:
        # python 2 -> 3
        sock.send(str(len(string_data)).ljust(16).encode())
    sock.send(string_data)