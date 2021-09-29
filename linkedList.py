class Node(object):
    def __init__(self,data):
        self.data = data
        self.nextNode = None
    

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    def insertStart(self,data):
        self.size = self.size + 1 
        newNode = Node(data);

        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode

    def traverseList(self):
        actualNode = self.head
        while actualNode is not None:
            print((actualNode.data))
            actualNode = actualNode.nextNode
    
    def insertEnd(self,data):
        self.size = self.size + 1
        newNode = Node(data)
        actualNode = self.head
        while actualNode.nextNode is not None:
            actualNode = actualNode.nextNode
        actualNode.nextNode = newNode
    
    def remove(self,data):
        self.size = self.size -1
        if self.head is None:
            return;
        currentNode = self.head
        previousNode = None
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
        if previousNode is None:
            self.head = currentNode.nextNode
        else:
            previousNode.nextNode = currentNode.nextNode

    def search(self,data):
        if self.head is None:
            return;
        currentNode = self.head
        previousNode = None
        while currentNode.data != data:
            previousNode = currentNode
            currentNode = currentNode.nextNode
            if(currentNode == None):
                break
        if(currentNode == None):
            print("Oops!The song that you searched for doesn't exist :( ")
        else:
            print("Yay!Here's is the song that you searched for!Found {} successfully!".format(data))

    def len(self):
        if self.head is None:
            return;
        length =0
        currentNode = self.head
        #previousNode = None
        while currentNode != None:
            #previousNode = currentNode
            currentNode = currentNode.nextNode
            length = length+1
        print("Wohoo!! You have {} songs in your playlist!".format(length))

    def sortt(self):
        if self.head is None:
            return 
        lst = []
        currentNode = self.head
        while currentNode != None:
            lst.append(currentNode.data)
            currentNode = currentNode.nextNode
        lst.sort()
        print("The sorted Playlist is here!")
        print(*lst,sep='\n')
        
        
        
        



    
            





l1 = LinkedList()
l1.insertStart("Zaara")
l1.insertStart("Abi")
l1.insertStart("Hapie")
l1.insertEnd("Rhea")
l1.insertEnd("Sia")
l1.remove("Zaara")
l1.search("Rhea")
l1.search("Niv")
l1.search("Sen")
l1.len()
l1.sortt()
#l1.traverseList()
