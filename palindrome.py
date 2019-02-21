def silly():
    res=[]
    done=False
    while not done:
       date=input('plese input the date,when u done put enter:')
       if date=='':done=1
       else:res.append(date)   
    temp=res[:]
    temp.reverse()
    ans=(temp==res)
    if ans:print("This is a palindrome ")
         
    else:print("it's not a palindrome")
         
               
