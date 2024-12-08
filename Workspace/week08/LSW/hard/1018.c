#include <stdio.h>
<<<<<<< HEAD
<<<<<<< HEAD
int main() {

=======
=======
>>>>>>> refs/remotes/origin/main

int count_changes(char board[8][8], char w[8][8], char b[8][8]) {
    int i, j;
    int changes_w = 0, changes_b = 0;

    for(i=0; i<8; i++) {
        for(j=0;j<8;j++) {
            if (board[i][j]!=w[i][j]) {
                changes_w++;
            }
            if (board[i][j]!=b[i][j]) {
                changes_b++;
            }
        }
    }

    return (changes_w<changes_b) ? changes_w : changes_b;
}

int main(void) {
    int n, m, i, j, x, y;
    int changes=64;
    char board[50][50];
    scanf("%d %d",&n, &m);

    for (i=0; i<n; i++) {
        scanf("%s", board[i]);
    }

    char chess_w[8][8] = {
        "WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW",
        "WBWBWBWB","BWBWBWBW","WBWBWBWB","BWBWBWBW"
    };
    char chess_b[8][8] = {
        "BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB",
        "BWBWBWBW","WBWBWBWB","BWBWBWBW","WBWBWBWB"
    };

    for (i=0; i <= n-8; i++) {
        for (j=0; j <= m-8; j++) {
            char sub_board[8][8];

            for(x=0;x<8;x++) {
                for (y=0;y<8;y++) {
                    sub_board[x][y] = board[i+x][j+y];
                }
            }
            int temp = count_changes(sub_board, chess_w, chess_b);

            if (temp < changes) {changes = temp;}
        }
    }

    printf("%d\n", changes);

    return 0;
<<<<<<< HEAD
>>>>>>> refs/remotes/origin/main
=======
>>>>>>> refs/remotes/origin/main
}