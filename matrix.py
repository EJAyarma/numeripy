"""
This class models a matrix
"""

from collections import namedtuple

# Named tuple to describe dimension of matrix
Dimension = namedtuple('Dimension', ['rows', 'cols'])


class Matrix():
    def __init__(self, values: list):
        self.values = values
        self.dim = Dimension(len(values), len(values[0]))

    @classmethod
    def from_string(cls, s):
        """
        Create a matrix from string
        """
        values = [r.split() for r in s.split('; ')]
        return cls(values)

    @classmethod
    def from_zeros(cls, r, c=None):
        if c == None:
            values = [[0]*r for _ in range(r)]
            return cls(values)
        else:
            values = [[0]*c for _ in range(r)]
            return cls(values)

    @classmethod
    def unit_matrix(cls, n):
        """Create an n by n unit matrix"""
        zeros_matrix = cls.from_zeros(n)
        values = zeros_matrix.values
        for i in range(n):
            row = values[i]
            row[i] = 1
        return zeros_matrix

    @staticmethod
    def utm_from(m):
        """Create an upper triangular matrix from matrix m"""
        rows, cols = m.dim
        if rows == cols:
            for i in range(len(m.values)):
                el = m.values[i]
                for j in range(len(el)):
                    if j < i:
                        m.values[i][j] = 0
        else:
            raise ValueError('Dimension error')
        return m

    @staticmethod
    def unit_utm_from(m):
        """Create a unit upper triangular matrix from matrix m"""
        rows, cols = m.dim
        if rows == cols:
            for i in range(len(m.values)):
                el = m.values[i]
                for j in range(len(el)):
                    if j < i:
                        m.values[i][j] = 0
                    elif j == i:
                        m.values[i][j] = 1
        else:
            raise ValueError('Dimension error')
        return m

    @staticmethod
    def ltm_from(m):
        """Create a lower triangular matrix from matrix m"""
        rows, cols = m.dim
        if rows == cols:
            for i in range(len(m.values)):
                el = m.values[i]
                for j in range(len(el)):
                    if j > i:
                        m.values[i][j] = 0
        else:
            raise ValueError('Dimension error')
        return m

    @staticmethod
    def unit_ltm_from(m):
        """Create a unit lower triangular matrix from matrix m"""
        rows, cols = m.dim
        if rows == cols:
            for i in range(len(m.values)):
                el = m.values[i]
                for j in range(len(el)):
                    if j > i:
                        m.values[i][j] = 0
                    elif j == i:
                        m.values[i][j] = 1
        else:
            raise ValueError('Dimension error')
        return m

    def trns(self):
        """return the transpose of a matrix"""
        cols, rows = self.dim
        t_m = self.from_zeros(rows, cols)
        values = (self.values[j][i] for i, v in enumerate(t_m.values)
                  for j, _ in enumerate(v))
        for k in range(rows):
            for l in range(cols):
                t_m.values[k][l] = next(values)
        return t_m

    def det(self):
        pass

    def inv(self):
        """Return the inverse of a matrix"""
        pass

    def __str__(self) -> str:
        return '\n'.join(str(v) for v in self.values)

    def __repr__(self) -> str:
        rows, cols = self.dim
        return 'Matrix({} X {})'.format(rows, cols)

    def __add__(self, other):
        dim1 = self.dim
        dim2 = self.dim
        if dim1 == dim2:
            values1 = self.values
            values2 = other.values
            for i, v in enumerate(values1):
                for j, _ in enumerate(v):
                    values1[i][j] += values2[i][j]
        else:
            raise ValueError('Dimension error')
        return self

    def __sub__(self, other):
        dim1 = self.dim
        dim2 = self.dim
        if dim1 == dim2:
            values1 = self.values
            values2 = other.values
            for i, v in enumerate(values1):
                for j, _ in enumerate(v):
                    values1[i][j] -= values2[i][j]
        else:
            raise ValueError('Dimension error')
        return self

    def __mult__(self, other):
        pass

    def __neg__(self):
        v = self.values
        for i, v in enumerate(v):
            for j, _ in enumerate(v):
                v[i][j] -v[i][j]

    def __eq__(self, other):
        pass

    def dim(self) -> list:
        pass

    def is_utm(self):
        pass

    def is_unit_utm(self):
        pass

    def is_ltm(self):
        pass

    def is_unit_ltm(self):
        pass

    def is_symmetric(self):
        pass
