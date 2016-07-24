# The goal of this problem is to implement a variant of the 2-SUM algorithm 
# (covered in the Week 6 lecture on hash table applications).
#
# The file contains 1 million integers, both positive and negative (there might be some repetitions!).
# This is your npSorteday of integers, with the ith row of the file specifying the ith entry of the npSorteday.
#
# Your task is to compute the number of target values t in the interval [-10000,10000] (inclusive) 
# such that there are distinct numbers x,y in the input file that satisfy x+y=t. 
# (NOTE: ensuring distinctness requires a one-line addition to the algorithm from lecture.)
#
# Write your numeric answer (an integer between 0 and 20001) in the space provided.

import numpy as np

# test
# input: [-3, -1, 1, 2, 9, 11, 7, 6, 2]. We want t -> [3,10] , inclusively
#
# output: 29
#
# pairs:
#
#     (-3, 6) (-3, 7) (-3, 9) (-3, 11)
#     (-1, 6) (-1, 7) (-1, 9) (-1, 11)
#     (1, 2) (1, 6) (1, 7) (1, 9)
#     (2, 1) (2, 2) (2, 6) (2, 7)
#     (6, -3) (6, -1) (6, 1) (6, 2)
#     (7, -3) (7, -1) (7, 1) (7, 2)
#     (9, -3) (9, -1) (9, 1)
#     (11, -3) (11, -1)


# load contents of text file into a list numList
NUMLIST_FILENAME = "prob-2sum.txt" # requested interval: [-10000, 10000] / output: 427
# NUMLIST_FILENAME = "tests/prob-2sum-0.txt" # requested interval: [3, 10] / output: 28

inFile = open(NUMLIST_FILENAME, 'r')

# initializing the list
with inFile as f:
    numList = [int(integers.strip()) for integers in f.readlines()]

npList = np.array(numList)

# test limits
# topLimit = 10
# bottomLimit = 3

# assignment duties
topLimit = 10000
bottomLimit = -10000

counter = 0

summs = []

# removing duplications and sorting the npSorteday
npUnique = np.unique(npList)
npSorted = np.sort(npUnique)

for x in npSorted:

    if len(npSorted) > 0:
        pairs = np.where((npSorted >= bottomLimit-x) & (npSorted <= topLimit-x))

        if(len(pairs[0]) > 0):
            for p in pairs[0]:
                s = x + npSorted[p]
                if(s not in summs):
                    summs.append(s)

        npSorted = np.delete(npSorted, 0)
    




print('result', len(summs))
