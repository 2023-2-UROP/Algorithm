#include <iostream>
#include <cstring>
#include <cstdlib>
#include <ctime>
using namespace std;

#define pass 1
#define fail 0
#define forward 1
#define backward 0

int flag = 0;
int grid[9][9] = {0};
int sub_grid[3][3] = {0};

int check_row(int row, int grid[9][9]) {
    for (int i = 0; i < 9; i++) {
        for (int j = i + 1; j < 9; j++) {
            if ((grid[row][i] != 0) || (grid[row][j] != 0)) {
                if (grid[row][i] == grid[row][j]) {
                    return fail;
                }
            }
        }
    }
    return pass;
}

int check_column(int column, int grid[9][9]) {
    int i = 0, j = 0;
    for (i = 0; i < 9; i++) {
        for (j = i + 1; j < 9; j++) {
            if ((grid[i][column] != 0) || (grid[j][column] != 0)) {
                if (grid[i][column] == grid[j][column]) {
                    return fail;
                }
            }
        }
    }
    return pass;
}

int check_dupl(int arr[9]) {
    for (int i = 0; i < 9; i++) {
        for (int j = i + 1; j < 9; j++) {
            if (arr[i] != 0 || arr[j] != 0) {
                if (arr[i] == arr[j]) {
                    return 1;
                }
            }
        }
    }
    return 0;
}

int check_3x3(int grid[9][9]) {
    int b[9];
    int k = 0;

    for (int r = 0; r < 3; r++) {
        for (int c = 0; c < 3; c++) {
            for (int row = r * 3; row < ((r + 1) * 3); row++) {
                for (int col = c * 3; col < ((c + 1) * 3); col++) {
                    b[k++] = grid[row][col];
                }
            }
            sub_grid[r][c] = check_dupl(b);
            k = 0;
        }
    }
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            if (sub_grid[i][j] == 1)
                return fail;
        }
    }
    return pass;
}

int isPossibleNum(int i, int j, int num) {
    int start_row = i - i % 3;
    int start_col = j - j % 3;

    for (int row = 0; row < 3; row++) {
        for (int col = 0; col < 3; col++) {
            if ((row + start_row) == i && (col + start_col) == j) {
                continue;
            }
            if (grid[row + start_row][col + start_col] == num)
                return fail;
        }
    }
    return pass;
}

int check_elements() {
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            if (grid[i][j] < 1 || grid[i][j] > 9)
                return fail;
        }
    }
    return pass;
}

int main() {
    int filled = 0;
    int row[81], column[81];
    int flag_occupied = 0;
    int dir = forward;
    clock_t start, end;
    double cpu_time_used;

    cout << "Enter numbers : \n";

    for (int l = 0; l < 9; l++) {
        for (int m = 0; m < 9; m++) {
            cin >> grid[l][m];
        }
    }

    cout << "\n --- Entry finished ---\n";
    start = clock();

    for (int n = 0; n < 9; n++) {
        for (int o = 0; o < 9; o++) {
            if (grid[n][o] > 0) {
                row[filled] = n;
                column[filled] = o;
                filled++;
            }
        }
    }
    cout << "\nx:" << " filled : " << filled << "\n";
    for (int l = 0; l < 9; l++) {
        if (check_row(l, grid) == fail) {
            cout << "\n identical numbers in row\n";
            return 0;
        }
        if (check_column(l, grid) == fail) {
            cout << "\n identical numbers in column\n";
            return 0;
        }
    }
    if (check_3x3(grid) == fail) {
        cout << "\n identical numbers in box\n";
        return 0;
    }

    cout << "\n";
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) { 
            for (int x = 0; x < filled; x++) { // 미리 채워진 칸은 건너뜀
                if ((i == row[x]) && (j == column[x])) { 
                    x = 0; 
                    flag_occupied = 1;
                    break;
                }
            }
            if (flag_occupied == 1) { // 미리 채워진 칸은 처리하지 않고
                flag_occupied = 0;    // 다음 칸으로 이동
                if (dir == forward)
                    continue;
                else {
                    // 역방향 이동하는 경우 두 칸 이동
                    j--; 
                    j--; 
                    // 행의 시작점을 넘어가면 행도 변경
                    if (j < -1 && i > 0) {
                        i--;
                        j = 7;
                    }
                    continue;
                }
            }

            if (dir == backward) { // 역방향 이동 중인 경우
                grid[i][j]++; // 현재 칸의 숫자를 증가
                // 숫자가 9를 초과하면 0으로 초기화하고 이전 칸으로 이동
                if (grid[i][j] > 9) {
                    grid[i][j] = 0;
                    j--;
                    j--;
                    if (j < -1 && i > 0) {
                        i--;
                        j = 7;
                    }
                    continue;
                }
            }
            
            // 현재 칸에 가능한 숫자를 찾음
            while (grid[i][j] <= 9) {
                if (grid[i][j] == 0) {
                    grid[i][j] = 1;
                }

                // 현재 숫자가 행, 열, 박스의 규칙에 어긋나지 않는지 확인합
                if (check_row(i, grid) & check_column(j, grid) & isPossibleNum(i, j, grid[i][j])) {
                    dir = forward; // 규칙에 맞으면 정방향으로 이동
                    break;
                } else {
                    grid[i][j]++; // 규칙에 맞지 않으면 숫자를 증가
                    // 숫자가 9를 초과하면 0으로 초기화하고 역방향으로 이동
                    if (grid[i][j] > 9) {
                        grid[i][j] = 0;
                        j--;
                        j--;
                        if (j < -1 && i > 0) {
                            i--;
                            j = 7;
                        }
                        dir = backward; // 역방향으로 이동
                        break;
                    }
                }
            }
            if (j < -3) { // 만약 해결할 수 없으면 "No Solution"을 출력
                cout << "\n No Solution";
                return 0;
            }
        }
    }
    for (int i = 0; i < 9; i++) {
        for (int j = 0; j < 9; j++) {
            cout << grid[i][j] << " ";
        }
        cout << endl;
    }

    end = clock();
    cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
    cout << "\ntime : " << cpu_time_used;
    return 0;
}