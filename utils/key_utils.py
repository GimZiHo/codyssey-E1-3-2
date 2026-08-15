def extract_filter_size(group_key: str) -> int:
    """size_N 형식의 필터 키에서 크기 N을 반환한다."""
    parts = group_key.split("_")

    if (
        len(parts) != 2
        or parts[0] != "size"
        or not parts[1].isdigit()
    ):
        raise ValueError(
            f"잘못된 필터 그룹 키입니다: {group_key}"
        )

    size: int = int(parts[1])

    if size <= 0:
        raise ValueError("필터 크기는 1 이상이어야 합니다.")

    return size

def extract_pattern_size(pattern_key: str) -> int:
    """size_N_idx 형식의 패턴 키에서 크기 N을 반환한다."""
    parts = pattern_key.split("_")

    if (
        len(parts) != 3
        or parts[0] != "size"
        or not parts[1].isdigit()
        or not parts[2].isdigit()
    ):
        raise ValueError(
            f"잘못된 패턴 키입니다: {pattern_key}"
        )

    # 두 번째 값이 패턴의 크기다.
    size: int = int(parts[1])

    if size <= 0:
        raise ValueError("패턴 크기는 1 이상이어야 합니다.")

    return size