'''
Given an array of integers heights representing the histogram's bar height 
where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

'''



def largestRectangleArea(heights):
    max_area = 0  # Variable to store the maximum area of a rectangle found so far
    stack = []  # Stack to store the indices of the histogram bars

    # Iterate through each bar in the histogram
    for i, h in enumerate(heights):
        # While the stack is not empty and the current bar's height is less than or equal to 
        # the height of the bar at the top of the stack
        while stack and heights[stack[-1]] >= h:
            # Pop the top bar's index from the stack
            top_index = stack.pop()
            
            # Calculate the width of the rectangle formed by the popped bar
            # If the stack is empty, the width is `i` (the entire length from the beginning to `i`)
            # Otherwise, the width is the distance between the current index `i` and the index of the 
            # bar now at the top of the stack minus one
            width = i - stack[-1] - 1 if stack else i
            
            # Calculate the area of the rectangle using the height of the popped bar and the calculated width
            max_area = max(max_area, heights[top_index] * width)

        # Push the current bar's index onto the stack
        stack.append(i)

    # Process any remaining bars in the stack
    while stack:
        # Pop the top bar's index from the stack
        top_index = stack.pop()
        
        # Calculate the width of the rectangle formed by the popped bar
        # If the stack is empty, the width is the total length of the histogram
        # Otherwise, the width is the distance between the end of the histogram and the index of the 
        # bar now at the top of the stack minus one
        width = len(heights) - stack[-1] - 1 if stack else len(heights)
        
        # Calculate the area of the rectangle using the height of the popped bar and the calculated width
        max_area = max(max_area, heights[top_index] * width)

    # Return the maximum area found
    return max_area




def largestRectangleArea(heights):
    """
    Calculates the largest rectangular area in a histogram.

    Args:
        heights: A list of integers representing the heights of the bars in the histogram.

    Returns:
        The largest rectangular area in the histogram.
    """

    heights.append(0)  # Add a sentinel value to ensure all bars are processed
    stack = []
    max_area = 0

    for i, h in enumerate(heights):
        """
        Iterate through each bar in the histogram.
        """

        while stack and heights[stack[-1]] > h:
            """
            Pop bars from the stack while the current bar is shorter than the top bar.
            Calculate the area of the rectangle formed by the popped bar and the current bar.
            """
            top_index = stack.pop()
            width = i - stack[-1] - 1 if stack else i
            max_area = max(max_area, heights[top_index] * width)

        stack.append(i)

    return max_area