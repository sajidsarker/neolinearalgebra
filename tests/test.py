import unittest
import math

from neolinearalgebra import Matrix

'''
A (check: list)
A (check: list of lists)
A (check: inconsistent dimensions)
A (check: empty)
A (check: data type)
A (check: square matrix)
A + C (check error) (2*2)
2 * A
A * 2
A * A
A * B
A + B * 3 - 2 * A + B * A + 1
A @ A
A @ B
A @ C
A @ V
A @ I
I @ A
2 * (I @ A + B)
A + B * 3 - 2 * A + B @ A + 1
A.assign() (check error)
A.fill() (check error)
A.retrieve() (check error)
(A*B).transpose()
(A@B).transpose()
A.trace() (4*4)
A.trace() (3*1)
A.diagonal().trace()
(A*B).transpose().trace()
(A@B).transpose().trace()
A.determinant()
B.determinant()
C.determinant()
D.determinant([[1]])
A.inverse()
B.inverse() (check non invertible)
C.inverse() (check non square)
D.inverse() (check unimodal)
A.inverse().transpose().trace()
Commutative Law of Addition
A+B=B+A
Associative Law of Addition
A+(B+C)=(A+B)+C
Associative Law of Multiplication
A@(B@C)=(A@B)@C
Distributive Law of Matrix Algebra
A@(B+C)=A@B+A@C
k*(A+B)=k*A+k*B
Transposition
A.transpose().transpose()=A
(A+B).transpose()=A.transpose()+B.transpose()
(A@B).transpose()=B.transpose()@A.transpose()
A@B@C=C.transpose()@B.transpose()@A.transpose()
A@I=I@A
A@I=A
I@A=A
Inversion
A@A.inverse()=I
A.inverse()@A=I
A.inverse().inverse()=A
(A@B).inverse()=B.inverse()@A.inverse()
(A@B@C).inverse=C.inverse()@B.inverse()@A.inverse()
A.transpose().inverse()=A.inverse().transpose()
'''

class TestMatrix(unittest.TestCase):
	def test_validation_1(self):
		out = [[1, 0], [0, 1]]
		self.assertEqual(Matrix([[1, 0], [0, 1]]).data, out, "Incorrect matrix configuration.")

	def test_vector_1(self):
		out = [[1], [0]]
		self.assertEqual(Matrix([[1], [0]]).data, out, "Incorrect vector configuration.")

	def test_vector_2(self):
		out = [[1, 0]]
		self.assertEqual(Matrix([[1, 0]]).data, out, "Incorrect vector configuration.")

	def test_assign_1(self):
		out = [[1, 2, 3], [0, 1, 0], [0, 0, 1]]
		matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
		matrix.assign(0, 1, 2)
		matrix.assign(0, 2, 3)
		self.assertEqual(matrix.data, out, "Incorrect matrix assignment.")

	def test_fill_1(self):
		out = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
		matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
		matrix.fill((0, 3), (0, 3), 1)
		self.assertEqual(matrix.data, out, "Incorrect matrix fill.")

	def test_retrieve_1(self):
		out = 5
		matrix = Matrix([[1, 0, 0], [0, 5, 0], [0, 0, 1]])
		self.assertEqual(matrix.retrieve(1, 1), out, "Incorrect matrix retrieval.")

	def test_diagonal_1(self):
		out = [[1], [1], [1]]
		matrix = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
		self.assertEqual(matrix.diagonal().data, out, "Incorrect matrix diagonalisation.")

	def test_diagonal_2(self):
		out = [[1], [1]]
		matrix = Matrix([[1, 0], [0, 1], [0, 0]])
		self.assertEqual(matrix.diagonal().data, out, "Incorrect matrix diagonalisation.")

	def test_magnitude_1(self):
		out = math.sqrt(1**2 + 2**2 + 3**2)
		matrix = Matrix([[1, 2, 3]])
		self.assertEqual(matrix.magnitude(), out, "Incorrect matrix magnitude.")

	def test_magnitude_2(self):
		out = math.sqrt(1**2 + 2**2 + 3**2)
		matrix = Matrix([[1], [2], [3]])
		self.assertEqual(matrix.magnitude(), out, "Incorrect matrix magnitude.")

	def test_transpose_1(self):
		out = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
		matrix = Matrix([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
		self.assertEqual(matrix.transpose().data, out, "Incorrect matrix transposition.")

	def test_transpose_2(self):
		out = [[1, 2], [1, 2], [1, 2]]
		matrix = Matrix([[1, 1, 1], [2, 2, 2]])
		self.assertEqual(matrix.transpose().data, out, "Incorrect matrix transposition.")

	def test_add_1(self):
		out = [[5, 5], [5, 5]]
		matrix = Matrix([[0, 0], [0, 0]])
		self.assertEqual((matrix + 5).data, out, "Incorrect matrix addition.")

	def test_add_2(self):
		out = [[5, 5], [5, 5]]
		matrix = Matrix([[0, 0], [0, 0]])
		self.assertEqual((5 + matrix).data, out, "Incorrect matrix addition.")

	def test_add_3(self):
		out = [[5, 5], [5, 5]]
		matrix_1 = Matrix([[2, 2], [2, 2]])
		matrix_2 = Matrix([[3, 3], [3, 3]])
		self.assertEqual((matrix_1 + matrix_2).data, out, "Incorrect matrix addition.")

	def test_sub_1(self):
		out = [[-5, -5], [-5, -5]]
		matrix = Matrix([[0, 0], [0, 0]])
		self.assertEqual((matrix - 5).data, out, "Incorrect matrix subtraction.")

	def test_sub_2(self):
		out = [[5, 5], [5, 5]]
		matrix = Matrix([[0, 0], [0, 0]])
		self.assertEqual((5 - matrix).data, out, "Incorrect matrix subtraction.")

	def test_sub_3(self):
		out = [[-1, -1], [-1, -1]]
		matrix_1 = Matrix([[2, 2], [2, 2]])
		matrix_2 = Matrix([[3, 3], [3, 3]])
		self.assertEqual((matrix_1 - matrix_2).data, out, "Incorrect matrix addition.")

'''
    def test_determinant_1(self):
        self.assert()
    def test_inverse_1(self):
        self.assert()
    def test_add_1(self):
        self.assert()
    def test_sub_1(self):
        self.assert()
    def test_mul_1(self):
        self.assert()
    def test_mul_2(self):
        self.assert()
    def test_matmul_1(self):
        self.assert()
    def test_matmul_2(self):
        self.assert()
'''

if __name__ == '__main__':
	unittest.main()
