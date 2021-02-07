from typing import TypedDict, Generic, TypeVar

K = TypeVar("K")
V = TypeVar("V")

class GenericDict(TypedDict):
    key: K
    value: V

class HashMap(Generic[K,V]):
    __genericDict: GenericDict = None

    def __init__(self):
        self.__genericDict = GenericDict([K,V])
