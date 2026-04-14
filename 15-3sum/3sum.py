class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # ✅ Use a set to hold unique triplets — helps automatically remove duplicate results.
        # Each triplet will be stored as a tuple because lists are unhashable in sets.
        res = []

        # ✅ Sort the array to allow two-pointer traversal (sorted order is key to efficiency).
        nums.sort()

        # ✅ Outer loop: pick each element as the fixed number one by one.
        for i,n in enumerate(nums):
            if n > 0:
                break
            if i > 0 and n == nums[i-1]:
                continue

            # Two pointers: one starts right after the fixed element, the other at the end.
            left, right = i + 1, len(nums) - 1

            # Move pointers inward until they meet.
            while left < right:
                # Compute the sum of the three chosen elements.
                s = n + nums[left] + nums[right]

                if s == 0:
                    # ✅ Found a valid triplet that sums to zero.
                    # Store as tuple to avoid duplicate lists.
                    res.append([n, nums[left], nums[right]])
                    
                    left += 1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1

                elif s < 0:
                    # Sum too small → need a bigger number.
                    # Move left pointer rightward (toward larger numbers).
                    left += 1

                else:
                    # Sum too large → need a smaller number.
                    # Move right pointer leftward (toward smaller numbers).
                    right -= 1

        # ✅ Convert the set of tuples into a list of lists (as required by LeetCode).
        return res