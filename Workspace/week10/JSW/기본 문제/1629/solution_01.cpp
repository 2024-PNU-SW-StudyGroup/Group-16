#include <iostream>

using namespace std;
int main() {
    int A, B, C;
    long long result = 1;
    cin >> A >> B >> C;
    for (int i = 0; i < B; i++) {
        result *= A;
        result %= C;
    }
    cout << result << endl;
    return 0;
}