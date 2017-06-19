#Author: Cecelia Williams
#Last Revision: 05.12.2017
#Description: Chapter 27 Exercise 2
class Node:
    def __init__(self,value):
        self.value = value
        self.leftSide = None
        self.rightSide = None

    def insert(self,data):
        if self.value == data:
            return False
        elif self.value > data:
            if self.leftSide:
                return self.leftSide.insert(data)
            else:
                self.leftSide = Node(data)
                return True
        else:
            if self.rightSide:
                return self.rightSide.insert(data)
            else:
                self.rightSide = Node(data)
                return True

    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.leftSide:
                return self.leftSide.find(data)
            else:
                return False
        else:
            if self.rightSide:
                return self.rightSide.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.leftSide:
                self.leftSide.preorder()
            if self.rightSide:
                self.rightSide.preorder()

    def postorder(self):
        if self:
            print(str(self.value))
            if self.leftSide:
                self.leftSide.postorder()
            if self.rightSide:
                self.rightSide.postorder()
            print(str(self.value))

    def inorder(self):
        if self:
            print(str(self.value))
            if self.leftSide:
                self.leftSide.inorder()
            print(str(self.value))
            if self.rightSide:
                self.rightSide.inorder()

    def order_indented(self, level = 0):
        if self is None: return
        order_indented(self.rightSide, level + 1)
        print(" " * level + str(self.value))
        order_indented(self.leftSide, level + 1)
        
            


class Tree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def find(self,data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self):
        print("Preorder")
        self.root.preorder()

    def postorder(self):
        print("Postorder")
        self.root.postorder()

    def inorder(self):
        print("In Order")
        self.root.inorder()

    def order_indented(self):
        print("Indented Tree")
        self.root.order_indented()



bst = Tree()
bst.insert(10)
print(bst.insert(15))
bst.preorder()
bst.postorder()
bst.inorder()

