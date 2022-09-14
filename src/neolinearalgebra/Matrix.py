import sys
import math

class Matrix:
    '''Matrix class containing attributes and methods designed for Matrix operations in Linear Algebra.
    Attributes:
        data (list): Values used to construct the matrix. Must be a list of lists of data type int or float only.
        rows (int): Number of rows of the matrix.
        cols (int): Number of columns of the matrix.
        shape (tuple): Tuple containing number of rows and columns of the matrix. Must be a tuple of data type int only.
        size (int): Number of elements in the matrix.
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
        '''Checks provided values used to construct the matrix by conducting a series of integrity checks.
        Args:
            data (list): Values used to construct the matrix. Must be a list of lists of data type int or float only.
        Returns:
            bool: Whether all integrity checks have successfully passed for the provided data to be valid for conversion into a matrix. True if successfully passed all checks, False otherwise.
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
        '''Checks if the provided matrix is a list.
        Args:
            data (list): Values used to construct the matrix. Must be a list of lists of data type int or float only.
        Returns:
            bool: Whether the provided data is a valid list for conversion into a matrix.
        '''
        if isinstance(data, list) == False:
            raise TypeError('Expecting matrix to be formatted as a list.')
            return False
        else:
            return True


    def check_if_list_of_lists(self, data) -> bool:
        '''Checks if the provided matrix is a list of lists.
        Args:
            data (list): Values used to construct the matrix. Must be a list of lists of data type int or float only.
        Returns:
            bool: Whether the provided data is a valid list of lists for conversion into a matrix.
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
        '''Checks if the provided matrix has consistent dimensions.
        Args:
            data (list): Values used to construct the matrix. Must be a list of lists of data type int or float only.
        Returns:
            bool: Whether the provided data has consistent dimensions in terms of rows and columns for conversion into a matrix.
        '''
        ncols = [len(x) for x in data]
        if sum(ncols) / len(ncols) != ncols[0]:
            raise IndexError('Expecting matrix to be provided with consistent dimensions.')
            return False
        else:
            return True
        
    def check_if_empty(self, data) -> bool:
        '''Checks if the provided matrix has empty columns.
        Args:
            data (list): Values used to construct the matrix. Must be a list of lists of data type int or float only.
        Returns:
            bool: Whether the provided data is an empty list or list of lists.
        '''
        ncols = [len(x) for x in data]
        if ncols[0] == 0:
            raise IndexError('Expecting matrix to be non-empty.')
            return True
        else:
            return False
    
    def check_if_numeric_dtype(self, data) -> bool:
        '''Checks if the provided matrix contains values of type int or float only.
        Args:
            data (list): Values used to construct the matrix. Must be a list of lists of data type int or float only.
        Returns:
            bool: Whether the provided data is int or float only for conversion into a matrix.
        '''
        for i in range(len(data)):
            checks = [isinstance(x, (int, float)) == False for x in data[i]]
            if sum(checks) > 0:
                raise ValueError('Expecting matrix to contain values of type int or float only.')
                return False
        return True
    
    
    def check_if_square_matrix(self, data) -> bool:
        '''Checks if the provided matrix is a square matrix.
        Args:
            data (list): Values used to construct the matrix. Must be a list of lists of data type int or float only.
        Returns:
            bool: Whether the provided data has consistent square dimensions with rows and columns being equal for conversion into a matrix.
        '''
        return len(data) == len(data[0])
    
    
    def check_if_vector(self, data) -> bool:
        '''Checks if the provided matrix is a row or column vector.
        Args:
            data (list): Values used to construct the matrix. Must be a list of lists of data type int or float only.
        Returns:
            bool: Whether the provided data has dimensions in terms of a row vector or a column vector for conversion into a matrix.
        '''
        return len(data) == 1 or len(data[0]) == 1


    def assign(self, row, col, value) -> None:
        '''Assigns a value to the specified row and column in the matrix.
        
        Args:
            row (int): Row index
            col (int): Column index
            value (int, float): Value to be assigned
        
        Returns:
            None
        '''
        if isinstance(value, (int, float)) == False:
            raise Exception('Value must be of type int or float only.')

        self.data[row][col] = value


    def fill(self, rows, cols, value) -> None:
        '''Fills specified row range and column range with a value in the matrix.
        
        Args:
            rows (tuple): Tuple of row range (start, end) as dtype int
            cols (tuple): Tuple of column range (start, end) as dtype int
            value (int, float): Value to be assigned
        
        Returns:
            None
        '''
        if isinstance(value, (int, float)) == False:
            raise Exception('Value must be of type int or float only.')

        for row in range(rows[0], rows[1]):
            for col in range(cols[0], cols[1]):
                self.data[row][col] = value


    def retrieve(self, row, col) -> float:
        '''Retrieves the value of the specified row and column in the matrix.
        
        Args:
            row (int): Row index
            col (int): Column index
        
        Returns:
            float: Value specified with row and column in the matrix.
        '''
        return self.data[row][col]


    def diagonal(self) -> object:
        '''Gets the diagonal of the matrix.
        
        Args:
            None
        
        Returns:
            object: Matrix object containing the diagonal of the Matrix.
        '''
        output = []

        for i in range(self.rows):
            if i < self.cols:
                output.append([self.data[i][i]])

        return Matrix(output)


    def trace(self) -> float:
        '''Gets the trace of the matrix.
        
        Args:
            None
        
        Returns:
            float: Trace of the Matrix.
        '''
        data = self.diagonal().data.copy()
        output = sum([sum(x) for x in data])

        return output


    def magnitude(self) -> float:
        '''Gets the magnitude of the row vector or column vector.
        
        Args:
            None
        
        Returns:
            float: Magnitude of the row vector or column vector.
        '''
        if self.check_if_vector(self.data) == False:
            raise Exception('Matrix must be a row or column vector only.')

        data, output = self.data.copy(), []

        for row in range(self.rows):
            for col in range(self.cols):
                output.append(self.data[row][col]**2)
        
        self.data = data

        return math.sqrt(sum(output))


    def transpose(self) -> object:
        '''Gets the transpose of the matrix.
        
        Args:
            None
        
        Returns:
            object: Matrix object containing the transpose of the matrix.
        '''
        output, row = [], []

        for j in range(self.cols):
            for i in range(self.rows):
                row.append(self.data[i][j])
            output.append(row)
            row = []

        return Matrix(output)


    def determinant(self) -> float:
        '''Gets the determinant of the matrix.
        
        Args:
            None
        
        Returns:
            float: Determinant of the matrix.
        '''
        if self.check_if_square_matrix(self.data) == False:
            raise ValueError('Matrix determinant cannot be derived as it is a non-square matrix. Please provide a square matrix.')

        matrix, det = self.data.copy(), 0
        indices = list(range(len(matrix)))

        if len(matrix) == 2 and len(matrix[0]) == 2:
            return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

        for focus_column in indices:
            principal_minor = matrix[1:].copy()
            
            for row in range(len(principal_minor)):
                principal_minor[row] = principal_minor[row][0:focus_column] + principal_minor[row][focus_column+1:]

            sub_det = Matrix(principal_minor).determinant()
            det += (-1)**(focus_column % 2) * matrix[0][focus_column] * sub_det

        return det


    def inverse(self) -> object:
        '''Gets the inverse of the matrix.
        
        Args:
            None
        
        Returns:
            object: Matrix object containing the inverse of the matrix.
        '''
        if self.check_if_square_matrix(self.data) == False and self.rows < 2:
            raise ValueError('Matrix is non-invertible as it is a non-square matrix. Please provide a square matrix of dimensions greater than or equal to (2, 2).')

        det = self.determinant()

        if det == 0:
            raise Exception('Matrix is non-invertible as the determinant is 0.')

        # Calculate the Inverse of the Determinant
        inv_det = 1 / det

        # Calculate Determinants of Principal Minors
        adjugate_matrix = []
        
        if self.shape == (2, 2):
            adjugate_matrix.append([self.data[1][1] * inv_det, -self.data[0][1] * inv_det])
            adjugate_matrix.append([-self.data[1][0] * inv_det, self.data[0][0] * inv_det])
            return Matrix(adjugate_matrix)

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
        '''Gets the sum of the matrices.
        
        Args:
            other (float): Scalar for pointwise addition
            other (object): Matrix object for matrix addition
        
        Returns:
            object: Matrix object containing the sum of the matrices.
        '''
        if isinstance(other, Matrix) == False:
            if isinstance(other, (int, float)) == False:
                raise TypeError('Expecting a matrix or a scalar of type int or float only.')
        else:
            if self.shape != other.shape:
                raise ValueError('Matrix dimensions are mismatched for pointwise matrix addition ({} != {})'.format(self.shape, other.shape))

        data, output = self.data.copy(), []

        # Scalar addition
        if isinstance(other, (int, float)):
            for row in range(self.rows):
                output.append([])
                for col in range(self.cols):
                    output[row].append(self.data[row][col] + other)

        # Matrix addition (pointwise)
        if isinstance(other, Matrix):
            for row in range(self.rows):
                output.append([])
                for col in range(self.cols):
                    output[row].append(self.data[row][col] + other.data[row][col])

        self.data = data

        return Matrix(output)


    def __ladd__(self, other) -> object:
        '''Gets the sum of the matrices.
        
        Args:
            other (float): Scalar for pointwise addition
            other (object): Matrix object for matrix addition
        
        Returns:
            object: Matrix object containing the sum of the matrices.
        '''
        return self.__add__(other)


    def __radd__(self, other) -> object:
        '''Gets the sum of the matrices.
        
        Args:
            other (float): Scalar for pointwise addition
            other (object): Matrix object for matrix addition
        
        Returns:
            object: Matrix object containing the sum of the matrices.
        '''
        return self.__add__(other)


    def __sub__(self, other) -> object:
        '''Gets the subtraction of the matrices.
        
        Args:
            other (float): Scalar for pointwise subtraction
            other (object): Matrix object for matrix subtraction
        
        Returns:
            object: Matrix object containing the subtraction of the matrices.
        '''
        if isinstance(other, Matrix) == False:
            if isinstance(other, (int, float)) == False:
                raise TypeError('Expecting a matrix or a scalar of type int or float only.')
        else:
            if self.shape != other.shape:
                raise ValueError('Matrix dimensions are mismatched for pointwise matrix subtraction ({} != {})'.format(self.shape, other.shape))

        data, output = self.data.copy(), []

        # Scalar subtraction
        if isinstance(other, (int, float)):
            for row in range(self.rows):
                output.append([])
                for col in range(self.cols):
                    output[row].append(self.data[row][col] - other)

        # Matrix subtraction (pointwise)
        if isinstance(other, Matrix):
            for row in range(self.rows):
                output.append([])
                for col in range(self.cols):
                    output[row].append(self.data[row][col] - other.data[row][col])

        self.data = data

        return Matrix(output)


    def __rsub__(self, other) -> object:
        '''Gets the subtraction of the matrices.
        
        Args:
            other (float): Scalar for pointwise subtraction
            other (object): Matrix object for matrix subtraction
        
        Returns:
            object: Matrix object containing the subtraction of the matrices.
        '''
        if isinstance(other, Matrix) == False:
            if isinstance(other, (int, float)) == False:
                raise TypeError('Expecting a matrix or a scalar of type int or float only.')
        else:
            if self.shape != other.shape:
                raise ValueError('Matrix dimensions are mismatched for pointwise matrix subtraction ({} != {})'.format(self.shape, other.shape))

        data, output = self.data.copy(), []

        # Scalar subtraction
        if isinstance(other, (int, float)):
            for row in range(self.rows):
                output.append([])
                for col in range(self.cols):
                    output[row].append(other - self.data[row][col])

        # Matrix subtraction (pointwise)
        if isinstance(other, Matrix):
            for row in range(self.rows):
                output.append([])
                for col in range(self.cols):
                    output[row].append(other.data[row][col] - self.data[row][col])

        self.data = data

        return Matrix(output)


    def __mul__(self, other) -> object:
        '''Gets the scalar or pointwise product of the matrices.
        
        Args:
            other (float): Scalar for pointwise multiplication
            other (object): Matrix object for pointwise multiplication
        
        Returns:
            object: Matrix object containing the scalar or pointwise product of the matrices.
        '''
        if isinstance(other, Matrix) == False:
            if isinstance(other, (int, float)) == False:
                raise TypeError('Expecting a matrix or a scalar of type int or float only.')
        else:
            if self.shape != other.shape:
                raise ValueError('Matrix dimensions are mismatched for pointwise matrix multiplication ({} != {})'.format(self.shape, other.shape))

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
        '''Gets the scalar or pointwise product of the matrices.
        
        Args:
            other (float): Scalar for pointwise multiplication
            other (object): Matrix object for pointwise multiplication
        
        Returns:
            object: Matrix object containing the scalar or pointwise product of the matrices.
        '''
        return self.__mul__(other)


    def __rmul__(self, other) -> object:
        '''Gets the scalar or pointwise product of the matrices.
        
        Args:
            other (float): Scalar for pointwise multiplication
            other (object): Matrix object for pointwise multiplication
        
        Returns:
            object: Matrix object containing the scalar or pointwise product of the matrices.
        '''
        return self.__mul__(other)


    def __matmul__(self, other) -> object:
        '''Gets the product of the matrices.
        
        Args:
            other (object): Matrix object for matrix multiplication
        
        Returns:
            object: Matrix object containing the product of the matrices.
        '''
        if self.cols != other.rows:
            raise ValueError('Matrix dimensions are mismatched for matrix multiplication ({} @ {}: {} != {})'.format(self.shape, other.shape, self.shape[1], other.shape[0]))

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
        '''Gets the product of the matrices.
        
        Args:
            other (object): Matrix object for matrix multiplication
        
        Returns:
            object: Matrix object containing the product of the matrices.
        '''
        return __matmul__(self, other)


    def __rmatmul__(self, other) -> object:
        '''Gets the product of the matrices.
        
        Args:
            other (object): Matrix object for matrix multiplication
        
        Returns:
            object: Matrix object containing the product of the matrices.
        '''
        return __matmul__(self, other)


    def __repr__(self) -> str:
        '''Gets the representation of the matrix.
        
        Args:
            None
        
        Returns:
            str: Matrix representation.
        '''
        matrix = str(self.data).replace('],', '],\n ')
        return "<class: 'Matrix'>\nDimensions: {} row(s) x {} column(s)\n {}\nSize: {} element(s), {} byte(s)".format(self.rows, self.cols, matrix, self.size, sys.getsizeof(self.data) + sys.getsizeof(self))