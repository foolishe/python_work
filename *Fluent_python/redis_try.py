import redis


r = redis.Redis()

r.set('hello','world')
print(r.get('hello'))

r.lpush('thanks','world')
r.lpop('thanks')

r.hset('hashtable','hello','world')
print(r.hget('hashtable','hello'))

r.sadd('happy','new year')
print(r.smembers('happy'))

r.zadd('sort',{'hello':500})
r.zadd('sort',{'try':110})
print(r.zrange('sort',0,-1))
print(r.zrem('sort','try'))
print(r.zrangebyscore('sort',0,10000))

print(r.get('hello'),r.lrange('thanks',0,-1))
