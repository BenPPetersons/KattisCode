#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

typedef long long ll;

int main() {
    cin.tie(0)->sync_with_stdio(0);

    int n;
    ll s, l, r;
    cin >> n >> s;

    for (int i = 0; i < n; ++i) {
        cin >> l >> r;

        if (l <= s && s <= r) {
            s++;
        }
    }

    cout << s << '\n';
    return 0;
}
