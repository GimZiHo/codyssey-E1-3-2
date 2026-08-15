import time

from models.matrix import Matrix
from services.npu_simulator import calculate_mac

def measure_average_time(
    pattern: Matrix,
    filter_matrix: Matrix,
    repeat_count: int,
) -> float:
    """MAC 연산을 반복하고 1회당 평균 시간을 ms로 반환한다."""
    if repeat_count <= 0:
        raise ValueError("반복 횟수는 1 이상이어야 합니다.")

    # 입력과 출력을 제외하고 MAC 함수 호출 구간만 측정한다.
    # time.perf_counter() : 프로그램의 짧은 실행 시간을 측정할 때 사용하는 정밀한 타이머(초)
    start_time: float = time.perf_counter()

    for _ in range(repeat_count):
        calculate_mac(pattern, filter_matrix)

    end_time: float = time.perf_counter()

    total_time_ms: float = (end_time - start_time) * 1000
    average_time_ms: float = total_time_ms / repeat_count

    return average_time_ms