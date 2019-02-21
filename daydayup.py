#daydayup
def dayup(x):
    dayup=1
    for i in range(365):
        if i%7 in [0,6]:
            dayup=(1-0.01)*dayup
        else:
            dayup=dayup*(1+x)
    return (dayup)

def dayupall(y):
    dayup=pow(1+y,365)
    return(dayup)

def day():
    
    dayfaction=0.01
    while dayup(dayfaction)<37.78:
        dayfaction+=0.001
        print(dayfaction)    
for i in range(12):
    print(chr(9800+i),end='33')
