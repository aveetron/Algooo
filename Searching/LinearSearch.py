number_list = [100,3,6,8,88,4,555,36,70,]
input_number = int(input())

for i in range(len(number_list)):
    if number_list[i] == input_number:
        print('found! index number {}'.format(number_list.index(number_list[i])))
        break
    else:
        print('not found')
        break
        