class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #arr that stores candidates
        candidates = []
        map = dict()
        degree = 0
        result = len(nums)
        #first find out the degree and the scope of each number
        for idx, num in enumerate(nums):
            num_info = map.setdefault(num, {
                'degree': 0,
                'begin': idx,
                'end': 0
            })
            num_info['degree'] += 1
            num_info['end'] = idx
            map[num] = num_info
            if degree < num_info['degree']:
                degree = num_info['degree']
                result = num_info['end'] - num_info['begin'] + 1
            elif degree == num_info['degree']:
                num_len = num_info['end'] - num_info['begin'] + 1
                result = num_len if num_len < result else result
        return result
