#brute force solution accepted
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        size1 = len(nums1)
        size2 = len(nums2)
        size = size1+size2
        med_idx =(size1+size2)//2
        arr=[]
        cnt=0
        cnt1=0
        cnt2=0
        while cnt1<size1 and cnt2<size2 and cnt-1<=med_idx:
            if nums1[cnt1]<nums2[cnt2]:
                arr.append(nums1[cnt1])
                cnt1+=1
                cnt+=1
            else:
                arr.append(nums2[cnt2])
                cnt2+=1
                cnt+=1
        #nums2 already added to arr
        while cnt1<size1 and cnt-1<med_idx:
            arr.append(nums1[cnt1])
            cnt1+=1
            cnt+=1
                
        while cnt2<size2 and cnt-2<med_idx:
            arr.append(nums2[cnt2])
            cnt2+=1
            cnt+=1
        
        median=0
        print(cnt,med_idx, arr)
        if size%2==0:
            median = (arr[med_idx-1]+arr[med_idx])/2
        else:
            median = arr[med_idx]
        return median
        
