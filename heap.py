class heap:
    def __init__(self, l, max=True, min=False):
        #Set if it is a selected or min heap
        #Multiplying a boolean opeartion by a False the boolean is flipped
        self.max = max * (not min)
        print(self.max)
        # /\ simple trick so the user can use either
        # max or min to specify which heap wants
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
          right = left + 1 if (left + 1) < len(self.heap) else left

          #Getting the child with the highest value (or min) - called selected
          if self.max:
            selected = right if (self.heap[right] > self.heap[left]) * self.max else left
          else:
            selected = right if (self.heap[right] < self.heap[left]) else left
          #If there is a swap
          #if (self.heap[selected] > self.heap[base]) * self.max:
          if ((self.heap[selected] > self.heap[base]) and self.max) \
          or \
             (self.heap[selected] < self.heap[base]) and (not self.max):
            #Swap
            self.heap[selected] , self.heap[base] = (self.heap[base], self.heap[selected])
            #Go to the swaped index and continue the iteration
            base = selected; continue
          else:
            print(self.heap)
            base -= 1; continue
    def __str__(self):
      return str(self.heap)

    def __len__(self):
      return len(self.heap)

    def __getitem__(self, index):
      return self.heap[index]
#------------------------------------------------------------------------------#

if __name__ == '__main__':
    from random import randint
    test = [randint(0,100) for i in range (11)]
    heap = heap(test, min=True)
    for i in range(0, len(heap)//2):
      print(heap[i] <= heap[i * 2 + 1] and heap[i] <= heap[i*2+2])
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
