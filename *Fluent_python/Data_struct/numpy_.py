import numpy


a = numpy.arange(12)
print(a,type(a),a.shape)

a.shape = 3,4

print(a,'\n',a[2],'\n',a[:,1],'\n',a.transpose())

numpy.save('floats-10M',a)
a1 = numpy.load('floats-10M.npy','r+')
print(a1)
a1 *=5
print(a1)
