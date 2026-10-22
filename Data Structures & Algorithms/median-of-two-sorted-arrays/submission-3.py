class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        total=len(nums1)+len(nums2)

        isFirstSmall=len(nums1)<=len(nums2)
        isSecondSmall=len(nums1)>len(nums2)

        if isFirstSmall:
            t=nums2
            nums2=nums1
            nums1=t
        
        # 1,2,3
        # 4,5,6
        # if nums1[len(nums1)-1]<=nums2[0]:
        #     if total%2==0 and len(nums1)==len(nums2):
        #         return (nums1[len(nums1)-1]+nums2[len(nums2)-1])/2
        #     elif total%2==0:
        #         return  (nums1[(total//2) -1]+nums1[total//2])/2
        #     else:
        #         return nums1[total//2]

        n1=len(nums1)
        n2=len(nums2)
        #always num1 will be big or= to smaller one

        l1=float('-inf')
        l2=float('-inf')
        r1=float('inf')
        r2=float('inf')
        l=0
        r=len(nums2)

        half=(total+1)//2
        # while(l1>=r2 or  l2>=r1 or (l1==float('-inf') and r2==float('inf') or l2==float('-inf') and r1==float('inf')) ): 
            # print(l1>=r2,l2>=r1 , (l1==float('-inf') and r2==float('inf') or l2==float('-inf') and r1==float('inf')) )
            # print("while")
        while True:   
            mid2=l+((r-l)//2)
            mid1=half-mid2
            # print(nums1,nums2)

            # print("mid1",mid1)
            # print("mid2",mid2)
            l1=float('-inf')
            l2=float('-inf')
            r1=float('inf')
            r2=float('inf')

            l1_index=mid1-1
            r1_index=mid1

            l2_index=mid2-1
            r2_index=mid2
            # print(l1_index,l2_index,r1_index,r2_index)
            if l1_index>=0:
                l1=nums1[l1_index]
            
            if r1_index<len(nums1):
                r1=nums1[r1_index]
            
            if l2_index>=0:
                l2=nums2[l2_index]

            if r2_index<len(nums2):
                r2=nums2[r2_index]

            if l1>r2:
                l=mid2+1
            elif l2>r1:
                r=mid2-1
            else:
                break
            # print( l1, r1)
            # print( l2, r2)
            # print(l1>=r2,l2>=r1 , (l1==-1 and r2==float('inf') or l2==-1 and r1==float('inf')) )

        # print("condition satisfy")

        # print( l1, r1)
        # print( l2, r2)


        if total%2==0:
            return (max(l1,l2)+min(r1,r2)) /2
        else:
            return max(l1,l2)
        


        #   2,3,10
#         1,9,  l1=3 r1=inf

#         2,3,10  l2=2. r2=inf

# 6/2 =3 



