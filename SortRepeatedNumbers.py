N=input()
a = [input() for x in range(N)]
b=[]
for i in a:
    count=0
    for j in a:
        if j==i:
            count+=1
        else :
            continue
    if count>1:
        if i in b:
            continue
        if not b or b[-1]<i:
            b.append(i)
        else:
            b.insert(b.index(b[-1]),i)
if not b:
    print 'Unique'
else:
    print b
