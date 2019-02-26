import reprlib,re

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)

class SentenceIterator:

    def __init__(self,words):
        delf.words = words
        self.index = 0

    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()

    def __iter__(self):
        return self


class Sentence:

    def __init__(self,text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word

class Sentence:

    def __init__(self,text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))

class squeuee:

    def __init__(self,begin,step,end=None):
        self.begin = begin
        self.step = step
        self.end = end

    def __iter__(self):
        result = type(self.begin + self.step)(self.begin)
        forever = self.end is None
        index = 0

        while forever or result < self.end:
            yield result
            index += 1
            result = self.begin + self.step * index

import itertools

def aritprog_gen(begin,step,end=None):
        first = type(begin + step)(begin)
        ap_gen = itertools.count(first,step)
        if end is not None:
            ap_gen = itertools.takewhile(lambda n: n < end,ap_gen)
        return ap_gen
