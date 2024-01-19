### GETTIN IP_ADRESSES ###
import socket
def get_ipv6_address():
    # Create a socket using AF_INET6 as the address family
    with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
        # Connect to a remote server using IPv6
        # You can use any public IPv6 server, here I'm using Google's public DNS IPv6
        s.connect(("2001:4860:4860::8888", 80))
        # Get the local address to which the socket is bound
        # The address is a four-tuple (host, port, flowinfo, scope_id)
        host, port, flowinfo, scope_id = s.getsockname()
        return host
# ipv6_address = get_ipv6_address()
# print(f"Host IPv6 Address: {ipv6_address}")

def get_ipv4_address():
    # Create a socket using AF_INET as the address family
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as y:

        y.connect(("8.8.8.8", 80))

        host4, port = y.getsockname()
        return host4
ipv4_address = get_ipv4_address()
#print(f"Host IPv4 Address: {ipv4_address}")


import requests
def get_public_ip_address():
    response = requests.get('https://api.ipify.org')
    if response.status_code == 200:
        return response.text
    else:
        return "Unable to get public IP address"

public_ip_address = get_public_ip_address()
#print(f"Public IP Address: {public_ip_address}")
