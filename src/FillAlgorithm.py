'''
Created on Dec 10, 2019

@author: Phil M. H.
'''
import random

''''OLD STUFF:count up to 1024 (10 positions, 2 options each
x = 0,1,2..1024
#x%(2*i)

 
for bucketCount in range(0, 10):
    for maxSize in range(0, 10):
        for targetFill in range(0,bucketCount):
            for directionBin in range(0, bucketCount): #a number, but to be treated as 0011110011 for forward or backwards search
                 
                list = []
             
list = [random.randint(1, maxSize) for _ in range(bucketCount)]
print(list)'''

binList = [1,2,3,4,5];
binCount =13
maxSize = 5
#fill binList with all possible values-orders

solutions = []
alpha = 0.5
#
def search_recurse(i, v: list, bC):
    #deal with current i value
    if(i in v):
        return
    else:
        bC += binList[i]
        v.append(i)
    if (len(v) > len(binList)*alpha): #if we've filled half the bins
#         print("v: " + str(len(v)) + "|" + str(len(binList))+ "|" + str(alpha))
        solutions.append(bC)
        return
    
    for i in range (1, len(binList)-1):
        search_recurse((i-i)%len(binList), v[:], bC) #utilize the fact that list[-1] gets last element

def search():
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