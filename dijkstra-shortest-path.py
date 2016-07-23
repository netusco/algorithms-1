#!/usr/bin/python

# Dijkstra's shortest-path algorithm
#
# The file contains an adjacency list representation of an undirected weighted graph with 200 vertices labeled 1 to 200. 
# Each row consists of the node tuples that are adjacent to that particular vertex along with the length of that edge. 
# For example, the 6th row has 6 as the first entry indicating that this row corresponds to the vertex labeled 6. 
# The next entry of this row "141,8200" indicates that there is an edge between vertex 6 and vertex 141 that has length 8200. 
# The rest of the pairs of this row indicate the other vertices adjacent to vertex 6 and the lengths of the corresponding edges.
#
# Your task is to run Dijkstra's shortest-path algorithm on this graph, using 1 (the first vertex) as the source vertex, 
# and to compute the shortest-path distances between 1 and every other vertex of the graph. 
# If there is no path between a vertex v and vertex 1, we'll define the shortest-path distance between 1 and v to be 1000000.
#
# You should report the shortest-path distances to the following ten vertices, in order: 7,37,59,82,99,115,133,165,188,197. 
# You should encode the distances as a comma-separated string of integers. 
# So if you find that all ten of these vertices except 115 are at distance 1000 away from vertex 1 and 115 is 2000 distance away, 
# then your answer should be 1000,1000,1000,1000,1000,2000,1000,1000,1000,1000. 
# Remember the order of reporting DOES MATTER, and the string should be in the same order in which the above ten vertices are given. 
# The string should not contain any spaces. Please type your answer in the space provided.
#
# IMPLEMENTATION NOTES: This graph is small enough that the straightforward O(mn) time implementation of Dijkstra's algorithm 
# should work fine. OPTIONAL: For those of you seeking an additional challenge, try implementing the heap-based version. 
# Note this requires a heap that supports deletions, and you'll probably need to maintain some kind of mapping between vertices 
# and their positions in the heap.

# load contents of text file into a list numList
NUMLIST_FILENAME = "dijkstraData.txt" # Answer: [2599, 2610, 2947, 2052, 2367, 2399, 2029, 2442, 2505, 3068]
# All nodes shortest distances
# {1: 0, 2: 2971, 3: 2644, 4: 3056, 5: 2525, 6: 2818, 7: 2599, 8: 1875, 9: 745, 10: 3205, 11: 1551, 12: 2906, 13: 2394, 14: 1803, 
# 15: 2942, 16: 1837, 17: 3111, 18: 2284, 19: 1044, 20: 2351, 21: 3676, 22: 4028, 23: 2650, 24: 3653, 25: 2249, 26: 2150, 27: 1222, 
# 28: 2090, 29: 3540, 30: 2303, 31: 3455, 32: 3004, 33: 2551, 34: 2656, 35: 998, 36: 2236, 37: 2610, 38: 3548, 39: 1851, 40: 4091, 
# 41: 2732, 42: 2040, 43: 3312, 44: 2142, 45: 3438, 46: 2937, 47: 2979, 48: 2757, 49: 2437, 50: 3152, 51: 2503, 52: 2817, 53: 2420, 
# 54: 3369, 55: 2862, 56: 2609, 57: 2857, 58: 3668, 59: 2947, 60: 2592, 61: 1676, 62: 2573, 63: 2498, 64: 2047, 65: 826, 66: 3393, 
# 67: 2535, 68: 4636, 69: 3650, 70: 743, 71: 1265, 72: 1539, 73: 3007, 74: 4286, 75: 2720, 76: 3220, 77: 2298, 78: 2795, 79: 2806, 
# 80: 982, 81: 2976, 82: 2052, 83: 3997, 84: 2656, 85: 1193, 86: 2461, 87: 1608, 88: 3046, 89: 3261, 90: 2018, 91: 2786, 92: 647, 
# 93: 3542, 94: 3415, 95: 2186, 96: 2398, 97: 4248, 98: 3515, 99: 2367, 100: 2970, 101: 3536, 102: 2478, 103: 1826, 104: 2551, 
# 105: 3368, 106: 2303, 107: 2540, 108: 1169, 109: 3140, 110: 2317, 111: 2535, 112: 1759, 113: 1899, 114: 508, 115: 2399, 116: 3513, 
# 117: 2597, 118: 2176, 119: 1090, 120: 2328, 121: 2818, 122: 1306, 123: 2805, 124: 2057, 125: 2618, 126: 1694, 127: 3285, 128: 1203, 
# 129: 676, 130: 1820, 131: 1445, 132: 2468, 133: 2029, 134: 1257, 135: 1533, 136: 2417, 137: 3599, 138: 2494, 139: 4101, 140: 546, 
# 141: 1889, 142: 2616, 143: 2141, 144: 2359, 145: 648, 146: 2682, 147: 3464, 148: 2873, 149: 3109, 150: 2183, 151: 5341, 152: 1832, 
# 153: 2080, 154: 1831, 155: 2001, 156: 3013, 157: 2143, 158: 1376, 159: 1627, 160: 2403, 161: 4772, 162: 2556, 163: 2124, 164: 1693, 
# 165: 2442, 166: 3814, 167: 2630, 168: 2038, 169: 2776, 170: 1365, 171: 3929, 172: 1990, 173: 2069, 174: 3558, 175: 1432, 176: 2279, 
# 177: 3829, 178: 2435, 179: 3691, 180: 3027, 181: 2345, 182: 5264, 183: 2145, 184: 2703, 185: 2884, 186: 3806, 187: 1151, 188: 2505, 
# 189: 2340, 190: 2596, 191: 4123, 192: 1737, 193: 3136, 194: 1073, 195: 1707, 196: 2417, 197: 3068, 198: 1724, 199: 815, 200: 2060}

# NUMLIST_FILENAME = "tests/dijkstra-0.txt" # cspd: {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 4, 7: 3, 8: 2}
# NUMLIST_FILENAME = "tests/dijkstra-1.txt" # cspd: {1: 0, 2: 1, 3: 3, 4: 6}
# NUMLIST_FILENAME = "tests/dijkstra-2.txt" # cspd: {1: 0, 2: 1, 3: 3, 4: 2, 5: 1000000}
# NUMLIST_FILENAME = "tests/dijkstra-3.txt" # cspd: {1:0, 2:1, 3:4, 4:5, 5:3, 6:4, 7:3, 8:2, 9:3, 10:6, 11:5}

inFile = open(NUMLIST_FILENAME, 'r')

s = 1           # source
pv = [s]        # processed vertices
cspd = {s:0}    # computed shortest path distances
csp = [s]       # computed shortest paths
graph = {}      # the adjacent graph with edge distances in format {vertice: [(edge, distance)]}
result = []     # computed shortest path distances of requested vertices

tv = [7,37,59,82,99,115,133,165,188,197]  # vertices requested to solve dijkstraData assignment


# tv = [1,2,3,4,5,6,7,8]                    # target vertices test 0
# tv = [1,2,3,4]                            # target vertices test 1
# tv = [1,2,3,4,5]                          # target vertices test 2
# tv = [1,2,3,4,5,6,7,8,9,10,11]            # target vertices test 3


# initializing the graph with an array of edges [tale, head]
for f in inFile:
    splited = f.split()
    v = int(splited.pop(0))
    graph[v] = []
    for d in splited:
        a, b = map(int, d.split(',', 1))
        graph[v].append((a,b))


# compute distances for all tv target vertices
for v in tv:
    counter = 0

    # do while v vertice has not been processed
    while v not in pv:

        shortest = 0

        # search for Dijkstra's greedy score for (v,w)
        for n in pv:
            counter += 1

            # loop within edges
            for e in graph[n]:
                
                # distance from source
                d = cspd[n] + e[1]

                # get the shortest path out of pv 
                shortest = e[0] if e[0] not in pv and (not shortest or d < cspd[shortest]) else shortest

                # keep track of the shortest distance to e[0] node
                cspd[e[0]] = d if e[0] not in cspd or d < cspd[e[0]] else cspd[e[0]]

        if not shortest:
            cspd[v] = 1000000 # this is the requested answer given for distance of unconnected nodes from source
            pv.append(v)
        else:
            pv.append(shortest)

    # gather result distances for requested nodes
    result.append(cspd[v])


# print computed shortest path distances
print("cspd", cspd)

# print result of the target vertices computed shortest path distances
print("result", result)

