'''
Repeating XOR
'''

import binascii
import itertools

PLAINTEXT = '''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''
KEY = 'ICE'
EXPECTED = b'0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f '


def repeating_xor(text, key):
    return ''.join((chr(ord(p) ^ ord(k)) for p, k in zip(text, itertools.cycle(key))))



if __name__ == "__main__":
    # Encrypt plaintext
    cyphertext = repeating_xor(PLAINTEXT, KEY)
    print(f"Encrypted text: {cyphertext}")

    # Decrypt cyphertext
    plain = repeating_xor(cyphertext, KEY)
    print(f"Plaintext: {plain}")

    # Converting cyphertext to a hexadecimal format
    cyphertext = binascii.hexlify(bytes(repeating_xor(PLAINTEXT, KEY), 'utf-8'))

    # Comparing hexed cyphertext to expeted value
    if EXPECTED == cyphertext:
        print("Succes")