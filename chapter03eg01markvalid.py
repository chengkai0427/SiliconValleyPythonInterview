class MarkValid:
    '''
    给定字符串s，其中包括英文字母和左右小括号，请删除最少括号使得括号字符有效（即小括号左右匹配）。
    '''
    def __init__(self, mark:str):
        import re
        if not re.match(r'^[A-Za-z()]+$', mark):
            raise ValueError("参数mark只能包含字母和括号")
        self.mark = mark
    def to_valid(self)->str:
        from collections import deque
        parentheses = deque()
        for n,a in enumerate(self.mark):
            if a == ')':
                if parentheses and self.mark[parentheses[-1]]=='(':
                    parentheses.pop()
                else:
                    parentheses.append(n)
            elif a == '(':
                parentheses.append(n)
        if parentheses:
            s=''
            for n in range(len(self.mark)):
                if parentheses and n == parentheses[0]:
                    parentheses.popleft()
                elif not parentheses:
                    s+=self.mark[n:]
                    break
                else:
                    s+=self.mark[n]
            return s
        else:
            return self.mark
if __name__ == '__main__':
    print(MarkValid(input("请输入待校证的标记：")).to_valid())