import unittest
# Just import the sort to test as sort
from selection import selection as sort
from random import randint, seed
class bubble(unittest.TestCase):

    def setUp(self):
        self.nSorts = 100
        self.lists = [[randint(0,100) for i in range(10,100)] for i in range(self.nSorts)]

    def test_sort(self):
        lists = []
        for l in self.lists:
            sort(l)
            lists.append(self.is_sorted(l))
        print("All {0} lists are sorted: {1}".format(self.nSorts,all(lists)))
        self.assertTrue(all(lists))

    def is_sorted(self, list):
        return all(list[i] <= list [i+1] for i in range(len(list)-1))



if __name__ == '__main__':
    seed(1)
    unittest.main()
