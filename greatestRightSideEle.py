# 1. Problem: REPLACE ELEMENTS WITH GREATEST ELEMENT ON RIGHT SIDE
list = [17, 18, 5, 4, 6, 1]
"""
so object of this code is to REPLACE ELEMENTS WITH GREATEST ELEMENT ON RIGHT SIDE.
the logic we are using is:
1. first we are looping the list in reverse order
2. then we are comparing max of i index ele and rightmax which is initialy -1 
3. then we are updating the rightmax and list i index value
"""

rightMax = -1
for i in range(len(list) - 1, -1, -1):
    newMax = max(list[i], rightMax)
    list[i] = rightMax
    rightMax = newMax
print(list)
