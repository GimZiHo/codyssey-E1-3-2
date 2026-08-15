from input_utils.console_input import input_matrix
from models.matrix import Matrix
from reports.console_reporter import print_user_result
from services.npu_simulator import calculate_mac, judge
from services.performance_analyzer import measure_average_time


REPEAT_COUNT: int = 10


def run_user_input_mode():
    """3x3 사용자 입력 모드의 전체 실행 순서를 관리한다."""

    # 1. 필터 두 개와 판별할 패턴을 입력받는다.
    filter_a: Matrix = input_matrix("필터 A", 3)
    filter_b: Matrix = input_matrix("필터 B", 3)
    pattern: Matrix = input_matrix("패턴", 3)

    # 3. 입력 패턴을 각 필터와 비교하여 MAC 점수를 구한다.
    score_a: float = calculate_mac(pattern, filter_a)
    score_b: float = calculate_mac(pattern, filter_b)

    # 4. 두 점수를 비교하여 A, B 또는 판정 불가를 결정한다.
    judgment: str = judge(
        score_a,
        score_b,
        "A",
        "B",
        "판정 불가",
    )

    # 5. 같은 MAC 연산을 10회 실행하여 평균 시간을 구한다.
    average_mac_time: float = measure_average_time(
        pattern,
        filter_a,
        REPEAT_COUNT,
    )

    # 6. 점수, 평균 시간, 판정 결과를 콘솔에 출력한다.
    print_user_result(
        score_a,
        score_b,
        average_mac_time,
        judgment,
        REPEAT_COUNT
    )