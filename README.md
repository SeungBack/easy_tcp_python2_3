# easy-tcp-python2-3

[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
[![PyPI version](https://badge.fury.io/py/easy-tcp-python2-3.svg)](https://badge.fury.io/py/easy-tcp-python2-3)
[![PyPI license](https://img.shields.io/pypi/l/ansicolortags.svg)](https://github.com/SeungBack/easy_tcp_python2_3)
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FSeungBack%2Feasy_tcp_python2_3&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)
[![Python 2.7](https://img.shields.io/badge/python-2.7-blue.svg)](https://www.python.org/downloads/release/python-270/)
[![Python 3](https://img.shields.io/badge/python-3-blue.svg)](https://www.python.org/downloads/release/python-370/)
[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/SeungBack/easy_tcp_python2_3/issues)


- easy socket programming between python 2 and 3 without compatibility issues
- receive and send the list, json or image via pickle and cv2 (jpeg)

## Dependencies
- python 2 or python 3 (>=3.7)
- opencv-python
- [pickle-compat](https://pypi.org/project/pickle-compat/)

## Installation
```
$ pip install easy-tcp-python2-3
```

## Usage

send a sample list and image from a server to client
### Server
```
from easy_tcp_python2_3 import socket_utils as su
import numpy as np
sock, add = su.initialize_server('localhost', 7777)
sample_list = [1, 2]
print("Send list:, sample_list)
su.sendall_pickle(sock, sample_list)
sample_image = np.uint8(np.zeros([480, 640]))
print("Send image:, sample_image.shape)
su.sendall_image(sock, sample_image)
```

### Client
```
from easy_tcp_python2_3 import socket_utils as su
sock = su.initialize_client('localhost', 7777)
recv_list = su.recvall_pickle(sock)
print("Received list:", recv_list)
recv_image = su.recvall_image(sock)
print("Received image:"recv_image.shape)
```

## Authors
* **Seunghyeok Back** [seungback](https://github.com/SeungBack)

## License
This project is licensed under the MIT License
