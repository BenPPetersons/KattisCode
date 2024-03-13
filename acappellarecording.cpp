#include <bits/stdc++.h>

using namespace std;

#define all(x) begin(x), end(x)

typedef long long ll;

ll num, diff, temp;
vector<ll> notes(num);

int main() {
    cin >> num >> diff;

    for (ll i = 0; i < num; ++i) { 
        cin >> temp;
        notes.push_back(temp);
    }

    sort(notes.begin(), notes.end());
    // for (long unsigned int i = 0; i < notes.size(); ++i) {
    //     cout << notes[i] << " ";
    // }
    // cout << "\n";
    
    ll count = 0;
    ll highestNote = -1;

    for (auto note : notes) {
        if (note > highestNote) {
            highestNote = note + diff;
            count += 1;
        }
    }
    
    cout << count << "\n";

    return 0;
}