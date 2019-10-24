import random
import queue 

#get() removes in FIFO style


#BFS node Addition Queue
BFSNodeAddQueue = queue.Queue(maxsize=1000)
#Print Queue
printQueue = queue.Queue(maxsize=1000)


#node structure
class node:
    #inititalization defaults for root
    def __init__(self,data=0,previous=""):
        self.data = data
        self.children = []
        #address of parent; for root = ""
        self.previous=previous


#root storage node creation #root and generic object creation for other nodes #obj
obj = node()
root = obj
#insert created node address to end of queue; here,root
BFSNodeAddQueue.put(obj)

while(1):
    #Get FIFO style node address from Queue
    obj = BFSNodeAddQueue.get()
    #node creation termination condition
    choice = input("Stop y/n?")
    if choice=="y":
        break
    #creating 4 children for each node
    for i in range(4):
        data = int(input("Enter some data: "))
        #create node with parameters: data,address of previous node
        n1 = node(data,obj)
        #Append address of created node to children list of previous node
        obj.children.append(n1)
        #insert created node address to end of queue
        BFSNodeAddQueue.put(n1)

#print: BFS Style
#get root addr
printobj = root
#store in print queue for standard procedure
printQueue.put(printobj)

#termination cond for print
while(printQueue.empty()==False):
    #Address FIFO style
    pr = printQueue.get()
    print(pr.data)
    #Put children of node in children list into queue
    for i in range(len(pr.children)):
        printQueue.put(pr.children[i])

