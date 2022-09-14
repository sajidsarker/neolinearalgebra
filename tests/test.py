import unittest

import sys
sys.path.insert(1, './src/neolinearalgebra/')

import file

# from neolinearalgebra import Matrix

'''
A (check: list)
A (check: list of lists)
A (check: inconsistent dimensions)
A (check: empty)
A (check: data type)
A (check: square matrix)
A + A (3*3)
A + B (3*3)
A + C (check error) (2*2)
A + B + A
A - A
A - B
A - C (check error)
A - B - A
2 * A
A * 2
A * A
A * B
A + B * 3 - 2 * A + B * A
A @ A
A @ B
A @ C
A @ V
A @ I
I @ A
2 * (I @ A + B)
A + B * 3 - 2 * A + B @ A
A.assign()
A.assign() (check error)
A.fill()
A.fill() (check error)
A.retrieve()
A.retrieve() (check error)
A.transpose()
B.transpose()
(A*B).transpose()
(A@B).transpose()
A.diagonal() (3*3)
A.diagonal() (2*3)
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
	self.assertEqual(Matrix([[1, 0], [0, 1]]), Matrix([[1, 0], [0, 1]]), "Incorrect matrix configuration.")
    def test_vector_1(self):
	self.assertEqual(Matrix([[1], [0]]), Matrix([[1], [0]]), "Incorrect vector configuration.")
    def test_vector_2(self):
	self.assertEqual(Matrix([[1, 0]]), Matrix([[1, 0]]), "Incorrect vector configuration.")
    def test_assign_1(self):
        self.assert()
    def test_fill_1(self):
        self.assert()
    def test_retrieve_1(self):
        self.assert()
    def test_diagonal_1(self):
        self.assert()
    def test_magnitude_1(self):
        self.assert()
    def test_transpose_1(self):
        self.assert()
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

if __name__ == '__main__':
	unittest.main()
