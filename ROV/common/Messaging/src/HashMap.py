from typing import Dict, Generic, TypeVar

#Generics for the key and value
K = TypeVar("K")
V = TypeVar("V")

#A hashmap with generics implemented using a dictionary
class HashMap(Generic[K,V]):
    #The dictionary that holds the key value pairs
    __dict: Dict[K,V] = None

    #Creates the dictionary
    def __init__(self):
        self.__dict = dict()

    #Stores a key value pair into the hashmap
    #Returns the previous value if the key already exists in the hashmap
    def put(self, key: K, value: V) -> V:
        prevValue = self.get(key)

        self.__dict.update({key: value})

        return prevValue

    #Gets the value from the hashmap that corresponds to the provided key
    def get(self, key: K) -> V:
        return self.__dict.get(key)

    #Removes the key-value pair that corresponds to the provided key
    #Returns the value if the key exists in the hashmap
    def remove(self, key: K) -> V:
        value = self.get(key)

        if not value == None:
            self.__dict.pop(key)

        return value

    #Gets the number of key-value pairs in the hashmap
    def size(self) -> int:
        return len(self.__dict)
