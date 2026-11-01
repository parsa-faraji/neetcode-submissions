class Solution { // Define the solution class.
    public int maxArea(int[] heights) { // Find the maximum container area.
        int left = 0; // Start at the first bar.
        int right = heights.length - 1; // Start at the last bar.
        int best = 0; // Track the largest area found.

        while (left < right) { // Continue until the pointers meet.
            int area = (right - left) * Math.min(heights[left], heights[right]); // Calculate the current area.
            if (area > best) { // Check whether this area is larger.
                best = area; // Save the larger area.
            } // Finish updating the best area.
            if (heights[left] < heights[right]) { // Check whether the left bar is shorter.
                left++; // Move past the shorter left bar.
            } else { // The right bar is shorter or equal.
                right--; // Move past the right bar.
            } // Finish moving one pointer.
        } // Finish examining pairs.
        return best; // Return the maximum area.
    } // Finish the method.
} // Finish the class.
