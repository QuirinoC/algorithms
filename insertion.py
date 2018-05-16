def insertion(l):
    #For each element in the list except the first one
    for i in range(1, len(l)):
        #Swap the elements in the list from 'i' then
        #going backwards until we reach the end or
        #we find and element smaller than 'i'
        while (i - 1) >= 0 and l[i] < l[i-1]:
            l[i], l[i-1] = (l[i-1], l[i])
            i -= 1


if __name__ == "__main__":
    l = [9,8,7,6,5,4,3,2,1]
    insertion(l)
    print(l)
#[3,2,1]
