import sys
import string
import random


def get_dictionary(alphabet, ciphered_alphabet):
    dictionary = {}
    for letter, ciphered_letter in zip(alphabet, ciphered_alphabet):
        dictionary[letter] = ciphered_letter
    return dictionary


def get_dictionary_list(dictionary):
    dictionary_list = []
    for key, value in dictionary.items():
        dictionary_list.append(f'{key},{value}\n')
    return dictionary_list


def writelines(filename, content):
    with open(filename, 'w') as file:
        return file.writelines(content)


def main(output_file):
    alphabet = string.ascii_lowercase
    ciphered_alphabet = random.sample(alphabet, len(alphabet))
    dictionary = get_dictionary(alphabet, ciphered_alphabet)
    dictionary_list = get_dictionary_list(dictionary)
    writelines(output_file, dictionary_list)


if __name__ == '__main__':
    main(sys.argv[1])
