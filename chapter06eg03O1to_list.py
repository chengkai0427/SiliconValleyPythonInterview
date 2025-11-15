class o1to_list:
    def __init__(self):
        self.lst = []
        self.value_index = {}
    def insert(self,value: object)->bool:
        if value in self.value_index:
            return False
        self.lst.append(value)
        self.value_index[value] = len(self.lst)-1
        return True
    def remove(self,value: object)->bool:
        if value not in self.value_index:
            return False
        self.value_index[self.lst[-1]] = self.value_index[value]
        self.lst[self.value_index[value]],self.lst[-1] = self.lst[-1],self.lst[self.value_index[value]]
        self.lst.pop()
        del self.value_index[value]
        return True
    def getrangdom(self)->int:
        import random
        return self.lst[random.randint(0,len(self.lst)-1)]
#test
o1to_list = o1to_list()
o1to_list.insert(1)
o1to_list.insert(2)
o1to_list.insert(3)
o1to_list.insert(4)
o1to_list.insert(5)
print(o1to_list.lst)
print(o1to_list.value_index)
o1to_list.remove(2)
print(o1to_list.lst)
print(o1to_list.value_index)
print(o1to_list.getrangdom())