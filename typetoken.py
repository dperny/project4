class Typed_Token:
    def __init__(self,kind,value):
        self.kind = kind
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.kind,self.value)
    
    def __eq__(self,other):
        return self.value == other.value
    
    def __ne__(self,other):
        return self.value != other.value
