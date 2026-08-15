import json

from models.matrix import Matrix


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


def create_matrix(values, size: int, name: str) -> Matrix:
    """JSON 배열을 검증하고 Matrix로 변환한다."""
    if not isinstance(values, list) or len(values) != size:
        raise ValueError(f"{name}의 행은 {size}개여야 합니다.")

    rows = []
    for row_number, values_in_row in enumerate(values, start=1):
        if not isinstance(values_in_row, list) or len(values_in_row) != size:
            raise ValueError(f"{name} {row_number}행은 {size}개의 값이 필요합니다.")
        if any(not isinstance(value, (int, float)) for value in values_in_row):
            raise ValueError(f"{name}에 숫자가 아닌 값이 있습니다.")
        rows.append([float(value) for value in values_in_row])

    return Matrix(rows)
