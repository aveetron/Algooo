
def bubble_sort(number_list):
    for i in range(len(number_list)):
        for j in range(len(number_list) - i -1):
            if number_list[j] > number_list[j+1]:
                temp = number_list[j]
                number_list[j] = number_list[j+1]
                number_list[j+1] = temp
    print(number_list)


if __name__ == "__main__":
    number_list = [100,3,55,-10,67,433,20,765,1000,46,99]
    bubble_sort(number_list)