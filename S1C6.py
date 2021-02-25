import binascii
import itertools

byte_string = b''.join([binascii.a2b_base64(line.strip()) for line in open("s1c6_cyphertext.txt").readlines()])


def count_set_bits(n: int) -> int:
    # Counter for storing number of bits set
    count = 0
    # Loop continues until n == 0
    while(n):
        # if least significant bit is set to 1, add 1 to count
        count += n & 1
        # shift right 1. This will move all the bits 1 place to the right. Leaving a zero at the most significant bit. Eg. 0b111 becomes 0b011
        n >>= 1
    return count


def hamming_distance(buf1: bytes, buf2: bytes) -> int:
    # Check if strings are equal in size
    assert len(buf1) == len(buf2)
    #print(f"Calculating hamming distance between {buf1} and {buf2}")
    # counter for hamming distance
    hm = 0
    for i in range(len(buf1)):
        # XOR the ordinal values for each of the characters in the given strings. The numbers of bits set in this number is the hamming distance between the two characters.
        number = buf1[i] ^ buf2[i]
        # Calculating the bits set (== hamming distance between the two characters)
        hm += count_set_bits(number)
    return hm


def split_in_chunks(iterable, blocksize: int) -> list:
    # chunks = []
    # Iterate over the entire text file in steps of the blocksize
    # for i in range(0, len(iterable), blocksize):
    # This will only append full length blocks. The last part of the file is skipped this way.
    #    if i < len(iterable) - blocksize:
    #        chunks.append(iterable[i:i + blocksize])
    chunks = [iterable[i:i + blocksize] for i in range(0, len(iterable), blocksize) if i < len(iterable) - blocksize]
    return chunks


def transposev2(text, key_size):
    chunks = split_in_chunks(byte_string, key_size)
    transposed = list(zip(*chunks))
    return transposed


def single_byte_xor(buf, i: int):
    '''
    :param buf: binary string
    :param i: single integer (0,255) to xor with
    :return: xored string and the integer used for the xor operation
    '''
    decoded = binascii.unhexlify(buf)
    my_list = [a ^ i for a in decoded]
    my_string = ''
    for number in my_list:
        my_string += chr(number)
    return (my_string, i)


def get_english_score(input_bytes):
    """
    Compares each input byte to a character frequency
    chart and returns the score of a message based on the
    relative frequency the characters occur in the English
    language
    Taken from https://laconicwolf.com/2018/05/29/cryptopals-challenge-3-single-byte-xor-cipher-in-python/
    :param input_bytes: The input string of bytes to have it's character's
                        frequencies analyzed.
    :returns: And integer representing the total sum of encountered character frequencies.
              Higher means a more-likely-valid english string.
    """
    # From https://en.wikipedia.org/wiki/Letter_frequency
    # with the exception of ' ', which I estimated.
    character_frequencies = {
        'a': .08167, 'b': .01492, 'c': .02782, 'd': .04253,
        'e': .12702, 'f': .02228, 'g': .02015, 'h': .06094,
        'i': .06094, 'j': .00153, 'k': .00772, 'l': .04025,
        'm': .02406, 'n': .06749, 'o': .07507, 'p': .01929,
        'q': .00095, 'r': .05987, 's': .06327, 't': .09056,
        'u': .02758, 'v': .00978, 'w': .02360, 'x': .00150,
        'y': .01974, 'z': .00074, ' ': .13000
    }
    return sum([character_frequencies.get(chr(byte), 0) for byte in input_bytes.lower()])

my_string = b"Hi This is an English sentence"
b= b"AAAAAAAAAE EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"
print(get_english_score(my_string))
print(get_english_score(b))


def transpose(text: bytes, keysize: int) -> list:
    '''
    Text is split up into chunks of keysize. A new block is created for every 1st, 2nd, 3rd (.. 29th)  byte of these chunks
    '''
    transposed_chunks = []
    for i in range(0, keysize):
        result = b''
        chunks = split_in_chunks(text, keysize)
        for chunk in chunks:
            result += chunk[i:i + 1]
        transposed_chunks.append(result)
    return transposed_chunks


def guess_key(blocks: list) -> str:
    possible_key = ''
    for chunk in blocks:
        chunk = binascii.hexlify(chunk)
        scores = {}
        for i in range(0, 255):
            xored, xor = single_byte_xor(chunk,i)
            xored = bytes(xored, "utf-8")
            score = get_english_score(xored)
            scores[i] = score
        sorted_scores = list(sorted(scores.items(), key=lambda kv: kv[1], reverse=True))
        top_score = chr(sorted_scores[0][0])
        possible_key += str(top_score)
    return possible_key


def repeating_xor(text, key):
    '''
    p is already in ordinal value. So no need for the ord() method.
    itertools.cycle will cycle over the key for the entire length of text
    Each character in text (p)  is XORED with every cycled character in key (k).
    '''
    return ''.join((chr(p ^ ord(k)) for p, k in zip(text, itertools.cycle(key))))


hm_= dict()
for i in range(2, 40):
    # Split text in keysize blocks
    blocks = split_in_chunks(byte_string,i)
    # create two blocks of keysize
    block_1 = blocks[0]
    block_2 = blocks[1]
    hamming_distances = []
    # Iterate over the all the blocks
    for block in blocks:
        # for each block calculate hamming distance between the block and block1 or block2
        hamming_distances.append(hamming_distance(block, block_1))
        hamming_distances.append(hamming_distance(block, block_2))
    # add all the hamming disances together and divide by number of hamming distances in the list
    mean = sum(hamming_distances)/len(hamming_distances)
    # devide by keysize
    normalized = mean / i
    # create a dictionary with keysize:normalized hamming distance pairs
    hm_[i] = normalized
    # sort dictionary by values, low to high
    sorted_hm = list(sorted(hm_.items(), key=lambda item: item[1]))

# Possible key length: 29, 4 and 5
top3_keys = sorted_hm[:3]
print("Possible keys:")
for key in top3_keys:
    print(key[0], end=" ")


ts = []
ts = transpose(byte_string,29)
#possible_key = guess_key(ts)
#print(repeating_xor(byte_string, possible_key))











