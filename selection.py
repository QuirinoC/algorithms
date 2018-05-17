def selectedion(list):
    """
        This function sorts a list using the selectedion sort algorithm

    """
    #Used to get just the needed slice of the list on each iteration
    index = 0
    for i in range(len(list)):
        min = index
        # Since we already set the min to be the index, we do not need to
        # compare with the index itself
        # Doing this i save about 20 ms when running tests for 10 000 lists
        for i in range(index + 1, len(list)):
            #If we find a value smaller than the current min, we set it as min
            if list[i] < list[min]: min = i
        #Swap the min value with the current index
        list[index] , list[min] = (list[min], list[index])
        index += 1


if __name__=='__main__':
    a = [3,2,1]
    selectedion(a)
    print(a)
