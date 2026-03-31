class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        std::map<char, int> counter_s;
        std::map<char, int> counter_t;

        for (char c: s) {
            counter_s[c]++;
        }

        for (char c: t) {
            counter_t[c]++;
        }

        if (counter_s == counter_t) {
            return true;
        }

        return false;
    }
};
