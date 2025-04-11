import socket
import json
import struct

def tplink_encrypt(data):
    key = 171
    result = b""
    for char in data:
        xor = key ^ ord(char)
        key = xor
        result += bytes([xor])
    return result

def tplink_decrypt(data):
    key = 171
    result = ""
    for byte in data:
        result += chr(byte ^ key)
        key = byte
    return result

def send_command(ip, port, payload):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))

    message = tplink_encrypt(json.dumps(payload))
    sock.send(struct.pack(">I", len(message)) + message)

    length = struct.unpack(">I", sock.recv(4))[0]
    response = sock.recv(length)

    sock.close()
    return tplink_decrypt(response)

# Send 'get_sysinfo' command to the smart plug
plug_ip = "192.168.12.18"
payload = {"system": {"get_sysinfo": {}}}

response = send_command(plug_ip, 9999, payload)
print(response)
