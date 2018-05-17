class heap:
    def __init__(self, l, max=True):
        #Set if it is a selected or min heap
        #Multiplying a boolean opeartion by a False the boolean is flipped
        self.max = max
        self.heap = l
        self.heapify()

    def heapify(self):
        #Heapify of a list using the list ifself, no need for a tree
        base = len(self.heap) // 2 - 1
        while base >= 0:
          left = (base * 2) + 1
          #Test if the current node has no childs
          #Breaking if so and going to the next(previous) one
          if (left >= len(self.heap)): base-=1; continue
          #-------------------------------------------------------#
          #Making the right child the left one if the node has no right
          right = left + 1 if left + 1 < len(self.heap) else left
          #Getting the child with the highest value (or min) - called selected
          selected = right if (self.heap[right] > self.heap[left]) * self.max else left
          if (self.heap[selected] > self.heap[base]) * self.max:
            self.heap[selected] , self.heap[base] = (self.heap[base], self.heap[selected])
            base = selected; continue
          else:
            base -= 1; continue


    def __str__(self):
      return str(self.heap)
#------------------------------------------------------------------------------#

if __name__ == '__main__':
    from random import randint
    lists = [[randint(0,100) for i in range(10,100)] for i in range(100)]
    for i, val in enumerate(lists):
      lists[i] = heap(val)
    l = [1,2,3,4,5]
    heap = heap(l, max=True)
    print(heap)


'''
for   [1,2,3,4,5]
index  0 1 2 3 4
n = 5
floor(n / 2) = 2

    1
   / \
  2   3
 / \
4   5
'''
