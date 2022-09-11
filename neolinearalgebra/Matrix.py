import sys
import math

class Matrix:
    '''
    Description
    Attributes
    data
    rows
    cols
    shape
    size
    '''
    def __init__(self, data):
        if self.check_integrity(data) == False:
            raise ValueError('Matrix is incorrectly configured with empty matrix or row, column, or data type mismatch. Please provide a list of lists containing only ints or floats of consistent dimensions.')

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

        if self.check_if_list(data) == False:
            return False
        
        if self.check_if_list_of_lists(data) == False:
            return False

        if self.check_if_consistent_dimensions(data) == False:
            return False

        if self.check_if_empty(data) == True:
            return False
        
        if self.check_if_numeric_dtype(data) == False:
            return False

        return True

    
    def check_if_list(self, data) -> bool:
        '''
        Checks if the provided matrix is a list.
        '''
        if isinstance(data, list) == False:
            raise TypeError('Expecting matrix to be formatted as a list.')
            return False
        else:
            return True


    def check_if_list_of_lists(self, data) -> bool:
        '''
        Checks if the provided matrix is a list of lists
        '''
        if len(data) == 0:
            raise TypeError('Expecting matrix to be formatted as a list of lists.')
            return False
        checks = [isinstance(x, list) == False for x in data]
        if True in checks:
            raise TypeError('Expecting matrix to be formatted as a list of lists.')
            return False
        else:
            return True


    def check_if_consistent_dimensions(self, data) -> bool:
        '''
        Checks if the provided matrix has consistent dimensions.
        '''
        ncols = [len(x) for x in data]
        if sum(ncols) / len(ncols) != ncols[0]:
            raise IndexError('Expecting matrix to be provided with consistent dimensions.')
            return False
        else:
            return True
        
    def check_if_empty(self, data) -> bool:
        '''
        Checks if the provided matrix has empty columns.
        '''
        ncols = [len(x) for x in data]
        if ncols[0] == 0:
            raise IndexError('Expecting matrix to be non-empty.')
            return True
        else:
            return False
    
    def check_if_numeric_dtype(self, data) -> bool:
        '''
        Checks if the provided matrix contains values of type int or float only.
        '''
        for i in range(len(data)):
            checks = [isinstance(x, (int, float)) == False for x in data[i]]
            if sum(checks) > 0:
                raise ValueError('Expecting matrix to contain values of type int or float only.')
                return False
        return True
    
    
    def check_if_square_matrix(self, data) -> bool:
        '''
        Checks if the provided matrix is a square matrix.
        '''
        return len(data) == len(data[0])
    
    
    def check_if_vector(self, data) -> bool:
        '''
        Checks if the provided matrix is a row or column vector.
        '''
        return len(data) == 1 or len(data[0]) == 1


    def assign(self, row, col, value) -> None:
        if isinstance(value, (int, float)) == False:
            raise Exception('Value must be of type int or float only.')

        self.data[row][col] = value


    def fill(self, rows, cols, value) -> None:
        if isinstance(value, (int, float)) == False:
            raise Exception('Value must be of type int or float only.')

        for row in range(rows[0], rows[1]):
            for col in range(cols[0], cols[1]):
                self.data[row][col] = value


    def retrieve(self, row, col) -> (int, float):
        return self.data[row][col]


    def diagonal(self) -> object:
        output = []

        for i in range(self.rows):
            if i < self.cols:
                output.append([self.data[i][i]])

        return Matrix(output)


    def trace(self) -> float:
        output, data = 0, self.diagonal().data

        for row in range(len(data)):
            output += sum(data[row])

        return output


    def magnitude(self) -> float:
        if self.check_if_vector(self.data) == False:
            raise Exception('Matrix must be a row or column vector only.')

        output = []

        for row in range(self.rows):
            for col in range(self.cols):
                output.append(self.data[row][col]**2)

        return math.sqrt(sum(output))


    def transpose(self) -> object:
        output, row = [], []

        for j in range(self.cols):
            for i in range(self.rows):
                row.append(self.data[i][j])
            output.append(row)
            row = []

        return Matrix(output)


    def determinant(self) -> float:
        if self.check_if_square_matrix(self.data) == False:
            raise Exception('Matrix determinant cannot be derived as it is a non-square matrix. Please provide a square matrix.')

        output, det = self.data, 0
        indices = list(range(len(output)))

        if len(output) == 1 and len(output[0]) == 1:
            return output[0][0]

        if len(output) == 2 and len(output[0]) == 2:
            return output[0][0] * output[1][1] - output[1][0] * output[0][1]

        for focus_column in indices:
            principal_minor = output[1:]
            for row in range(len(principal_minor)):
                principal_minor[row] = principal_minor[row][0:focus_column] + principal_minor[row][focus_column+1:]

        sub_det = Matrix(principal_minor).determinant()
        det += (-1)**(focus_column % 2) * output[0][focus_column] * sub_det

        return det


    def inverse(self) -> object:
        if self.check_if_square_matrix(self.data) == False and self.rows < 2:
            raise Exception('Matrix is non-invertible as it is a non-square matrix. Please provide a square matrix of dimensions greater than or equal to (2, 2).')

        det = self.determinant()

        if det == 0:
            raise Exception('Matrix is non-invertible as the determinant is 0.')

        # Calculate the Inverse of the Determinant
        inv_det = 1 / det

        # Calculate Determinants of Principal Minors
        adjugate_matrix = []

        for i in range(self.rows):
            adjugate_matrix.append([])
            for j in range(self.cols):
                # Retrieve data non-destructively for generating Principal Minors
                principal_minor = []
                for row in range(self.rows):
                    principal_minor.append(self.data[row].copy())

                # Generate Principal Minors
                for row in range(len(principal_minor)):
                    principal_minor[row].pop(j)
                principal_minor.pop(i)

                # Populate Adjugate Matrix
                det = Matrix(principal_minor).determinant()
                adjugate_matrix[i].append(det)

        # Calculate the Product of Cofactors, Inverse of Determinant, and Adjugate Matrix
        for row in range(self.rows):
            for col in range(self.cols):
                adjugate_matrix[row][col] *= (-1)**(i + j) * inv_det

        return Matrix(adjugate_matrix).transpose()


    def __add__(self, other) -> object:
        if other.shape != self.shape:
            raise Exception('Matrix dimensions are mismatched ({} != {}). Please add (2) matrices of the same dimensions.'.format(self.shape, other.shape))

        data, output = self.data, []

        for row in range(self.rows):
            output.append([])
            for col in range(self.cols):
                output[row].append(self.data[row][col] + other.data[row][col])

        self.data = data

        return Matrix(output)


    def __ladd__(self, other) -> object:
        return self.__add__(other)


    def __radd__(self, other) -> object:
        return self.__add__(other)


    def __sub__(self, other) -> object:
        if other.shape != self.shape:
            raise Exception('Matrix dimensions are mismatched ({} != {}). Please subtract (2) matrices of the same dimensions.'.format(self.shape, other.shape))

        data, output = self.data, []

        for row in range(self.rows):
            output.append([])
            for col in range(self.cols):
                output[row].append(self.data[row][col] - other.data[row][col])

        self.data = data

        return Matrix(output)


    def __lsub__(self, other) -> object:
        return self.__sub__(other)


    def __rsub__(self, other) -> object:
        return self.__sub__(other)


    def __mul__(self, other) -> object:
        if isinstance(other, Matrix) == False:
            if isinstance(other, (int, float)) == False:
                raise Exception('Expecting a matrix or a scalar of type int or float only.')
        else:
            if self.size != other.size:
                raise Exception('Matrix dimensions are mismatched for pointwise matrix multiplication ({} != {})'.format(self.shape, other.shape))

        data, output = self.data, []
        
        # Scalar multiplication
        if isinstance(other, (int, float)):
            for row in range(self.rows):
                output.append([])
                for col in range(self.cols):
                    output[row].append(self.data[row][col] * other)

        # Matrix multiplication (pointwise)
        if isinstance(other, Matrix):
            for row in range(self.rows):
                output.append([])
                for col in range(self.cols):
                    output[row].append(self.data[row][col] * other.data[row][col])

        self.data = data

        return Matrix(output)


    def __lmul__(self, other) -> object:
        return self.__mul__(other)


    def __rmul__(self, other) -> object:
        return self.__mul__(other)


    def __matmul__(self, other) -> object:
        if self.cols != other.rows:
            raise Exception('Matrix dimensions are mismatched for matrix multiplication ({} @ {}: {} != {})'.format(self.shape, other.shape, self.shape[1], other.shape[0]))

        data, output = self.data, []

        n, m, c = self.rows, self.cols, other.cols
        for i in range(n):
            output.append([])
            for j in range(c):
                value = 0
                for k in range(m):
                    value += self.data[i][k] * other.data[k][j]
                output[i].append(value)

        self.data = data

        return Matrix(output)


    def __lmatmul__(self, other) -> object:
        return __matmul__(self, other)


    def __rmatmul__(self, other) -> object:
        return __matmul__(self, other)


    def __repr__(self) -> str:
        matrix = str(self.data).replace('],', '],\n ')
        return "<class: 'Matrix'>\nDimensions: {} row(s) x {} column(s)\n {}\nSize: {} element(s), {} byte(s)".format(self.rows, self.cols, matrix, self.size, sys.getsizeof(self))
