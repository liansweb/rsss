from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return_list = []
        n = len(nums)

        if n <= 1:
            return nums  # 如果列表长度小于等于1，无需排序

        for i in range(0, n-1, 2):
            if nums[i] < nums[i+1]:
                return_list.extend([nums[i], nums[i+1]])
            else:
                return_list.extend([nums[i+1], nums[i]])

        # 处理剩余的奇数个元素
        if n % 2 == 1:
            return_list.append(nums[-1])

        return return_list

# 使用示例
solution = Solution()
result = solution.sortArray([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
print(result)

