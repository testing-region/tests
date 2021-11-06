#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    int best[n];
    for (int i; i < n; i++){
        cin >> best[i];
    }

    int bestSum = 0;

    for (int a = 0; a < n; a++) {
        for (int b = a; b < n; b++) {
	    int sum = 0;
	    for (int k = a; k <= b; k++) {
	        sum += best[k];
	    }
            bestSum = max(bestSum, sum);
	}
    }
    cout << bestSum << '\n';   
}
