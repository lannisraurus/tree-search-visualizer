import node
from graphics import *
import time

#You can edit this function and try out different graph search methods
def func(message:Text,start_nodes:list):
    """
    message -> The information message on the screen, add information need be (for visualization)
    start_nodes -> the list of mother/start nodes
    NOTE: This may all be altered for your specific objective. The default example shown here is
    a depth search.
    """

    #Auxiliary recursive function
    def recurs(message:Text,start:node):
        #Display node information to the information tab
        info = start.get_info()
        new_name = f"Information:\nNode {start.get_num()}"
        for i in info:
            new_name += "\n"+str(i[0])+" = "+str(i[1])
        message.setText(new_name)
        #White->Green
        start.switch_colour('green')
        #Sleep for x seconds (for visualization)
        time.sleep(0.35)
        #Recursion -> depth search
        for i in start:
            recurs(message,i)
        #Green->White (this is where a return statement would be placed. the node closes)
        start.switch_colour('white')

    #Uses user-defined function (recurs) in all start nodes (mother_nodes)
    for i in start_nodes:
        recurs(message,i)