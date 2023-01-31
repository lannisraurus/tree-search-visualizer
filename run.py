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

#Stores a graph in an orderly manner to allow for visualization
def load_nodes():
    result = []
    file = open('graph.data','r')
    for line in file:
        words = line.split(' ')
        if words[0]=="NODE":
            attributes = {}
            for attribute in words[2:]:
                dict_elems = attribute.split("=")
                attributes[dict_elems[0]] = float(dict_elems[1])
            result.append(node(int(words[1]),attributes))
        elif words[0]=="ADD":
            for i in result:
                if i.get_num()==int(words[1]):
                    for j in result:
                        if j.get_num()==int(words[2]):
                            print("ADDING")
                            i.add_dep(j)

    file.close()
    return result



#Finds the mother nodes
def mother_nodes(nodes:list):
    dependants = []
    for i in nodes:
        for j in i:
            if j not in dependants:
                dependants.append(j)
    return [i for i in nodes if i not in dependants]


#Draws the graph tree given a window and an ordered graph structure
def draw_graph(win:GraphWin,graph:list):
    a = 0






#Main function
def main():
    win = GraphWin('Graph Recursion', 1080, 720)
    nodes = load_nodes()
    mother = mother_nodes(nodes)

    for i in nodes: print(i)
    static_ui(win)
    while win.isOpen():

        #Keyboard events
        if win.getKey()=="Q" or win.getKey()=="q": win.close()
        elif win.getKey()=="E" or win.getKey()=="e": func(win,mother_nodes)
        




main()
























"""
head = Circle(Point(40,100), 25) # set center and radius
head.setFill("yellow")
head.draw(win)

eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
eye2.setWidth(3)
eye2.draw(win)
"""
