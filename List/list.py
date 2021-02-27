l = [1,2,3.3,4.5, "F", "six", [7]]

for e in l: #iteration
    print(e,end=", ")
print()    
for i in range(len(l)): #iteration using length of array
    print(l[i],end=", ")
print()

l.append(8.1) #add value 8.1 at right end
l.append(9) #add value 9 at right end
l.append(9) #add value 9 at right end
l.remove(8.1) #delete value 8.1

print(l.count(9))


