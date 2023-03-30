#tests
from grid import Grid
from data_structures.referential_array import ArrayR
#from data_structures.sorted_list_adt import  SortedList

from data_structures.array_sorted_list import ArraySortedList



class ChachuGrid:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.data = [[] for i in range(5)]






        self.data = [['X'] * cols for row in range(rows)]

    def __iter__(self):
        yield from self.data

    def __getitem__(self, row):
        return self.data[row]

    def __setitem__(self, row):
        return self.data[row]


        # what should this be?


def main():
    """ Main function """

    t=ChachuGrid (2,3)



    # for x in t:
    #     print(x)

    #print (t[0][1])


    mygrid = Grid ("some", 3, 3)
    mygrid[0][0] = "layout store 1"
    mygrid[0][1] = "layout store 2"
    mygrid[0][2] = "layout store 3"


    print (mygrid[0][2])










if __name__ == "__main__":
    main()
