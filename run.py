#install the graphics.py library (pip install graphics.py)-> https://pypi.org/project/graphics.py/
from graphics import *
from func_edit import func
from node import node
import time

#Loads up nodes from save file (may be altered for different data type readings)
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

#Finds the mother nodes (given a list of nodes)
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

#Finds greatest path length (given an array of starting nodes (for display purposes))
def max_path_length(mother:list):
    def search(nodes:list,lis=[],count=1):
        for i in nodes:
            lis.append(count)
            search(i,lis,count+1)
    max_list = []
    search(mother,max_list)
    return max(max_list)

#Builds the underlying graph structure (Assigns circles to the nodes)
def build_graph(win:GraphWin,mother:list,step:int,level:int):
    next = []
    for i in mother:
        for j in i:
            if j not in next:
                next.append(j)
    start = 200
    x_step = (win.getWidth()-start*2)/(len(mother)-1) if len(mother)-1>0 \
        else (win.getWidth()-start*2)/2
    for j in mother:
        j.assign_circle(Circle(Point(start,level),x_step/5))
        start+=x_step
    if len(next)>0:
        build_graph(win,next,step,level+step)

#Draws the nodes assigned in the build graph phase
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

#Draws the connection lines between the nodes
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

#Draw the node ID's on top of them (the node number)
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

#Main function -> This is where all the code is executed
def main():
    #Open window
    win = GraphWin('Graph Recursion', 1080, 720)
    win.setBackground('black')
    #Define UI elements
    message1 = Text(Point(70, 30), 'E - propagate')
    message2 = Text(Point(48, 50), 'Q - Quit')
    message3 = Text(Point(win.getWidth()/2,win.getHeight()-100),' ')
    #Load node list and select starting nodes
    nodes = []
    load_nodes(nodes)
    mother = mother_nodes(nodes)
    #Assigns positions to the graph nodes
    build_graph(win,mother,(win.getHeight()-360)/(max_path_length(mother)-1),100)
    #Draws details - connections, nodes and text
    draw_connections(win,mother)
    draw_nodes(win,mother)
    draw_numbers(win,mother)
    #Draws UI to screen
    message1.setTextColor('white')
    message2.setTextColor('white')
    message3.setTextColor('white')
    message1.draw(win)
    message2.draw(win)
    message3.draw(win)
    #While Open Loop
    while win.isOpen():
        #Keyboard input
        key = win.getKey()
        #Events - key presses
        if key=="Q" or key=="q":
            message2.setTextColor('green')
            time.sleep(0.3)
            win.close()
        elif key=="E" or key=="e":
            message1.setTextColor('green')
            #RUN USER DEFINED FUNCTION
            return_value = func(message3,mother)
            #EDIT MESSAGE THREE TO DISPLAY THE RETURN OF THE USER DEFINED FUNCTION
            message3.setText(repr(return_value))
            message1.setTextColor('white')
        
#Call main
main()
