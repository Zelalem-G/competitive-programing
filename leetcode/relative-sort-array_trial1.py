class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        count = [0]*1001

        for n in arr1:
            count[n] += 1

        c = 0
        for n in arr2:
            while count[n]>0:
                arr1[c] = n
                c += 1
                count[n] -= 1
        for i in range(len(count)): 
            while count[i]>0:
                arr1[c] = i
                c += 1
                count[i] -= 1
        return arr1