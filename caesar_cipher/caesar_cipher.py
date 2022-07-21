

def encrypt(text_to_encript, key):

    shifted_value = ''

    for c in text_to_encript:

        if c.isupper():  # check uppercase

            c_index = ord(c) - ord('A')
            c_shifted = (c_index + key) % 26 + ord('A')
            c_new = chr(c_shifted)
            shifted_value += c_new

        elif c.islower():  # check lowercase

            c_index = ord(c) - ord('a')
            c_shifted = (c_index + key) % 26 + ord('a')
            c_new = chr(c_shifted)
            shifted_value += c_new

        elif c.isdigit():
            c_new = (int(c) + 0)
            shifted_value += str(c_new)

        else:
            shifted_value += c

    return shifted_value


def decrypt(encoded_msg, key):
    return encrypt(encoded_msg, -key)


def crack(encoded_msg, key):
    pass


# if __name__ == '__main__':
    # test1 = encrypt("1234", 3)
    # print(test1)
    # test2 = encrypt('789', 3)
    # print(test2)
    # test3 = encrypt('123', 7236)
    # print(test3)
    # test4 = decrypt('4567', 3)
