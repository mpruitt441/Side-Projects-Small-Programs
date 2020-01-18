start = None
last = None
qfirst = None
qlast = None

#todo:class variables to allow multiple instances of each data structure

# Implementation of Circularly Doubly Linked List
class CDLL:
    def __init(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def insertBegin(self, val):
        global start
        # insert value into a new node
        if start == None: #if the list is empty, create a node that points to itself
            newNode = CDLL(val)
            newNode.next = newNode
            newNode.prev = newNode

        else:
            newNode = CDLL(val)
            newNode.next = start
            newNode.prev = start.prev
            start.prev.next = newNode

        start = newNode

        
        return

    def insertEnd(self, val):
        global start
        if start == None:
            newnode = CDLL(val)
            newnode.next = newnode
            newnode.prev = newnode

        else:
            last = start.prev
            newnode = CDLL(val)
            newnode.next = start
            newnode.prev = last
            last.next = newnode
            start.prev = newnode

        return

    def insertAfter(self, dataval, node):
        global start
        #check if the node type is CDLL
        #this makes it so that the function actually only works when the list has values
        if type(node) is CDLL:
            newnode = CDLL(dataval)
            newnode.next = node.next
            node.next.prev = newnode
            node.next = newnode
            newnode.prev = node 
            return

        else:
            print("ERROR! 'node' value must be CDLL type")
            return

    def insertBefore(self, dataval, node):
        global start
        #check if the node type is CDLL
        #this makes it so that the function actually only works when the list has values
        if type(node) is CDLL:
            newnode = CDLL(dataval)
            
            newnode.next = node
            newnode.prev = node.prev

            node.prev.next = newnode
            node.prev = newnode
            return
        else:
            print("ERROR! 'node' value must be CDLL type")
            return
    def display(self):
        global start
        temp = start
        if start == None:
            print("Circularly Doubly Linked List is empty!!!! Oh no!")
            return
        else:
            # print current data
            print(temp.data," ")
            # check if the next value is start. if it isnt, traverse then print data
            while (temp.next != start):
                temp = temp.next
                print(temp.data, " ")
    def removeFirst(self):
        global start
        temp = start
        start.prev.next = start.next
        start.next.prev = start.prev
        start = start.next
        del temp
        return
    def removeLast(self):
        global start
        lastitem = start.prev
        lastitem.prev.next = start
        start.prev = lastitem.prev
        del lastitem
        return
    def removeData(self,data):
        # only removes one item with this data
        global start
        if start == None:
            print("No data..")
            return
        temp = start

        while temp.data != data & temp.next != temp:
            temp = temp.next

        if temp.data == data:
            if temp == start:# if this is the first item in the list, need to set a new head
                deletable = temp
                temp.next = start
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                del deletable
            else:
                deletable = temp
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                del deletable

        else:
            print("No item found")

        return

    def removeAllData(self,data):
        global start
        if start == None:
            print("No data..")
            return
        temp = start
        x = data
        while temp.data != data and temp.next != temp and temp.next != start:
            temp = temp.next
        if temp.data == data:
            if temp == start:
                deletable = temp
                temp.next = start
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                del deletable
                self.removeAllData(x)
            else:
                deletable = temp
                temp.prev.next = temp.next
                temp.next.prev = temp.prev
                del deletable
                self.removeAllData(x)
        else:
            print("Last item deleted or no item found")
        return
        

# Implementation of Stack
class Stack:
    
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None


    def add(self,data):
        global last
        if last == None:
            last = Stack(data)
            last.next = None

        else:
            newdata = Stack(data)
            newdata.prev = last
            last.next = newdata
            newdata.next = None
        return

    def pop(self):
        global last
        if last == None:
            print("There's nothing in the stack")
            return
        else:
            print("popping:", last.data)
            if last.prev == None:
                print("This is the last item in the stack")
                last = None
                return
            else:
                #assign last to a temporary variable
                temp = last
                last = last.prev
                del temp
                return
    
    def display(self):
        if last == None:
            print("There's nothing in the stack")
        else:
            temp = last
            if temp.prev == None:
                print("Only one item in the stack:", temp.data)
            else:
                print("Last item in the stack:",temp.data)

            while temp.prev != None:
                temp.prev = temp
                print(temp.data)
                if(temp.prev == None):
                    print("First item in the stack:")
        return
                
# Implementation of Queue
class Q:

    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
    
    def queueup(self,data):
        global qfirst, qlast

        if qfirst == None or qlast == None: # if there's nobody in the queue, you're first!
            qfirst = Q(data)
            qlast = qfirst
        else:
            newdata = Q(data)
            qlast.next = newdata
            newdata.prev = qlast
            qlast = newdata
            qlast.next = None
        return


    def nextInLine(self): # someone passes the queue
        global qfirst

        if qfirst == None:
            print("Queue is empty..")
        else:
            temp = qfirst
            qfirst = qfirst.next
            print(temp.data, "has passed the queue")
            qfirst.prev = None
        return

    def exitQ(self,data):
        #specific item exits from queue
        global qfirst, qlast

        if qfirst == None:
            print("Queue is empty..:")
        else:
            temp = qfirst # set the first item as a temporary item so we can start iterating through
            while temp.data != data and temp.next != temp:
                temp = temp.next
            if temp.data == data:
                if temp.next == None and temp.prev == None:
                    print("This is the only item in the queue")
                elif (temp.next == None):
                    temp.prev.next = None
                    qlast = temp.prev
                    print(temp.data, "Is leaving the queue..")
                else:
                    deletable = temp
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    del deletable
            else:
                print("No item found")


        return
