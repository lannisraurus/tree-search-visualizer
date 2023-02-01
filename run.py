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
        elif words[0]=="ADD":
            one = 0
            while one < len(store):
                if store[one].get_num()==int(words[1]):
                    two = 0
                    while two < len(store):
                        if store[two].get_num()==int(words[2]):
                            store[one]+=store[two]
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

#Finds greatest path length
def max_path_length(mother:list):
    def search(nodes:list,lis=[],count=1):
        for i in nodes:
            lis.append(count)
            search(i,lis,count+1)
    max_list = []
    search(mother,max_list)
    return max(max_list)

#Draws the graph tree given a window and an ordered graph structure
def build_graph(win:GraphWin,mother:list,step:int,level:int):
    next = []
    for i in mother:
        for j in i:
            if j not in next:
                next.append(j)
    start = 200
    x_step = (win.getWidth()-start*2)/(len(mother)-1) if len(mother)-1>0 else 0
    for j in mother:
        j.assign_circle(Circle(Point(start,level),step/5))
        start+=x_step
    if len(next)>0:
        build_graph(win,next,step,level+step)

def draw_nodes(win:GraphWin,mother:list):
    next = []
    for i in mother:
        i.get_circle().undraw()
        i.get_circle().draw(win)
        for j in i:
            if j not in next:
                next.append(j)
    if len(next)>0:
        draw_nodes(win,next)

def draw_connections(win:GraphWin,mother:list):
    next = []
    for i in mother:
        for j in i:
            if j not in next:
                next.append(j)
            i.assign_connection(j)
    for i in mother:
        for j in i.get_connections():
            j.undraw()
            j.draw(win)
    if len(next)>0:
        draw_connections(win,next)

def draw_numbers(win:GraphWin,mother:list):
    next = []
    for i in mother:
        i.get_splash().undraw()
        i.get_splash().draw(win)
        for j in i:
            if j not in next:
                next.append(j)
    if len(next)>0:
        draw_numbers(win,next)


#Main function
def main():
    win = GraphWin('Graph Recursion', 1080, 720)
    nodes = []
    load_nodes(nodes)
    mother = mother_nodes(nodes)
    build_graph(win,mother,(win.getHeight()-200)/(max_path_length(mother)-1),100)
    draw_connections(win,mother)
    draw_nodes(win,mother)
    draw_numbers(win,mother)
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
