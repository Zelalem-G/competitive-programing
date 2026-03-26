class NumMatrix(object):

    def __init__(self, matrix):
        self.prefixMatrix = []

        # row prefix
        for i in range(len(matrix)):
            row = [0]*len(matrix[0])
            cur = 0
            for j in range(len(matrix[0])):
                row[j] = matrix[i][j] + cur
                cur += matrix[i][j]
            self.prefixMatrix.append(row)

        for j in range(len(matrix[0])):
            cur = 0
            for i in range(len(matrix)):
                val = self.prefixMatrix[i][j]   
                self.prefixMatrix[i][j] = val + cur
                cur += val

    def sumRegion(self, row1, col1, row2, col2):
        full = self.prefixMatrix[row2][col2]

        if col1-1 < 0 and row1-1 < 0:
            return full
        elif col1-1 < 0:
            return full - self.prefixMatrix[row1-1][col2]
        elif row1-1 < 0:
            return full - self.prefixMatrix[row2][col1-1]
        else:
            return (full 
                    - self.prefixMatrix[row2][col1-1] 
                    - self.prefixMatrix[row1-1][col2] 
                    + self.prefixMatrix[row1-1][col1-1])