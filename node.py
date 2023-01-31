from graphics import *

class node():
    """
    A class that stores the information of a single node in the graph
    """
    def __init__(self,num:int,info:dict={}):
        """
        Creates a node object. prev id a list of previous nodes (optional), next is a list of following nodes
        (also optional). **kwagrs is a dictionary between variable name and value, like a=0. This may be used for
        special search algorithms and storing information along the way
        """
        self._num = int(num)
        self._next = []
        self._info = info

    def __str__(self):
        return f"Node {self._num} :: Dependants{[str(i) for i in self._next]}, Info{self._info}"

    def get_num(self):
        return self._num

    def assign_circle(self,circle:Circle):
        self._circle = circle

    #Adds/replaces information
    def add_info(self,key,value):
        self._info[key] = value

    #Adds a dependant
    def __iadd__(self,n):
        if not isinstance(n,node):
            raise ValueError("NODE ADD - not a node")
        if n not in self._next:
            self._next.append(n)
        return self

    #Iterates over the dependants (_next)
    def __iter__(self):
        self._iterator = 0
        return self
    def __next__(self):
        self._iterator+=1
        if self._iterator < len(self._next):
            return self._next[self._iterator]
        raise StopIteration

    #Get dictionary of object information
    def get_info(self): return self._info
    
