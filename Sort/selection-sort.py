class SelectionSort(object):

    def __init__(self,number_list):
        self.number_list = number_list

    def sort_list(self):
        for i in range(len(self.number_list)):
            min_index = i
            for j in range(i, len(self.number_list)):
                if self.number_list[j] < self.number_list[min_index]:
                    min_index = j
            
            temp = self.number_list[i]
            self.number_list[i] = self.number_list[min_index]
            self.number_list[min_index] = temp
        return self.number_list


sel = SelectionSort([7,3,5,10,2])
print(sel.sort_list())   






'''
    Executing output step by step ->
    [2, 3, 5, 10, 7]
    [2, 3, 5, 10, 7]
    [2, 3, 5, 10, 7]
    [2, 3, 5, 7, 10]
    [2, 3, 5, 7, 10]
'''