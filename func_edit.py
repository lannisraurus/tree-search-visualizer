import node
from graphics import *
import time

def func(win:GraphWin,start_nodes:list):
    def recurs(win,start:node):
        start.switch_colour()
        time.sleep(0.2)
        for i in start:
            recurs(win,i)
        start.switch_colour()
    for i in start_nodes:
        recurs(win,i)