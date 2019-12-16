'''
Created on Dec 10, 2019

@author: Phil M. H.
'''

''''OLD STUFF:count up to 1024 (10 positions, 2 options each
x = 0,1,2..1024
#x%(2*index)

 
for bucketCount in range(0, 10):
    for maxSize in range(0, 10):
        for targetFill in range(0,bucketCount):
            for directionBin in range(0, bucketCount): #a number, but to be treated as 0011110011 for forward or backwards search
                 
                list = []
             
list = [random.randint(1, maxSize) for _ in range(bucketCount)]
print(list)'''

binList = [0,1,2,3,4,5];

#fill binList with all possible values-orders

solutions = []
targetFraction = 0.5
#
def search(index, visited: list, currentBallCount):
    #deal with current index value
    if(index in visited):
        return
    else:
        currentBallCount += binList[index]
        visited.append(index)
    if (len(visited) > len(binList)*targetFraction): #if we've filled half the bins
        solutions.append(currentBallCount)
        return
    
    for i in range (1, len(binList)-1):
        search((index-i)%len(binList), visited[:], currentBallCount) #utilize the fact that list[-1] gets last element
    

# myList = [0,1,2,3,4,5] #i=2, 2-6=-4
# print(myList[-6]) ##prints 2

for i in range(0,len(binList)):
    search(i, [], 0)
    
print("Solutions: " + str(solutions))
print("Unique solutions:" + str(set(solutions)))
print("min: " + str(min(solutions)))