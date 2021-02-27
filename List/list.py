l = [1,2,3.3,4.5, "F", "six", [7]]

for e in l: #iteration
    print(e,end=", ")
print()    
for i in range(len(l)): #iteration using length of array
    print(l[i],end=", ")
print()

l.append(9) #add value 9 at right end
l.append(8.1) #add value 8.1 at right end
l.append(9) #add value 9 at right end
l.remove(9) #delete value 8.1
for i in range(len(l)): #iteration using length of array
    print(l[i],end=", ")
print()

print(l.count(9))

l_deep = l
l_shallow=l.copy()
l.clear()
print("Deep copy refers to same memory as the other:", l_deep)
print("Shallow copy is created at a different memory:",l_shallow)

intl = [2,1,4,3]
intl.sort(reverse=True)#in-place sorting
print(intl)


neg = [-2,-1]
zero = [0]
pos = [1,2]
num = neg + zero + pos
print("num = ", num)
print(num.pop(2),": ", num)







