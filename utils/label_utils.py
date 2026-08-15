from typing import Dict


LABEL_MAP: Dict[str, str] = {
    "+": "Cross",
    "cross": "Cross",
    "x": "X",
}


def normalize_label(label: str) -> str:
    """외부 라벨을 프로그램의 표준 라벨로 변환한다."""
    if not isinstance(label, str):
        raise ValueError("라벨은 문자열이어야 합니다.")

    key: str = label.strip().lower()

    if key not in LABEL_MAP:
        raise ValueError(f"지원하지 않는 라벨입니다: {label}")

    return LABEL_MAP[key]