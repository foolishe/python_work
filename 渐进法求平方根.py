#渐进法求平方根
def sqre(x,y):
 print('x是要开方的数，y是精度')
 guess=x/2
 i=1
 while abs(guess**2-x)>y and i<100:
     print(i,guess,'i am good')
     guess=guess-(guess**2-x)/(2*guess)
     i+=1
 return(guess)
