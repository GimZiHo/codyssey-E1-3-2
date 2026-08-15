import json
from typing import Any, Dict

from models.matrix import Matrix


def load_json(filename: str) -> Dict[str, Any]:
    """JSON 파일을 읽어 딕셔너리로 반환한다."""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            data: Any = json.load(file)
    except FileNotFoundError:
        raise ValueError(f"{filename} 파일을 찾을 수 없습니다.")
    except json.JSONDecodeError:
        raise ValueError(f"{filename}의 JSON 형식이 잘못되었습니다.")
    except OSError as error:
        raise ValueError(f"{filename}을 읽지 못했습니다: {error}")

    if not isinstance(data, dict):
        raise ValueError("JSON의 최상위 데이터는 객체여야 합니다.")

    return data

def get_required_object(
    data: Dict[str, Any],
    key: str,
) -> Dict[str, Any]:
    """필수 키의 값을 딕셔너리로 반환한다."""
    if key not in data:
        raise ValueError(f"필수 항목 '{key}'가 없습니다.")

    value: Any = data[key]

    if not isinstance(value, dict):
        raise ValueError(f"'{key}'는 객체 형식이어야 합니다.")

    return value

def create_matrix(
    raw_matrix: Any,
    size: int,
    name: str,
) -> Matrix:
    """JSON의 N×N 숫자 리스트를 Matrix로 변환한다."""
    if not isinstance(raw_matrix, list) or len(raw_matrix) != size:
        raise ValueError(
            f"{name}: 행의 개수는 {size}개여야 합니다."
        )

    rows: List[List[float]] = []

    # 모든 행의 길이와 값의 타입을 검사한다.
    for row_number, raw_row in enumerate(raw_matrix, start=1):
        if not isinstance(raw_row, list) or len(raw_row) != size:
            raise ValueError(
                f"{name}: {row_number}행에는 "
                f"{size}개의 값이 필요합니다."
            )

        row: List[float] = []

        for value in raw_row:
            if not isinstance(value, (int, float)):
                raise ValueError(
                    f"{name}: 숫자가 아닌 값이 있습니다."
                )

            row.append(float(value))

        rows.append(row)

    return Matrix(rows)