
**📄 net_info.py**
```python
import socket
import uuid

hostname = socket.gethostname()
ip_adresse = socket.gethostbyname(hostname)
mac_adresse = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff)
                        for elements in range(0, 8*6, 8)][::-1])

print(f"Hostname: {hostname}")
print(f"IP-Adresse: {ip_adresse}")
print(f"MAC-Adresse: {mac_adresse}")
