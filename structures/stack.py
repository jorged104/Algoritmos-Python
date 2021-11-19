class Node():
    def __init__(self, data : str):
        super().__init__()
        self.data = data 
        self.next = None
    
class stack():

    def __init__(self):
        self.head : Node = None
    
    def push(self ,data :str):
        nodo = Node(data)

        if self.head == None:
            self.head = nodo
            return
        
        nodo.next = self.head
        self.head = nodo
    
    def pop(self) -> str:
    
        if self.head == None:
            return ""
        
        nodo = self.head
        self.head = nodo.next
        return nodo.data

if __name__ == "__main__":

    pila = stack()
    pila.push("Python")
    pila.push("Java")
    pila.push("Golang")
    pila.push("C#")
    print(pila.pop())
    print(pila.pop())
    pila.push("C++")
    print(pila.pop())
    print(pila.pop())
    print(pila.pop())
    
        

