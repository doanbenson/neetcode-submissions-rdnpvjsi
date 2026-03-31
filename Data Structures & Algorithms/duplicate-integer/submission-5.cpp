class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::unordered_set<int> counter;

        for (int num : nums) {
            if (counter.find(num) != counter.end()) {
                return true;
            }
            counter.insert(num);
        }

        return false;
    }
};