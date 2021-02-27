l = [1,2,3.3,4.5, "F", "six", [7]]

for e in l: #iteration
    print(e)
    
for i in range(len(l)): #iteration using length of array
    print(l[i])
    
l.append(8) #add value 8 at right end
l.append(8.1) #add value 8 at right end
l.remove(8) #delete value 8

print(l.count)


