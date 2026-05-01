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

	def test_validation_not_list(self):
		"""Constructor must reject a plain non-list argument."""
		with self.assertRaises(Exception):
			Matrix("not a list")
 
	def test_validation_not_list_of_lists(self):
		"""Constructor must reject a flat (1-D) list."""
		with self.assertRaises(Exception):
			Matrix([1, 2, 3])
 
	def test_validation_inconsistent_dimensions(self):
		"""Rows of differing lengths must be rejected."""
		with self.assertRaises(Exception):
			Matrix([[1, 2], [3]])
 
	def test_validation_empty(self):
		"""An empty list must be rejected."""
		with self.assertRaises(Exception):
			Matrix([])
 
	def test_validation_wrong_dtype(self):
		"""Non-numeric elements must be rejected."""
		with self.assertRaises(Exception):
			Matrix([["a", "b"], ["c", "d"]])
 
	def test_validation_square(self):
		"""A square matrix should be accepted without error."""
		m = Matrix([[1, 2], [3, 4]])
		self.assertEqual(len(m.data), 2)
		self.assertEqual(len(m.data[0]), 2)
 
	def test_add_dimension_mismatch(self):
		"""Adding matrices with incompatible dimensions must raise an error."""
		A = Matrix([[1, 2], [3, 4]])
		C = Matrix([[1, 2, 3], [4, 5, 6]])
		with self.assertRaises(Exception):
			_ = A + C

	def test_assign_out_of_bounds(self):
		"""assign() with an out-of-range index must raise an error."""
		m = Matrix([[1, 0], [0, 1]])
		with self.assertRaises(Exception):
			m.assign(5, 5, 99)
 
	def test_fill_out_of_bounds(self):
		"""fill() with an out-of-range range must raise an error."""
		m = Matrix([[1, 0], [0, 1]])
		with self.assertRaises(Exception):
			m.fill((0, 10), (0, 10), 1)
 
	def test_retrieve_out_of_bounds(self):
		"""retrieve() with an out-of-range index must raise an error."""
		m = Matrix([[1, 0], [0, 1]])
		with self.assertRaises(Exception):
			m.retrieve(5, 5)

	def test_scalar_mul_left(self):
		"""2 * A should double every element."""
		A = Matrix(A_DATA)
		result = 2 * A
		expected = [[2 * v for v in row] for row in A_DATA]
		self.assertEqual(result.data, expected, "Incorrect left scalar multiplication.")
 
	def test_scalar_mul_right(self):
		"""A * 2 should double every element."""
		A = Matrix(A_DATA)
		result = A * 2
		expected = [[2 * v for v in row] for row in A_DATA]
		self.assertEqual(result.data, expected, "Incorrect right scalar multiplication.")

	def test_elementwise_mul_same(self):
		"""A * A should square every element."""
		A = Matrix(A_DATA)
		result = A * A
		expected = [[A_DATA[i][j] ** 2 for j in range(len(A_DATA[0]))]
					for i in range(len(A_DATA))]
		self.assertEqual(result.data, expected,
						 "Incorrect element-wise self-multiplication.")
 
	def test_elementwise_mul_diff(self):
		"""A * B should multiply element-by-element."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		result = A * B
		expected = [[A_DATA[i][j] * B_DATA[i][j] for j in range(len(A_DATA[0]))]
					for i in range(len(A_DATA))]
		self.assertEqual(result.data, expected,
						 "Incorrect element-wise multiplication.")

	def test_mixed_expression_elementwise(self):
		"""A + B*3 - 2*A + B*A + 1 (element-wise * throughout)."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		result = A + B * 3 - 2 * A + B * A + 1
		n, m = len(A_DATA), len(A_DATA[0])
		expected = [
			[A_DATA[i][j] + B_DATA[i][j] * 3 - 2 * A_DATA[i][j]
			 + B_DATA[i][j] * A_DATA[i][j] + 1
			 for j in range(m)]
			for i in range(n)
		]
		self.assertEqual(result.data, expected, "Incorrect mixed expression (element-wise).")

	def test_matmul_square(self):
		"""A @ A – square matrix self-product."""
		A = Matrix(A_DATA)
		result = A @ A
		n = len(A_DATA)
		expected = [
			[sum(A_DATA[i][k] * A_DATA[k][j] for k in range(n)) for j in range(n)]
			for i in range(n)
		]
		self.assertEqual(result.data, expected, "Incorrect matrix self-multiplication.")
 
	def test_matmul_ab(self):
		"""A @ B – two different square matrices."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		result = A @ B
		n = len(A_DATA)
		expected = [
			[sum(A_DATA[i][k] * B_DATA[k][j] for k in range(n)) for j in range(n)]
			for i in range(n)
		]
		self.assertEqual(result.data, expected, "Incorrect matrix multiplication A@B.")
 
	def test_matmul_nonsquare(self):
		"""A(3×3) @ C(3×2) – valid non-square product."""
		A = Matrix(A_DATA)
		C = Matrix(C_DATA)
		result = A @ C
		expected = [
			[sum(A_DATA[i][k] * C_DATA[k][j]
				 for k in range(len(A_DATA[0])))
			 for j in range(len(C_DATA[0]))]
			for i in range(len(A_DATA))
		]
		self.assertEqual(result.data, expected,
						 "Incorrect non-square matrix multiplication.")
 
	def test_matmul_vector(self):
		"""A @ V – matrix times a column vector."""
		A = Matrix(A_DATA)
		V = Matrix(V_DATA)
		result = A @ V
		expected = [
			[sum(A_DATA[i][k] * V_DATA[k][0] for k in range(len(A_DATA[0])))]
			for i in range(len(A_DATA))
		]
		self.assertEqual(result.data, expected,
						 "Incorrect matrix-vector multiplication.")
 
	def test_matmul_identity_right(self):
		"""A @ I = A."""
		A = Matrix(A_DATA)
		I = identity(3)
		result = A @ I
		self.assertEqual(result.data, A_DATA, "A @ I should equal A.")
 
	def test_matmul_identity_left(self):
		"""I @ A = A."""
		A = Matrix(A_DATA)
		I = identity(3)
		result = I @ A
		self.assertEqual(result.data, A_DATA, "I @ A should equal A.")
 
	def test_matmul_scalar_expression(self):
		"""2 * (I @ A + B) – scalar applied to a matmul expression."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		I = identity(3)
		result = 2 * (I @ A + B)
		n, m = len(A_DATA), len(A_DATA[0])
		expected = [[2 * (A_DATA[i][j] + B_DATA[i][j]) for j in range(m)]
					for i in range(n)]
		self.assertEqual(result.data, expected,
						 "Incorrect result for 2*(I@A+B).")
 
	def test_mixed_expression_matmul(self):
		"""A + B*3 - 2*A + B@A + 1 (matmul for B@A)."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		n, m = len(A_DATA), len(A_DATA[0])
		BA = [[sum(B_DATA[i][k] * A_DATA[k][j] for k in range(m))
			   for j in range(m)]
			  for i in range(n)]
		result = A + B * 3 - 2 * A + B @ A + 1
		expected = [
			[A_DATA[i][j] + 3 * B_DATA[i][j] - 2 * A_DATA[i][j] + BA[i][j] + 1
			 for j in range(m)]
			for i in range(n)
		]
		self.assertEqual(result.data, expected,
						 "Incorrect mixed expression with matmul.")

	def test_transpose_elementwise_product(self):
		"""(A*B).transpose() – transpose of element-wise product."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		result = (A * B).transpose()
		ew = [[A_DATA[i][j] * B_DATA[i][j] for j in range(len(A_DATA[0]))]
			  for i in range(len(A_DATA))]
		expected = [[ew[j][i] for j in range(len(ew))]
					for i in range(len(ew[0]))]
		self.assertEqual(result.data, expected,
						 "Incorrect transpose of element-wise product.")
 
	def test_transpose_matmul_product(self):
		"""(A@B).transpose() – transpose of matrix product."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		result = (A @ B).transpose()
		n = len(A_DATA)
		ab = [[sum(A_DATA[i][k] * B_DATA[k][j] for k in range(n))
			   for j in range(n)]
			  for i in range(n)]
		expected = [[ab[j][i] for j in range(n)] for i in range(n)]
		self.assertEqual(result.data, expected,
						 "Incorrect transpose of matrix product.")
 
 	def test_trace_4x4(self):
		"""trace() on a 4×4 matrix."""
		data = [[1, 2, 3, 4],
				[5, 6, 7, 8],
				[9, 10, 11, 12],
				[13, 14, 15, 16]]
		m = Matrix(data)
		self.assertEqual(m.trace(), 1 + 6 + 11 + 16,
						 "Incorrect trace for 4×4 matrix.")
 
	def test_trace_non_square_error(self):
		"""trace() on a non-square matrix must raise an error."""
		m = Matrix([[1, 2, 3]])   # 1×3
		with self.assertRaises(Exception):
			m.trace()
 
	def test_trace_via_diagonal(self):
		"""A.diagonal().trace() – trace computed through the diagonal vector."""
		A = Matrix(A_DATA)
		diag_sum = sum(A_DATA[i][i] for i in range(len(A_DATA)))
		self.assertEqual(A.diagonal().trace(), diag_sum,
						 "diagonal().trace() does not match expected sum.")
 
	def test_trace_elementwise_product_transpose(self):
		"""(A*B).transpose().trace()."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		result_trace = (A * B).transpose().trace()
		# Trace is invariant under transpose, equals sum of diagonal of A*B
		expected = sum(A_DATA[i][i] * B_DATA[i][i] for i in range(len(A_DATA)))
		self.assertEqual(result_trace, expected,
						 "Incorrect (A*B).T trace.")
 
	def test_trace_matmul_product_transpose(self):
		"""(A@B).transpose().trace()."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		result_trace = (A @ B).transpose().trace()
		n = len(A_DATA)
		ab_diag_sum = sum(
			sum(A_DATA[i][k] * B_DATA[k][i] for k in range(n))
			for i in range(n)
		)
		self.assertEqual(result_trace, ab_diag_sum,
						 "Incorrect (A@B).T trace.")

	def test_determinant_a(self):
		"""det(A) for invertible 3×3."""
		A = Matrix(A_DATA)
		# det([[2,1,3],[0,4,1],[5,2,6]]) = 2*(24-2) - 1*(0-5) + 3*(0-20) = 44+5-60 = -11
		self.assertAlmostEqual(A.determinant(), -11, places=9,
							   msg="Incorrect determinant for A.")
 
	def test_determinant_b(self):
		"""det(B) for invertible 3×3."""
		B = Matrix(B_DATA)
		# det([[1,2,0],[3,1,4],[2,0,1]]) = 1*(1-0) - 2*(3-8) + 0 = 1+10 = 11
		self.assertAlmostEqual(B.determinant(), 11, places=9,
							   msg="Incorrect determinant for B.")
 
	def test_determinant_singular(self):
		"""det of a singular (non-invertible) matrix must be 0."""
		S = Matrix(SNG_DATA)
		self.assertAlmostEqual(S.determinant(), 0, places=9,
							   msg="Determinant of singular matrix should be 0.")
 
	def test_determinant_1x1(self):
		"""det([[k]]) = k."""
		D = Matrix(D_DATA)
		self.assertAlmostEqual(D.determinant(), 1, places=9,
							   msg="Incorrect 1×1 determinant.")
 
	def test_determinant_non_square_error(self):
		"""determinant() on a non-square matrix must raise an error."""
		C = Matrix(C_DATA)
		with self.assertRaises(Exception):
			C.determinant()

	def test_inverse_a(self):
		"""A @ A.inverse() should equal I."""
		A = Matrix(A_DATA)
		I = identity(3)
		result = A @ A.inverse()
		self.assertTrue(approx_equal(result, I),
						"A @ A.inverse() should equal the identity.")
 
	def test_inverse_singular_error(self):
		"""inverse() on a singular matrix must raise an error."""
		S = Matrix(SNG_DATA)
		with self.assertRaises(Exception):
			S.inverse()
 
	def test_inverse_non_square_error(self):
		"""inverse() on a non-square matrix must raise an error."""
		C = Matrix(C_DATA)
		with self.assertRaises(Exception):
			C.inverse()
 
	def test_inverse_1x1(self):
		"""inverse of [[k]] = [[1/k]]."""
		D = Matrix([[4]])
		result = D.inverse()
		self.assertAlmostEqual(result.data[0][0], 0.25, places=9,
							   msg="Incorrect 1×1 inverse.")
 
	def test_inverse_transpose_trace(self):
		"""A.inverse().transpose().trace() – combined operation."""
		A = Matrix(A_DATA)
		result = A.inverse().transpose().trace()
		# Must simply not raise and return a finite number
		self.assertTrue(math.isfinite(result),
						"inverse().transpose().trace() should be a finite number.")

	def test_law_commutative_addition(self):
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		self.assertEqual((A + B).data, (B + A).data,
						 "Commutative law A+B=B+A failed.")

	def test_law_associative_addition(self):
		A = Matrix([[1, 2], [3, 4]])
		B = Matrix([[5, 6], [7, 8]])
		C = Matrix([[9, 10], [11, 12]])
		lhs = A + (B + C)
		rhs = (A + B) + C
		self.assertEqual(lhs.data, rhs.data,
						 "Associative law A+(B+C)=(A+B)+C failed.")

	def test_law_associative_multiplication(self):
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		C = Matrix([[2, 0, 1], [1, 3, 0], [0, 1, 2]])
		lhs = A @ (B @ C)
		rhs = (A @ B) @ C
		self.assertTrue(approx_equal(lhs, rhs),
						"Associative law A@(B@C)=(A@B)@C failed.")

	def test_law_distributive_matmul(self):
		"""A @ (B + C) = A@B + A@C."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		C = Matrix([[2, 0, 1], [1, 3, 0], [0, 1, 2]])
		lhs = A @ (B + C)
		rhs = A @ B + A @ C
		self.assertTrue(approx_equal(lhs, rhs),
						"Distributive law A@(B+C)=A@B+A@C failed.")
 
	def test_law_distributive_scalar(self):
		"""k * (A + B) = k*A + k*B."""
		k = 5
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		lhs = k * (A + B)
		rhs = k * A + k * B
		self.assertEqual(lhs.data, rhs.data,
						 "Distributive law k*(A+B)=k*A+k*B failed.")

	def test_law_transpose_involution(self):
		"""(A^T)^T = A."""
		A = Matrix(A_DATA)
		self.assertEqual(A.transpose().transpose().data, A_DATA,
						 "Double transpose should return original matrix.")
 
	def test_law_transpose_sum(self):
		"""(A + B)^T = A^T + B^T."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		lhs = (A + B).transpose()
		rhs = A.transpose() + B.transpose()
		self.assertEqual(lhs.data, rhs.data,
						 "(A+B).T = A.T+B.T failed.")
 
	def test_law_transpose_product(self):
		"""(A @ B)^T = B^T @ A^T."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		lhs = (A @ B).transpose()
		rhs = B.transpose() @ A.transpose()
		self.assertTrue(approx_equal(lhs, rhs),
						"(A@B).T = B.T@A.T failed.")
 
	def test_law_transpose_triple_product(self):
		"""A @ B @ C = (C^T @ B^T @ A^T)^T."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		C = Matrix([[2, 0, 1], [1, 3, 0], [0, 1, 2]])
		lhs = A @ B @ C
		rhs = (C.transpose() @ B.transpose() @ A.transpose()).transpose()
		self.assertTrue(approx_equal(lhs, rhs),
						"A@B@C = (C.T@B.T@A.T).T failed.")
 
	def test_law_identity_right(self):
		"""A @ I = A."""
		A = Matrix(A_DATA)
		I = identity(3)
		self.assertEqual((A @ I).data, A_DATA, "A@I should equal A.")
 
	def test_law_identity_left(self):
		"""I @ A = A."""
		A = Matrix(A_DATA)
		I = identity(3)
		self.assertEqual((I @ A).data, A_DATA, "I@A should equal A.")
 
	def test_law_identity_commute(self):
		"""A @ I = I @ A."""
		A = Matrix(A_DATA)
		I = identity(3)
		self.assertEqual((A @ I).data, (I @ A).data, "A@I should equal I@A.")

	def test_law_inverse_right(self):
		"""A @ A^{-1} = I."""
		A = Matrix(A_DATA)
		I = identity(3)
		self.assertTrue(approx_equal(A @ A.inverse(), I),
						"A @ A.inverse() should equal I.")
 
	def test_law_inverse_left(self):
		"""A^{-1} @ A = I."""
		A = Matrix(A_DATA)
		I = identity(3)
		self.assertTrue(approx_equal(A.inverse() @ A, I),
						"A.inverse() @ A should equal I.")
 
	def test_law_inverse_involution(self):
		"""(A^{-1})^{-1} = A."""
		A = Matrix(A_DATA)
		result = A.inverse().inverse()
		self.assertTrue(approx_equal(result, A),
						"(A.inverse()).inverse() should equal A.")
 
	def test_law_inverse_product_ab(self):
		"""(A @ B)^{-1} = B^{-1} @ A^{-1}."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		lhs = (A @ B).inverse()
		rhs = B.inverse() @ A.inverse()
		self.assertTrue(approx_equal(lhs, rhs),
						"(A@B).inverse() = B.inverse()@A.inverse() failed.")
 
	def test_law_inverse_product_abc(self):
		"""(A @ B @ C)^{-1} = C^{-1} @ B^{-1} @ A^{-1}."""
		A = Matrix(A_DATA)
		B = Matrix(B_DATA)
		C = Matrix([[2, 1, 0], [1, 3, 1], [0, 1, 2]])
		lhs = (A @ B @ C).inverse()
		rhs = C.inverse() @ B.inverse() @ A.inverse()
		self.assertTrue(approx_equal(lhs, rhs),
						"(A@B@C).inverse() = C.inv@B.inv@A.inv failed.")
 
	def test_law_transpose_inverse_commute(self):
		"""(A^T)^{-1} = (A^{-1})^T."""
		A = Matrix(A_DATA)
		lhs = A.transpose().inverse()
		rhs = A.inverse().transpose()
		self.assertTrue(approx_equal(lhs, rhs),
						"A.transpose().inverse() = A.inverse().transpose() failed.")

if __name__ == '__main__':
	unittest.main()
