from abc import ABCMeta, abstractmethod
from functools import wraps


def method_proxy(func):
    @wraps(func)
    def inner(self, *args):
        if self._inited_obj is empty:
            self._setup()
        return func(self._inited_obj, *args)
    return inner


empty = object()


class LazyObject(metaclass=ABCMeta):

    _inited_obj = None

    def __init__(self):
        self._inited_obj = empty

    @abstractmethod
    def _setup(self):
        pass

    __getattr__ = method_proxy(getattr)

    def __setattr__(self, name, value):
        if name=="_inited_obj":
            self.__dict__[name] = value  # 实例对象
        else:
            if self._inited_obj is empty:
                self._setup()
            setattr(self._inited_obj, name, value)

    def __delattr__(self, name):
        if name=="_inited_obj":
            raise TypeError("_inited_obj 属性不可删除")
        if self._inited_obj is empty:
            self._setup()
        delattr(self._inited_obj, name)


class LazyDemo(LazyObject):
    def _setup(self):
        self._inited_obj = Demo()

    def clean(self):
        self._inited_obj = empty


class Demo:
    def __init__(self):
        self.a = 1


if __name__ == "__main__":
    demo = LazyDemo()
    print(demo.a)
    # demo._inited_obj = 3
    # print(demo._inited_obj)
    # demo.clean()
    demo.b = 2
    print(demo.b)

