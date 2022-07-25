from nltk.corpus import words, names
import ssl
import nltk


try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context


nltk.download("words", quiet=True)
nltk.download("names", quiet=True)


word_list = words.words()
name_list = names.words()


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


def crack(encoded_msg):

    non_sense = ''

    for i in range(1, 27):
        new_word = decrypt(encoded_msg, i)
        words = new_word.split()
        count = 0
        for j in range(0, len(encoded_msg.split())):
            if words[j] in word_list:
                count += 1
                if count > (.5*len(encoded_msg.split())):
                    return new_word
                else:
                    continue

    if count <= 1:
        return non_sense


if __name__ == '__main__':
    phrase = "Ix fhw txe fofg of ndhrl, it nad tho hndrk of allkd."
    encrypted = encrypt(phrase, 10)
    last_test = crack(encrypted)
    print(last_test)
