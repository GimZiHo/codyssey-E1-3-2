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


def print_json_result(result: dict) -> None:
    """JSON 패턴 하나의 분석 결과를 출력한다."""
    print()
    print(f"--- {result['key']} ---")

    if result["reason"]:
        print(f"판정: FAIL ({result['reason']})")
        return

    print(f"Cross 점수: {result['cross_score']}")
    print(f"X 점수: {result['x_score']}")
    print(
        f"판정: {result['judgment']} | "
        f"expected: {result['expected']} | {result['status']}"
    )


def print_performance_table(rows: list, repeat_count: int) -> None:
    """크기별 MAC 연산 시간을 표로 출력한다."""
    print()
    print(f"[성능 분석: 평균/{repeat_count}회]")
    print("크기       평균 시간(ms)    연산 횟수")
    print("-------------------------------------")
    for size, average_time in rows:
        print(f"{size}×{size:<6} {average_time:>12.6f} {size * size:>12}")


def print_summary(results: list) -> None:
    """JSON 분석의 전체 PASS/FAIL 결과를 요약한다."""
    passed = sum(result["status"] == "PASS" for result in results)
    failed_results = [result for result in results if result["status"] == "FAIL"]

    print()
    print("[결과 요약]")
    print(f"총 테스트: {len(results)}개")
    print(f"통과: {passed}개")
    print(f"실패: {len(failed_results)}개")

    if failed_results:
        print("실패 케이스:")
        for result in failed_results:
            reason = result["reason"] or (
                f"판정 {result['judgment']} / expected {result['expected']}"
            )
            print(f"- {result['key']}: {reason}")
