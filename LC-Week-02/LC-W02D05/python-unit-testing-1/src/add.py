# src/add.py

def addition(x, y):
    """Simple addition function"""
    return x + y


class Calculator():
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def addition(self):
        # If x and y are not integers 
        # return: Enter a valid integer
        
        if type(self.x) == int and type(self.y) == int:
            return self.x + self.y
        
        # if isinstance(self.x, int) and isinstance(self.y, int):
        #     return self.x + self.y
        
        raise ValueError("Value is not an integer value")





