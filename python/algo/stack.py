class Stack:
    """
    Implementation of stack data structure
    """

    def init_stack(self):
        self.stack = []

    def check_if_empty(self):
        len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed item: {item}")

    def pop(self):
        if self.check_if_empty():
            print("Stack is empty")
        else:
            print(f"Removed item: {self.stack[len(self.stack) - 1]}")
            self.stack.pop()

    def display(self):
        print(self.stack)



nums = Stack()
nums.init_stack()
nums.push(12)
nums.push(2)
nums.push(45)
nums.pop()
nums.push(7)
nums.display()
