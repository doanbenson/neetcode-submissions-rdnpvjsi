class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_arr = [[] for i in range(len(nums) + 1)] #[[3, 1]] -> [2,2] -> [[freq, num]]
        counter = Counter(nums)
        res = []

        for num, freq in counter.items():
            frequency_arr[freq].append(num)
 
        for freq in range(len(frequency_arr) - 1, 0, -1):
            for num in frequency_arr[freq]:
                res.append(num)
                if len(res) == k:
                    return res


        