#Function to call the actual sort method, but using default parameters
def quick_sort(elements):
    '''
    This function uses quick to help as an aux to sort in place
    '''
    quick(elements, 0, len(elements) - 1)

def quick(elements, left, pivot):
    #Left 
    leftIndex = left
    

    #Get the pivot
    right = pivot - 1

    if (right-left) < 0:
        return

    while True:
   

        #Get left index
        while elements[left] <= elements[pivot] and left != right:
            left += 1

        #Get the right index
        while elements[right] >= elements[pivot] and left != right:
            right -= 1

        if left == right:
            if elements[left] > elements[pivot]:
                elements[left], elements[pivot] = (elements[pivot], elements[left])
            break
        else:
            elements[left], elements[right] = (elements[right], elements[left])
   
    

    quick(elements, leftIndex, left)
    quick(elements, left+1, pivot)

        

if __name__=='__main__':

    from random import randint, seed
    rand_seed = randint(0,10000)
    print(f'Random seed: {rand_seed}')
    seed(rand_seed)
    test = [randint(0,100) for x in range(11)]
    
    #test = [9,8,7,6,5,4,3,2,1]
    print(test)
    quick_sort(test)
    print(test)