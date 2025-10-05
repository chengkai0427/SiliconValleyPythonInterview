import re
class ValidNumber:
    def __init__(self, number:str):
        self.number = number

    def is_valid(self):
        pattern = re.compile(r'^[+-]?([0-9]+[.]?[0-9]*|[0-9]*[.]?[0-9]+)([eE][+-]?[0-9]+)?$')
        return bool(pattern.match(self.number))

# Testing the code
print(ValidNumber('123').is_valid())
print(ValidNumber('-1.2e-3.4').is_valid())
print(ValidNumber('12a3').is_valid())
print(ValidNumber('123.').is_valid())