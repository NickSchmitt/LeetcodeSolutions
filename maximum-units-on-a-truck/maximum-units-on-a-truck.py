class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        """
        go through multiplying to find total units
        [[5,10],[2,5],[4,7],[3,9]]
        [50, 10, 28, 27] = number of units
        
        
        find the combination of boxes that gets us closest to the total but not over
        """
        boxTypes.sort(key=lambda box: box[1], reverse=True)
        total_units = 0
        
        for boxes, units in boxTypes:
            if truckSize-boxes >= 0:
                total_units += boxes * units
                truckSize-=boxes
            else:
                total_units += truckSize * units
                break
        
        return total_units

        