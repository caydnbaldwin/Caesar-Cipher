import sys

# read in file
def readlines(filename):
    with open(filename) as file:
        return file.readlines()

# put characters into dictionary
def get_substitution_cipher(substitution_cipher):
    dictionary = {}
    for line in substitution_cipher:
        line = line.strip()
        dictionary[line[2]] = line[0]
    return dictionary


def get_decoded(cipher_text, substitution_cipher):
    decoded = ''
    for line in cipher_text:
        for character in line:
            # decode character using caesar cipher
            if character.isupper():
                new_character = character.lower()
                new_letter = substitution_cipher.get(new_character, character)
                decoded += new_letter.upper()
            else:
                new_letter = substitution_cipher.get(character, character)
                decoded += new_letter
    return decoded

# write the decoded text to file
def writelines(filename, content):
    with open(filename, 'w') as file:
        return file.writelines(content)


def main(simple_substitution_cipher, input_file, output_file):
    cipher_text = readlines(input_file)
    substitution_cipher = readlines(simple_substitution_cipher)
    substitution_cipher = get_substitution_cipher(substitution_cipher)
    decoded = get_decoded(cipher_text, substitution_cipher)
    writelines(output_file, decoded)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
