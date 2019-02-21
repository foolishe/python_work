def exchange(a,b):
    temp=a
    a=b
    b=temp
    return a,b 
def sort(a,p,q,key):
    i=p;j=q
    for j in range(q):
        if a[j]<=key:
            a[i],a[j]=exchange(a[i],a[j])
            i+=1
    i=i-1
    return i
def findx(a,n):
    key=[]
    b,c,d,e,f=[],[],[],[],[]
    for i in a:
        if a.index(i)<=n//5+1:
            b.append(i)
        if n//5+1<a.index(i)<=n*2//5+1:
            c.append(i)
        if n*2//5+1<a.index(i)<=n*3//5+1:
            d.append(i)
        if n*3//5+1<a.index(i)<=n*4//5+1:
            e.append(i)
        if n*4//5+1<a.index(i)<=n:
            f.append(i)
        for i in range(len(f),n//5+1):
            f.append(0)
    for i in range(n//5+1):
        k=[b[i],c[i],d[i],e[i],f[i]]
        k=sort(k)
        key.append(k[2])
    x=key[n//10]
    return x
def indexa(a,k):#a为数组，寻找a【k】的值，一般用来找中位数a[n/2]
    key=find(a)
    i=sort(a,0,len(a),key)
    if i==k:
        return key
    elif i>k:
        a=a[:i]
        indexa(a,k)
    else:
        a=a[i:]
        indexa(a,k-i)
a=[1,2,3,4,5,6,7,8,9,10,11]
##res=sort(a,0,len(a),8)
res1=findx(a,len(a))
print(res1)



