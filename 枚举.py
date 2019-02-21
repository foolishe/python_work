##x+y+z=100
##5x+y+z/3=100andz%3=0
def meiju():
    for x in range(100):
        for y in range(100):
            z=100-x-y
            if 5*x+y+z/3==100 and z%3==0:
               print('x={},y={},z={}'.format(x,y,z))
            
