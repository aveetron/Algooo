def binary_search(number_list, val):
    if len(number_list) == 0 or (len(number_list) == 1 and number_list[0]!=val):
        return False

    middle = len(number_list) // 2
    mid = number_list[middle]
    if val == mid: 
        return True
    if val < mid:
        return binary_search(number_list[: number_list[middle]], val)
    if val > mid:
        return binary_search(number_list[middle+1 : ],val)


if __name__ == "__main__":
    #the list must need to be sorted, if not then sort it : number_list.sort()
    number_list = [1,2,3,4,5,6,7,8,9,10]
    result = binary_search(number_list, 1000)
    print(result)
