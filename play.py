a=99
while a<1000:
    a=a+1
    k=str(a)
    if int(k[1])**3+int(k[2])**3+int(k[0])**3==a:
        if k[1]>k[0]:
            if k[2]>k[1]:
                a1=k[0];a2=k[1];a3=k[2]
            elif k[2]>k[0]:
                a1=k[0];a3=k[1];a2=k[2]
            else:
                a1=k[2];a3=k[1];a2=k[0]
        else:
            if k[2]>k[0]:
                a1=k[1];a2=k[0];a3=k[2]
            elif k[2]<k[1]:
                a1=k[2];a2=k[1];a3=k[0]
            else:
                a1=ky[1];a2=k[2];a3=k[0]  
        print('{},{},{}'.format(int(a1),int(a2),int(a3)))
        
a=100
c=''
while a<1000:
    k=str(a)
    b=int(k[1])**3+int(k[2])**3+int(k[0])**3
    if b==a:
        c+=k
    a=a+1
ans=eval(c)    
print('{:,}'.format(ans))  
