import binascii
import base64


def hex_to_b64(s):
    #decoded = binascii.unhexlify(s)
    return base64.b64encode(s).decode('ascii')

if __name__ == "__main__":
    x = b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
    print(hex_to_b64(x))