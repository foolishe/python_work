a = dict(one=1,two=2,three=3)
b = {'one':1,'two':2,'three':3}
c = dict(zip(['one','two','three'],[1,2,3]))
d = dict([('two',2),('one',1),('three',3)])
e = dict({'three':3,'one':1,'two':2})
print(a==b==c==d==e)

DIAL_CODES = [
    (86,'china'),
    (91,'india'),
    (1,'united states'),
    (62,'indonesia'),
    (55,'brazil'),
    (92,'pakistan'),
    (880,'bangladesh'),
    (234,'nigeria'),
    (7,'russia'),
    (81,'janpan'),
]
country_code = {country.title(): code for code,country
    in DIAL_CODES
    if code <66}
print(country_code)

import sys,re


WORD_RE = re.compile(r'\w+')
index = {}
with open(sys.argv[1],encoding='utf-8') as fp:
    print(fp)
    for line_no,line in enumerate(fp,1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start()+1
            location = (line_no,column_no)

            occurrences = index.get(word,[])
            occurrences.append(location)
            index[word] = occurrences

            index.setdefault(word,[]).append(location)
            my_dict.setdefault(key,[]).append(new_value)

            if key not in my_dict:
                my_dict[key] = []
            my_dict[key].append(new_valueaa)

        for word in sorted (index,key=str.upper()):
            print(word,index[word])
