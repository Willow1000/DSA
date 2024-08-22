class Node:
    def __init__(self,data):
        self.data=data
    def __repr__(self):
        return f"{self.data}"

class linkeList:
    def __init__(self):
        self.head=None
    def is_empty(self)            :
        return self.head==None
    def size(self):
        count=0
        current=self.head

        while current:
            count+=1
            current=current.next_node
        return count
    def add(self,data):
        new_node=Node(data)            
        new_node.next_node=self.head
        self.head=new_node

    def insert(self,index,data):
        if index==0:
            self.add(data)    
        elif index>0:
            position=index
            current=self.head
            new_node=Node(data)
            while position > 1:
                current=current.next_node
                position-=1

            previous_node=current
            next_node=current.next_node

            previous_node.next_node=new_node
            new_node.next_node=next_node

        return current

    def __repr__(self):
        nodes=[]
        current=self.head

        while current:
            if current == self.head:
                nodes.append(f"Head:{current}")
            elif current.next_node ==  None:
                nodes.append(f"Tail:{current}")
            else:
                nodes.append(current)
            current=current.next_node
        return f"{nodes}"        

    def remove(self,key=None,index=None):
        current=self.head

        if key:
            found=False

            while current and not found:
                if current==self.head and current.data==key:
                    self.head=current.next_node
                    found=True
                elif current.data==key:
                    found=True    
                else:
                    previous=current
                    current=current.next_node
            previous.next_node=current.next_node    
            if found:
                return True
            else:
                return False


        elif index:
            assert(index < self.size()),'IndexOutOfRange'
            position=index
            if index==0:
                self.head=current.next_node
            elif index>0:
                while position!=0:
                    previous=current
                    current=current.next_node
                    position-=1

                previous.next_node=current.next_node


items=linkeList()    
items.add(10)  
items.add(7)
items.add(15)
items.insert(1,33)
items.remove(key=33)
print(items)

