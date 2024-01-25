class Node:
    def __init__(self,val=0):
        self.val=val
        self.next=None
    
    def __str__(self):
        temp = self.next
        values = [self.val]

        while temp:
            values.append(temp.val)
            temp = temp.next
        return ' -> '.join(map(str, values))

class MyLinkedList:
    def __init__(self):
        self.head = Node()
           
    def get(self, index: int) -> int:
        # print('get',self.head)
        # if we had a dummy node 
        # increment the node
        index += 1

        # first step -> store the head in temp variable
        temp = self.head

        for _ in range(index):
            if temp == None:
                return -1
            temp = temp.next

        # return the value of the temp if temp exists
        if temp == None:
            return -1

        return temp.val

        

    def addAtHead(self, val: int) -> None:
        # print('addhead',self.head)
        
        # # if val was the first value
        # if self.head == None:
        #     self.head = Node(val)
        #     return
        
        # # we don't want to loose our head
        # # store the head at temp
        # temp = self.head

        # # intialize a new node
        # self.head = Node(val)

        # #connect the head with the temp
        # self.head.next = temp

        # basically add at head means add after the dummy node which is the 1 index
        self.addAtIndex(0, val)




        

    def addAtTail(self, val: int) -> None:
        # print('addtail',self.head)
        # if val was the first value
        # if self.head == None:
        #     self.head = Node(val)
        #     return
        
        # store the head reference
        temp = self.head

        # move until we reach the last node
        while temp and temp.next:
            # move to the next iteration
            temp = temp.next
        
        # temp is now the last node
        # temp.next will be the position to add the val
        temp.next = Node(val)


    def addAtIndex(self, index: int, val: int) -> None:
        # print('addindex',self.head)
        # # check if it is the first element
        # if index == 0:
        #     self.addAtHead(val)
        #     return
        
        # # update index by decrementing one
        # index -= 1

        # store our head in temp variable
        temp = self.head

        for i in range(index):
            # end of linked list without reaching the index
            if temp == None:
                return
            
            # move temp to the next node
            temp = temp.next
        
        # temp -> none could be?
        if temp == None:
            return
        
        # temp is now the value we have add after
        # create a new node
        new_node = Node(val)

        # update the pointers
        new_node.next = temp.next
        temp.next = new_node

            



    def deleteAtIndex(self, index: int) -> None:
        # print('delete index',self.head)
        # # if index == 0 -> first value
        # if index == 0:
        #     self.head = self.head.next
        #     return
        
        # # update the index 
        # index -= 1

        # store the head in temp variable
        temp = self.head

        for i in range(index):
            # end of linked list without reaching the index
            if temp == None:
                return
            
            # move temp to the next node
            temp = temp.next

        # temp -> none could be?
        if temp == None:
            return

        # temp is the value before to the value we want to delete
        # None.next -> should be checked
        if temp.next:
            # previous value next is now the next value of the deleted node
            temp.next = temp.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)