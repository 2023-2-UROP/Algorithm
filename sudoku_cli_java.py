import subprocess

def run_java_program(java_file, input_data):
    try:
        # 컴파일 Java 파일 (sudoku_solver.java)
        # subprocess.run(["javac", "/path/to/java/project/SudokuSolver.java"], check=True)
        subprocess.run(["javac", "./sudoku_java.java"], check=True)
        # Java 프로그램 실행
        process = subprocess.Popen(
            ["java", java_file.replace(".java", "")],
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        stdout, stderr = process.communicate(input_data)
        return stdout
    except subprocess.CalledProcessError as e:
        return f"Java compilation failed: {e}"
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    print("스도쿠를 입력하세요 (9x9 숫자 배열, 빈 칸은 0으로 표시):")
    input_data = ""
    for _ in range(9):
        input_row = input()
        input_data += input_row + "\n"

    java_file = "sudoku_java.java"  # Java 프로그램 파일명
    result = run_java_program(java_file, input_data)
    print(result)
