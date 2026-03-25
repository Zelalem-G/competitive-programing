class Solution(object):
    def lengthOfLongestSubstring(self, s):
        left=0
        temp=set()
        maxium=0
        for i in range(len(s)):
            while s[i] in temp:
                temp.remove(s[left])
                left+=1
            temp.add(s[i])
            maxium=max(maxium,len(temp))
        return maxium