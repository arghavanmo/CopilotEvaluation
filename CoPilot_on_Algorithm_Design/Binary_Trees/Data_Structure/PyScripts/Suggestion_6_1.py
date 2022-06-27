

class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
                self.left.parent = self
            else:
                self.left.insert(value)
        elif value > self.value:
            if self.right is None:
                self.right = BST(value)
                self.right.parent = self
            else:
                self.right.insert(value)
        else:
            print(""Value already in tree!"")
    def search(self, value):
        if value < self.value:
            if self.left is None:
                return None
            else:
                return self.left.search(value)
        elif value > self.value:
            if self.right is None:
                return None
            else:
                return self.right.search(value)
        else:
            return self
    def delete(self, value):
        if value < self.value:
            if self.left is None:
                print(""Value not in tree!"")
            else:
                self.left.delete(value)
        elif value > self.value:
            if self.right is None:
                print(""Value not in tree!"")
            else:
                self.right.delete(value)
        else:
            if self.left is None and self.right is None:
                if self.parent.left == self:
                    self.parent.left = None
                else:
                    self.parent.right = None
            elif self.left is None:
                if self.parent.left == self:
                    self.parent.left = self.right
                else:
                    self.parent.right = self.right
            elif self.right is None:
                if self.parent.left == self:
                    self.parent.left = self.left
                else:
                    self.parent.right = self.left

