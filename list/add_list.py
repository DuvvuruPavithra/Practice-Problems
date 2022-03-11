'''
Add the elements and find the positin of newly added index value
'''

list = [1, 3, 5, 7, 10]


def add_element(array, element):
    for i in range(len(array)):
        if array[i] > element:
            array.insert(i, element)
            return array, i
    array.append(element)
    return array, len(array)


if __name__ == "__main__":
    total_list, index_of_added = add_element(list, 12)
    print("After added the value in list is:", total_list)
    print("The position of added value is:", index_of_added)
