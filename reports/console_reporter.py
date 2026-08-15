from models.matrix import Matrix


def print_user_result(
    score_a: float,
    score_b: float,
    average_mac_time: float,
    judgment: str,
    repeat_count: int,
) -> None:
    """사용자 입력 모드의 MAC 결과를 출력한다."""
    print()
    print("[MAC 결과]")
    print(f"A 점수: {score_a}")
    print(f"B 점수: {score_b}")
    print(
        f"연산 시간(평균/{repeat_count}회): "
        f"{average_mac_time:.6f} ms"
    )
    print(f"판정: {judgment}")
