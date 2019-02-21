vals=(90,9,8,8,2,20,9,9,9,8,8,8,16,15,23,50,16,27,29,28,34,22,24,24,44,5,55,7)
w=(3,3,4,4,5,5,5,4,2,3,4,9,5,1,8,1,3,1,5,8,7,9,8,9,7,8,9,8)
v=(2,2,3,3,5,5,3,2,7,9,8,7,6,7,6,7,3,8,3,7,3,8,7,8,7,6,2,8)
av=40
aw=40
numbcalls=0
def maxvals(w,v,aw,av,vals,i):
    m={}
    return fastmaxvals(w,v,aw,av,i,m,vals)
def fastmaxvals(w,v,aw,av,i,m,vals):
    global numbcalls
    numbcalls+=1
    try:return m[(i,aw,av)]
    except KeyError:
        if i==0:
           if v[i]<=av and w[i]<=aw:
                m[(i,aw,av)]=vals[i]
                return vals[i]
           else:return 0
    withouti=fastmaxvals(w,v,aw,av,i-1,m,vals)
    if not(v[i]<=av and w[i]<=aw):
            m[(i,aw,av)]=withouti
            return withouti
    else:
            withi=vals[i]+fastmaxvals(w,v,aw-w[i],av-v[i],i-1,m,vals)
            m[(i,aw,av)]=withi
    res=max(withi,withouti)
    m[(i,aw,av)]=res
    return res
        

res=maxvals(w,v,aw,av,vals,len(vals)-1)
print('\nnumbcalls is :{}  maxvals is {} '.format(numbcalls,res))


