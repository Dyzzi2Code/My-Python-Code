#Author: Cecelia Williams
#Last Revision: 05.12.2017
#Description: Chapter 26 Exercise 2
class PriorityQueue:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return not self.items

    def insert(self, item):
        self.items.append(item)
        
    def remove(self):
        maxi = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[maxi]:
                maxi = i
        item = self.items[maxi]
        del self.items[maxi]
        return item

    def print_queue(self):
        print(self.items)

def main():
    

    q = PriorityQueue()
    for fruit in ["Apple", "Banana", "Cantalope", "Elderberry", "Blackberry",
                  "Grape", "Honeyberry", "Strawberry", "Jostaberry",
                  "Kiwi", "Lime", "Mango"]:
        q.insert(fruit)
        

    if not q.is_empty():
        print(q.print_queue())


    add_decision = input("Do you want to add any fruit to the list?\n")
    if add_decision == "yes" or add_decision == "Yes":
        add_me = input("Enter the name of the fruit to add:\n")
        q.insert(add_me)
        if not q.is_empty():
            print(q.print_queue())
    
    remove_decision = input("Would you like to remove a fruit from the list?\n")
    if remove_decision == "yes" or remove_decision == "Yes":
            remove_me = ("Enter the name of the fruit to remove:\n")
            q.remove(remove_me)
            if not q.is_empty():
                print(q.print_queue())
        

  
    



main()
