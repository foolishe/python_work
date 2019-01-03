from collections import namedtuple

City = namedtuple('City','name country population coordinates')
tokyo = City('Tokyo','JP',36.933,(35.689722,139.691667))
print(tokyo,tokyo[3],'\n',tokyo.population)
print(City._fields)
LatLong = namedtuple('LatLong','lat long')
delhi_data = ('Delhi NCR','IN',21.935,LatLong(28.613889,77.208889))

print(City(*delhi_data))

delhi = City._make(delhi_data)
print(delhi._asdict())

for key,value in delhi._asdict().items():
    print(key + ':',value)

metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('Sao Paulo','BR',19.649,(-23.547778,-46.635822))]

print('{:15} | {:^9} | {:^9}'.format('','Lat','Long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'

for name ,cc , pop ,(latitude,longitude) in metro_areas:
    if longitude <= 0:
        print(fmt.format(name,latitude,longitude))

'a petty example:'
t = (1,3,[32,54])
t[2].extend([54,65])
#t[2] += [50,60]

print(t)
