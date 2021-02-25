
import operator
import binascii

ETAOIN = 'ETAOINSHRDLCUMWFGYPBVKJXQZ'
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open("S1C4input.txt", "rb") as fh:
    b_array_list =[]
    for line in fh:
        b_array_list.append(line.strip())


def single_byte_xor(buf, i):
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


def get_letter_score(words):
    '''
    This function will return the percentage of alphabetic characters in a given string
    '''
    score = 0
    for word in words:
        if 65 <= ord(word) <= 90 or 97 <= ord(word) <= 122:
            score += 1
    if score > 0:
        return score/ len(words)
    else :
        return score


def get_letter_count(message):
    '''
    This function will return the letter count for a given string
    '''
    letterCount = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0,
                   'G': 0, 'H': 0, 'I': 0, 'J': 0, 'K': 0, 'L': 0, 'M': 0, 'N': 0,
                   'O': 0, 'P': 0, 'Q': 0, 'R': 0, 'S': 0, 'T': 0, 'U': 0, 'V': 0,
                   'W': 0, 'X': 0, 'Y': 0, 'Z': 0}
    for letter in message.upper():
        if letter in LETTERS:
            letterCount[letter] += 1
    return letterCount


def get_frequency_score(message):
    '''
    Returns the amount of letters in a frequency count dictionary that matches the frequency count of the english language
        for the six most common and the last six least common charcters in this frequency count.
    '''
    english_match = 0
    letter_count = get_letter_count(message)
    sorted_d = dict(sorted(letter_count.items(), key=operator.itemgetter(1), reverse=True))
    frequency_order = list(sorted_d.keys())
    for letter in frequency_order[:6]:
        if letter in ETAOIN[0:6]:
            english_match += 1
    for letter in frequency_order[-6:]:
        if letter in ETAOIN[-6:]:
            english_match += 1
    return english_match

if __name__ == "__main__":
    for b_array in b_array_list:
        for i in range(0, 256):
            xored, xor = single_byte_xor(b_array, i)
            letter_score = get_letter_score(xored)
            frequency_score = get_frequency_score(xored)
            if letter_score > 0.75:
                if frequency_score > 7:
                    print(f"Decoded sentence:\t {xored} ")
                    print(f"\t[*] LETTER Score:{letter_score*100}% alphabetic characters")
                    print(f"\t[*] FREQUENCY Score: {frequency_score} matches with ETAION frequency count ")
                    print(f"\t[*] Xored with {chr(xor)} or in ordinal value: {xor}")
                    print("-----------------------------------------------------------")




