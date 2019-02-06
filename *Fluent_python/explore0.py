from collections import abc


class FrozenJSON:

    def __init__(self,mapping):
        self._data = dict(mapping)

    def __getattr__(self,name):
        print(name)
        if hasattr(self._data,name):
            return getattr(self._data,name)
        else:
            return FrozenJSON.build(self._data[name])

    @classmethod
    def build(cls,obj):
        if isinstance(obj,abc.Mapping):
            return cls(obj)
        elif isinstance(obj,abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj #点睛之笔。

test = FrozenJSON({'guess':{'name':'david','age':'34',},'place':'public'})
print(test.guess.name) # 递归调用。
