class Solution(object):
    def pancakeSort(self, arr):
        res=[]
        for k in range(len(arr)-1,-1,-1):
            max_index=k 
            for j in range(k):
                if arr[j]>arr[max_index]:
                    max_index=j
            arr[0:max_index+1] = arr[0:max_index+1][::-1]
            arr[0:k+1] = arr[0:k+1][::-1]
            res.append(max_index+1)
            res.append(k+1)
        return res
        