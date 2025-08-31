class BinaryAdd:
    def __init__(self, b1:str, b2:str):
        if len(b1)!=b1.count('1')+b1.count('0') or len(b2)!=b2.count('1')+b2.count('0'):
            raise ValueError("Invalid binary number")
        self.b1 = b1
        self.b2 = b2

    def add(self) -> str:
        result = ''
        carry = 0
        for i in range(-1,-max(len(self.b1),len(self.b2))-1,-1):
            add1=0
            add2=0
            if i>=-len(self.b1):
                add1=1 if self.b1[i]=='1' else 0
            if i>=-len(self.b2):
                add2=1 if self.b2[i]=='1' else 0
            sum_ = add1+add2+carry
            result = str(sum_ % 2) + result
            carry = sum_ // 2
        if carry:
            result = str(carry) + result
        return result
# Example usage:
b1 = '1011'
b2 = '1101'
binary_add = BinaryAdd(b1, b2)
print(binary_add.add()) # Output: '10000'