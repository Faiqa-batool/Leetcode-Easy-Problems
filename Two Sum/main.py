class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}  # Dictionary to store the number and its index
        for index, num in enumerate(nums):
            complement = target - num  # The number that we need to find
            if complement in num_to_index:
                return [num_to_index[complement], index]  # Return indices if complement is found
            num_to_index[num] = index  # Store the index of the current number

if __name__ == "__main__":
    # Input: List of numbers
    nums = list(map(int, input("Enter the list of numbers separated by spaces: ").split()))
    # Input: Target number
    target = int(input("Enter the target number: "))
    
    # Create an instance of the Solution class
    solution = Solution()
    
    # Call the twoSum function and store the result
    result = solution.twoSum(nums, target)
    
    # Print the result
    print("Indices of the two numbers that add up to the target are:", result)


