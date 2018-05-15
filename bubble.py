def bubble(list):
    '''Pythonic way of implementing buble sort'''

    #Optimization flag
    sorted = True
    
    r = range(len(list) - 1)

    #Used to run the swap n times
    for j in range(len(list)):

        #Perform the swap
        for i in r:
            if (list[i] <= list[i+1]):
                list[i:i+2] = (list[i],list[i+1])
            else:
                sorted = False
                list[i:i+2] = (list[i+1],list[i])

        #If there was no swap during a j iteration then we know
        #Our list is sorted
        if (sorted): return


if __name__ == "__main__":
    list = ['c','b','a']
    bubble(list)
    print(list)
