import binascii

x = b'1c0111001f010100061a024b53535009181c'
y = b'686974207468652062756c6c277320657965'
expected = b'746865206b696420646f6e277420706c6179'

def fixed_xor(a, b):
    assert len(a) == len(b)
    a = binascii.unhexlify(a)
    b = binascii.unhexlify(b)
    return bytes([a[i] ^ b[i] for i in range(len(a))])



answer = fixed_xor(x,y)
print(binascii.hexlify(answer))

