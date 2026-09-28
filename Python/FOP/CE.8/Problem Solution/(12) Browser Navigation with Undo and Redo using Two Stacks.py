class Browser:
    def __init__(self):
        self.back_stack = []
        self.forward_stack = []
        self.current = None
    def visit(self, url):    
        if self.current:
            self.back_stack.append(self.current)
        self.current = url
        self.forward_stack.clear()
    def go_back(self):
        if self.back_stack:
            self.forward_stack.append(self.current)        
            self.current = self.back_stack.pop()
        return self.current
    def go_forward(self):
        if self.forward_stack:
            self.back_stack.append(self.current)
            self.current = self.forward_stack.pop()
        return self.current