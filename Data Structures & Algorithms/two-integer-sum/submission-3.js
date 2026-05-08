class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const seenNums = new Map();

        for (let i = 0; i < nums.length; i++) {
            const currVal = nums[i]
            const complement = target - currVal

            if (seenNums.has(complement)) {
                return [seenNums.get(complement), i]
            }

            seenNums.set(currVal, i)
        }
    }
}
