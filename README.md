# easy-tcp-python2-3

- easy socket programming between python 2 and 3 without compatibility issues
- receive and send the list, json or image via pickle and cv2 


## Dependencies
- python 2 or python 3 (>=3.7)
- opencv-python
- [pickle-compat](https://pypi.org/project/pickle-compat/)

## Installation
```
$ pip install easy_tcp_python2_3
```

## Usage

- send a sample list and image from a server to client
```
# server
from easy_tcp_python2_3 import socket_utils as su
import numpy as np
from PIL import Image
sock, add = su.initialize_server('localhost', 7777)
sample_list = [1, 2]
su.sendall_pickle(sock, sample_list)
sample_image = np.uint8(np.zeros([480, 640]))
su.sendall_image(sock, sample_image)

# client
from easy_tcp_python2_3 import socket_utils as su
sock = su.initialize_client('localhost', 7777)
recv_list = su.recvall_pickle(sock)
print(recv_list)
recv_image = su.recvall_image(sock)
print(recv_image)
```

## Authors
* **Seunghyeok Back** [seungback](https://github.com/SeungBack)

## License
This project is licensed under the MIT License
