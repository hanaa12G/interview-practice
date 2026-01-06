#include <bits/stdc++.h>
using namespace std;

int snakesAndLadders(vector<vector<int>> const& board) {

    vector<int> positions = {};
    bool ltr = true;
    int i = 0;
    for (auto rit = board.rbegin(); rit != board.rend(); ++rit) {
        vector<int> row = *rit;
        if (ltr) {
            for (auto cit = row.begin(); cit != row.end(); ++cit) {
                if (*cit != -1) {
                    positions.push_back(*cit - 1);
                }
                else {
                    positions.push_back(-1);
                }
            }
        }
        else {
            for (auto cit = row.rbegin(); cit != row.rend(); ++cit) {
                if (*cit != -1) {
                    positions.push_back(*cit - 1);
                }
                else {
                    positions.push_back(-1);
                }
            }
        }
        ltr = !ltr;
    }

    auto dest = [&positions] (int i) {
        assert(i <= positions.size());
        if (positions[i] != -1) {
            return positions[i];
        }
        return i;
    };

    int end = positions.size() - 1;
    
    using position = pair<int, int>;

    queue<position> next_positions = {};
    next_positions.push(make_pair(0, 0));
    set<int> visited = { 0 };

    while (!next_positions.empty()) {
        position next = next_positions.front();
        next_positions.pop();
        // cout << "At " << next.first << " , step made: " << next.second << endl;

        int i = next.first + 1;
        for (; i < end && i < next.first + 6; ++i) {
            int j = dest(i);
            // cout << j << " is created from " << next.first << " by " << i << ", ";
            if (j == end) {
                return next.second + 1;
            }
            if (!visited.count(j)) {
                // cout << "push" << endl;
                visited.insert(j);
                next_positions.push(make_pair(j, next.second + 1));
            }
            else {
                // cout << "skipped" << endl;
            }
        }
        if (i == end) {
            return next.second + 1;
        }
    }
    return -1;
}

int main() {
    // cout << snakesAndLadders({
    //     {-1,-1,-1,-1,-1,-1},
    //     {-1,-1,-1,-1,-1,-1},
    //     {-1,-1,-1,-1,-1,-1},
    //     {-1,35,-1,-1,13,-1},
    //     {-1,-1,-1,-1,-1,-1},
    //     {-1,15,-1,-1,-1,-1}
    // }) << endl;;
    return 0;
}
