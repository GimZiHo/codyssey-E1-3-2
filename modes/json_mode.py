from typing import Any, Dict

from input_utils.json_loader import (
    get_required_object,
    load_json,
)


DATA_FILENAME: str = "data.json"


def run_json_mode() -> None:
    """data.json 분석 모드의 전체 실행 순서를 관리한다."""

    try:
        # 1. data.json 파일을 읽는다.
        data: Dict[str, Any] = load_json(DATA_FILENAME)

        # 2. 필수 항목을 가져온다.
        filters: Dict[str, Any] = get_required_object(
            data,
            "filters",
        )
        patterns: Dict[str, Any] = get_required_object(
            data,
            "patterns",
        )
    except ValueError as error:
        print(f"JSON 처리 실패: {error}")
        return

    print("data.json 로드 완료")
    print(f"필터 그룹: {len(filters)}개")
    print(f"패턴: {len(patterns)}개")