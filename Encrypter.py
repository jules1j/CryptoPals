from S1C5 import repeating_xor
KEY = 'BOOMDAGGA'
with open("test.txt", 'r') as fh:
    b_array_list = []
    for line in fh:
        b_array_list.append(line.rstrip())

with open("encrypted.txt", "w") as testfile:
    test_list = []
    for line in b_array_list:
        testfile.write(repeating_xor(line,KEY) + '\n')

with open("decrypted.txt", "w") as my_file:
    cypher = open("encrypted.txt", 'r')
    cypher_list = []
    for text in cypher:
        cypher_list.append(text.rstrip('\n'))
    for line in cypher_list:
        my_file.write(repeating_xor(line, KEY) + '\n')
