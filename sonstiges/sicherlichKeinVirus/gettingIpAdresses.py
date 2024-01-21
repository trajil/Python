import socket
import requests

def get_ipv4_address():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as y:
            y.connect(("8.8.8.8", 80))                                      # PUBLIC GOOOGLE SERVER FOR IPv4
            host4, port = y.getsockname()
            return host4
    except Exception as e:
        return f"Failed to get IPv4 address: {e}"

def get_ipv6_address():
    try:
        with socket.socket(socket.AF_INET6, socket.SOCK_DGRAM) as s:
            s.connect(("2001:4860:4860::8888", 80))                         # PUBLIC GOOOGLE SERVER FOR IPv6
            host, port, flowinfo, scope_id = s.getsockname()
            return host
    except Exception as e:
        return f"Failed to get IPv6 address: {e}"


def get_public_ip_address():
    try:
        response = requests.get('https://api.ipify.org')                    # PUBLIC GOOOGLE SERVER FOR IPv4
        if response.status_code == 200:
            return response.text
        else:
            return "Unable to get public IP address"
    except Exception as e:
        return f"Failed to get public IP address: {e}"

# Example usage
ipv4_address = get_ipv4_address()
ipv6_address = get_ipv6_address()
public_ip_address = get_public_ip_address()

print(f"Host IPv6 Address: {ipv6_address}")
print(f"Host IPv4 Address: {ipv4_address}")
print(f"Public IP Address: {public_ip_address}")
