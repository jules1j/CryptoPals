from binascii import a2b_base64, unhexlify, hexlify, b2a_base64

def fixed_xor(buffer1: bytes, buffer2: bytes) -> bytes:
    return bytes([(b1 ^ b2) for b1, b2 in zip(buffer1, buffer2)])

def hamming_distance(buffer1: bytes, buffer2: bytes) -> int:
    distance = sum(bin(i).count("1") for i in fixed_xor(buffer1, buffer2))
    return distance

byte_string = b''.join([a2b_base64(line.strip()) for line in open("s1c6_cyphertext.txt").readlines()])
keysize_distances = []
for keysize in range(2, 40):
    blocks = [byte_string[i * keysize: (i + 1) * keysize] for i in range(4)]
    distances = [hamming_distance(blocks[i], blocks[j]) for i in range(len(blocks)-1) for j in range(1, len(blocks))]
    distance = sum(distances) / len(distances)
    distance /= keysize
    keysize_distances.append((keysize, distance))
keysize = sorted(keysize_distances, key=lambda x: x[1])[0][0]

print(keysize)