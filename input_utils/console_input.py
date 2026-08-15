from typing import List

from models.matrix import Matrix


def select_mode() -> str:
    print()
    print("[모드 선택]")
    print("1. 사용자 입력 (3x3)")
    print("2. data.json 분석")

    while True:
        mode = input("선택: ")

        if mode in ("1", "2"):
            return mode

        print("입력 오류: 1 또는 2를 입력하세요.")

def input_matrix(name, size) -> Matrix:
    """N×N 숫자를 입력받아 Matrix 객체로 반환한다."""
    print()
    print(f"[{name} 입력]")
    print(f"각 줄에 숫자 {size}개를 공백으로 구분해서 입력하세요.")

    rows = []

    # 필요한 행의 수만큼 한 행씩 입력받는다.
    for row_number in range(1, size + 1):
        row = input_row(row_number, size)
        rows.append(row)

    print(f"{name} 저장 완료")

    return Matrix(rows)


def input_row(row_number, size) -> List[float]:
    """올바른 한 행이 입력될 때까지 반복한다."""
    while True:
        text = input(f"{row_number}행: ")

        try:
            return parse_row(text, size)
        except ValueError as error:
            print(f"입력 형식 오류: {error}")


def parse_row(text, size) -> List[float]:
    """입력 문자열을 숫자 리스트로 변환한다."""
    values = text.split()

    if len(values) != size:
        raise ValueError(f"각 줄에 {size}개의 숫자를 입력하세요.")

    try:
        return [float(value) for value in values]
    except ValueError:
        raise ValueError("숫자만 입력하세요.")