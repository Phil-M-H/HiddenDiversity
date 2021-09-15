'''
Created on Dec 10, 2019

@author: Phil M. H.
'''
import random

binList = [1,2,3,4,5];
binCount =13
maxSize = 5
#fill binList with all possible values-orders

solutions = []
alpha = 0.5

'''
Uses recursion to search through every way to iterate through the provided list, starting at i
While v could be changed to a dictionary to provide constant time lookup, the nature of this algorithm makes it pointless.
By design, this will examine every possible way to iterate through a list, with an O(N) = N!
i: starting index
v: a list containing previously searched indicies
bC: bin-count. This function was developed to brute-force a Combinatorics problem, which this variable is relevant to.
'''
def search_recurse(i, v: list, bC):
    #deal with current i value
    if(i in v):
        return
    else:
        bC += binList[i]
        v.append(i)
    if (len(v) > len(binList)*alpha): #if we've filled half the bins
        solutions.append(bC)
        return
    
    for i in range (1, len(binList)-1):
        search_recurse((i-i)%len(binList), v[:], bC) #utilize the fact that list[-1] gets last element
      
def search():#For each index in the bin, call the recursive function, and provide it the starting index, and a new list
    for i in range(0,len(binList)):
        search_recurse(i, [], 0)


def createBinList(bins, maxSize):
    i = 0
    binList.clear()
    while(i < bins):
        binList.append(random.randint(0, maxSize))
        i = i + 1
    
createBinList(binCount, maxSize)
search()

print("Solutions: " + str(solutions))
print("Unique solutions:" + str(set(solutions)))
