class Matrix:
    """N×N 숫자 데이터를 저장하고 관리한다."""

    def __init__(self, values) -> None:
        # 2차원 리스트와 행렬의 크기를 저장한다.
        self.values = values
        self.size = len(values)

    def get_value(self, row, column) -> float:
        """지정한 행과 열의 값을 반환한다."""
        return self.values[row][column]

    def set_value(self, row, column, value)-> None:
        """지정한 행과 열에 값을 저장한다."""
        self.values[row][column] = value