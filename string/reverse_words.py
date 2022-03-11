'''
To reverse a string in the same place
'''
def reverse_string(string):
    string1 = ""
    for i in string:
        string1 = i + string1
    return string1


if __name__ == "__main__":
    string = "Hello World"
    print("The original string is: ", string)
    print("The reverse string is", reverse_string(string))
