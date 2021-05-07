import unittest
from matrix import Matrix


class TestMatrix(unittest.TestCase):

    def setUp(self):
        self.m1 = Matrix.from_string('1 2; 3 4')
        self.m2 = Matrix.from_string('1 2; 3 4')
        self.m3 = Matrix.from_string('5; 6')
        self.m4 = Matrix.from_string('1 2 3; 4 5 6; 7 8 9')
        self.m5 = Matrix.from_string('1 2 3 0; 6 5 45 0; 7 8 9 0; 0 0 0 1')

    def test_matrix_from_string(self):
        self.assertListEqual(self.m1.values, [[1, 2], [3, 4]])

    def test_matrix_add(self):
        m = self.m1 - self.m2
        self.assertListEqual(m.values, [[0, 0], [0, 0]])

    def test_matrix_multiply(self):
        m = self.m1 * self.m3
        self.assertListEqual(m.values, [[17], [39]])

    def test_equalityy(self):
        b = self.m1 == self.m2
        self.assertTrue(b)

    def test_minor_matrix(self):
        minor_matrix = self.m4._minor_matrix(2, 3)
        self.assertListEqual(minor_matrix, [[1, 2], [7, 8]])

    def test_det(self):
        d = self.m5.det()
        self.assertEqual(d, 246)


if __name__ == '__main__':
    unittest.main()