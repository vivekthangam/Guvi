a=[1,3,2,3,1,2,3,4,3]
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
