list1 = [21, 1, 3, 14, 5]
list2 = [8, 10, 28, 9, 6]


def sum_two_list():
    list = []
    # print(list1+list2)
    length_list = len(list1)
    for i in range(length_list):
        list.append(list1[i] + list2[i])
        print("The sum of two list is", list)


if __name__ == "__main__":
    sum_two_list()
