#include <iostream>
#include <vector>

using namespace std;

vector<int> find_primes_in_range(int start, int end) {
    vector<int> primes;
    for (int num = start; num <= end; num++) {
        for (int primes=2;primes<=num/2;i++){
            if (num%primes==0){
                return primes;
            }
        }
    }
}

int main() {
    int start, end;

    cin >> start >> end;

    vector<int> primes = find_primes_in_range(start, end);

    for (int num : primes) {
        cout << num << " ";
    }
    cout << endl;

    return 0;
}