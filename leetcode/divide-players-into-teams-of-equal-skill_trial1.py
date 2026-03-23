class Solution:
    def dividePlayers(self, skill):
        skill.sort()

        l=0
        r=len(skill)-1
        chemistry=skill[l]*skill[r]
        total=skill[l]+skill[r]
        l+=1
        r-=1

        while l<r:
            cur = skill[l]+skill[r]
            if cur != total:
                return -1
            else:
                chemistry += skill[l]*skill[r]
            
            l+=1
            r-=1
        return chemistry