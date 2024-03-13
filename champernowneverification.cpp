#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

typedef long long ll;

int main() {
    cin.tie(0)->sync_with_stdio(0);

    string s;
    cin >> s;

    ll i = 1;
    ll max = 10;
    int dig = 1;

    for (long unsigned int pos = 0; pos < s.size(); ++pos) {

        if (i == max) {
            max *= 10;
            dig++;
        }

        // ll ans = stoll(s.substr(pos, dig));
        // cout << pos << " " << dig << " num: " << ans << "\n";

        if (stoll(s.substr(pos, dig)) != i) {
            cout << -1 << endl;
            return 0;
        }
        else {
            i++;
            pos += dig - 1;
        }
    }
    cout << i-1 << '\n';
    return 0;
}