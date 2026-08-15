from io_utils.console_output import (
    print_json_result,
    print_performance_table,
    print_summary,
)
from io_utils.json_loader import (
    create_matrix,
    extract_filter_size,
    extract_pattern_size,
    get_object,
    load_json,
    normalize_label,
)
from models.matrix import Matrix
from services.npu_simulator import calculate_mac, judge, measure_average_time


DATA_FILENAME = "data.json"
REPEAT_COUNT = 10


def create_filter_group(data: dict, size: int, group_key: str) -> dict:
    """필터 키를 정규화하고 Matrix로 변환한다."""
    filters = {}
    for label, values in data.items():
        standard_label = normalize_label(label)
        filters[standard_label] = create_matrix(
            values,
            size,
            f"{group_key}.{label}",
        )

    if "Cross" not in filters or "X" not in filters:
        raise ValueError(f"{group_key}에 Cross와 X 필터가 필요합니다.")
    return filters


def load_filter_groups(data: dict) -> dict:
    """필터 그룹을 검증하고 크기별로 로드한다."""
    loaded_filters = {}
    print()
    print("[필터 로드]")

    for group_key, filter_data in data.items():
        try:
            size = extract_filter_size(group_key)
            if not isinstance(filter_data, dict):
                raise ValueError("필터 데이터는 객체여야 합니다.")
            loaded_filters[group_key] = create_filter_group(
                filter_data,
                size,
                group_key,
            )
            print(f"✓ {group_key} 필터 로드 완료 (Cross, X)")
        except ValueError as error:
            print(f"✗ {group_key} 필터 로드 실패: {error}")

    return loaded_filters


def analyze_pattern(
    pattern_key: str,
    pattern_data: dict,
    filter_groups: dict,
) -> dict:
    """패턴 하나를 검증하고 판정한다."""
    result = {
        "key": pattern_key,
        "cross_score": None,
        "x_score": None,
        "judgment": None,
        "expected": None,
        "status": "FAIL",
        "reason": "",
        "sample": None,
    }

    try:
        size = extract_pattern_size(pattern_key)
        if not isinstance(pattern_data, dict):
            raise ValueError("패턴 데이터는 객체여야 합니다.")

        group_key = f"size_{size}"
        filter_matrices = filter_groups.get(group_key)
        if not isinstance(filter_matrices, dict):
            raise ValueError(f"{group_key} 필터가 없습니다.")

        pattern = create_matrix(pattern_data.get("input"), size, pattern_key)
        cross_filter = filter_matrices["Cross"]
        x_filter = filter_matrices["X"]
        expected = normalize_label(pattern_data.get("expected"))

        cross_score = calculate_mac(pattern, cross_filter)
        x_score = calculate_mac(pattern, x_filter)
        judgment = judge(cross_score, x_score, "Cross", "X", "UNDECIDED")

        result.update({
            "cross_score": cross_score,
            "x_score": x_score,
            "judgment": judgment,
            "expected": expected,
            "status": "PASS" if judgment == expected else "FAIL",
            "sample": (pattern, cross_filter),
        })
    except ValueError as error:
        result["reason"] = str(error)

    return result


def create_performance_rows(results: list) -> list:
    """3×3과 JSON의 크기별 평균 연산 시간을 계산한다."""
    base = Matrix([[1.0, 0.0, 1.0], [0.0, 1.0, 0.0], [1.0, 0.0, 1.0]])
    samples = {3: (base, base)}

    for result in results:
        if result["sample"]:
            pattern, filter_matrix = result["sample"]
            samples.setdefault(pattern.size, (pattern, filter_matrix))

    rows = []
    for size in sorted(samples):
        pattern, filter_matrix = samples[size]
        average_time = measure_average_time(pattern, filter_matrix, REPEAT_COUNT)
        rows.append((size, average_time))
    return rows


def run_json_mode() -> None:
    """data.json 분석 모드를 실행한다."""
    try:
        data = load_json(DATA_FILENAME)
        filter_data = get_object(data, "filters")
        patterns = get_object(data, "patterns")
    except ValueError as error:
        print(f"JSON 처리 실패: {error}")
        return

    filter_groups = load_filter_groups(filter_data)

    results = []
    for key, pattern_data in patterns.items():
        result = analyze_pattern(key, pattern_data, filter_groups)
        results.append(result)
        print_json_result(result)

    print_performance_table(create_performance_rows(results), REPEAT_COUNT)
    print_summary(results)
