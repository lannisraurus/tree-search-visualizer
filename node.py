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
        self._circle = None
        self._connections = []
        self._switch = True

    def __str__(self):
        return f"Node {self._num} :: Dependants{[str(i) for i in self._next]}, Info{self._info}"

    def get_num(self):
        return self._num

    def assign_circle(self,circle:Circle):
        self._circle = circle
        self._circle.setFill("white")

    def get_circle_pos(self):
        return self._circle.getCenter()

    def get_splash(self):
        result = Text(self.get_circle_pos(),str(self._num))
        result.setTextColor('black')
        return result

    def assign_connection(self,second_node):
        self._connections.append(Line(self.get_circle_pos(),second_node.get_circle_pos()))
        self._connections[-1].setFill("white")
        self._connections[-1].setWidth(2)

    def get_connections(self):
        return self._connections

    def get_circle(self):
        return self._circle

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
        if self._iterator < len(self._next):
            result = self._next[self._iterator]
            self._iterator+=1
            return result
        raise StopIteration

    #Get dictionary of object information
    def get_info(self): return self._info
    
    def switch_colour(self):
        if self._switch == True:
            self._circle.setFill('green')
            self._switch = False
        else:
            self._circle.setFill('white')
            self._switch = True