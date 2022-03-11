'''
To find the sum of consecutive elements in the given list
'''
def sum_of_Consecutive():
    list = [4, 7, 3, 2, 9, 2, 1]
    print("The original list is : ", list)
    # using zip() to get pairing.
    result = [a + b for a, b in zip(list, list[1:] + [list[0]])]
    # printing result
    print("After sum of two consecutive elements is : " , result)

if __name__ == "__main__":
    sum_of_Consecutive()




