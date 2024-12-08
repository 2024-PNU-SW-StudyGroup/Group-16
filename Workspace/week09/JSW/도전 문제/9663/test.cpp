#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char answer[100];
bool visited[100];
void permutations(char *str, int n, int depth=0) {
    if (depth == n) {
        puts(answer);
        return;
    }
    for (int i = 0; i < strlen(str); i++) {
        if (visited[i]) continue;
        answer[depth] = str[i];
        visited[i] = true;
        permutations(str, n, depth+1);
        visited[i] = false;
    }
}
void combinations(char *str, int n, int depth = 0) {
    if (depth > 1 && answer[depth-2] > answer[depth-1]) return;
    if (depth == n) {
        puts(answer);
        return;
    }
    for (int i = 0; i < strlen(str); i++) {
        if (visited[i]) continue;
        answer[depth] = str[i];
        visited[i] = true;
        combinations(str, n, depth+1);
        visited[i] = false;
    }
}

int main() {
    char str[] = "ABCDE";
    permutations(str, 2);
    combinations(str, 3);
    return 0;
}