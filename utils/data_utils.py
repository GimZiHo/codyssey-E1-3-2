def extract_size(key: str, part_count: int) -> int:
    """size_N 또는 size_N_idx 키에서 N을 반환한다."""
    parts = key.split("_")
    if len(parts) != part_count or parts[0] != "size" or not parts[1].isdigit():
        raise ValueError(f"잘못된 키입니다: {key}")
    if part_count == 3 and not parts[2].isdigit():
        raise ValueError(f"잘못된 패턴 키입니다: {key}")

    size = int(parts[1])
    if size <= 0:
        raise ValueError("행렬 크기는 1 이상이어야 합니다.")
    return size


def normalize_label(label: str) -> str:
    """JSON 라벨을 Cross 또는 X로 표준화한다."""
    if not isinstance(label, str):
        raise ValueError("라벨은 문자열이어야 합니다.")

    labels = {"+": "Cross", "cross": "Cross", "x": "X"}
    key = label.strip().lower()
    if key not in labels:
        raise ValueError(f"지원하지 않는 라벨입니다: {label}")
    return labels[key]
