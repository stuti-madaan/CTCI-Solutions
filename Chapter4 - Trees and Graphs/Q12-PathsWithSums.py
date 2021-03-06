from node import *

#my 1st solution
def getAllPaths(root):
    paths = []
    jafoi = set()
    queue = [(root, [])]
    while len(queue) != 0:
        current = queue.pop()
        if current[0] not in jafoi:
            jafoi.add(current[0])
            #paths.append( current[1] + [current[0].data] )
            if current[0].left != None:
                queue.insert(0, ( current[0].left, current[1] + [ current[0].data] ) )
            if current[0].right != None:
                queue.insert(0, (current[0].right, current[1] + [current[0].data] ) )
            if current[0].left == None and current[0].right == None:
                paths.append( current[1] + [current[0].data] )
    return paths

def getSubsequenceSum(path, targetSum):
    mapData = { 0 : [-1]}
    runningSum = 0
    resp = []
    for i in range(len(path)):
        runningSum += path[i]
        if runningSum - targetSum in mapData:
            for index in mapData[runningSum - targetSum ]:
                resp.append( path[index+1: i+1] )
        if runningSum not in mapData:
            mapData[runningSum] = [i]
        else:
            mapData[runningSum].append(i)
    return resp

def getPathsWithSum( root, num):
    allPaths = getAllPaths(root)
    resp = []
    for path in allPaths:
        tempSeq =  getSubsequenceSum( path, num)
        for subSeq in tempSeq:
            if subSeq != None and subSeq not in resp:
                resp.append(subSeq)
    return resp

#Book's solution

def countPathsWithSum(root, targetSum):
    if root == None:
        return 0
    pathCount = {}
    incrementHashTable(pathCount, 0, 1)
    return realCount(root, targetSum, 0, pathCount)

def realCount(node, targetSum, runningSum, pathCount):
    if node == None:
        return 0
    runningSum += node.data
    incrementHashTable(pathCount, runningSum, 1)

    soma = runningSum - targetSum
    totalPaths = pathCount[soma] if soma in pathCount else 0

    totalPaths += realCount(node.left, targetSum, runningSum, pathCount)
    totalPaths += realCount(node.right, targetSum, runningSum, pathCount)

    incrementHashTable(pathCount, runningSum, -1)
    return totalPaths

def incrementHashTable( hashTable, key, delta):
    if key not in hashTable:
        hashTable[key] = 0
    hashTable[key] += delta


def main():
    a = BNode(10)
    a.left = BNode(5)
    a.right = BNode(-3)
    a.left.left = BNode(3)
    a.left.left.left = BNode(3)
    a.right.right = BNode(11)
    a.left.right = BNode(2)
    a.left.right.right = BNode(1)
    a.left.left.right = BNode(-2)
    print getPathsWithSum(a, 8)
    print countPathsWithSum(a, 8)
    #print getAllPaths(a)
    #print getSubsequenceSum( [1,5,2,3, 4, 8, 7], 7)
if __name__ == '__main__':
    main()
