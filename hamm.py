

def hamming_distance(buf1, buf2):
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

def count_set_bits(n):
    # Counter for storing number of bits set
    count = 0
    # Loop continues until n == 0
    while(n):
        # if least significant bit is set to 1, add 1 to count
        count += n & 1
        # shift right 1. This will move all the bits 1 place to the right. Leaving a zero at the most significant bit. Eg. 0b111 becomes 0b011
        n >>= 1
    return count

if __name__ == "__main__":
    # Using byte arrays to store the strings, so we don't have to use ord() all the time
    b1 = bytearray(b"this is a test")
    b2 = bytearray(b"wokka wokka!!!")
    print(hamming_distance(b1, b2))
