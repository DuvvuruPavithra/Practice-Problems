''' Frequency of character in given String '''

string = "Hello, How are you?"
dict = {}

def freq_characters():
    for i in string:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1
    print(dict)

if __name__ == "__main__":
    freq_characters()
