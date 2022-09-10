import math

class Matrix:
    
    def __init__(self, data):
        if self.check_integrity(data) == False:
            raise Exception('Matrix is incorrectly configured with empty matrix or row, column, or data type mismatch. Please provide a list of lists containing only ints or floats of consistent dimensions.')

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
        
        # Check if provided matrix has empty columns
        if ncols[0] == 0:
            return False
        
        # Check if provided matrix contains values of type int or float only
        for i in range(len(data)):
            checks = [isinstance(x, (int, float)) == False for x in data[i]]
            if sum(checks) > 0:
                return False

        return True


    def assign(self, row, col, value) -> None:
        if isinstance(value, (int, float)) == False:
            raise Exception('Value must be of type int or float only.')

        self.data[row][col] = value


    def fill(self, rows, cols, value) -> None:
        if isinstance(value, (int, float)) == False:
            raise Exception('Value must be of type int or float only.')

        for i in range(rows[0], rows[1], 1):
            for j in range(cols[0], cols[1], 1):
                self.data[i][j] = value


    def retrieve(self, row, col) -> (int, float):
        return self.data[row][col]


    def diagonal(self) -> object:
        output = []

        for i in range(self.rows):
            if i < self.cols:
                output.append([self.data[i][i]])

        return Matrix(output)


    def magnitude(self) -> float:
        if not (self.shape[0] == 1 or self.shape[1] == 1):
            raise Exception('Matrix must be a row or column vector only.')

        output = []

        for i in range(self.rows):
            for j in range(self.cols):
                output.append(self.data[i][j]**2)

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
        if self.shape[0] != self.shape[1]:
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
        if self.shape[0] != self.shape[1] and self.shape[0] < 2:
            raise Exception('Matrix is not invertible as it is a non-square matrix. Please provide a square matrix.')

        det = self.determinant()

        if det == 0:
            raise Exception('Matrix is not invertible as the determinant is 0.')

        # Calculate the Inverse of the Determinant
        inv_det = 1 / det

        # Calculate Determinants of Principal Minors
        adjugate_matrix = []

        for i in range(self.shape[0]):
            adjugate_matrix.append([])
            for j in range(self.shape[1]):
                principal_minor = self.data.copy()
                print('{}: {}'.format((i, j), principal_minor))
                for row in range(len(principal_minor)):
                    principal_minor[row].pop(j)
                principal_minor.pop(i)
                det_pm = Matrix(principal_minor).determinant()
                print('{}: {}'.format(det_pm, principal_minor))
                adjugate_matrix[i].append(det_pm)

        print(adjugate_matrix)

        # Calculate the Product of Cofactors, Inverse of Determinant, and Adjugate Matrix
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                adjugate_matrix[i][j] *= (-1)**(i + j) * inv_det

        return Matrix(adjugate_matrix)


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


    def __ladd__(self, other) -> object:
        return self.__add__(other)


    def __radd__(self, other) -> object:
        return self.__add__(other)


    def __sub__(self, other) -> object:
        if other.shape != self.shape:
            raise Exception('Matrix dimensions are mismatched ({} != {}). Please subtract (2) matrices of the same dimensions.'.format(self.shape, other.shape))

        data, output = self.data, []

        for i in range(self.rows):
            output.append([])
            for j in range(self.cols):
                output[i].append(self.data[i][j] - other.data[i][j])

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


    def __lmul__(self, other) -> object:
        return self.__mul__(other)


    def __rmul__(self, other) -> object:
        return self.__mul__(other)


    def __matmul__(self, other) -> object:
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


    def __lmatmul__(self, other) -> object:
        return __matmul__(self, other)


    def __rmatmul__(self, other) -> object:
        return __matmul__(self, other)


    def __repr__(self) -> str:
        matrix = str(self.data).replace('],', '],\n ')
        return "<class: 'Matrix'>\nDimensions: {} row(s) x {} column(s)\n {}\nSize: {}".format(self.rows, self.cols, matrix, self.size)
