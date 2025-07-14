class Solution(object):

    def trap(self, height):
        """

        :type height: List[int]
        :rtype: int
        """
      
        if not height or len(height) < 3:
            return 0

     
        left, right = 0, len(height) - 1

        left_max, right_max = height[left], height[right]
        
        total_water = 0

        while left < right:

            
            if left_max < right_max:

                left += 1

                left_max = max(left_max, height[left])

                total_water += left_max - height[left]
            else:
                
                right -= 1

                right_max = max(right_max, height[right])

                total_water += right_max - height[right]
                
        return total_water