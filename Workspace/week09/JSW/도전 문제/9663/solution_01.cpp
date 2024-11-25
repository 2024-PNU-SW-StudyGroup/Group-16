// Problem: N-Queen(https://www.acmicpc.net/problem/9663)
// Date: 2024.11.25
// Comment: 통과.
// -> 무적의 C++

#include <iostream>

static int N;
static int* state;
static bool* visited;
static int count;
bool isValid(int* state, int depth) {
    int y_up = state[depth-1];
    int y_down = state[depth-1];
    for (int i = depth-2; i >= 0; i--) {
        y_up += 1;
        y_down -= 1;
        if (state[i] == y_up || state[i] == y_down) {
            return false;
        }
    }
    return true;
}
void recurse(int depth) {
    if (!isValid(state, depth)) {
        return;
    }
    if (depth == N) {
        count++;
        return;
    }
    for (int i = 0; i < N; i++) {
        if (!visited[i]) {
            visited[i] = true;
            state[depth] = i;
            recurse(depth+1);
            visited[i] = false;
        }
    }
}
int main() {
    std::cin >> N;
    state = new int[N];
    visited = new bool[N];
    count = 0;
    recurse(0);
    std::cout << count;


    delete[] state;
    delete[] visited;
    
    return 0;
}