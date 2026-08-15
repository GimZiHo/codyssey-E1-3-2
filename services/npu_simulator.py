from models.matrix import Matrix


EPSILON: float = 1e-9


def calculate_mac(
    self,
    pattern: Matrix,
    filter_matrix: Matrix,
) -> float:
    """패턴과 필터의 MAC 점수를 계산한다."""
    self.validate_same_size(pattern, filter_matrix)

    score: float = 0.0

    # 같은 위치의 값을 곱하고 점수에 누적한다.
    for row in range(pattern.size):
        for column in range(pattern.size):
            pattern_value: float = pattern.get_value(row, column)
            filter_value: float = filter_matrix.get_value(row, column)

            score += pattern_value * filter_value

    return score

def judge(
    self,
    first_score: float,
    second_score: float,
    first_label: str,
    second_label: str,
    undecided_label: str,
) -> str:
    """두 점수를 비교하여 판정 라벨을 반환한다."""

    # 점수 차이가 허용오차보다 작으면 동점으로 처리한다.
    if abs(first_score - second_score) < self.EPSILON:
        return undecided_label

    if first_score > second_score:
        return first_label

    return second_label

def validate_same_size(
    self,
    pattern: Matrix,
    filter_matrix: Matrix,
) -> None:
    """패턴과 필터의 크기가 같은지 검사한다."""
    if pattern.size != filter_matrix.size:
        raise ValueError(
            "패턴과 필터의 크기가 일치하지 않습니다."
        )