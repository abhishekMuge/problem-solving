"""
problem: 2 sum
objective: find the elements from array whose sum is equal to target value
solution: 
we can solve the solution by two way:
1. brute force: search all posible combination of elements which statisfy the target value
2. by using hashmap: so what we can do, first we can find the diff between element and target if the value is available in hashmap then we return it, else we return
    we are going the add currunt element in hashmap.
return value: [idx, idx]
note: there should be only one pair which statify the target value
also we are storing value in hashmap in { value: index } this format.
"""

nums = [2, 1, 5, 3]
target = 5
hashmap = {}

for idx, value in enumerate(nums):
    diff = target - value
    if(diff in hashmap):
        print([hashmap[diff], idx])
    hashmap[value] = idx
