'''
given two string to find the common character in that two strings
'''

string1 = 'hello'
string2 = 'world'


def common_char():
    char1 = set(string1)
    char2 = set(string2)
    # intersection() method returns a set that contains the similarity between two or more sets.
    common = set.intersection(char1, char2)
    print(common)


if __name__ == "__main__":
    common_char()
