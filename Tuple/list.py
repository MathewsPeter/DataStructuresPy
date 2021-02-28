t = (1,2,3.3,4.5, "F", "six", [7], 8, (8,))

for e in t: #iteration
    print(e,end=", ")
print()    
for i in range(len(t)): #iteration using length of array
    print(t[i],end=", ")
print()

print(t.count(8))
print(t.index(8))
print(t.index((8,)))

for i in range(t.__len__()): #iteration using length of array
    print(t[i],end=", ")
print()

print(t.count(9))

t_deep = t
t_shallow=t.copy()
t.clear()
print("Deep copy refers to same memory as the other:", t_deep)
print("Shallow copy is created at a different memory:",t_shallow)

intl = [2,1,4,3]
intl.sort(reverse=True)#in-place sorting
print(intl)


neg = [-2,-1]
zero = [0]
pos = [1,2]
num = neg + zero + pos
print("num = ", num)
print(num.pop(2),": ", num)







