class Node():
    def __init__(self,data : str ) -> None:
        self.data = data
        self.next = None

class queue():
    def __init__(self):
        self.head : Node  = None

    def Enqueue(self, data : str):
        node = Node(data)
        
        if self.head == None:
            self.head = node
            return
        
        temp = self.head
        while temp.next != None:
            temp = temp.next 
        
        temp.next = node
        
    def Dequeue(self) -> str :
        if self.head == None:
            return ""
        temp = self.head 
        self.head = self.head.next
        return temp.data
        

if __name__ == "__main__":
    cola = queue()
    cola.Enqueue("Python")
    cola.Enqueue("Java")
    cola.Enqueue("C++")
    print(cola.Dequeue())
    print(cola.Dequeue())
    print(cola.Dequeue())
    print(cola.Dequeue())

