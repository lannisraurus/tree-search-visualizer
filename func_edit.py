import node
from graphics import *
import time

#You can edit this function and try out different graph search methods
def func(win:GraphWin,message:Text,start_nodes:list):

    #EDIT HERE! - Must include two switch instances to show the searched nodes
    def recurs(win,message:Text,start:node):
        #Display node information to the information tab
        info = start.get_info()
        new_name = f"Information:\nNode {start.get_num()}"
        for i in info:
            new_name += "\n"+str(i[0])+" = "+str(i[1])
        message.setText(new_name)
        #White->Green
        start.switch_colour()
        #Sleep for x seconds (for visualization)
        time.sleep(0.35)
        for i in start:
            recurs(win,message,i)
        #Green->White
        start.switch_colour()

    #Uses user-defined function in all start nodes (mother_nodes)
    for i in start_nodes:
        recurs(win,message,i)