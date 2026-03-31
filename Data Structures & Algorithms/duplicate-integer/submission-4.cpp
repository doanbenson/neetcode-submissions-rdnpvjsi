class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        std::map<int, int> numCounter;

        for (int num : nums) {
            if (numCounter.contains(num)) {
                numCounter[num]++;
            } else {
                numCounter[num] = 1;
            }
        }

        for (const auto& entry : numCounter) {
            if (entry.second > 1) {
                return true;
            }
        }

        return false;
    }
};