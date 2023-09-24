import subprocess

def run_cpp_program(input_data):
    try:
        # C++ 코드 컴파일
        # subprocess.run(["g++", "/path/to/cpp/project/ssudo.cpp", "-o", "sudoku_solver"], check=True)
        subprocess.run(["g++", "./ssudo.cpp", "-o", "sudoku_solver"], check=True)
        # C++ 프로그램 실행
        process = subprocess.Popen(
            ["./sudoku_solver"],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input_data)
        return stdout
    except subprocess.CalledProcessError as e:
        return f"C++ compilation failed: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("스도쿠를 입력하세요 (9x9 숫자 배열, 빈 칸은 0으로 표시):")
    input_data = ""
    for _ in range(9):
        input_row = input()
        input_data += input_row + "\n"

    result = run_cpp_program(input_data)
    print(result)
