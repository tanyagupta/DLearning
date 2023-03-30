#tests
from grid import Grid
from data_structures.referential_array import ArrayR
#from data_structures.sorted_list_adt import  SortedList

from data_structures.array_sorted_list import ArraySortedList



class Test:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.data = [['X'] * cols for row in range(rows)]

    def __iter__(self):
        yield from self.data

    def __getitem__(self, row):
        return self.data[row]
        # what should this be?


def main():
    """ Main function """

    t=Test (2,3)

    

    for x in t:
        print(x)




    mygrid = Grid ("some", 3, 3)
    # look at the following
    print (mygrid [0])










if __name__ == "__main__":
    main()
