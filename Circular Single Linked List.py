class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class Operation:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beg(self,ele):
        self.ele = ele

        if self.head == None:
            node = Node(self.ele,None)
            self.head = node
            self.tail = node
            return

        node = Node(self.ele, self.head)
        self.head = node
        self.tail.next = self.head

    def insert_pos(self,ele,pos):
        self.ele = ele
        self.pos = pos
        if self.pos > 1 and self.head == None:
            print("Invalid Position")
            return

        if self.pos == 1:
            self.insert_beg(self.ele)
            return

        count = 1
        temp = self.head
        while count != self.pos-1:
            if temp.next != self.head:
                temp = temp.next
                count += 1
            else:
                print("Invalid Position")
                return
                
        if temp.next == self.head:
            self.insert_end(self.ele)
            return
        
        node = Node(self.ele,temp.next)
        temp.next = node

    def insert_end(self,ele):
        self.ele = ele
        if self.head == None:
            self.insert_beg(self.ele)
            return

        node = Node(self.ele,self.head)
        self.tail.next = node
        self.tail = node
        node.next = self.head

    def delete_beg(self):
        if self.head == None:
            print("Empty")
            return

        if self.head.next == None:
            self.head = None
            self.tail = None
            return
        
        self.head = self.head.next
        self.tail.next = self.head

    def delete_pos(self,pos):
        self.pos = pos
        if self.head == None:
            print("Empty")
            return

        if self.pos == 1:
            self.delete_beg()
            return

        count = 1
        temp = self.head
        while count != self.pos-1:
            if temp.next != self.head:
                temp = temp.next
                count += 1
            else:
                print("Invalid Position")
                return

        if temp.next == self.head:
            print("Invalid Position")
            return
        
        if temp.next == self.tail:
            self.delete_end()
            return
        
        temp.next = temp.next.next

    def delete_end(self):
        if self.head == None:
            print("Empty")
            return

        temp = self.head
        while temp.next != self.tail:
            temp = temp.next

        self.tail = temp
        temp.next = self.head

    def search(self,ele):
        self.ele = ele
        temp = self.head
        while temp:
            if self.ele == temp.data:
                return True
            temp = temp.next
            if temp == self.head:
                break
        return False

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end='-->')
            temp = temp.next
            if temp == self.head:
                break
        print()
        

print('''1.Insert at beginning  2.Insert at position  3.Insert at end
4.Delete at beginning  5.Delete at position  6.Delete at end
7.Search               8.Display             9.Exit''')

CLL = Operation()

while True:
    choice = int(input("\nChoice: "))

    if choice==1:
        ele = input("Element: ")
        CLL.insert_beg(ele)

    elif choice==2:
        ele = input("Element: ")
        pos = int(input("Position: "))
        CLL.insert_pos(ele,pos)

    elif choice==3:
        ele = input("Element: ")
        CLL.insert_end(ele)

    elif choice==4:
        CLL.delete_beg()

    elif choice==5:
        pos = int(input("Position: "))
        CLL.delete_pos(pos)

    elif choice==6:
        CLL.delete_end()

    elif choice==7:
        ele = input("Element: ")
        print(CLL.search(ele))

    elif choice==8:
        CLL.display()

    else:
        exit()

