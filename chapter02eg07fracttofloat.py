class Fraction:
    def __init__(self, numerator:int, denominator:int):
        self.numerator = numerator
        self.denominator = denominator

    def to_float(self)->str:
        singe="-" if (self.numerator<0 and self.denominator>0) or (self.numerator>0 and self.denominator<0) else ""
        num=abs(self.numerator)
        den=abs(self.denominator)
        if not num % den:
            return singe+str(num / den)[:-2]
        else:
            result=singe+str(num // den)+"."
            num=num % den
            mod_dict={num:len(result)}
            while num:
                result+=str(num*10 // den)
                num=num*10 % den
                if num in mod_dict:
                    result=result[:mod_dict[num]]+"("+result[mod_dict[num]:]+")"
                    break
                mod_dict[num]=len(result)
            return result

# Example usage
f = Fraction(9, 3)
print(f.to_float()) # Output: 3
f = Fraction(-1, 3)
print(f.to_float()) # Output: -0.(3)