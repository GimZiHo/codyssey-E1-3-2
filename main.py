from input_utils.console_input import select_mode
from modes.json_mode import run_json_mode
from modes.user_input_mode import run_user_input_mode

def main():
    print("=== Mini NPU Simulator ===")

    mode = select_mode()

    if mode == "1":
        run_user_input_mode()
    else:
        run_json_mode()


if __name__ == "__main__":
    main()