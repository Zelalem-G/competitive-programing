ps = input()
n = int(input())

b = False
e = False
exact = False

barks = []

for _ in range(n):
    w = input()
    if w == ps:
        exact = True
        
    barks.append(w)
    
if exact:
    print("YES")
else:        
    for bark in barks:
        if bark[0] == ps[1]:
            b = True
        
        if bark[1] == ps[0]:
            e = True
            
    if b and e:
        print("YES")
    else:
        print("NO")