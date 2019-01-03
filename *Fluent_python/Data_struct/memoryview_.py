import array


numbers = array.array('h',[-2,-1,0,3,4])

memv = memoryview(numbers)

print(len(memv),memv[0])

memv_oct = memv.cast('B')
print(memv_oct.tolist())

print(memv_oct)
print(memv_oct[2])
memv_oct[2]=4

print(memv_oct[5])

print(numbers)
