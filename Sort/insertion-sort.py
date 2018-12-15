def insertion_sort(number_list, length_of_number_list):
    for i in range(1,length_of_number_list):
        item = number_list[i]
        j =i-1
        while j>=0 and number_list[j] > item:
            number_list[j+1] = number_list[j]
            j = j - 1

        number_list[j+1] = item

    return number_list


if __name__ == "__main__":
    number_list = [5,3,4,2,1]
    result = insertion_sort(number_list, len(number_list))
    print(result)