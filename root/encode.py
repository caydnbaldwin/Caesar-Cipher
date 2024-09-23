import sys

# read in file
def readlines(filename):
    with open(filename) as file:
        return file.readlines()

# put characters into a dictionary
def get_substitution_cipher(substitution_cipher):
    dictionary = {}
    for line in substitution_cipher:
        line = line.strip()
        dictionary[line[0]] = line[2]
    return dictionary


def get_encoded(plaintext, substitution_cipher):
    encoded = ''
    for line in plaintext:
        for character in line:
            # encode character using caesar cipher
            if character.isupper():
                new_character = character.lower()
                new_letter = substitution_cipher.get(new_character, character)
                encoded += new_letter.upper()
            else:
                new_letter = substitution_cipher.get(character, character)
                encoded += new_letter
    return encoded

# write encoded text to file
def writelines(filename, content):
    with open(filename, 'w') as file:
        return file.writelines(content)


def main(simple_substitution_cipher, input_file, output_file):
    plaintext = readlines(input_file)
    substitution_cipher = readlines(simple_substitution_cipher)
    substitution_cipher = get_substitution_cipher(substitution_cipher)
    encoded = get_encoded(plaintext, substitution_cipher)
    writelines(output_file, encoded)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
