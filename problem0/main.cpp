#include <iostream>
using namespace std;

int main() {
    long long squareSum = 0;
    int limit = 928000;

    for (int i = 1; i <= limit; i++) {
        long long square = 1LL * i * i;  
        if (square % 2 == 1) {
            squareSum += square;
        }
    }

    cout << "Answer is: " << squareSum << endl;
    return 0;
}
