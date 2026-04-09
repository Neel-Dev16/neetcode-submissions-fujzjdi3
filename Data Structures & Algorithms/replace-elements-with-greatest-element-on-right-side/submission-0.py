class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        arr=arr[::-1]
        maximum=arr[0]
        arr[0]=-1
        for i in range(1,len(arr)):
            if arr[i]>maximum:
                temp=arr[i]
                arr[i]=maximum
                maximum=temp
            else:
                arr[i]=maximum
        return arr[::-1]

        