from heap import heap
def heap_sort(list, max=True, min=False):
    is_max = max * (not min)
    '''
        This function is a heap sort implemented using the class heap found
        in this same repo
        Note: This is a sort in place
    '''
    sorted = [None for i in range(len(list))]
    heap_list = heap(list, is_max)
    for i, val in enumerate(heap_list.heap):
        index = -i-1 if is_max else i
        list[index] = heap_list.get()


if __name__ == '__main__':
    test = [2,1,3,5,4,6,7,8,5,9]
    heap_sort(test, min=True)
    print(test)
