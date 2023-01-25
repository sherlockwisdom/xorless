#!/usr/bin/env python3


"""
Trying out the implementation of xor
in modern python to see if I can replicate
the modern data mirroring behaviour
"""

"""
Random encryption key has to be the same length as the data for the math
XOR properties to hold true
"""

def print_bytes(data: str):
    return (r'\x' + r'\x'.join(f'{b:02x}' for b in bytes(data, 'utf8')))

def get_binary(data):
    # binary = [f'{str.encode(d):0>8b}' for d in data]
    # data = str.encode(data)
    # binary = [print(f'{d:0>8b}') for d in data]
    # binary = [f'{d:0>8b}' for d in data]
    binary = [f'{d:0>8b}' for d in data]

    return binary

def get_inverse(data):
    '''data = binary input'''
    inverse = ''.join([str(int(not bool(int(i)))) for i in data])
    return inverse

def get_key(data):
    # inverse = [get_inverse(i) for i in data]
    import secrets

    key = secrets.token_bytes(len(data))
    print("key: ", key)
    key = get_binary(key)

    # inverse = [get_inverse(i) for i in key]
    return key

def xor_operator(data1, data2):
    data = []
    for i in range(len(data1)):
        '''d1 = 8 bits'''
        d1 = data1[i]
        d2 = data2[i]

        byte_data = ""

        for j in range(len(d1)):
            byte_data += str(int(bool(int(d1[j])) ^ bool(int(d2[j]))))

        data.append(byte_data)

    return data

data = "hello world"
print("original: ", print_bytes(data))

binary = get_binary(str.encode(data))
print("original binary: ", binary, len(binary))

key_binary = get_key(binary)
print("key binary: ",  key_binary, len(key_binary))

xor_binary = xor_operator(binary, key_binary)
print("xor binary: ", xor_binary)

original_binary = xor_operator(xor_binary, key_binary)
print("original binary: ", original_binary)

assert(binary == original_binary)
