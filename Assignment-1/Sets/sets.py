set = {1, 2, 3}

#add element
set.add(4)  
print(set)

#remove element
set.remove(2)          
print(set)

#no error if missing
set.discard(10)     
print(set)

#remove random element
set.pop()     
print(set)

#clear all elements
set.clear()           
print(set)

s2 = {3, 4, 5,5,6}
#combine and common values
print(set.union(s2))        
print(set.intersection(s2))