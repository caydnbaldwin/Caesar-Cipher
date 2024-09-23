import sys

# read in file
def readfile(filename):
    with open(filename) as file:
        return file.read()

# frequency analysis
def get_frequency(line):
    dictionary = {}
    # count each instance of each character
    for character in line:
        # add new key if character not already in dictionary
        if character.lower() not in dictionary:
            dictionary[character.lower()] = 0
        dictionary[character.lower()] += 1
    # calculate frequency of character
    for key, value in dictionary.items():
        new_value = round(value / len(line), 3)
        dictionary[key] = new_value
    return dictionary


def main(input_file):
    line = readfile(input_file)
    frequency = get_frequency(line)
    print(frequency)


if __name__ == '__main__':
    main(sys.argv[1])
