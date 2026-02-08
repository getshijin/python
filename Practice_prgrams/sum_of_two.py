class solution:
    def sum_of_two(self, nums, target):
        dict = {}

        for i in range(0,len(nums)):
                        # ? = 6 -5
            second_num = target - nums[i]
            if second_num in dict:
                print(dict)
                return [i,dict[second_num]]
            dict[nums[i]] = i

if __name__ == "__main__":
    nums = [5, 3, 7 ,8, 2, 4, 3]
    target = 6
    obj = solution()
    result = obj.sum_of_two(nums, target)
    print(result)  # Output: [0, 1]