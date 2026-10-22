class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        l=0
        r=len(matrix)*len(matrix[0]) -1

        row=len(matrix)
        col=len(matrix[0])

        while l<=r:
            mid_index=l+((r-l)//2)
            print("mid index",mid_index)
            r_idx=(mid_index//col)
            c_idx=mid_index%col
            mid_val=matrix[r_idx][c_idx]

            if mid_val==target:
                return True
            elif mid_val<target:
                l=mid_index+1
            elif mid_val>target:
                r=mid_index-1



        return False
        