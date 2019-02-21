def fastmaxval(w,v,i,aw,m):
    global numbcalls
    numbcalls+=1
    try:
        return m[(i,aw)]
    except KeyError:
        if i==0:
            if w[i]<=aw:
                m[(i,aw)]=v[i]
                return v[i]
            else:
                m[(i,aw)]=0
                return 0
        withouti=fastmaxval(w,v,i-1,aw,m)
        if w[i]>aw:
            m[(i,aw)]=withouti
            return withouti
        else:
            withi=v[i]+fastmaxval(w,v,i-1,aw-w[i],m)
        res=max(withi,withouti)
        m[(i,aw)]=res
        return res
def maxval0(w,v,i,aw):
    m={}
    return fastmaxval(w,v,i,aw,m)



def maxval(w,v,i,aw):
    global numbcalls
    numbcalls+=1
    if i==0:
        if w[i]<=aw:
            return v[i]
        else:return 0
    withouti=maxval(w,v,i-1,aw)
    if w[i]>aw:
         return withouti
    else: withi=v[i]+maxval(w,v,i-1,aw-w[i])
    res=max(withi,withouti)
    return res
     
##weights=(1,1,5,5,3,3,4,4)
##numbcalls=0
##vals=(15,15,10,10,9,9,5,5)
weights=(1,1,5,5,3,3,4,4,2,3,3,9,3,7,8,6,8,5,4,3,7,8,6,6,5,3,2,1)
numbcalls=0
vals=(15,15,10,10,9,9,5,5,8,9,20,30,20,15,17,38,50,45,40,39,29,9,8,7)
res=maxval(weights,vals,len(vals)-1,12)
print('maxvals={}   numbcalls={}'.format(res,numbcalls))
numbcalls=0
res=maxval0(weights,vals,len(vals)-1,12)
print('fastmaxvals={}   numbcalls={}'.format(res,numbcalls))
