class Solution:
    def search(self, nums: List[int], target: int) -> int:


        l=0
        r=len(nums)
        while l<r:
            print(l,r)
            mid=l+((r-l)//2)
            print("mid",mid)
            if nums[mid]==target:
                return  mid
            elif nums[mid]<target:
                l=mid+1
            else:
                r=mid
            
        return -1
   