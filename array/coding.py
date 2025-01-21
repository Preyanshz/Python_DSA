def findPair(arr,target):
    hash_map = {}
    for i in range(len(arr)):
        if target - arr[i] in hash_map:
            return {arr[i],target-arr[i]}
        hash_map[arr[i]] = i
    return None    

arr = list(map(int,input().split()))
target = int(input())

pairs = findPair(arr,target)
if pairs != None:
    print("Pair found:",pairs)
else:
    print("Pair not found")
