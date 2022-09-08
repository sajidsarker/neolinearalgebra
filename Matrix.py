#!/usr/bin/env python3
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
    
    def fill(self, row_range_start, row_range_end, col_range_start, col_range_end, value) -> None:
        if isinstance(value, (int, float)) == False:
            raise Exception('Value must be of type int or float only.')
	for i in range(row_range_start, row_range_end, 1):
		for j in range(col_range_start, col_range_end, 1):
			self.data[i][j] = value
 
    def retrieve(self, row, col) -> (int, float):
        return self.data[row][col]

    def diagonal(self) -> object:
        matrix = []
        for i in range(self.rows):
            if i < self.cols:
                matrix.append([self.data[i][i]])
        return Matrix(matrix)

    def transpose(self) -> object:
        matrix, row = [], []
        for j in range(self.cols):
            for i in range(self.rows):
                row.append(self.data[i][j])
            matrix.append(row)
            row = []
        return Matrix(matrix)

    # TODO
    def inverse(self) -> object:
        if self.shape[0] != self.shape[1] and self.shape[0] < 2:
            raise Exception('Matrix is not invertible as it is a non-square matrix. Please provide a square matrix with dimensions greater than or equal to (2, 2).')
        matrix = [[1], [0]]
        return Matrix(matrix)

    # TODO
    def determinant(self) -> float:
        if self.shape[0] != self.shape[1] and self.shape[0] < 2:
            raise Exception('Matrix determinant cannot be derived as it is a non-square matrix. Please provide a square matrix with dimensions greater than or equal to (2, 2).')
        return 0

    def __add__(self, other) -> object:
        if other.shape != self.shape:
            raise Exception('Matrix dimensions are mismatched ({} != {}). Please add (2) matrices of the same dimensions.'.format(self.shape, other.shape))
        data, output = self.data, []
        for i in range(self.rows):
            output.append([])
            for j in range(self.cols):
                output[i].append(self.data[i][j] + other.data[i][j])
        self.data = data
        return Matrix(output)

    def __sub__(self, other):
        if other.shape != self.shape:
            raise Exception('Matrix dimensions are mismatched ({} != {}). Please subtract (2) matrices of the same dimensions.'.format(self.shape, other.shape))
        data, output = self.data, []
        for i in range(self.rows):
            output.append([])
            for j in range(self.cols):
                output[i].append(self.data[i][j] - other.data[i][j])
        self.data = data
        return Matrix(output)

    def __mul__(self, scalar) -> object:
        if isinstance(scalar, (int, float)) == False:
            raise Exception('Scalar must be of type int or float only.')
        data, output = self.data, []
        for i in range(self.rows):
            output.append([])
            for j in range(self.cols):
                output[i].append(self.data[i][j] * scalar)
        self.data = data
        return Matrix(output)

    def __lmul__(self, scalar) -> Matrix:
	self.__mul__(scalar)

    def __rmul__(self, scalar) -> Matrix:
	self.__mul__(scalar)

    # TODO
    #def __mul__(self, other):
    #    pass

    # TODO
    #def cross(self, other):
    #    pass

    # TODO
    #def dot(self, other):
    #    pass

    def __repr__(self) -> str:
        matrix = str(self.data).replace('],', '],\n ')
        return "<class: 'Matrix'>\nDimensions: {} row(s) x {} column(s)\n {}\nSize: {}".format(self.rows, self.cols, matrix, self.size)
