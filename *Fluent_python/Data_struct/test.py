def f(a,*,b=0):
    return a,b

# print(f(4,6,6)) f(5,6,b=5) 会报错
print(f(5,b='gdf'))
