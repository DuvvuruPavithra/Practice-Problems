list = [11, 12, 5, -4, -26, 7, -19, 32]

def sum_pos_neg(array):
    positive = 0
    negative = 0
    for i in array:
        if i >= 0:
            positive += i
            print("The Positive element is", positive)
        if i <= 0:
            negative += i
            print("The Negative element is", negative)
    return positive, negative

if __name__ == "__main__":
    add, add1 = sum_pos_neg(list)
    print(f"The sum of Positive element is: {add}")
    print(f"The sum of Negative element is: {add1}")






