class Matrix():
    def __init__(self):
        pass

    @classmethod
    def unit_matrix(cls, n) -> Matrix:
        """Create an n by n unit matrix"""
        pass

    @classmethod
    def utm(cls, m) -> Matrix:
        """Create an upper triangular matrix from matrix m"""
        pass

    @classmethod
    def unit_utm(cls, m) -> Matrix:
        """Create a unit upper triangular matrix from matrix m"""
        pass

    @classmethod
    def ltm(cls, m) -> Matrix:
        """Create a lower triangular matrix from matrix m"""
        pass

    @classmethod
    def unit_ltm(cls, m) -> Matrix:
        """Create a unit lower triangular matrix from matrix m"""
        pass

    @classmethod
    def transpose(cls, m) -> Matrix:
        """Create a unit lower triangular matrix from matrix m"""
        pass

    def __str__(self) -> str:
        pass

    def __repr__(self) -> str:
        pass

    def __add__(self, other):
        pass

    def __sub__(self, other):
        pass

    def __mult__(self, other):
        pass

    def __ne__(self, o: object) -> bool:
        pass

    def __eq__(self, other):
        pass

    def inverse(self) -> int:
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