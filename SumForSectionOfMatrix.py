class SumForSectionOfMatrix:
    def __init__(self,matrix:list[list[int]]):
        row=len(matrix)
        col=len(matrix[0])
        self.matrix=[[0]*(col+1) for _ in range(row+1)]#此处用列表推导式初始化矩阵，
        # 请注意与self.matrix=[[0]*(col+1)]*(row+1)进行区别
        for i in range(row):
            for j in range(col):
                self.matrix[i+1][j+1]=self.matrix[i][j+1]+self.matrix[i+1][j]+matrix[i][j]-self.matrix[i][j]
    def sumRegion(self,row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix[row2+1][col2+1]-self.matrix[row2+1][col1]-self.matrix[row1][col2+1]+self.matrix[row1][col1]
A=[[1]*3]*3
s=SumForSectionOfMatrix(A)
print(s.matrix)
print(s.sumRegion(0,0,2,2))