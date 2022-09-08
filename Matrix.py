import math

class Matrix:
    
    def __init__(self, data):
        if self.check_integrity(data) == False:
            raise Exception('Matrix is incorrectly configured with row, column, or data type mismatch. Please provide a list of lists containing only ints or floats of consistent dimensions.')
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        self.shape = (self.rows, self.cols)
        self.size = self.rows * self.cols

    def check_integrity(self, data) -> bool:
        '''
        Args - data (list): ...
        Returns - bool
        '''
        # Check if provided matrix is a list
        if isinstance(data, list) == False:
            return False
        
        # Check if provided matrix is a list of lists
        checks = [isinstance(x, list) == False for x in data]
        if True in checks:
            return False
        
        # Check if provided matrix has consistent dimensions
        ncols = [len(x) for x in data]
        if sum(ncols) / len(ncols) != ncols[0]:
            return False
        
        # Check if provided matrix contains values of type int or float only
        for i in range(len(data)):
            checks = [isinstance(x, (int, float)) == False for x in data[i]]
            if sum(checks) > 0:
                return False

    def assign(self, row, col, value) -> None:
        if isinstance(value, (int, float)) == False:
            raise Exception('Value must be of type int or float only.')
        self.data[row][col] = value

    def fill(self, rows, cols, value) -> None:
        if isinstance(value, (int, float)) == False:
            raise Exception('Value must be of type int or float only.')
        for i in range(rows[0], rows[1], 1):
            for j in range(cols[0], cols[1], 1):
                self.assign(i, j, value)
    
    def retrieve(self, row, col) -> (int, float):
        return self.data[row][col]

    def diagonal(self) -> Matrix:
        matrix = []
        for i in range(self.rows):
            if i < self.cols:
                matrix.append([self.data[i][i]])
        return Matrix(matrix)
    
    def magnitude(self) -> float:
        if not (self.shape[0] == 1 or self.shape[1] == 1):
            raise Exception('Matrix must be a row or column vector only.')
        matrix = []
        for i in range(self.rows):
            for j in range(self.cols):
                matrix.append(self.data[i][j]**2)
        return math.sqrt(sum(matrix))

    def transpose(self) -> Matrix:
        matrix, row = [], []
        for j in range(self.cols):
            for i in range(self.rows):
                row.append(self.data[i][j])
            matrix.append(row)
            row = []
        return Matrix(matrix)

    # TODO
    def inverse(self) -> Matrix:
        if self.shape[0] != self.shape[1] and self.shape[0] < 2:
            raise Exception('Matrix is not invertible as it is a non-square matrix. Please provide a square matrix with dimensions greater than or equal to (2, 2).')
        matrix = [[1], [0]]
        return Matrix(matrix)

    # TODO
    def determinant(self) -> float:
        if self.shape[0] != self.shape[1] and self.shape[0] < 2:
            raise Exception('Matrix determinant cannot be derived as it is a non-square matrix. Please provide a square matrix with dimensions greater than or equal to (2, 2).')
        return 0

    def __add__(self, other) -> Matrix:
        if other.shape != self.shape:
            raise Exception('Matrix dimensions are mismatched ({} != {}). Please add (2) matrices of the same dimensions.'.format(self.shape, other.shape))
        data, output = self.data, []
        for i in range(self.rows):
            output.append([])
            for j in range(self.cols):
                output[i].append(self.data[i][j] + other.data[i][j])
        self.data = data
        return Matrix(output)
    
    def __ladd__(self, other) -> Matrix:
        return self.__add__(other)

    def __radd__(self, other) -> Matrix:
        return self.__add__(other)

    def __sub__(self, other) -> Matrix:
        if other.shape != self.shape:
            raise Exception('Matrix dimensions are mismatched ({} != {}). Please subtract (2) matrices of the same dimensions.'.format(self.shape, other.shape))
        data, output = self.data, []
        for i in range(self.rows):
            output.append([])
            for j in range(self.cols):
                output[i].append(self.data[i][j] - other.data[i][j])
        self.data = data
        return Matrix(output)
    
    def __lsub__(self, other) -> Matrix:
        return self.__sub__(other)

    def __rsub__(self, other) -> Matrix:
        return self.__sub__(other)

    def __mul__(self, other) -> Matrix:
        if isinstance(other, Matrix) == False:
            if isinstance(other, (int, float)) == False:
                raise Exception('Expecting a matrix or a scalar of type int or float only.')
        else:
            if self.size != other.size:
                raise Exception('Matrix dimensions are mismatched for pointwise matrix multiplication ({} != {})'.format(self.shape, other.shape))

        data, output = self.data, []
        
        # Scalar multiplication
        if isinstance(other, (int, float)):
            for i in range(self.rows):
                output.append([])
                for j in range(self.cols):
                    output[i].append(self.data[i][j] * other)

        # Matrix multiplication (pointwise)
        if isinstance(other, Matrix):
            for i in range(self.rows):
                output.append([])
                for j in range(self.cols):
                    output[i].append(self.data[i][j] * other.data[i][j])

        self.data = data
        return Matrix(output)

    def __lmul__(self, other) -> Matrix:
        return self.__mul__(other)

    def __rmul__(self, other) -> Matrix:
        return self.__mul__(other)

    def __matmul__(self, other) -> Matrix:
        if self.cols != other.rows:
            raise Exception('Matrix dimensions are mismatched for matrix multiplication ({} @ {}: {} != {})'.format(self.shape, other.shape, self.shape[1], other.shape[0]))
        data, output = self.data, []
        n, m = self.shape[1], self.shape[1]
        for i in range(n):
            output.append([])
            for j in range(m):
                value = 0
                for k in range(n):
                    value += self.data[i][k] * other.data[k][j]
                output[i].append(value)
        self.data = data
        return Matrix(output)
    
    def __lmatmul__(self, other) -> Matrix:
        return __matmul__(self, other)
    
    def __rmatmul__(self, other) -> Matrix:
        return __matmul__(self, other)

    def __repr__(self) -> str:
        matrix = str(self.data).replace('],', '],\n ')
        return "<class: 'Matrix'>\nDimensions: {} row(s) x {} column(s)\n {}\nSize: {}".format(self.rows, self.cols, matrix, self.size)
