import re,sys

WORD_RE = re.compile(r'\w+')

index = {}

with open(sys.argv[-1],encoding='utf-8') as fp:
    for line_no,line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no,column_no)

            occurrences = index.get(word,[])
            occurrences.append(location)
            index[word] = occurrences
            #index.setdefault(word,[]).append(location)

for word in sorted(index,key=str.upper):
    print(word,index[word])

class StrKeyDict0(dict):
    def __missing__(self,key):
        if isinstance(key,str):
            raise KeyError
        return self[str(key)]

    def get(self,key,default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self,key):
        return str(key) in self.keys()

test = StrKeyDict0()

test['3'] = 'hello'
print(test[3],3 in test)

from types import MappingProxyType

d = {1:'A'}
d_proxy = MappingProxyType(d)
print(d_proxy)
print(d_proxy[1])
try:
    d_proxy[2] = 'x'
except:
    print('cant assignment')

d[2] = 8

print(d_proxy[2])
