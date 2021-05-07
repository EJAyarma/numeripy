"""
This class models a matrix. It contains methods for common
matrix operations and other methods for generating matrices.
"""

from collections import namedtuple

# Named tuple to describe dimension of matrix
Dimension = namedtuple('Dimension', ['rows', 'cols'])


class Matrix():
    def __init__(self, values: list):
        self.values = values
        self.dim = Dimension(len(values), len(values[0]))

    def __str__(self):
        return '\n'.join(str(v) for v in self.values)

    def __repr__(self):
        rows, cols = self.dim
        return 'Matrix({} X {})'.format(rows, cols)

    def __add__(self, other):
        """Overloading of addition operator on two matrices
        i.e. m1 + m2 where both m1 and m2 are Matrix objects"""
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
        """Overloading of subtraction operator on two matrices
        i.e. m1 - m2 where both m1 and m2 are Matrix objects"""
        return self.__add__(-other)

    def __mul__(self, other):
        """Overloading of multiplication operator on two matrices
        i.e. m1 * m2 where both m1 and m2 are Matrix objects"""
        rows1, cols1  = self.dim
        rows2, cols2 = other.dim
        if cols1 == rows2:
            new_m = self.from_zeros(rows1, cols2)
            s_v = self.values
            o_v = other.values
            for j in range(rows1):
                for k in range(cols2):
                    a = [s_v[j][l] * o_v[l][k] for l in range(cols1)]
                    new_m.values[j][k] = sum(a)
            return new_m
        else:
            raise ValueError('Dimension error')

    def __neg__(self):
        """Overloading of negation operator on two matrices
        i.e. -m where m is a Matrix object"""
        val = self.values
        for i, v in enumerate(val):
            for j, _ in enumerate(v):
                val[i][j] = -val[i][j]
        self.values = val
        return self

    def __eq__(self, other):
        """Overloading of equality conditional operator on two matrices
        i.e. m1 == m2 where both m1 and m2 are Matrix objects"""
        return self.values == other.values

    @classmethod
    def from_string(cls, s):
        """
        Constructor to create a matrix from string
        """
        v = []
        v_str = (r.split() for r in s.split('; '))
        for el in v_str:
            v_num = [int(n) for n in el]
            v.append(v_num)

        return cls(v)

    @classmethod
    def from_zeros(cls, r, c=None):
        """Constructor to create an r by c or r by r
        matrix with all entries 0"""
        if c == None:
            values = [[0]*r for _ in range(r)]
            return cls(values)
        else:
            values = [[0]*c for _ in range(r)]
            return cls(values)

    @classmethod
    def unit_matrix(cls, n):
        """Constructor to create an n by n unit matrix"""
        # Create n by n matrix with all entries 0
        zeros_matrix = cls.from_zeros(n)
        values = zeros_matrix.values
        for i in range(n):
            row = values[i]
            row[i] = 1 # Make all diagonal entries 1
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
                        # make entries below diagonal, 0
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
                        # make entries below diagonal, 0
                        m.values[i][j] = 0
                    elif j == i:
                        # make entries of diagonal, 1
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
                        # make entries above diagonal, 0
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
                        # make entries above diagonal, 0
                        m.values[i][j] = 0
                    elif j == i:
                        # make diagonal entries 1
                        m.values[i][j] = 1
        else:
            raise ValueError('Dimension error')
        return m

    def trns(self):
        """return the transpose of a matrix"""
        cols, rows = self.dim # Swaping of rows and columns
        t_m = self.from_zeros(rows, cols) # new matrix of zeros
        #the new matrix has the dimension of the transpose

        # generate entries of the transpose
        values = (self.values[j][i] for i, v in enumerate(t_m.values)
                  for j, _ in enumerate(v))
        # populate entries into the new matrix
        for k in range(rows):
            for l in range(cols):
                t_m.values[k][l] = next(values)
        return t_m

    def det(self):
        """Wrapper around _determinant() method"""
        if self.is_square_matrix():
            return self._determinant(self.values)
        else:
            raise ValueError('Dimension error')

    def _determinant(self, values):
        """Actual implementation of deterinant which uses recursion.
        This is a naive implementation since at the moment it can only 
        work for up to 3 by 3 matrix. Anything above 3 by 3 exhausts Python's
        Maximum recursion depth"""
        if len(values[0]) == 1: # deterinant of a 1 by 1 matrix
            return values[0][0]
        elif len(values[0]) == 2:  # determinant of a 2 by 2 matrix
            d = (values[0][0] * values[1][1]) - (values[1][0] * values[0][1])
            return d
        elif len(values[0]) >= 3: # determinant of a n by n matrix where n >= 3
            row1 = values[0]
            d = 0
            for i, factor in enumerate(row1):
                sign = (-1)**i
                # index is supplied to the _minor_matrix() method as starting from 1
                minor = self._determinant(self._minor_matrix(1, i + 1)) 
                d += factor * sign * minor
            return  d


    def _minor_matrix(self, a, b):
        """Return the minor of a particular 
        element in a square matrix at entry a,b
        The indices provided start from 1 but we do computations
        using lists which are zero indexed"""
        
        # Hence indices are changed to begin from 0
        a -= 1 
        b -= 1

        l = [] # list to store minor matrix entries
        for i, v in enumerate(self.values):
            m = [] # temporary row
            for j, w in enumerate(v):
                if not (i == a or j == b):
                    # append entries which are not in the row or column
                    # specified by a or b respectively
                    m.append(w)
            if len(m) != 0:
                l.append(m)
        return l

    def inv(self):
        """Return the inverse of a matrix"""
        pass

    def is_square_matrix(self):
        """Determine whether a matrix is square"""
        rows, cols = self.dim
        return rows == cols

    def is_symmetric(self):
        """"Determine whether a matrix is symmetric"""
        return self.trns() == self

    def is_symmetric(self):
        """"Determine whether a matrix is skew-symmetric"""
        return self.trns() == -self

    def is_utm(self):
        pass

    def is_unit_utm(self):
        pass

    def is_ltm(self):
        pass

    def is_unit_ltm(self):
        pass
