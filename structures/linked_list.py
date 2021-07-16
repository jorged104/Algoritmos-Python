class nodo():
	"""docstring for Nodo"""
	def __init__(self,data : str ):
		self.data = data
		self.next = None

class linked_list():
    
    def __init__(self):
        #Head is a fist node at list
        self.head =None
    
    def append(self,data:str):
        new_nodo = nodo(data)
        
        if self.head == None:
            self.head = new_nodo
        else:
            temp_nodo = self.head

            while temp_nodo != None:

                if temp_nodo.next == None:
                    temp_nodo.next = new_nodo
                    return

                temp_nodo = temp_nodo.next
    
    def find(self, data : str ) -> nodo:
        temp_nodo = self.head
        while temp_nodo != None:
            if temp_nodo.data == data:
                return temp_nodo

            temp_nodo = temp_nodo.next

        return None
    
    def __str__(self):
        result = ""
        temp_nodo = self.head 
        while temp_nodo != None:
            result += temp_nodo.data + ", "
            temp_nodo = temp_nodo.next
        return result

if __name__ == "__main__":
    lista = linked_list()
    lista.append("Python")
    lista.append("JavaScript")
    lista.append("Java")

    print("Lista :  " , str(lista))
    javascript = lista.find("JavaScript")
    print(javascript.data)