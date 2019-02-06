import collections.abc



class ForzenJSON:

    def __new__(cls,arg):
        if isinstance(arg,abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg,abc.MutableSequence):
            return[cls(item) for item in arg]
        else:
             return arg

    def __init__(self,mapping):
        self._data = {}
        for key,value in mapping.items():
            if iskeyword(key):
                key += '_'
            self._data[key] = value

    def __getattr__(self,name):
        if hasattr(self._data,name):
            return getattr(self.__data,name)
        else:
            return ForzenJSON(self.__data[name])
