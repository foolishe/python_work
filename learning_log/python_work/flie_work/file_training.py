file_name='learning_python.txt'
with open(file_name) as f_object:# with open will close the file when u open once.
    usefull_python=f_object
    for line in f_object:
        lines=line.replace('python','c')
        print(line.replace('python','javascript'))#保持了line的不变性，可以进行多次操作。
        print(line)
        print(lines)#这里如果直接输出 line 不会变成c
    #print(f_object.read(),1)
    #for line in usefull_python:
        #print(line,2)
#print(usefull_python.read(),5)
