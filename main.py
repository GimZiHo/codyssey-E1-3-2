import shutil
from pathlib import Path

from io_utils.console_input import select_mode
from modes.json_mode import run_json_mode
from modes.user_input_mode import run_user_input_mode


def main() -> None:
    try:
        print("=== Mini NPU Simulator ===")
        mode = select_mode()

        if mode == "1":
            run_user_input_mode()
        else:
            run_json_mode()
    finally:
        remove_python_cache()


def remove_python_cache() -> None:
    """프로젝트 안의 Python 캐시 디렉터리를 삭제한다."""
    project_directory = Path(__file__).resolve().parent
    for cache_directory in project_directory.rglob("__pycache__"):
        shutil.rmtree(cache_directory, ignore_errors=True)


if __name__ == "__main__":
    main()
