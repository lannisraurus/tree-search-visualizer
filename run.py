#install the graphics.py library (pip install graphics.py)-> https://pypi.org/project/graphics.py/
from graphics import *
from func_edit import func
from node import node

#Static UI elements
def static_ui(win:GraphWin):
    win.setBackground('black')
    message1 = Text(Point(70, 30), 'E - propagate')
    message2 = Text(Point(48, 50), 'Q - Quit')
    message1.setTextColor('white')
    message2.setTextColor('white')
    message1.draw(win)
    message2.draw(win)

#Loads up nodes from save file
def load_nodes(store:list):
    file = open('graph.data','r')
    for line in file:
        line.strip("\n")
        words = line.split(' ')
        if words[0]=="NODE":
            attributes = {}
            for attribute in words[2:]:
                dict_elems = attribute.split("=")
                attributes[dict_elems[0]] = float(dict_elems[1])
            obj = node(int(words[1]),attributes)
            store.append(obj)
    file.close()

#Connects node list
def connect_nodes(connect:list):
    file = open('graph.data','r')
    for line in file:
        words = line.split(' ')
        if words[0]=="ADD":
            one = 0
            while one < len(connect):
                if connect[one].get_num()==int(words[1]):
                    two = 0
                    while two < len(connect):
                        if connect[two].get_num()==int(words[2]):
                            connect[one]+=connect[two]
                            break
                        else:
                            two+=1
                    break
                else:
                    one+=1
    file.close()


#Finds the mother nodes
def mother_nodes(nodes:list):
    def aux(nod:node,lis:list):
        for i in nod:
            if i not in lis:
                lis.append(i)
            aux(i,lis)
    dependants = []
    for i in nodes:
        aux(i,dependants)
    return [k for k in nodes if k not in dependants]


#Draws the graph tree given a window and an ordered graph structure
def draw_graph(win:GraphWin,graph:list):
    a = 0


#Main function
def main():
    win = GraphWin('Graph Recursion', 1080, 720)
    nodes = []
    load_nodes(nodes)
    connect_nodes(nodes)
    mother = mother_nodes(nodes)
    static_ui(win)
    while win.isOpen():

        #Keyboard events
        key = win.getKey()
        if key=="Q" or key=="q": win.close()
        elif key=="E" or key=="e": func(win,mother)
        




main()
























"""
head = Circle(Point(40,100), 25) # set center and radius
head.setFill("yellow")
head.draw(win)

eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
eye2.setWidth(3)
eye2.draw(win)
"""
