class heap:
    '''
        This class supports both min and max heap
        max heap is set by default
        min to get min heap use either
        max=False or min=True the class will set it to min
            Note: If both are used then it will be set to max
        The purpose of this implementation is to be used in a heap sort
        So there is no deletion, only a get() method which removes root.
        Also insertion is not supported by itself.
            One could just append a new value and call the heapify method to achieve this
    '''
    def __init__(self, l, max=True, min=False):
        #Set if it is a selected or min heap
        #Multiplying a boolean opeartion by a False the boolean is flipped
        self.max = max * (not min)
        self.min = not self.max
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
            base -= 1; continue

    def get(self):
      #Save the value of the min/max
      val = self.heap[0]
      #Swap the root with the last element in the heap
      self.heap[0] , self.heap[-1] = (self.heap[-1], self.heap[0])
      #Reduce heap size
      self.heap = self.heap[:-1]
      current = 0
      #Tests that the current node has children
      while (current * 2 + 1) < len(self.heap):
          left = (current * 2) + 1
          right = left + 1 if (left + 1) < len(self.heap) else left
        #Depending on min or max is the element we want to swap with
          if self.max:
              selected = left if self.heap[left] >= self.heap[right] else right
              if self.heap[selected] > self.heap[current]:
                  self.heap[selected], self.heap[current] = (self.heap[current], self.heap[selected])
                  current = selected
              else:
                  break

          elif self.min:
              selected = left if self.heap[left] <= self.heap[right] else right
              if self.heap[selected] < self.heap[current]:
                  self.heap[selected], self.heap[current] = (self.heap[current], self.heap[selected])
                  current = selected
              else:
                  break
      return val
    def __str__(self):
      return str(self.heap)

    def __len__(self):
      return len(self.heap)

    def __getitem__(self, index):
      return self.heap[index]


#------------------------------------------------------------------------------#

if __name__ == '__main__':
    from random import randint

    '''Testing'''
    #Creates a 100 random lists
    lists = [[randint(0,100) for i in range(11)] for i in range(10)]
    are_heap = []
    for list in lists:
      #Create heap

      test = heap(list, max=False)
      is_heap = []
      for i in range(0, len(test)//2):
        is_heap.append(test[i] <= test[i * 2 + 1] and test[i] <= test[i*2+2])
      are_heap.append(all(is_heap))

    print(test)
    for i, val in enumerate(test.heap):
        print(test.get(), end=" ")
    print()


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
