class Node():
    def __init__(self , data: str):
        super().__init__()
        self.data :str  = data
        self.next :Node = None
        self.prev :Node = None

class circular_list():

    def __init__(self):
        self.head :Node = None
        
    def append(self,data :str ):
        new_nodo = Node(data)
        temp_node = self.head

        if temp_node == None:
            self.head = new_nodo
            new_nodo.next = new_nodo
            new_nodo.prev = new_nodo
            return
        
        """
            Go to last node 
        """
        temp_node = temp_node.prev

        temp_node.next = new_nodo
        new_nodo.prev = temp_node
        new_nodo.next = self.head

        self.head.prev = new_nodo
    

if __name__ == "__main__":
    list_double = circular_list()
    list_double.append("Python")
    list_double.append("JavaScript")
    list_double.append("Java")
    list_double.append("Go")
    list_double.append("Ruby")
    list_double.append("Now")

    temp_node = list_double.head
    count = 0 
    while count < 100:
        print(str(count) , "  ",temp_node.data)
        temp_node = temp_node.prev
        count += 1
        
        
        





    