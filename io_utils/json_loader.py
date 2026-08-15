"""JSON 파일을 읽고 데이터를 검증한다."""

import json

from models.matrix import Matrix


LABELS = {
    "+": "Cross",
    "cross": "Cross",
    "x": "X",
}


def load_json(filename: str) -> dict:
    """JSON 파일을 읽어 딕셔너리로 반환한다."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise ValueError(f"{filename} 파일을 찾을 수 없습니다.")
    except json.JSONDecodeError:
        raise ValueError(f"{filename}의 JSON 형식이 잘못되었습니다.")
    except OSError as error:
        raise ValueError(f"{filename}을 읽지 못했습니다: {error}")

    if not isinstance(data, dict):
        raise ValueError("JSON의 최상위 데이터는 객체여야 합니다.")
    return data


def get_object(data: dict, key: str) -> dict:
    """필수 키의 객체 값을 반환한다."""
    value = data.get(key)
    if not isinstance(value, dict):
        raise ValueError(f"'{key}' 객체가 필요합니다.")
    return value


def extract_filter_size(key: str) -> int:
    """size_N 형식의 필터 키에서 N을 반환한다."""
    parts = key.split("_")
    if len(parts) != 2 or parts[0] != "size" or not parts[1].isdigit():
        raise ValueError(f"잘못된 필터 키입니다: {key}")
    return _positive_size(parts[1])


def extract_pattern_size(key: str) -> int:
    """size_N_idx 형식의 패턴 키에서 N을 반환한다."""
    parts = key.split("_")
    if (
        len(parts) != 3
        or parts[0] != "size"
        or not parts[1].isdigit()
        or not parts[2].isdigit()
    ):
        raise ValueError(f"잘못된 패턴 키입니다: {key}")
    return _positive_size(parts[1])


def _positive_size(value: str) -> int:
    """문자열로 읽은 행렬 크기가 양수인지 검증한다."""
    size = int(value)
    if size <= 0:
        raise ValueError("행렬 크기는 1 이상이어야 합니다.")
    return size


def normalize_label(label: str) -> str:
    """JSON 라벨을 Cross 또는 X로 표준화한다."""
    if not isinstance(label, str):
        raise ValueError("라벨은 문자열이어야 합니다.")

    key = label.strip().lower()
    if key not in LABELS:
        raise ValueError(f"지원하지 않는 라벨입니다: {label}")
    return LABELS[key]


def create_matrix(values, size: int, name: str) -> Matrix:
    """JSON 배열을 검증하고 Matrix로 변환한다."""
    if not isinstance(values, list) or len(values) != size:
        raise ValueError(f"{name}의 행은 {size}개여야 합니다.")

    rows = []
    for row_number, values_in_row in enumerate(values, start=1):
        if not isinstance(values_in_row, list) or len(values_in_row) != size:
            raise ValueError(f"{name} {row_number}행은 {size}개의 값이 필요합니다.")
        if any(
            isinstance(value, bool) or not isinstance(value, (int, float))
            for value in values_in_row
        ):
            raise ValueError(f"{name}에 숫자가 아닌 값이 있습니다.")
        rows.append([float(value) for value in values_in_row])

    return Matrix(rows)
